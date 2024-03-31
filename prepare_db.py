import pymysql

connection = pymysql.connect(host="localhost", user="root", password="root")
cursor = connection.cursor()

# Executing SQL query
cursor.execute("DROP DATABASE IF EXISTS books_db;")
cursor.execute("CREATE DATABASE IF NOT EXISTS books_db;")
cursor.execute("USE books_db;")
cursor.execute("CREATE TABLE books (book_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, book_title VARCHAR(50) NOT NULL, book_author VARCHAR(50));")
cursor.execute(f"INSERT INTO books (book_title, book_author) VALUES ('Python', 'CKMUDULI');")
cursor.execute("SELECT * FROM books;")
for book in cursor.fetchall():
    print(book)
connection.commit()
cursor.close()
connection.close()