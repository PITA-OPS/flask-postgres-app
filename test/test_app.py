import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../app')))

import app as flask_app

def test_index():
    flask_app.app.testing = True
    client = flask_app.app.test_client()
    response = client.get('/')
    assert response.status_code == 200
