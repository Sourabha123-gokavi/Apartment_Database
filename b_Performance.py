import random
import sqlite3
conn = sqlite3.connect('DBT24_A1_PES1UG21CS608_Sourabha_Gokavi.db')
c = conn.cursor()

def select_all_and_count(table_name):
    c.execute(f"SELECT * FROM {table_name}")
    rows = c.fetchall()
    row_count = len(rows)
    print(f"Table: {table_name} ({row_count} rows)")
    for row in rows:
        print(row)
    print("\n")

table_names = ["Tenants", "Apartments", "MaintenanceRequests", "Payments", "Employees"]

for table_name in table_names:
    select_all_and_count(table_name)

# Index scan 
c.execute("SELECT * FROM Tenants WHERE tenant_id = 100")  # Assuming tenant_id is indexed
print("Index Scan Example:")
print(c.fetchone())

# Table scan 
c.execute("SELECT * FROM Apartments WHERE num_bedrooms = 3")  # Assuming num_bedrooms is not indexed
print("\nTable Scan Example:")
print(c.fetchone())

# Multi-table join 
c.execute('''SELECT Tenants.name, Apartments.apartment_no, MaintenanceRequests.issue_description
            FROM Tenants
            JOIN Apartments ON Tenants.apartment_no = Apartments.apartment_no
            JOIN MaintenanceRequests ON MaintenanceRequests.apartment_no = Apartments.apartment_no
            WHERE MaintenanceRequests.status = 'Pending' ''')
print("\nMulti-table Join Example:")
print(c.fetchall())
conn.close()
