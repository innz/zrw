__author__ = 'zrw'

from greenlet import greenlet

def test1(x, y):
    print gr1
    z = gr2.switch(x+y)
    print z

def test2(u):
    print u
    gr3.switch(42)

def test3(msg):
    print msg
    gr1.switch("abc", "def")


gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr3 = greenlet(test3)
gr1.switch("hello", " world")
