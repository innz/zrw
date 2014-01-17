__author__ = 'cmri'

import base64
import httplib2

class ReSTFullAgent(object):
    """send and receive"""
    def __init__(self, context):
        self._username = context.username
        self._password = context.password
        self._ebs_host = context.ebs_host
        self._ebs_port = context.ebs_port
        self._handle = self._get_http_handle()
        self._auth = self._get_auth()
        self._header = self._get_header()

    def _get_http_handle(self):
        return httplib2.Http()

    def _get_auth(self):
        return base64.encodestring(self._username + ":" +  self._password)
    def _get_header(self):
        return {'Authorization':'Basic' + self._auth, 'Content-Type':'text/xml'}

    def send_then_recv(self, url, xmlbody, optype = "POST"):
        resp, content = self._handle.request(url, optype, headers = self._header, body = xmlbody)
        return (resp, content)