from flask import Flask, render_template_string, request

app = Flask(__name__)

html_page = """
<!DOCTYPE html>
<html>
<head>
    <title>Azure Pro App</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', sans-serif;
        }

        body {
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            background: linear-gradient(135deg, #1e3c72, #2a5298);
        }

        .card {
            backdrop-filter: blur(15px);
            background: rgba(255, 255, 255, 0.1);
            padding: 40px;
            border-radius: 20px;
            text-align: center;
            color: white;
            width: 380px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.4);
        }

        h1 {
            margin-bottom: 10px;
        }

        p {
            margin-bottom: 20px;
            font-size: 14px;
            opacity: 0.8;
        }

        input {
            width: 100%;
            padding: 12px;
            border-radius: 10px;
            border: none;
            margin-bottom: 20px;
            outline: none;
            font-size: 14px;
        }

        button {
            width: 100%;
            padding: 12px;
            border: none;
            border-radius: 10px;
            background: linear-gradient(45deg, #ff6a00, #ee0979);
            color: white;
            font-weight: bold;
            cursor: pointer;
            transition: 0.3s;
        }

        button:hover {
            transform: scale(1.05);
        }

        .result {
            margin-top: 20px;
            font-size: 18px;
            color: #ffd369;
        }
    </style>
</head>
<body>

<div class="card">
    <h1>🚀 Azure Pro App</h1>
    <p>Enter your name to continue</p>

    <form method="POST">
        <input type="text" name="username" placeholder="Your name..." required>
        <button type="submit">Continue</button>
    </form>

    {% if name %}
        <div class="result">
            Welcome, {{name}} 👋
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
