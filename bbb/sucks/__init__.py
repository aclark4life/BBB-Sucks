
import collective.transmogrifier

try:
    eval("1 if True else 2")  # http://stackoverflow.com/questions/446052
    import configparser
except SyntaxError:
    import ConfigParser

def main():
    print 'BBB sucks!'
