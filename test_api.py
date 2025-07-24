import requests
import json

BASE_URL = 'http://127.0.0.1:8000/api/customers/'

def create_customer(name, phone, balance):
    data = {
        'name': name,
        'phone': phone,
        'balance': balance
    }
    response = requests.post(BASE_URL, json=data)
    print(f"Created customer: {response.status_code}")
    print(response.json())
    return response.json()

def get_all_customers():
    response = requests.get(BASE_URL)
    print(f"All customers: {response.status_code}")
    print(json.dumps(response.json(), indent=2))
    return response.json()

def get_customer(customer_id):
    response = requests.get(f"{BASE_URL}{customer_id}/")
    print(f"Get customer {customer_id}: {response.status_code}")
    print(json.dumps(response.json(), indent=2))
    return response.json()

def update_customer(customer_id, data):
    response = requests.patch(f"{BASE_URL}{customer_id}/", json=data)
    print(f"Update customer {customer_id}: {response.status_code}")
    print(json.dumps(response.json(), indent=2))
    return response.json()

def delete_customer(customer_id):
    response = requests.delete(f"{BASE_URL}{customer_id}/")
    print(f"Delete customer {customer_id}: {response.status_code}")
    return response.status_code

# Test the API
if __name__ == "__main__":
    # Create some customers
    customer1 = create_customer("John Doe", "123-456-7890", 1000.50)
    customer2 = create_customer("Jane Smith", "987-654-3210", 2500.75)
    customer3 = create_customer("Bob Johnson", "555-123-4567", 750.25)
    
    # Get all customers
    all_customers = get_all_customers()
    
    # Get a specific customer
    if all_customers and len(all_customers) > 0:
        customer_id = all_customers[0]['id']
        get_customer(customer_id)
        
        # Update a customer
        update_data = {'balance': 1500.00}
        update_customer(customer_id, update_data)
        
        # Delete a customer
        if len(all_customers) > 1:
            delete_customer(all_customers[-1]['id'])
    
    # Get all customers again to see changes
    get_all_customers()