import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", password="root")

# c = db.cursor()

# c.execute("CREATE DATABASE crud_db")

# fetching all the databases
# c.execute("SHOW DATABASES")

# create_product_table = """CREATE TABLE `crud_db`.`products` (
#   `prod_id` INT NOT NULL AUTO_INCREMENT,
#   `prod_name` VARCHAR(45) NULL,
#   `category` VARCHAR(45) NULL,
#   `price` INT NULL,
#    PRIMARY KEY (`prod_id`))"""

# c.execute(create_product_table)

# c = db.cursor()

# c.execute("desc products")

# # printing all the databases
# for i in c:
#     print(i)


def connect_to_database():
    # Replace these values with your database connection details
    config = {
        "user": "root",
        "password": "root",
        "host": "localhost",
        "database": "crud_db",
    }
    return mysql.connector.connect(**config)


def create_record(cursor):
    insert_query = """INSERT INTO products (
                        prod_name,
                        category,
                        price) 
                        VALUES  (%s, %s, %s)"""
    data = ("Samsung 4k LED TV", "Television", "200000")
    cursor.execute(insert_query, data)
    print("Record inserted.")
    # data = [
    #     ("iPhone 15 pro", "Mobile", "120000"),
    #     ("Samsung 4k LED TV", "Television", "200000"),
    #     ("Sony WH-1000XM3", "Audio", "30000"),
    #     ("Macbook pro 16 (2024)", "Laptop", "180000"),
    # ]

def read_records(cursor):
    select_query = "SELECT * FROM products"
    cursor.execute(select_query)
    results = cursor.fetchall()
    for row in results:
        print(row)

def update_record(cursor):
    update_query = "UPDATE products SET price = %s WHERE prod_id = %s"
    data = ("120000", "1")
    cursor.execute(update_query, data)
    print("Record updated.")


def delete_record(cursor):
    delete_query = "DELETE FROM products WHERE prod_id = 1"
    # data = ("1")
    cursor.execute(delete_query)
    print("Record deleted.")

def main():
    connection = connect_to_database()
    cursor = connection.cursor()

    try:
        # create_record(cursor)
        # update_record(cursor)
        # delete_record(cursor)
        read_records(cursor)
        connection.commit()  # Commit the transaction after all operations
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()


if __name__ == "__main__":
    main()



# # execute the insert commands for all rows and commit to the database
# c.executemany(employeetbl_insert, data)
# db.commit()

# # finally closing the database connection
# db.close()






