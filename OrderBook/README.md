<!-- TOC -->

- [How to run `order_book.py` script](#how-to-run-order_bookpy-script)
- [Software requirements](#software-requirements)
- [Example of input data](#example-of-input-data)
- [More business logic and explanation](#more-business-logic-and-explanation)
- [Additional thoughts - optimization](#additional-thoughts---optimization)

<!-- /TOC -->

## How to run `order_book.py` script

Firstly you need to be in OrderBook directory and then execute:

`./process_records.zsh`

This is zsh script that reads from standard input and save data to `data.json` file.

Additionally you can use definied function in `process_records.zsh` script:

- `clear` : that will delete everything from `data.json` file

- `edit_record` : this will update selected record

- `remove_record` : this will remove selected record from order book (`data.json` file)

Each time new order is added / removed or updated then `order_book.py` script will be executed and final status of order book will be displayed.

As additional feature of `process_records.zsh` - input orders are also saved to `history.json` file.

## Software requirements

- jq (https://stedolan.github.io/jq/) is installed

## Example of input data

```json
{"type": "iceberg", "order": {"direction": "sell", "id": 1, "price": 100, "quantity": 200,"peak": 100}}
{"type": "iceberg", "order": {"direction": "sell", "id": 2, "price": 100, "quantity": 300,"peak": 100}}
{"type": "iceberg", "order": {"direction": "sell", "id": 3, "price": 100, "quantity": 200,"peak": 100}}
{"type": "iceberg", "order": {"direction": "buy", "id": 4, "price": 100, "quantity": 500,"peak": 100}}
```

- After each new order is pasted to stdin press Enter / Return on your keyboard.

- When you want stop program presss CTRL+D

## More business logic and explanation

Explanations and examples could be found in `general_description.md` file.

## Additional thoughts - optimization

From efficient data sturucture perspective it seems to be good idea to use heapq (https://docs.python.org/3/library/heapq.html) liblary.

Nevertheless in `cons.md` file has been written some optimization steps that could be perfect fit for tasj simillar to this one.

As PoC of using heapq one function has been developed: `alternative.md`. But that was not tested in end-to-end solution.
