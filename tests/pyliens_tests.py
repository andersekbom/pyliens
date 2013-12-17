from nose.tools import *
#from nose.tools import set_trace; set_trace()

from main.pyliens import Alien

def test_alien():
    alien = Alien("binky")
    assert_equal(alien.name, "binkys")
