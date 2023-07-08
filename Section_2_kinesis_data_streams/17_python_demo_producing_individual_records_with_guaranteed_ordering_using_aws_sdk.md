# Python Demo producing individual records with guaranteed ordering using aws sdk

`boto3` https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

in this demo we are ordering the streamed data - sequence number from the api

```json
{
  "customer_id": "C1007",
  "seller_id": "jkq",
  "order_id": "0e74bd17-e901-4c44-9d21-73c13b86460c",
  "order_items": [
    {
      "product_name": "Hand Soap",
      "product_code": "A0004",
      "product_quantity": 3,
      "product_price": 1.99
    },
    {
      "product_name": "Dental Floss",
      "product_code": "A0003",
      "product_quantity": 1,
      "product_price": 0.99
    },
    {
      "product_name": "Toothbrush",
      "product_code": "A0002",
      "product_quantity": 5,
      "product_price": 5.99
    },
    {
      "product_name": "Hair Comb",
      "product_code": "A0001",
      "product_quantity": 6,
      "product_price": 2.99
    }
  ]
}
```
