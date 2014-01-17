__author__ = 'zrw'
#!/usr/bin/env python

import os
import lxml
from lxml import etree

userkey="username"
passkey="password"
hostkey="host"
portkey="port"

class BCEBSContext(object):
    """BCEBSContext"""
    def __init__(self):
        self._dict = self._get_context(os.getcwd() + "\\bcec.xml")
        self.username = "ebs" if userkey not in self._dict.keys() else self._dict[userkey]
        self.password = "ebs" if passkey not in self._dict.keys() else self._dict[passkey]
        self.ebs_host = "127.0.0.1" if hostkey not in self._dict.keys() else self._dict[hostkey]
        self.ebs_port = 8080 if portkey not in self._dict.keys() else int(self._dict[portkey])

    def _get_context(self, path):
        dict = {}
        root = etree.parse(path)
        for each in root.iter():
            dict[each.tag] = each.text
        return dict