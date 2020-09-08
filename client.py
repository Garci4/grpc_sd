import grpc
from concurrent import futures
import time

# generated classes
import file_system_pb2
import file_system_pb2_grpc

# original file_system.py
import file_system

channel = grpc.insecure_channel('localhost:50051')

stub = file_system_pb2_grpc.FSStub(channel)

path = file_system_pb2.ListFiles('/home')

response = stub.ListFiles(path)
print(response.value)