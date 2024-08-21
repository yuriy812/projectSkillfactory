import json
from collections import Counter


def average_cost(prices):
    return sum(prices) / len(prices) if prices else 0


def average_cost_per_product(prices, quantities):
    if not quantities or len(prices) != len(quantities):
        return 0
    total_value = sum(p * q for p, q in zip(prices, quantities))
    total_quantity = sum(quantities)
    return round(total_value / total_quantity, 2) if total_quantity else 0


# Initialize variables
max_price = 0
max_order = ''
max_quantity = 0
max_quantity_order = ''
price_list = []
quantity_list = []
date_list = []
max_orders_by_date = {}
MAX_ORDER_QUANTITY = 20
user_order_counts = Counter()

# Read the JSON file and process orders
try:
    with open('order_juiy_2023.json', 'r') as my_file:
        orders = json.load(my_file)

        # Loop through orders to gather maximums and collect prices/quantities
        for order_num, orders_data in orders.items():
            price = orders_data['price']
            quantity = orders_data['quantity']
            date = orders_data['date']
            user_id = orders_data['user_id']

            # Check and update maximums
            if price > max_price:
                max_order = order_num
                max_price = price
                max_user_id = user_id

            if quantity > max_quantity:
                max_quantity_order = order_num
                max_quantity = quantity

                # Collect prices and quantities
            price_list.append(price)
            quantity_list.append(quantity)
            date_list.append(date)
            user_order_counts[user_id] += quantity  # Count total orders per user

            # Count orders by date
            if date in max_orders_by_date:
                max_orders_by_date[date] += 1
            else:
                max_orders_by_date[date] = 1

                # Determine the date with the maximum number of orders
        max_orders_date = max(max_orders_by_date, key=max_orders_by_date.get)

        # Calculate averages
        average_order_price = average_cost(price_list)
        average_product_cost = average_cost_per_product(price_list, quantity_list)

        # Find the user with the highest total order value
        user_total_cost = {user_id: 0 for user_id in user_order_counts.keys()}
        for order_num, orders_data in orders.items():
            user_total_cost[orders_data['user_id']] += orders_data['price'] * orders_data['quantity']

        highest_user_id = max(user_total_cost, key=user_total_cost.get)

        # Print results
        print(f'1. Номер заказа с самой большой стоимостью: {max_order}, стоимость заказа: {max_price}')
        print(
            f'2. Номер заказа с самым большим количеством товаров: {max_quantity_order}, количество товаров: {max_quantity}')
        print(f'3. В какой день в июле было сделано больше всего заказов: {max_orders_date}')
        print(f'4. Какой пользователь сделал самое большое количество заказов за июль: {highest_user_id}')
        print(f'5. У какого пользователя самая большая суммарная стоимость заказов за июль: {max_user_id}')
        print(f'6. Средняя стоимость заказа в июле: {average_order_price}')
        print(f'7. Средняя стоимость товара в июле: {average_product_cost}')

except FileNotFoundError:
    print("File not found. Please check the filename and path.")
except json.JSONDecodeError:
    print("Error decoding JSON. Please check the file format.")
