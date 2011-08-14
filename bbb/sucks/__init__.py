
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

# http://plone.org/documentation/manual/upgrade-guide/version/upgrading-plone-3-x-to-4.0/updating-add-on-products-for-plone-4.0/detecting-plone-4
try: 
    # Plone 4 and higher 
    import plone.app.upgrade 
    PLONE_VERSION = 4
except ImportError: 
    PLONE_VERSION = 3

def main():
    print 'BBB sucks!'
    print '=========='
    print 'Version: Plone %d' % PLONE_VERSION
    print 'Imported: %s' % cp
    print 'Imported: %s' % zcml

