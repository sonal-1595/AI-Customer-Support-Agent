import random
from datetime import datetime

def track_order(order_id):
    # Simulate order tracking data
    statuses = ["Processing", "Shipped", "Out for Delivery", "Delivered"]
    current_status = random.choice(statuses)
    estimated_delivery = datetime.now().strftime("%Y-%m-%d")  # Simulate today's date for delivery

    response = f"Order ID: {order_id}\nCurrent Status: {current_status}\nEstimated Delivery Date: {estimated_delivery}"
    return response

def order_status_tool(query):
    # Extract order ID from the query (this is a simple simulation)
    order_id = query.split()[-1]  # Assume the last word is the order ID
    return track_order(order_id)

if __name__ == "__main__":    
    user_query = input("Please enter your order tracking query (e.g., 'Track order 12345'): ")
    result = order_status_tool(user_query)
    print(result)