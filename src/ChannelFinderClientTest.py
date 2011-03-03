'''
Created on Feb 15, 2011

@author: shroffk
'''
import unittest
from unittest.test.test_result import __init__
from ChannelFinderClient import ChannelFinderClient
from Channel import Channel, Property, Tag
import time
#===============================================================================
# 
#===============================================================================
class ConnectionTest(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testConnection(self):        
        baseurl = 'https://channelfinder.nsls2.bnl.gov:8181/ChannelFinder'
        self.assertNotEqual(ChannelFinderClient(BaseURL=baseurl), None, 'failed to create client')
        badBaseurl = ['', 'noSuchURL', 'https://channelfinder.nsls2.bnl.gov:8181/ChannelFinder/resources/']
        for url in badBaseurl:
            with self.assertRaises(Exception):ChannelFinderClient(BaseURL=url)
            
#===============================================================================
# 
#===============================================================================
class JSONparserTest(unittest.TestCase):
    
    multiChannels = {u'channels': {u'channel': [{u'@owner': u'shroffk', u'@name': u'Test_first:a<000>:0:0', u'properties': {u'property': [{u'@owner': u'shroffk', u'@name': u'Test_PropA', u'@value': u'0'}, {u'@owner': u'shroffk', u'@name': u'Test_PropB', u'@value': u'19'}, {u'@owner': u'shroffk', u'@name': u'Test_PropC', u'@value': u'ALL'}]}, u'tags': {u'tag': [{u'@owner': u'shroffk', u'@name': u'Test_TagA'}, {u'@owner': u'shroffk', u'@name': u'Test_TagB'}]}}, {u'@owner': u'shroffk', u'@name': u'Test_first:a<000>:0:1', u'properties': {u'property': [{u'@owner': u'shroffk', u'@name': u'Test_PropA', u'@value': u'1'}, {u'@owner': u'shroffk', u'@name': u'Test_PropB', u'@value': u'22'}, {u'@owner': u'shroffk', u'@name': u'Test_PropC', u'@value': u'ALL'}]}, u'tags': {u'tag': [{u'@owner': u'shroffk', u'@name': u'Test_TagA'}, {u'@owner': u'shroffk', u'@name': u'Test_TagB'}]}}, {u'@owner': u'shroffk', u'@name': u'Test_first:a<000>:0:2', u'properties': {u'property': [{u'@owner': u'shroffk', u'@name': u'Test_PropA', u'@value': u'2'}, {u'@owner': u'shroffk', u'@name': u'Test_PropB', u'@value': u'38'}, {u'@owner': u'shroffk', u'@name': u'Test_PropC', u'@value': u'ALL'}]}, u'tags': {u'tag': [{u'@owner': u'shroffk', u'@name': u'Test_TagA'}, {u'@owner': u'shroffk', u'@name': u'Test_TagB'}]}}, {u'@owner': u'shroffk', u'@name': u'Test_first:a<000>:0:3', u'properties': {u'property': [{u'@owner': u'shroffk', u'@name': u'Test_PropA', u'@value': u'3'}, {u'@owner': u'shroffk', u'@name': u'Test_PropB', u'@value': u'65'}, {u'@owner': u'shroffk', u'@name': u'Test_PropC', u'@value': u'ALL'}]}, u'tags': {u'tag': [{u'@owner': u'shroffk', u'@name': u'Test_TagA'}, {u'@owner': u'shroffk', u'@name': u'Test_TagB'}]}}, {u'@owner': u'shroffk', u'@name': u'Test_first:a<000>:0:4', u'properties': {u'property': [{u'@owner': u'shroffk', u'@name': u'Test_PropA', u'@value': u'4'}, {u'@owner': u'shroffk', u'@name': u'Test_PropB', u'@value': u'78'}, {u'@owner': u'shroffk', u'@name': u'Test_PropC', u'@value': u'ALL'}]}, u'tags': {u'tag': [{u'@owner': u'shroffk', u'@name': u'Test_TagA'}, {u'@owner': u'shroffk', u'@name': u'Test_TagB'}]}}, {u'@owner': u'shroffk', u'@name': u'Test_first:a<000>:0:5', u'properties': {u'property': [{u'@owner': u'shroffk', u'@name': u'Test_PropA', u'@value': u'5'}, {u'@owner': u'shroffk', u'@name': u'Test_PropB', u'@value': u'79'}, {u'@owner': u'shroffk', u'@name': u'Test_PropC', u'@value': u'ALL'}]}, u'tags': {u'tag': [{u'@owner': u'shroffk', u'@name': u'Test_TagA'}, {u'@owner': u'shroffk', u'@name': u'Test_TagB'}]}}, {u'@owner': u'shroffk', u'@name': u'Test_first:a<000>:0:6', u'properties': {u'property': [{u'@owner': u'shroffk', u'@name': u'Test_PropA', u'@value': u'6'}, {u'@owner': u'shroffk', u'@name': u'Test_PropB', u'@value': u'90'}, {u'@owner': u'shroffk', u'@name': u'Test_PropC', u'@value': u'ALL'}]}, u'tags': {u'tag': [{u'@owner': u'shroffk', u'@name': u'Test_TagA'}, {u'@owner': u'shroffk', u'@name': u'Test_TagB'}]}}, {u'@owner': u'shroffk', u'@name': u'Test_first:a<000>:0:7', u'properties': {u'property': [{u'@owner': u'shroffk', u'@name': u'Test_PropA', u'@value': u'7'}, {u'@owner': u'shroffk', u'@name': u'Test_PropB', u'@value': u'5'}, {u'@owner': u'shroffk', u'@name': u'Test_PropC', u'@value': u'ALL'}]}, u'tags': {u'tag': [{u'@owner': u'shroffk', u'@name': u'Test_TagA'}, {u'@owner': u'shroffk', u'@name': u'Test_TagB'}]}}, {u'@owner': u'shroffk', u'@name': u'Test_first:a<000>:0:8', u'properties': {u'property': [{u'@owner': u'shroffk', u'@name': u'Test_PropA', u'@value': u'8'}, {u'@owner': u'shroffk', u'@name': u'Test_PropB', u'@value': u'64'}, {u'@owner': u'shroffk', u'@name': u'Test_PropC', u'@value': u'ALL'}]}, u'tags': {u'tag': [{u'@owner': u'shroffk', u'@name': u'Test_TagA'}, {u'@owner': u'shroffk', u'@name': u'Test_TagB'}]}}, {u'@owner': u'shroffk', u'@name': u'Test_first:a<000>:0:9', u'properties': {u'property': [{u'@owner': u'shroffk', u'@name': u'Test_PropA', u'@value': u'9'}, {u'@owner': u'shroffk', u'@name': u'Test_PropB', u'@value': u'85'}, {u'@owner': u'shroffk', u'@name': u'Test_PropC', u'@value': u'ALL'}]}, u'tags': {u'tag': [{u'@owner': u'shroffk', u'@name': u'Test_TagA'}, {u'@owner': u'shroffk', u'@name': u'Test_TagB'}]}}]}}
    singleChannels = {u'channels': {u'channel': {u'@owner': u'shroffk', u'@name': u'Test_first:a<000>:0:2', u'properties': {u'property': [{u'@owner': u'shroffk', u'@name': u'Test_PropA', u'@value': u'2'}, {u'@owner': u'shroffk', u'@name': u'Test_PropB', u'@value': u'38'}, {u'@owner': u'shroffk', u'@name': u'Test_PropC', u'@value': u'ALL'}]}, u'tags': {u'tag': [{u'@owner': u'shroffk', u'@name': u'Test_TagA'}, {u'@owner': u'shroffk', u'@name': u'Test_TagB'}]}}}}
    channel = {u'@owner': u'shroffk', u'@name': u'Test_first:a<000>:0:0', u'properties': {u'property': [{u'@owner': u'shroffk', u'@name': u'Test_PropA', u'@value': u'0'}, {u'@owner': u'shroffk', u'@name': u'Test_PropB', u'@value': u'19'}, {u'@owner': u'shroffk', u'@name': u'Test_PropC', u'@value': u'ALL'}]}, u'tags': {u'tag': [{u'@owner': u'shroffk', u'@name': u'Test_TagA'}, {u'@owner': u'shroffk', u'@name': u'Test_TagB'}]}}
    noChannel = {u'channels': None}

    def testSingleChannelsParsing(self):
        reply = ChannelFinderClient.decodeChannels(self.singleChannels)
        self.assertTrue(len(reply) == 1, 'Parse Error');
        self.assertTrue(len(reply[0].Properties) == len (self.singleChannels[u'channels'][u'channel'][u'properties']['property']), 'single channel peoperties not parsed correctly')
        self.assertTrue(len(reply[0].Tags) == len(self.singleChannels[u'channels'][u'channel'][u'tags']['tag']), 'tags not correctly parsed')
        pass
    
    def testMultiChannelsParsing(self):
        reply = ChannelFinderClient.decodeChannels(self.multiChannels)
        self.assertTrue(len(reply) == len(self.multiChannels[u'channels'][u'channel']), 'incorrect number of channels in parsed result')
        pass
    
    def testNoChannelParsing(self):
        reply = ChannelFinderClient.decodeChannels(self.noChannel)
        self.assertTrue(not reply, 'failed parsing an emplty channels list')

    def testChannel(self):
        reply = ChannelFinderClient.decodeChannel(self.channel)
        self.assertTrue(reply.Name == self.channel[u'@name'])
        self.assertTrue(reply.Owner == self.channel[u'@owner'])
        self.assertTrue(len(reply.Properties) == len(self.channel[u'properties'][u'property']))
        self.assertTrue(len(reply.Tags) == len(self.channel[u'tags'][u'tag']))
        
    def testEncodeChannel(self):
        encodedChannel = ChannelFinderClient.encodeChannels(\
                                                            [Channel('Test_first:a<000>:0:0', 'shroffk', \
                                                                     [Property('Test_PropA', 'shroffk', '0'), \
                                                                      Property('Test_PropB', 'shroffk', '19'), \
                                                                      Property('Test_PropC', 'shroffk', 'ALL')], \
                                                                      [Tag('Test_TagA', 'shroffk'), \
                                                                       Tag('Test_TagB', 'shroffk')])])
#        print encodedChannel[u'channels'][u'channel']
        self.assertTrue(encodedChannel[u'channels'][u'channel'] == self.channel)
        
    def testEncodeChannels(self):
        self.assertTrue(self.multiChannels == ChannelFinderClient.encodeChannels(ChannelFinderClient.decodeChannels(self.multiChannels)))

#===============================================================================
# 
#===============================================================================
class OperationTest(unittest.TestCase):
    
    def setUp(self):
        baseurl = 'https://channelfinder.nsls2.bnl.gov:8181/ChannelFinder'
        self.client = ChannelFinderClient(BaseURL=baseurl, username='boss', password='1234')
        pass
    
    def tearDown(self):
        pass
    
    def testaddRemoveChannel(self):
        # Add a channel
        testChannel = Channel('pyChannelName', 'pyChannelOwner')
        self.client.add(channel=testChannel)
        result = self.client.find(name='pyChannelName')
        self.assertTrue(len(result) == 1, 'incorrect number of channels returned')
        self.assertTrue(result[0].Name == 'pyChannelName', 'incorrect channel returned')
        self.client.remove(channelName=testChannel.Name) 
        result = self.client.find(name='pyChannelName')
        self.assertTrue(result == None, 'incorrect number of channels returned')  
        pass
    
    def testAddRemoveChannels(self):
        testChannels = [Channel('pyChannel1', 'pyOwner'), \
                        Channel('pyChannel2', 'pyOwner'), \
                        Channel('pyChannel3', 'pyOwner')]
        self.client.add(channels=testChannels)
        r = self.client.find(name='pyChannel*')
        self.assertTrue(len(r) == 3, 'ERROR: # of channels returned expected ' + str(len(r)) + ' expected 3')
        # remove each individually
        for ch in testChannels:
#            print ch.Name
            self.client.remove(channelName=str(ch.Name))
        pass
    
    def testAddRemoveTag(self):
        testTag = Tag('pyTag', 'pyOwner')
        self.client.add(tag=testTag)
        self.assertTrue(self.client.findTag(tagName=testTag.Name).Name == testTag.Name, 'testTag not added')
        self.client.remove(tagName=testTag.Name)
        self.assertIsNone(self.client.findTag(tagName=testTag.Name), 'tag not removed correctly')
        pass
    
    def testAddRemoveTags(self):
        testTags = []
        testTags.append(Tag('pyTag1', 'pyOwner'))
        testTags.append(Tag('pyTag2', 'pyOwner'))
        testTags.append(Tag('pyTag3', 'pyOwner'))
        self.client.add(tags=testTags)
        # Check if all the tags were correctly Added
        for tag in testTags:
            self.assertTrue(self.client.findTag(tagName=tag.Name), 'Error: tag ' + tag.Name + ' was not added')
        # remove the Tags
        for tag in testTags:
            self.client.remove(tagName=tag.Name)
        # Check all the tags were correctly removed
        for tag in testTags:
            self.assertIsNone(self.client.findTag(tagName='pyTag1'), 'Error: tag ' + tag.Name + ' was not removed')
        pass
    
    def testGetAllTags(self):
        initial = len(self.client.getAllTags())
        testTags = []
        testTags.append(Tag('pyTag1', 'pyOwner'))
        testTags.append(Tag('pyTag2', 'pyOwner'))
        testTags.append(Tag('pyTag3', 'pyOwner'))
        self.client.add(tags=testTags)
        allTags = self.client.getAllTags();
        # this test introduces a race condition
        self.assertTrue(len(allTags) == (initial + 3), 'unexpected number of tags')
        for tag in testTags:
            self.assertTrue(tag in allTags, 'tag ' + tag.Name + ' missing')
        # remove the Tags
        for tag in testTags:
            self.client.remove(tagName=tag.Name)
        # Check all the tags were correctly removed
        for tag in testTags:
            self.assertIsNone(self.client.findTag(tagName='pyTag1'), 'Error: tag ' + tag.Name + ' was not removed')
    
    def testAddRemoveProperty(self):
        testProperty = Property('pyProp', 'pyOwner', value=33)
        self.client.add(property=testProperty)
        self.assertTrue(self.client.findProperty(propertyName=testProperty.Name), \
                        'Error: ' + testProperty.Name + ' failed to be added')
        self.client.remove(propertyName=testProperty.Name)
        self.assertIsNone(self.client.findProperty(propertyName=testProperty.Name), \
                        'Error: ' + testProperty.Name + ' failed to remove')        
        pass
    
    def testAddRemoveProperties(self):
        testProps = []
        testProps.append(Property('pyProp1', 'pyOwner'))
        testProps.append(Property('pyProp2', 'pyOwner'))
        testProps.append(Property('pyProp3', 'pyOwner'))
        self.client.add(properties=testProps)
        for prop in testProps:
            time.sleep(30)
            self.assertTrue(self.client.findProperty(propertyName=prop.Name), \
                            'Error: property ' + prop.Name + ' was not added.')
        for prop in testProps:
            self.client.remove(propertyName=prop.Name)
        for prop in testProps:
            time.sleep(30)
            self.assertIsNone(self.client.findProperty(propertyName=prop.Name), \
                            'Error: property ' + prop.Name + ' was not removed.')
        pass
    
    def testGetAllPropperties(self):
        pass


#===========================================================================
# Query Tests
#===========================================================================

class QueryTest(unittest.TestCase):
    
    def setUp(self):
        baseurl = 'https://channelfinder.nsls2.bnl.gov:8181/ChannelFinder'
        self.client = ChannelFinderClient(BaseURL=baseurl)
        pass


    def tearDown(self):
        pass
    
    def testQueryChannel(self):
        pass
    
    
#===============================================================================
#  ERROR tests
#===============================================================================

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testConnection']
#    suite = unittest.TestLoader().loadTestsFromTestCase(OperationTest)
#    unittest.TextTestRunner(verbosity=2).run(suite)
    
    unittest.main()
