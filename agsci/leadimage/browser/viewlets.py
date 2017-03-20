from plone.app.layout.viewlets import ViewletBase
from zope.component import getMultiAdapter
from ..interfaces import ILeadImageMarker as ILeadImage

class LeadImageViewlet(ViewletBase):

    def caption(self):
        return ILeadImage(self.context).leadimage_caption

    def full_width(self):
        return ILeadImage(self.context).leadimage_full_width

    def has_leadimage(self):
        return ILeadImage(self.context).has_leadimage

    def show(self):
        show = ILeadImage(self.context).leadimage_show
        return show and self.has_leadimage()

    def klass(self):
        if self.full_width():
            return "leadimage leadimage-full"

        return "leadimage"

    def tag(self, css_class='', scale='leadimage'):
        if self.has_leadimage():
            if self.full_width():
                scale = 'leadimage_full'
            return ILeadImage(self.context).tag(css_class=css_class, scale=scale)
        return ''

    def original_url(self):
        return '%s/@@images/leadimage' % self.context.absolute_url()

    def crop_image(self):
        crop_image_view = getMultiAdapter((self.context, self.request), name="crop-image")
        return crop_image_view.allowCrop()