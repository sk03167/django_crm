import psycopg2

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="xmtjk2w288",
    host="localhost",
    port="5432"
)

# Create a cursor object using the connection
cur = conn.cursor()

cur.execute("SELECT datname FROM pg_database")
# Fetch all rows from the result set
rows = cur.fetchall()

# Print the list of databases
print("List of databases:")
for row in rows:
    print(row[0])

# Close the cursor and connection
cur.close()
conn.close()