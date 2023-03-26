from app.order_book import (
    InitialData,
    IcebergOrder,
    LimitOrder,
    OrderDataFactory,
    OrderBook,
)
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))


# You can create your own JSON file for testing purposes
test_json = """
[
    {
        "type": "Iceberg",
        "order": {
            "direction": "Buy",
            "id": 1,
            "price": 100,
            "quantity": 200,
            "peak": 50
        }
    },
    {
        "type": "Limit",
        "order": {
            "direction": "Sell",
            "id": 2,
            "price": 90,
            "quantity": 120
        }
    }
]
"""

with open("test_data.json", "w") as f:
    f.write(test_json)


def test_read_json_from_file():
    data = InitialData.read_json_from_file("test_data.json")
    assert len(data) == 2
    assert data[0]["type"] == "Iceberg"
    assert data[1]["type"] == "Limit"


def test_create_order_objects_from_json():
    buy_orders, sell_orders = OrderDataFactory.create_order_objects_from_json(
        "test_data.json"
    )
    assert len(buy_orders) == 1
    assert len(sell_orders) == 1

    buy_order = buy_orders[1]
    assert isinstance(buy_order, IcebergOrder)
    assert buy_order.direction == "Buy"
    assert buy_order.order_id == 1
    assert buy_order.price == 100
    assert buy_order.quantity == 200
    assert buy_order.peak == 50

    sell_order = sell_orders[2]
    assert isinstance(sell_order, LimitOrder)
    assert sell_order.direction == "Sell"
    assert sell_order.order_id == 2
    assert sell_order.price == 90
    assert sell_order.quantity == 120


def test_match_orders():
    buy_orders, sell_orders = OrderDataFactory.create_order_objects_from_json(
        "test_data.json"
    )
    sorted_buy_orders, sorted_sell_orders = OrderDataFactory.sort_orders(
        buy_orders, sell_orders
    )
    matched_orders = OrderBook.match_orders(sorted_buy_orders, sorted_sell_orders)

    assert len(matched_orders) == 1
    buy_order, sell_order = matched_orders[0]
    assert buy_order.order_id == 1
    assert sell_order.order_id == 2


def test_clear_order_book():
    buy_orders, sell_orders = OrderDataFactory.create_order_objects_from_json(
        "test_data.json"
    )
    sorted_buy_orders, sorted_sell_orders = OrderDataFactory.sort_orders(
        buy_orders, sell_orders
    )
    cleaned_buy_orders, cleaned_sell_orders = OrderBook.clear_order_book(
        sorted_buy_orders, sorted_sell_orders
    )

    assert len(cleaned_buy_orders) == 1
    assert len(cleaned_sell_orders) == 1
    assert cleaned_buy_orders[0].quantity == 80
    assert cleaned_sell_orders[0].quantity == 0
