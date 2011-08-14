
import collective.transmogrifier

try:
    eval("1 if True else 2")  # http://stackoverflow.com/questions/446052
    import configparser as cp
except SyntaxError:
    import ConfigParser as cp

# BBB Zope 2.12
try:
    from Zope2.App import zcml
except ImportError:
    from Products.Five import zcml

def main():
    print 'BBB sucks!'
    print '=========='
    print 'Imported: %s' % cp
    print 'Imported: %s' % zcml

