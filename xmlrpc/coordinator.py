import xmlrpc.client
import sys

def sum(ports):
    nodes = []
    total_sum = 0
    for port in ports:
        nodes.append(f"http://127.0.0.1:{port}/")
    for i, node in enumerate(nodes):
        with xmlrpc.client.ServerProxy(node) as proxy:
            number = proxy.generate_number()
            print(f"Node {i} generated number: {number}")
            total_sum += number
    
    print(f"Total sum of numbers: {total_sum}")

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Usage: python xmlrpc_coordinator.py <port1> <port2> <port3> ...")
        sys.exit(1)
    sum(sys.argv[1:])
