from http.server import HTTPServer, BaseHTTPRequestHandler
import time

HOST = "192.168.  "
PORT=  9999

class AffafHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(bytes("<html><body><h1>HELLO WORLD!</h1></body></html>", "utf-8")) #can write anything in this line

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        self.wfile.write(bytes('{"time": "' +date +'"}',"utf-8"))

server= HTTPServer((HOST,PORT), AffafHTTP)

print("Server is running now on port 9999")
server.serve_forever()
server.server_close()
print("Server has stopped")

#curl <ip address>:<port number>
# for post request instead of get request
#curl <ip address>:<port number> -X POST
