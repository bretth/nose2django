try:
    __version__ = __import__('pkg_resources').get_distribution('nose2django').version
except:
    __version__ = ''