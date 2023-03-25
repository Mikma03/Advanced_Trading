<!-- TOC -->

- [Description:](#description)
- [Input:](#input)
- [Output:](#output)
- [Examples:](#examples)
  - [First example - data](#first-example---data)
  - [Second example - data](#second-example---data)
- [General description how Iceberg orders work:](#general-description-how-iceberg-orders-work)

<!-- /TOC -->

# Description:

​Your task is to implement an Order Book which handles two order types: Limit Order and Iceberg Order.
A Limit Order determines the highest price at which we are ready to buy (for "buy" orders) or the lowest price at which we are ready to sell (for "sell" orders).​ The program should read information about incoming orders from the standard input, it should update the status of the Order Book on an ongoing basis, and if as a result of adding an order a transaction occurs, the program should write the appropriate information to the standard output. What's more, after adding each order, the updated state of an order book should be written to the standard output.​

# Input:

​Each entry line corresponds to one new order in JSON format:

type: equal to "Iceberg" or "Limit"
order: contains detailed information about the order:
direction: equal to "Buy" or "Sell"
id: consecutive positive integers: 1, 2, 3, ...
price: positive integer
quantity: positive integer
peak: positive integer, this field is only present in the Iceberg orders

​It can be assumed that the input data will be correct and all integers appearing on the input will fit in a 32-bit signed integer variable.​

# Output:

​After loading the information about the new order from stdin, add it to the Order Book and then write to stdout the updated status of the Order Book as a JSON object.​

It should contain two fields: buyOrders and sellOrders which represent the list of buy or sell orders. Each order should contain id, price and quantity fields. The order on the list is determined by the price. "Buy" orders are sorted by price in a non-ascending order. "Sale" orders are sorted by price in a non-descending order. If the price is the same, id is deciding, i.e. we sort in ascending order by the time of adding the order to the Order Book.​ Additionally, if any transactions were made as a result of adding an order, they should be printed to stdout. We represent transactions as a JSON object with the following fields: buyOrderId, sellOrderId, price, quantity.

# Examples:

## First example - data

- For the following orders:

```json
{"type": "iceberg", "order": {"direction": "sell", "id": 1, "price": 100, "quantity": 200,"peak": 100}}
{"type": "iceberg", "order": {"direction": "sell", "id": 2, "price": 100, "quantity": 300,"peak": 100}}
{"type": "iceberg", "order": {"direction": "sell", "id": 3, "price": 100, "quantity": 200,"peak": 100}}
{"type": "iceberg", "order": {"direction": "buy", "id": 4, "price": 100, "quantity": 500,"peak": 100}}
```

- The final state of order book should be:

```json
{
  "sellOrders": [
    { "id": 3, "price": 100, "quantity": 100 },
    { "id": 2, "price": 100, "quantity": 100 }
  ],
  "buyOrders": []
}
```

## Second example - data

- input:

```json
{"type":"Limit","order":{"direction":"Buy","id":1,"price":14,"quantity":20}}

{"type":"Iceberg","order":{"direction":"Buy","id":2,"price":15,"quantity":50,"peak":20}}

{"type":"Limit","order":{"direction":"Sell","id":3,"price":16,"quantity":15}}

{"type":"Limit","order":{"direction":"Sell","id":4,"price":13,"quantity":60}}
```

- output:

```json
{"buyOrders": [{"id": 1, "price": 14, "quantity": 20}], "sellOrders": []}

{"buyOrders": [{"id": 2, "price": 15, "quantity": 20}, {"id": 1, "price": 14, "quantity": 20}], "sellOrders": []}

{"buyOrders": [{"id": 2, "price": 15, "quantity": 20}, {"id": 1, "price": 14, "quantity": 20}], "sellOrders": [{"id": 3, "price": 16, "quantity": 15}]}

{"buyOrders": [{"id": 1, "price": 14, "quantity": 10}], "sellOrders": [{"id": 3, "price": 16, "quantity": 15}]}

{"buyOrderId": 2, "sellOrderId": 4, "price": 15, "quantity": 20}
{"buyOrderId": 2, "sellOrderId": 4, "price": 15, "quantity": 20}
{"buyOrderId": 2, "sellOrderId": 4, "price": 15, "quantity": 10}
{"buyOrderId": 1, "sellOrderId": 4, "price": 14, "quantity": 10}
```

# General description how Iceberg orders work:

An iceberg order is an order that can be partially hidden from market view. Upon entry of the order, the participant must therefore specify the total order size and the visible “peak” size. The peak size is the maximum volume that will be shown to the market at any given instant. To maintain sufficient transparency in the market, a minimum peak size will be set, defined as a fraction of NMS for that stock. The trading system will manage the iceberg order by automatically introducing new full peaks into the matching algorithm and order book following complete execution of a revealed peak. Each time a new peak enters the order book, it is assigned a new timestamp and behaves in an identical manner to a conventional limit order. Acquisition of a new time stamp means that the hidden volume of an iceberg order loses time priority to other (visible) limit orders at the same price. As described above, however, the total volume (visible and hidden) of an iceberg order retains continuous price priority over all other volume at a strictly worse price.
