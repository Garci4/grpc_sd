import grpc
from concurrent import futures
import time

# generated classes
import file_system_pb2
import file_system_pb2_grpc

# original file_system.py
import file_system


class FSServicer(file_system_pb2_grpc.FSServicer):

  def ListFiles(self, request, context):
    response = file_system_pb2.PathFiles()
    try:
      for file in file_system.ListFiles(request.value):
        response.values.append(file)
    except Exception as e:
      print('ERROR -> -server- list files ', e)
    return response

  def OpenFile(self, request, context):
    response = file_system_pb2.Value()
    try:
      response.value = file_system.OpenFile(request.value)
    except Exception as e:
      print('ERROR -> -server- open file ', e)
    return response

  def CloseFile(self, request, context):
    response = file_system_pb2.Value()
    try:
      response.value = file_system.CloseFile(request.value)
    except Exception as e:
      print('ERROR -> -server- close file ', e)
    return response
    

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

file_system_pb2_grpc.add_FSServicer_to_server(FSServicer(), server)

print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

try:
  while True:
    time.sleep(86400)
except KeyboardInterrupt:
  server.stop(0)