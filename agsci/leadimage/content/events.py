from ..interfaces import ILeadImageMarker

from agsci.atlas.utilities import rescaleImage as _rescaleImage

def rescaleImage(context, event):

    max_width = 900.0
    max_height = 1200.0

    leadimage = ILeadImageMarker(context).get_leadimage()

    if leadimage:

        if _rescaleImage(leadimage):
            context.reindexObject()