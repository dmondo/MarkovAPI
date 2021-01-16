def test_app_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'hello world'
