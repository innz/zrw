__author__ = 'cmri'


def execQualysAction(username,password,url,request_data):
  import urllib,urrlib2
  xml_output = None
  try:
    base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
    headers = {'X-Requested-With' : 'urllib2','Content-Type': 'application/xml','Authorization': 'Basic %s' % base64string}
    req = urllib2.Request(url=url,data=request_data,headers=headers)
    response = urllib2.urlopen(req, timeout=int(TIMEOUT))
    xml_output = response.read()
    if args.verbose>1:
      print "Result of executing action request",request_data,"is:",xml_output
  except:
    xml_output = '<RESULT></RESULT>'
    traceback.print_exc(file=sys.stdout)
    print '-'*60