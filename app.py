from flask import Flask, render_template, request, redirect, url_for
import pymysql

# Establish db Connection...
connection = pymysql.connect(
    host="localhost", user="root", password="root", database="books_db"
)

# Create cursor object...
cursor = connection.cursor()

app = Flask(__name__)


@app.route("/")
def home():
    cursor.execute("SELECT * FROM books;")
    details = cursor.fetchall()
    return render_template("home.html", details=tuple(enumerate(details)))


@app.route("/add", methods=["GET", "POST"])
def add_books():
    if request.method == "POST":
        book_title = request.form.get("book_title")
        book_author = (
            request.form.get("book_author") if request.form.get("book_author") else None
        )
        if book_author:
            cursor.execute(
                f"INSERT INTO books (book_title, book_author) VALUES ('{book_title}','{book_author}');"
            )
        else:
            cursor.execute(
                f"INSERT INTO books (book_title, book_author) VALUES ('{book_title}',null);"
            )
        connection.commit()
        return redirect(url_for("home"))

    return render_template("add_books.html")


@app.route("/delete", methods=["GET", "POST"])
def del_books():
    def del_records(col: str, val):
        cursor.execute(f"delete from books where {col} = '{val}';")
        connection.commit()

    if request.method == "POST":
        if "book_id" in request.form:
            book_id = request.form.get("book_id")
            del_records("book_id", book_id)
        elif "book_title" in request.form:
            book_title = request.form.get("book_title")
            del_records("book_title", book_title)
        elif "book_author" in request.form:
            book_author = request.form.get("book_author")
            del_records("book_author", book_author)
        return redirect(url_for("home"))
    return render_template("delete_books.html")


@app.route("/update", methods=["GET", "POST"])
def update_books():
    if request.method == "POST":
        if "book_id_h" in request.form:
            book_id = request.form.get("book_id_h")
            cursor.execute(f"SELECT * FROM books WHERE book_id = '{book_id}';")
            details = cursor.fetchone()
            return render_template(
                "update_books.html", details=details, book_id=book_id
            )
        else:
            book_id = request.form.get("book_id")
            book_title = request.form.get("book_title")
            book_author = (
                None
                if request.form.get("book_author") == ""
                else request.form.get("book_author")
            )
            if book_author:
                cursor.execute(
                    f"UPDATE books SET book_title = '{book_title}', book_author = '{book_author}' WHERE book_id = '{book_id}'"
                )
            else:
                cursor.execute(
                    f"UPDATE books SET book_title = '{book_title}', book_author = null WHERE book_id = '{book_id}'"
                )

            connection.commit()
            return redirect(url_for("home"))
    return render_template("update_books.html")


if __name__ == "__main__":
    app.run(debug=True)
    # Close cursor and connection...
    cursor.close()
    connection.close()
