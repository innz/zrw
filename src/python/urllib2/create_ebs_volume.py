__author__ = 'zrw'

import urllib2
from urllib2 import *
import os
import sys
import lxml


ebs_user='ebs'
ebs_pass='ebs'

workdir = os.getcwd()
ebsconf = workdir + "\\bcebs.conf"

#url = 'http://www.baidu.com'
url = "http://192.168.34.211:8080/EBS_Management_System/ebs_pcsan_pages/login.jsp"
baseurl = "http://192.168.39.171:8080/EBS_Management_System/rest/volume"

xmlheader = """<?xml version="1.0" encoding="UTF-8"?>"""

xmlcreatevolume = """
<?xml version="1.0" encoding="UTF-8"?>
<CreateVolumeRequest>
    <sizeNum>2</sizeNum>
    <userID>admin</userID>
    <properties>
        <property>
            <key>sizeUnit</key>
            <value>G</value>
        </property>
    </properties>
</CreateVolumeRequest>
"""

def create_volume():
    #auth_handler = urllib2.HTTPBasicAuthHandler()
    #auth_handler.add_password(#realm='PDQ Application',
                          #uri='https://mahler:8092/site-updates.py',
    #                      user=ebs_user,
    #                      passwd=ebs_pass)
    #opener = urllib2.build_opener(auth_handler)
    # ...and install it globally so it can be used with urlopen.
    #urllib2.install_opener(opener)
    #urllib2.urlopen('http://www.example.com/login.html')

    base64string = base64.encodestring('%s:%s' % (ebs_user, ebs_pass)).replace('\n', '')
    headers = {
                'Content-Type': 'text/xml',
                'Authorization': 'Basic %s' % base64string}

    req = urllib2.Request(url=baseurl,data=xmlcreatevolume,headers=headers)
    response = urllib2.urlopen(req)
    xml_output = response.read()
    print xml_output

def run():
    create_volume()

if __name__ == "__main__":
    run()