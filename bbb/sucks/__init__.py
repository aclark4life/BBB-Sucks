
import collective.transmogrifier

try:
    eval("1 if True else 2")  # http://stackoverflow.com/questions/446052
    import configparser as cp
except SyntaxError:
    import ConfigParser as cp

def main():
    print 'BBB sucks!'
    print '=========='
    print 'Imported: %s' % cp

