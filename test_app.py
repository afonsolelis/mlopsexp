import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()  # Arrange: cria a aplicação
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    # Arrange: Preparação do ambiente já foi feita no fixture `client`

    # Act: Faz a requisição para a rota home ('/')
    response = client.get('/')

    # Assert: Verifica o código de status e o conteúdo da resposta
    assert response.status_code == 404
