from app.order_book import (
    InitialData,
    Order,
    IcebergOrder,
    LimitOrder,
)
import sys
import pytest
import json
from typing import Literal
from pathlib import Path


sys.path.insert(0, str(Path(__file__).parent.parent))


def test_read_json_from_file(tmp_path: Path):
    test_data = [
        {
            "type": "Iceberg",
            "order": {
                "direction": "Buy",
                "id": 1,
                "price": 100,
                "quantity": 200,
                "peak": 50,
            },
        },
    ]
    test_file = tmp_path / "test.json"
    test_file.write_text(json.dumps(test_data))

    result = InitialData.read_json_from_file(str(test_file))
    assert result == test_data


@pytest.mark.parametrize(
    "order_type, direction, order_id, price, quantity",
    [
        ("Iceberg", "Buy", 1, 100, 200),
        ("Limit", "Sell", 2, 110, 150),
    ],
)
def test_order_init(
    order_type: Literal["Iceberg", "Limit"],
    direction: Literal["Buy", "Sell"],
    order_id: Literal[1, 2],
    price: Literal[100, 110],
    quantity: Literal[200, 150],
):
    order = Order(order_type, direction, order_id, price, quantity)
    assert order.order_type == order_type
    assert order.direction == direction
    assert order.order_id == order_id
    assert order.price == price
    assert order.quantity == quantity


@pytest.mark.parametrize(
    "direction, order_id, price, quantity, peak",
    [
        ("Buy", 1, 100, 200, 50),
        ("Sell", 2, 110, 150, 30),
    ],
)
def test_iceberg_order_init(
    direction: Literal["Buy", "Sell"],
    order_id: Literal[1, 2],
    price: Literal[100, 110],
    quantity: Literal[200, 150],
    peak: Literal[50, 30],
):
    order = IcebergOrder(direction, order_id, price, quantity, peak)
    assert order.direction == direction
    assert order.order_id == order_id
    assert order.price == price
    assert order.quantity == quantity
    assert order.peak == peak


@pytest.mark.parametrize(
    "direction, order_id, price, quantity",
    [
        ("Buy", 1, 100, 200),
        ("Sell", 2, 110, 150),
    ],
)
def test_limit_order_init(
    direction: Literal["Buy", "Sell"],
    order_id: Literal[1, 2],
    price: Literal[100, 110],
    quantity: Literal[200, 150],
):
    order = LimitOrder(direction, order_id, price, quantity)
    assert order.direction == direction
    assert order.order_id == order_id
    assert order.price == price
    assert order.quantity == quantity
