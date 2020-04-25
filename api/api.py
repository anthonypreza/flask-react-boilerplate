from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from flask import Flask, jsonify

if TYPE_CHECKING:
    from flask import Response

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")
logging.getLogger("urllib3.connectionpool").setLevel(logging.CRITICAL)

LOGGER: logging.Logger = logging.getLogger(__name__)
LOGGER.info('Application starting...')


class App(Flask):
    """
    Main application class.
    """

    def __init__(self, name: str, static_url_path: str,
                 static_folder: str) -> None:
        """
        Main application initializer.
        """
        super(App, self).__init__(name,
                                  static_url_path=static_url_path,
                                  static_folder=static_folder)
        self.default_name = "World"
        self.api_root = "/api"


APP: App = App(__name__,
               static_url_path="/",
               static_folder=f'../build')


@APP.route("/")
def index() -> Response:
    """
    Return application index.
    """
    return APP.send_static_file("index.html")


@APP.route(APP.api_root + "/get_message", methods=['GET'])
def get_message() -> Response:
    """
    Handler for hello world API.
    """
    greeting: str = f'Hello, {APP.default_name}!'
    return jsonify(dict(message=greeting))


def main() -> None:
    """Start development server."""
    LOGGER.info("Starting server on port %s with debug=%s", 8000,
                False)
    APP.run(host="0.0.0.0", port=8000, debug=False)


if __name__ == "__main__":
    main()
