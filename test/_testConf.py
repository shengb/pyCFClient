# -*- coding: utf-8 -*-
"""
Internal module

Used to read the channelfinderapi.conf file

example file
cat ~/channelfinderapi.conf
[DEFAULT]
BaseURL=http://localhost:8080/ChannelFinder
username=MyUserName
password=MyPassword
"""

def __loadConfig():
    import os.path
    import ConfigParser
    dflt={'BaseURL':'https://localhost:8181/ChannelFinder',
          'username' : 'cf-update',
          'password' : '1234',
          'owner' : 'cf-update',
          'channelOwner' : 'cf-channels',
          'tagOwner' : 'cf-tags',
          'propOwner' : 'cf-properties'
        }
    cf=ConfigParser.SafeConfigParser(defaults=dflt)
#    print os.path.normpath(os.path.expanduser('~/channelfinderapi.conf'))
    cf.read([
        '/etc/channelfinderapi.conf',
        os.path.expanduser('~/channelfinderapi.conf'),
        'channelfinderapi.conf'
    ])
    return cf
_testConf=__loadConfig()