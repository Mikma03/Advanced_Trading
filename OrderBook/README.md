<!-- TOC -->

- [How to run `order_book.py` script](#how-to-run-order_bookpy-script)
  - [**Standard approach**](#standard-approach)
  - [**Docker container**](#docker-container)
- [Software requirements](#software-requirements)
- [Example of input data](#example-of-input-data)
- [More business logic and explanation](#more-business-logic-and-explanation)
- [Additional thoughts - optimization](#additional-thoughts---optimization)
- [TODO](#todo)
- [Other instruction for developers](#other-instruction-for-developers)
  - [pre-commit](#pre-commit)
  - [Tests](#tests)
- [Additional resources](#additional-resources)

<!-- /TOC -->

## How to run `order_book.py` script

---

### **Standard approach**

---

Firstly you need to be in the `OrderBook/app` directory and then execute in the terminal the following command:

> `./process_records.zsh`

This is a zsh script that reads from standard input and saves data to a `data.json` file. In the backgroud `order_book.py` program will be running.

Additionally, you can use defined functions in the `process_records.zsh` script (this is additional funcionallity):

- `clear` : that will delete everything from `data.json`

- `edit_record` : this will update selected record

- `remove_record` : this will remove a selected record from order book (`data.json`)

Each time a new order is added/removed or updated the `order_book.py` script will be executed and the final status of the order book will be displayed to standard output (in so called standard approach).

As an additional feature of `process_records.zsh` - input orders are also saved to the `history.json` file. For tracking purposes.

---

### **Docker container**

---

As an alternative approach, docker image was built. The assumption here is that you have Docker / Docker Desktop installed on your machine. Then easily, the docker image could be built from `Dockerfile` which is part of this folder. With following instructions.

Docker container is built based on official images. Moreover, as a simple way to interact with running containers Flask app was developed. You can get access to running image in your web browser on `5001` port - local host.

Go to root directory (Dockerfile level) and next:

> `docker build -t order_book_image .`

> `docker run -d --name order_book_container -p 5001:5001 order_book_image`

You can acess that under following http:

> `http://127.0.0.1:5001`

When you want to stop docker container

> `docker stop order_book_container`

When you want delete docker container

> `docker -rm order_book_container`

This way of building app has almost the same functionality as standard approach. Nevertheless there are some differences:

- each time when you want provide new record, you need to manually delete previous one

- you do not have functionality to update or delete particullar record

- you can clear `data.json` file just providing `clear` key word to box

- as output you will receive final status of order book and matched orders (ransactions) but that is not formatted

---

## Software requirements

---

- jq (https://stedolan.github.io/jq/) need to be installed

- pytest (https://pypi.org/project/pytest/) need to be installed

## Example of input data

---

```json
{"type": "iceberg", "order": {"direction": "sell", "id": 1, "price": 100, "quantity": 200,"peak": 100}}
{"type": "iceberg", "order": {"direction": "sell", "id": 2, "price": 100, "quantity": 300,"peak": 100}}
{"type": "iceberg", "order": {"direction": "sell", "id": 3, "price": 100, "quantity": 200,"peak": 100}}
{"type": "iceberg", "order": {"direction": "buy", "id": 4, "price": 100, "quantity": 500,"peak": 100}}
```

- After each new order is pasted to stdin press Enter / Return on your keyboard (docker approach is different at this point, please read above)

- When you want to stop program press CTRL+D (I'm using UNIX base OS)

## More business logic and explanation

---

Explanations and examples could be found in the `general_description.md` file. Where description was provided. The reader wants to read this file twice before attempting to understand the implementation.

## Additional thoughts - optimization

---

From an efficient data structure perspective it seems to be a good idea to use heapq (https://docs.python.org/3/library/heapq.html) library.

Nevertheless in the `cons.md` file has been written some optimization steps that could be a perfect fit for a task similar to this one.

As PoC of using heapq one function has been developed: `alternative_match_orders.py`. But that was not tested in an end-to-end solution.

## TODO

---

- Formatting: to be in line with description of the task. As it is not implemented yet: final OrderBook status and transactions

## Other instruction for developers

---

### pre-commit

---

- Install `pre-commit` tool by running `pip install pre-commit`.

- Create a `.pre-commit-config.yaml` file in the root directory of the project.

- Define the pre-commit hooks you want to use in the file, using the appropriate syntax.

- Run `pre-commit install` to install the hooks specified in the configuration file to the project's Git repository.

- Run `pre-commit run` to execute the hooks on the files that are about to be committed.

---

### Tests

---

Tests are in `OrderBook/tests`. Pytest was used for those purposes.

In your terminal, make sure you are in the OrderBook directory:

> `cd OrderBook`

Run the tests from the OrderBook directory:

> `pytest tests/test_generic.py`

or

> `pytest tests/test_orderbook.py`

---

## Additional resources

---

Reinforcement Learning and OrderBook example and mathematical proof.

- https://stanford.edu/~ashlearn/RLForFinanceBook/chapter9.pdf
