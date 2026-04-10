from flask import Flask, render_template_string, request
import mysql.connector

app = Flask(__name__)

# DB connection
conn = mysql.connector.connect(
    host="<your-server>.mysql.database.azure.com",
    user="mysqladmin",
    password="<your-password>",
    database="myappdb"
)

html = """
<h2>Enter Name</h2>
<form method="POST">
    <input type="text" name="username">
    <button type="submit">Save</button>
</form>

{% if msg %}
<p>{{msg}}</p>
{% endif %}
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    msg = ""
    if request.method == 'POST':
        name = request.form.get('username')

        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
        conn.commit()

        msg = "Saved successfully!"

    return render_template_string(html, msg=msg)

if __name__ == "__main__":
    app.run()
