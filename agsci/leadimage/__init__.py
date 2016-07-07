from zope.i18nmessageid import MessageFactory
leadimageMessageFactory = MessageFactory('agsci.leadimage')

from content.behaviors import ILeadImageBase
from interfaces import ILeadImageMarker
from plone.indexer import indexer
from zope.component import provideAdapter

def initialize(context):
    pass

@indexer(ILeadImageBase)
def hasLeadImage(context):

    try:
        return ILeadImageMarker(context).has_leadimage
    except TypeError:
        return False

provideAdapter(hasLeadImage, name='hasLeadImage')