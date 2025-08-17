from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>DevOps Final</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #6a11cb, #2575fc);
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .card {
                background: rgba(255, 255, 255, 0.1);
                padding: 30px;
                border-radius: 15px;
                text-align: center;
                box-shadow: 0 8px 20px rgba(0,0,0,0.3);
            }
            h1 {
                font-size: 2.5rem;
                margin-bottom: 10px;
            }
            p {
                font-size: 1.2rem;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Scarlette te dice 'HOLA'</h1>
            <p>CI/CD funcionando con Flask, Docker y Render</p>
        </div>
    </body>
    </html>
    """
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


