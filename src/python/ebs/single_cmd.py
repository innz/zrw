__author__ = 'cmri'

#!/usr/bin/env python


"""
BC-EBS Volume Driver.

"""

import os
import re
import httplib2
import base64
from lxml import etree
import urllib
import urllib2




url = "http://192.168.34.211:8080/EBS_Management_System/rest/volume/"

xmlbody = """
<?xml version="1.0" encoding="UTF-8"?>
<CreateVolumeRequest>
<sizeNum>2</sizeNum>
<userID>admin</userID>
</CreateVolumeRequest>
"""

ebs_user = "ebs"
ebs_pass = "ebs"


def run():
    handle = httplib2.Http()
    #auth = base64.encodestring(ebs_user +':' + ebs_pass)
    auth = base64.encodestring("ebs"+":"+"ebs")
    #    header = {'Authorization':'Basic' + auth, 'Content-Type':'text/xml'}
    #header = {'Authorization':'Basic' + auth, 'Content-Type':'text/xml'}
    resp, content = handle.request(url, method="POST",
                                   headers={'Authorization':'Basic' + auth},
                                   body=xmlbody)
    print url
    #print header
    print xmlbody

    print resp

def run2():
    pass

if __name__ == "__main__":
	run()