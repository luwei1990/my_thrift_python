import socket
import sys

sys.path.append('gen-py')

from helloworld import HelloWorld
from helloworld.ttypes import *

from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class HelloWorldHandle:
    def ping(self):
        return "Pong"

    def say(self, msg):
        ret = "Received:" + msg
        print ret
        return ret

handler =HelloWorldHandle()
processor = HelloWorld.Processor(handler)

transport = TSocket.TServerSocket("localhost", 9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()

server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

print "Start thrift server inpython "
server.serve()

print "done!"