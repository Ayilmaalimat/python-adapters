import psycopg2

DB = psycopg2.connect(
  database="postgres", 
  user="postgres", 
  password="psql", 
  host="localhost", 
  port="5432",
)

cursor = DB.cursor()
