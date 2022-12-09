# -*- coding: utf-8 -*-
# date: 2022/12/09
# author: AxelHowe
import grpc
from concurrent import futures


class SSLCredentialsMixin:
    CRT_PATH = None
    KEY_PATH = None
    _SERVER_CERTIFICATE = None
    _SERVER_CERTIFICATE_KEY = None

    def __init__(self) -> None:
        self.load_credentials()

    def load_credentials(self):
        '''
        讀取 SSL 憑證檔案
        '''
        with open(self.CRT_PATH, 'rb') as f:
            self._SERVER_CERTIFICATE = f.read()
        with open(self.KEY_PATH, 'rb') as f:
            self._SERVER_CERTIFICATE_KEY = f.read()


class BasegRPCServer:

    max_workers = 10
    interceptors = ()  # Tuple

    host = '127.0.0.1'
    port = 50051
    _server = None

    def __init__(self) -> None:
        thread_pool = futures.ThreadPoolExecutor(self.max_workers)
        self._server = grpc.server(
            thread_pool,
            interceptors=self.interceptors
        )

        self.register_service()

    def run(self):
        '''
        沒有 SSL 憑證
        '''
        self._server.add_insecure_port(f'{self.host}:{self.port}')
        self._server.start()
        self._server.wait_for_termination()

    def register_service(self):
        '''
        寫好的 service 在這裡宣告
        '''
        pass


class SSLgRPCServer(BasegRPCServer,
                    SSLCredentialsMixin):

    def run(self):
        '''
        有 SSL 憑證
        '''
        channel_credential = grpc.ssl_server_credentials(((
            self._SERVER_CERTIFICATE_KEY,
            self._SERVER_CERTIFICATE,
        ),))
        self._server.add_secure_port('0.0.0.0:50051', channel_credential)
        self._server.start()
        self._server.wait_for_termination()
