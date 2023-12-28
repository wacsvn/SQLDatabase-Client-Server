import socket

class SocketClient:
    def __init__(self, host, port):
        # create socket object and connect to server's host and port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((host, port))
        # store host and port
        self.host = host
        self.port = port

    def __del__(self):
        # close socket
        self.socket.close()

    def __str__(self):
        return f"SocketClient(host='{self.host}', port={self.port})"

    def __enter__(self):
        # return the instance itself
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        # perform cleanup or finalization tasks and handle any exceptions
        self.socket.close()
        if exc_type is not None:
            print(f"An error occurred: {exc_value}")

    def __call__(self, query):
        # send a query to the server and receive the result
        self.socket.send(query.encode("utf-8"))
        result = self.socket.recv(1024).decode("utf-8")
        return result

# test
client = SocketClient("localhost", 9999)
print(client)

# use the instance as a function and pass the query as an argument
result = client("SELECT * FROM 'co2' LIMIT 0,10;")
print(result)

# test querying
with client as c:
    result = c("SELECT * FROM 'co2' LIMIT 0,10;")
    print(result)
