import json

import mock

from api import api

test_client = api.APP.test_client()


def test_hello_api():
    """Docstring in public method."""
    rv = test_client.get("/api/get_message")
    assert rv.status_code == 200
    assert json.loads(rv.data) == {"message": "Hello, World!"}


@mock.patch("api.api.APP.run")
def test_main(mock_run):
    """Docstring in public method."""
    api.main()
    mock_run.assert_called_with(debug=False, host="0.0.0.0", port=8000)
