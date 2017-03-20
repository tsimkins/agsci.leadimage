from plone.indexer import indexer
from zope.component import provideAdapter

from .content.behaviors import ILeadImageBase
from .interfaces import ILeadImageMarker

@indexer(ILeadImageBase)
def hasLeadImage(context):

    try:
        return ILeadImageMarker(context).has_leadimage
    except TypeError:
        return False

provideAdapter(hasLeadImage, name='hasLeadImage')