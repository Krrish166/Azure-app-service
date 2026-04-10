from flask import Flask, render_template_string, request

app = Flask(__name__)

html_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Azure Python App</title>
    <style>
        body {
            margin: 0;
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #667eea, #764ba2);
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            color: white;
        }

        .container {
            background: rgba(0,0,0,0.3);
            padding: 40px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 8px 30px rgba(0,0,0,0.3);
            width: 350px;
        }

        h1 {
            margin-bottom: 10px;
        }

        p {
            font-size: 14px;
            margin-bottom: 20px;
        }

        input {
            width: 80%;
            padding: 10px;
            border: none;
            border-radius: 8px;
            margin-bottom: 15px;
            outline: none;
        }

        button {
            padding: 10px 20px;
            border: none;
            border-radius: 8px;
            background: #ff7eb3;
            color: white;
            font-weight: bold;
            cursor: pointer;
            transition: 0.3s;
        }

        button:hover {
            background: #ff4f9a;
        }

        .result {
            margin-top: 20px;
            font-size: 18px;
            color: #ffd369;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>🚀 Azure App</h1>
    <p>Enter your name</p>

    <form method="POST">
        <input type="text" name="username" placeholder="Your name..." required>
        <br>
        <button type="submit">Submit</button>
    </form>

    {% if name %}
        <div class="result">
            Hello, {{name}} 👋
        </div>
    {% endif %}
</div>

</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def home():
    name = None
    if request.method == 'POST':
        name = request.form.get('username')
    return render_template_string(html_page, name=name)

if __name__ == "__main__":
    app.run()
