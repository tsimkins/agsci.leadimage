from zope.i18nmessageid import MessageFactory

leadimageMessageFactory = MessageFactory('agsci.leadimage')

# Register indexers
import agsci.leadimage.indexer

def initialize(context):
    pass

