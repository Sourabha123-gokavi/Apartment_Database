import sqlite3
import random
conn = sqlite3.connect('DBT24_A1_PES1UG21CS608_Sourabha_Gokavi.db')
c = conn.cursor()

def generate_indian_name():
    first_names = ["Aditya", "Aarav", "Aanya", "Arjun", "Aisha", "Amit", "Deepika", "Dev", "Esha", "Gautam", "Ishaan", "Kavya", "Krish", 
    "Meera", "Neha", "Nikhil", "Priya", "Rahul", "Riya", "Sahil", "Shreya", "Tanvi", "Varun", "Vidya", "Yash"]
    last_names = ["Agarwal", "Bhatt", "Chopra", "Desai", "Gupta", "Joshi", "Kumar", "Mishra", "Patel", "Sharma", "Singh", "Verma"]
    return random.choice(first_names) + " " + random.choice(last_names)

for i in range(1, 10001):
    name = generate_indian_name()
    apartment_no = "A" + str(random.randint(1, 1000))
    contact_number = "+91" + str(random.randint(6000000000, 9999999999))
    c.execute("INSERT INTO Tenants (name, apartment_no, contact_number) VALUES (?, ?, ?)", (name, apartment_no, contact_number))

for i in range(1, 1001):
    apartment_no = "A" + str(i)
    num_bedrooms = random.randint(1, 4)
    rent_amount = random.uniform(10000, 50000)
    c.execute("INSERT INTO Apartments (apartment_no, num_bedrooms, rent_amount) VALUES (?, ?, ?)", (apartment_no, num_bedrooms, rent_amount))

for i in range(1, 10001):  
    apartment_no = "A" + str(random.randint(1, 1000))
    issue_description = "Issue #" + str(i)
    request_date = "2024-03-18"  # Example date
    status = random.choice(["Pending", "In Progress", "Completed"])
    c.execute("INSERT INTO MaintenanceRequests (apartment_no, issue_description, request_date, status) VALUES (?, ?, ?, ?)", (apartment_no, issue_description, request_date, status))

for i in range(1, 5001):
    tenant_id = random.randint(1, 10000)
    amount = random.uniform(5000, 20000)
    payment_date = "2024-03-18"  # Example date
    c.execute("INSERT INTO Payments (tenant_id, amount, payment_date) VALUES (?, ?, ?)", (tenant_id, amount, payment_date))

for i in range(1, 101):
    name = generate_indian_name()
    position = random.choice(["Manager", "Maintenance Staff", "Security Guard"])
    contact_number = "+91" + str(random.randint(6000000000, 9999999999))
    c.execute("INSERT INTO Employees (name, position, contact_number) VALUES (?, ?, ?)", (name, position, contact_number))
conn.commit()
conn.close()
