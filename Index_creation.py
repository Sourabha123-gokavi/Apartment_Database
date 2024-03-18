import sqlite3
conn = sqlite3.connect('DBT24_A1_PES1UG21CS608_Sourabha_Gokavi.db')
c = conn.cursor()
# Creatig the indexe on the Tenants table
c.execute("CREATE INDEX IF NOT EXISTS idx_tenant_apartment_no ON Tenants (apartment_no)")
c.execute("CREATE INDEX IF NOT EXISTS idx_tenant_contact_number ON Tenants (contact_number)")

# Creating the indexe on the Apartments table
c.execute("CREATE INDEX IF NOT EXISTS idx_apartment_num_bedrooms ON Apartments (num_bedrooms)")

# Creating the indexe on the MaintenanceRequests table
c.execute("CREATE INDEX IF NOT EXISTS idx_maintenance_apartment_no ON MaintenanceRequests (apartment_no)")
c.execute("CREATE INDEX IF NOT EXISTS idx_maintenance_status ON MaintenanceRequests (status)")
conn.commit()

#query part
c.execute('''EXPLAIN QUERY PLAN
             SELECT * FROM Tenants WHERE apartment_no = "A456" ''')
print("Query Plan without Index:")
print(c.fetchall())

# Runnig the query with index
c.execute('''EXPLAIN QUERY PLAN
             SELECT * FROM Tenants WHERE apartment_no = 'A456' ''')
print("\nQuery Plan with Index:")
print(c.fetchall())

conn.close()
