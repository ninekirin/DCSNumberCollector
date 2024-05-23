from concurrent import futures
import grpc
import random
import dcs_number_collector_pb2
import dcs_number_collector_pb2_grpc

class DCSNumberCollectorServicer(dcs_number_collector_pb2_grpc.DCSNumberCollectorServicer):
    def CollectNumbers(self, request, context):
        number = random.randint(1, 10)
        return dcs_number_collector_pb2.CollectResponse(number=number)

def serve(port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    dcs_number_collector_pb2_grpc.add_DCSNumberCollectorServicer_to_server(DCSNumberCollectorServicer(), server)
    server.add_insecure_port(f'[::]:{port}')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve(50051)
