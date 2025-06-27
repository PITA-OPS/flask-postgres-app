import os
import app as flask_app

def test_index():
    os.environ['DB_HOST'] = 'localhost'
    os.environ['DB_NAME'] = 'flaskdb'
    os.environ['DB_USER'] = 'flaskuser'
    os.environ['DB_PASS'] = 'flaskpass'
    client = flask_app.app.test_client()
    response = client.get('/')
    assert response.status_code == 200
