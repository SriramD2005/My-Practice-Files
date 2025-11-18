import sqlite3
import pandas as pd

# Step 1: Load CSV into pandas DataFrame
df = pd.read_csv('your_file.csv')

# Step 2: Create SQLite in-memory database
conn = sqlite3.connect(':memory:')

# Step 3: Load DataFrame into SQLite
df.to_sql('data', conn, index=False, if_exists='replace')

# Step 4: Query the data
query = "SELECT * FROM data WHERE column_name = 'some_value'"
result = pd.read_sql_query(query, conn)
print(result)

# Step 5: Close the connection
conn.close()