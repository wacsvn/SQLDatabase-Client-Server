import socket
import sqlite3
import threading

class SocketServer:
    def __init__(self, host, port, db):
        # create a server socket and bind it with host and port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))
        # store host, port, and db as attributes
        self.host = host
        self.port = port
        self.db = db

    def __del__(self):
        # close the server socket and release any resources
        self.socket.close()

    def __str__(self):
        # return a human-readable representation of the class
        return f"SocketServer(host='{self.host}', port={self.port}, db='{self.db}')"

    def __enter__(self):
        # return the instance itself and perform any necessary setup
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.socket.close()
        if exc_type is not None:
            print(f"An error occurred: {exc_value}")

    def __call__(self, max_connections=5):
        # listen for incoming connections from clients and handle them
        self.socket.listen(max_connections)
        print(f"Server listening on {self.host}:{self.port}")
        while True:
            # accept a connection from a client
            clientsocket, address = self.socket.accept()
            # create a thread to handle the client
            thread = threading.Thread(target=self.handle_client, args=(clientsocket, address))
            thread.start()

    def handle_client(self, clientsocket, address):
        # handle each client connection
        print(f"Accepted connection from {address}")
        # receive query from the client
        query = clientsocket.recv(1024).decode("utf-8")
        print(f"Received query: {query}")
        connection = sqlite3.connect(self.db)
        # execute query and fetch the result
        cursor = connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        connection.close()
        # send result back to client
        clientsocket.send(str(result).encode("utf-8"))
        print(f"Sent result: {result}")

        # close client socket
        clientsocket.close()

# create an instance of the class and pass the host, port, and database name
server = SocketServer("localhost", 9999, "climate_data4.db")
print(server)
server(5)

with server as s:
    s(5)
