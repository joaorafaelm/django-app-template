import pytest
from procrastinate import testing
from procrastinate.contrib.django import procrastinate_app


@pytest.fixture
def app():
    in_memory = testing.InMemoryConnector()

    with procrastinate_app.current_app.replace_connector(in_memory) as app:
        yield app
