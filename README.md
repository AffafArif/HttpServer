# Simple HTTP Server

This project is a basic **HTTP Server** implemented in Python using the `http.server` library. The server runs on a specified local IP address and port, enabling it to handle both GET and POST requests. When accessed through a GET request, the server responds with a simple HTML page displaying "HELLO WORLD!" in the browser. On receiving a POST request, it returns a JSON object containing the current server time in a `YYYY-MM-DD HH:MM:SS` format, providing a simple time-stamp response. This server is a straightforward example of handling HTTP requests in Python and can be tested using tools like `curl`. To test, the server can be accessed by specifying the IP address and port, with `-X POST` included for POST requests.
## Language
Python


