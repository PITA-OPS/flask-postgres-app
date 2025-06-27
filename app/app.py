from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def index():
    try:
        conn = psycopg2.connect(
            host=os.environ.get('DB_HOST'),
            database=os.environ.get('DB_NAME'),
            user=os.environ.get('DB_USER'),
            password=os.environ.get('DB_PASS')
        )
        conn.close()
        return "Connected to PostgreSQL successfully!"
    except Exception as e:
        return f"Database connection failed: {str(e)}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
