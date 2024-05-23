from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
import random
import sys

def generate_number():
    return random.randint(1, 10)

def run_server(port):
    server = SimpleJSONRPCServer(('0.0.0.0', port))
    server.register_function(generate_number, "generate_number")
    print(f"Serving on port {port}")
    server.serve_forever()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python xmlrpc_node.py <port>")
        sys.exit(1)
    run_server(int(sys.argv[1]))
