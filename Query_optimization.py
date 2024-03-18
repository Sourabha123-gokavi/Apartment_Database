# query optimization with varied join order
import sqlite3
import time
# Connect to the SQLite database
conn = sqlite3.connect('DBT24_A1_PES1UG21CS608_Sourabha_Gokavi.db')
c = conn.cursor()

# query 
query = '''
        SELECT t.name, a.apartment_no, m.issue_description
        FROM Tenants t
        JOIN Apartments a ON t.apartment_no = a.apartment_no
        JOIN MaintenanceRequests m ON m.apartment_no = a.apartment_no
        WHERE m.status = 'Pending'
        '''
# calculating the time
# query execution before optimization
start_time = time.time()
c.execute(query)
result_before = c.fetchall()
before = time.time() - start_time
print("Time(Before):", before)

# changing the join order
# Changing join order and using LEFT OUTER JOIN
new_qurey = '''
                SELECT t.name, a.apartment_no, m.issue_description
                FROM MaintenanceRequests m
                LEFT OUTER JOIN Apartments a ON m.apartment_no = a.apartment_no
                JOIN Tenants t ON t.apartment_no = a.apartment_no
                WHERE m.status = 'Pending'
                '''
                # calculatin the time 
start_time = time.time()
c.execute(new_qurey)
result_after = c.fetchall()
new_time = time.time() - start_time
print("Time(After):", new_time)

print("Optimized or not (Trur / False)---->", new_time<before)

conn.close()
