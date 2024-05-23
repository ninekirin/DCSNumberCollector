# dcs_client.py
import grpc
import dcs_number_collector_pb2
import dcs_number_collector_pb2_grpc

def run():
    nodes = ["127.0.0.1:50051"] # Add more nodes here
    total_sum = 0
    
    for i, node in enumerate(nodes):
        with grpc.insecure_channel(node) as channel:
            stub = dcs_number_collector_pb2_grpc.DCSNumberCollectorStub(channel)
            response = stub.CollectNumbers(dcs_number_collector_pb2.CollectRequest(node_id=i))
            print(f"Node {i} generated number: {response.number}")
            total_sum += response.number
    
    print(f"Total sum of numbers: {total_sum}")

if __name__ == '__main__':
    run()