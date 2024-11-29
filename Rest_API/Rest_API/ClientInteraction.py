import requests
import json

BASE_URL = "http://127.0.0.1:8000/api/products."

def add_product(name, description, price):
    product_data = {
        "name": name,
        "description": description,
        "price":price
    }
    response = requests.post(BASE_URL, json=product_data)

    if response.status_code == 201:
        print("Woohoo! Product added successfully!")
        print("Response:", response.json())

    elif response.status_code == 400:
        print("Oops! Something went wrong. Failed to add product")
        print("Error details:", response.json())

    else: 
        print("Try again later")

def get_all_products():
    response = requests.get(BASE_URL)

    if response.status_code == 200:
        print("Products fetched successfully!")
        products = response.json()
        print("This are the list of products: ")
        for product in products:
            print(f"ID: {product['id]']}, Name: {product['name']}, Description: {product['description']}, Price: {product['price']}")

    else:
        print(f"Failed to fetch products. Status code:, response.status_code")
        print("Error details:", response.json())

#Example
if __name__ == "__main__":
    
    #Adds a new product 
    add_product("Cartoon", "Spongebob", 2000.0)
    
    # Retrieve and print all products
    get_all_products()