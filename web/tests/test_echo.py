import os
import tempfile

import pytest

from . import echo


@pytest.fixture
def client():
    # db_fd, echo.app.config['SQLALCHEMY_DATABASE_URI'] = ':memory:'
    echo.app.config['SQLALCHEMY_DATABASE_URI'] = ':memory:'
    echo.app.config['TESTING'] = True

    with echo.app.test_client() as client:
        with echo.app.app_context():
            echo.db.create_all()
        yield client

    # os.close(db_fd)
    os.unlink(echo.app.config['DATABASE'])


def test_empty_db(client):
    """Start with a blank database."""

    rv = client.get('/')
    import pdb
    pdb.set_trace()
    assert b'No entries here so far' in rv.data
