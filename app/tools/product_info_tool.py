def get_product_info(product_id):
    # Simulate product information retrieval
    products = {
        "101": {"name": "Wireless Mouse", "price": "$25.99", "stock": "Available"},
        "102": {"name": "Bluetooth Headphones", "price": "$59.99", "stock": "Out of Stock"},
        "103": {"name": "USB-C Charger", "price": "$19.99", "stock": "Available"},
    }
    
    product_info = products.get(product_id, None)
    
    if product_info:
        response = f"Product ID: {product_id}\nName: {product_info['name']}\nPrice: {product_info['price']}\nStock Status: {product_info['stock']}"
    else:
        response = f"Product with ID {product_id} not found."
    
    return response

if __name__ == "__main__":
    user_query = input("Please enter the product ID to get information (e.g., 'Get product info 101'): ")
    product_id = user_query.split()[-1]  # Assume the last word is the product ID
    result = get_product_info(product_id)
    print(result)