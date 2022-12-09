# -*- coding: utf-8 -*-
# date: 2022/12/09
# author: AxelHowe
import os
import scan_pb2_grpc
from server import ScanServicer
from server import SignatureValidationInterceptor
from gRPC_server import SSLgRPCServer


class TestSSLServer(SSLgRPCServer):
    host = '127.0.0.1'
    port = 50051
    interceptors = (SignatureValidationInterceptor(),)

    KEY_PATH = os.path.join(os.path.split(__file__)[0], 'server.key')
    CRT_PATH = os.path.join(os.path.split(__file__)[0], 'server.crt')

    def register_service(self):
        scan_pb2_grpc.add_ScanServiceServicer_to_server(
            ScanServicer(), self._server)


if __name__ == "__main__":
    '''
    gRPC Server class 的使用範例
    '''
    server = TestSSLServer()
    server.run()
