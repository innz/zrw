__author__ = 'zrw'


from greenlet import greenlet

def test1():
    print 12
    gr2.switch()
    print 34
    gr2.switch()

def test2():
    print 56
    gr1.switch()
    print 78
#    gr1.switch()


gr1 = greenlet(test1)
gr2 = greenlet(test2)

gr1.switch()

try:
    gr2.switch()
except:
    print "gr2 down"
print 88
