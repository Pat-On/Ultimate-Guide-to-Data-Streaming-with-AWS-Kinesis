import base64
import json
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def decode_record(record: bytes) -> dict:
    string_data = base64.b64decode(record).decode('utf-8')
    return json.loads(string_data)


def lambda_handler(event, context):
    # slicing to last 3 records
    logger.info(f"Orders Consumer Handler Invoked with Records {event['Records'][:3]}")

    for record in event['Records']:
        try:
            # decode_record is using b64 to decode it
            order = decode_record(record['kinesis']['data'])
            logger.info({
              'message': 'Processed order record',
              'order': order
            })
        except Exception as e:
            logger.error({
                'error': 'failed-decoding-record',
                'exception': str(e),
                'record': record
            })
            raise e
