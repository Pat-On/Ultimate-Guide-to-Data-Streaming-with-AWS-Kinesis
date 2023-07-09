import copy
import json
import logging
import random
import sys
import time

import boto3

from uuid import uuid4

from collections import namedtuple


logging.basicConfig(
  format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
  datefmt='%Y-%m-%d %H:%M:%S',
  level=logging.INFO,
  handlers=[
      logging.FileHandler("producer.log"),
      logging.StreamHandler(sys.stdout)
  ]
)

Product = namedtuple('Product', ['code', 'name', 'price'])

products = [
    Product('A0001', 'Hair Comb', 2.99),
    Product('A0002', 'Toothbrush', 5.99),
    Product('A0003', 'Dental Floss', 0.99),
    Product('A0004', 'Hand Soap', 1.99)
]

seller_ids = ['abc', 'xyz', 'jkq', 'wrp']
customer_ids = [
    "C1000", "C1001", "C1002", "C1003", "C1004", "C1005", "C1006", "C1007", "C1008", "C1009",
    "C1010", "C1011", "C1012", "C1013", "C1014", "C1015", "C1016", "C1017", "C1018", "C1019",
]


def make_orderitems():
    order_id = str(uuid4())
    seller_id = random.choice(seller_ids)
    customer_id = random.choice(customer_ids)
    order_items = []

    available_products = copy.copy(products)
    n_products = random.randint(1, len(products))
    for _ in range(n_products):
        product = random.choice(available_products)
        available_products.remove(product)
        qty = random.randint(1, 10)

        order_items.append({
            'customer_id': customer_id,
            'order_id': order_id,
            'seller_id': seller_id,
            'product_name': product.name,
            'product_code': product.code,
            'product_quantity': qty,
            'product_price': product.price
        })

    return order_items


def main(args):
    logging.info('Starting PutRecord Producer')

    stream_name = args[1]
    kinesis = boto3.client('kinesis')

    while True:
        # Generate fake order data
        items = make_orderitems()
        logging.info(f'Generated {len(items)} order items')

        combined_records = []
        for item in items:
            combined_records.append((item, {
                'Data': json.dumps(item).encode('utf-8'),
                'PartitionKey': item['seller_id']
            }))

        try:
            # break apart orders from records as separate lists
            order_items, records = map(list, zip(*combined_records))

            # write records to Kinesis via PutRecords API
            response = kinesis.put_records(Records=records,
                                        StreamName=stream_name)

            # inspect records to check for any that failed to be written to Kinesis
            for i, record_response in enumerate(response['Records']):
                error_code = record_response.get('ErrorCode')
                oi = order_items[i]
                if error_code:
                    err_msg = record_response['ErrorMessage']
                    logging.error(f"Failed to produce {oi} because {err_msg}")
                else:
                    seq = record_response['SequenceNumber']
                    shard = record_response['ShardId']
                    logging.info(f"Produced {oi} sequence {seq} to Shard {shard}")

        except Exception as e:
            logging.error({
                'message': 'Error producing records',
                'error': str(e),
                'records': combined_records
            })

        time.sleep(0.3)


if __name__ == '__main__':
    main(sys.argv)
