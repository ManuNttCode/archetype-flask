from flask import url_for

def test_root(client, app):
    with app.app_context():
            response = client.get(url_for('api.root'))
            assert response.status_code == 200
            assert response.get_json() == {'result': 'Funcionando!!!'}