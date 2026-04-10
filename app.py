from flask import Flask, render_template_string, request
import mysql.connector
import os

app = Flask(__name__)

# DB connection using environment variables
conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    database=os.getenv("DB_NAME")
)

html = """
<h2>Enter Name</h2>
<form method="POST">
    <input type="text" name="username" required>
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
