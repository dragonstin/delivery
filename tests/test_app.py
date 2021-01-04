
def test_app_is_created(app):
    assert app.name == 'delivery.app'


def test_config_is_loaded(config):
    assert config["DEBUG"] is False


def test_request_returns_404(client):
    assert client.get("/url_not_exists").status_code == 404


# Live server is the way to use selenium
#def test_real_request(live_server):