from webtest import TestApp,AppError
import app
import pytest


class TestApplication:

    @pytest.fixture
    def test_client(self):
        return TestApp(app.app)

    def test_successful_echo(self,test_client):
        client = test_client
        response = client.get('/echo/hello')

        assert response.status_code == 200

    def test_echo_no_path_param_supplied(self,test_client):
        client = test_client
        with pytest.raises(AppError):
            client.get('/echo')

    def test_successful_query(self,test_client):
        client = test_client
        response = client.get('/queries?foo=bar')

        assert response.status_code == 200

    def test_query_no_params_supplied(self, test_client):
        client = test_client
        with pytest.raises(AppError):
            client.get('/queries')
