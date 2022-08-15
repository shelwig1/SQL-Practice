import mysql.connector
from mysql.connector import Error
import pandas as pd

#run loop that asks for host, user and pass, then we have a python interface with
#the database

def create_server_connection(host_name, user_name, user_password):
	connection = None
	try:
		connection = mysql.connector.connect(
			host = host_name,
			user = user_name,
			passwd = user_password
		)

		print("MySQL Database connection successful")

	except Error as err:
		print(f"Error: '{err}'")

	return connection



def create_db_connection(host_name, user_name, user_password, db_name):
	connection = None
	try:
		connection = mysql.connector.connect(
			host = host_name,
			user = user_name,
			passwd = user_password,
			database = db_name
		)

		print("MySQL Database connection successful")

	except Error as err:
		print(f"Error: '{err}'")

	return connection



def create_database(connection, query):
	cursor = connection.cursor()
	try:
		cursor.execute(query)
		print("Database created successfully")

	except Error as err:
		print(f"Error: '{err}'")



def execute_query(connection,query):
	cursor = connection.cursor()
	try:
		cursor.execute(query)
		connection.commit()
		print("Query successful")
	except Error as err:
		print(f"Error: '{err}'")


connection = create_server_connection("localhost","root","password")

create_database_query = "CREATE DATABASE school"
create_database(connection, create_database_query)


create_teacher_table = """
CREATE TABLE teacher (
  teacher_id INT PRIMARY KEY,
  first_name VARCHAR(40) NOT NULL,
  last_name VARCHAR(40) NOT NULL,
  language_1 VARCHAR(3) NOT NULL,
  language_2 VARCHAR(3),
  dob DATE,
  tax_id INT UNIQUE,
  phone_no VARCHAR(20)
  );
 """

connection = create_db_connection("localhost", "root", "password","school") 
execute_query(connection, create_teacher_table) # Execute our defined query


create_client_table = """
CREATE TABLE client (
  client_id INT PRIMARY KEY,
  client_name VARCHAR(40) NOT NULL,
  address VARCHAR(60) NOT NULL,
  industry VARCHAR(20)
);
 """

create_participant_table = """
CREATE TABLE participant (
  participant_id INT PRIMARY KEY,
  first_name VARCHAR(40) NOT NULL,
  last_name VARCHAR(40) NOT NULL,
  phone_no VARCHAR(20),
  client INT
);
"""

create_course_table = """
CREATE TABLE course (
  course_id INT PRIMARY KEY,
  course_name VARCHAR(40) NOT NULL,
  language VARCHAR(3) NOT NULL,
  level VARCHAR(2),
  course_length_weeks INT,
  start_date DATE,
  in_school BOOLEAN,
  teacher INT,
  client INT
);
"""


connection = create_db_connection("localhost", "root", pw, db)
execute_query(connection, create_client_table)
execute_query(connection, create_participant_table)
execute_query(connection, create_course_table)