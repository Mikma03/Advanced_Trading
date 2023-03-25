import heapq


class OrderBook:
    @staticmethod
    def match_orders(
        buy_orders: list[Union[IcebergOrder, LimitOrder]],
        sell_orders: list[Union[IcebergOrder, LimitOrder]],
    ) -> List[tuple[Union[IcebergOrder, LimitOrder], Union[IcebergOrder, LimitOrder]]]:
        matched_orders = []

        buy_heap = [(-order.price, order.order_id, order) for order in buy_orders]
        sell_heap = [(order.price, order.order_id, order) for order in sell_orders]

        heapq.heapify(buy_heap)
        heapq.heapify(sell_heap)

        while buy_heap and sell_heap:
            max_buy_price, _, buy_order = heapq.heappop(buy_heap)
            min_sell_price, _, sell_order = heapq.heappop(sell_heap)

            if -max_buy_price >= min_sell_price:
                matched_quantity = OrderBook.calculate_matched_quantity(
                    buy_order, sell_order
                )

                if matched_quantity > 0:
                    matched_orders.append((buy_order, sell_order))

                    OrderBook.subtract_matched_amount(
                        [(buy_order, sell_order, matched_quantity)]
                    )

                    if buy_order.quantity > 0:
                        heapq.heappush(
                            buy_heap, (-buy_order.price, buy_order.order_id, buy_order)
                        )

                    if sell_order.quantity > 0:
                        heapq.heappush(
                            sell_heap,
                            (sell_order.price, sell_order.order_id, sell_order),
                        )

            else:
                heapq.heappush(
                    buy_heap, (-max_buy_price, buy_order.order_id, buy_order)
                )
                heapq.heappush(
                    sell_heap, (min_sell_price, sell_order.order_id, sell_order)
                )
                break

        return matched_orders
