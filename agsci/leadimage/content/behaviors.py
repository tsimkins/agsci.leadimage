from plone.autoform import directives as form
from plone.autoform.interfaces import IFormFieldProvider
from plone.namedfile.field import NamedBlobImage
from plone.namedfile.file import NamedBlobImage as _NamedBlobImage
from plone.supermodel import model
from z3c.form.interfaces import IEditForm, IAddForm
from zope import schema
from zope.component import adapter
from zope.interface import provider, implementer

from .. import leadimageMessageFactory as _
from ..interfaces import ILeadImageMarker

@provider(IFormFieldProvider)
class ILeadImageBase(model.Schema):

    leadimage = NamedBlobImage(
        title=_(u"Lead Image"),
        description=_(u"This image can be displayed above the content and in folder listings."),
        required=False,
    )

    leadimage_caption = schema.TextLine(
        title=_(u"Lead image caption"),
        description=_(u""),
        max_length=255,
        required=False,
    )

    leadimage_show = schema.Bool(
        title=_(u"Show Lead Image on this item"),
        description=_(u"This will show the lead image on the object display."),
        default=True,
    )

    leadimage_full_width = schema.Bool(
        title=_(u"Full width lead image"),
        description=_(u"This will show a large lead image on the object display."),
        default=False,
    )

@provider(IFormFieldProvider)
class ILeadImage(ILeadImageBase):

    form.omitted('leadimage', 'leadimage_caption', 'leadimage_show', 'leadimage_full_width')
    form.mode(leadimage_show='hidden', leadimage_full_width='hidden')
    form.no_omit(IEditForm, 'leadimage', 'leadimage_caption')
    form.no_omit(IAddForm, 'leadimage', 'leadimage_caption')


@adapter(ILeadImageBase)
@implementer(ILeadImageMarker)
class LeadImage(object):

    def __init__(self, context):
        self.context = context

    @property
    def leadimage_caption(self):
        return getattr(self.context, "leadimage_caption", None)

    @property
    def leadimage_full_width(self):
        return getattr(self.context, "leadimage_full_width", False)

    @property
    def leadimage_show(self):
        return getattr(self.context, "leadimage_show", True)

    @property
    def has_leadimage(self):
        leadimage = getattr(self.context, 'leadimage', None)

        if leadimage and hasattr(leadimage, 'size') and leadimage.size > 0:
            return True

        return False

    def tag(self, css_class='leadimage', scale='leadimage_folder'):
        alt = getattr(self.context, 'leadimage_caption', '')
        images = self.context.restrictedTraverse('@@images')
        if self.has_leadimage:
            return images.tag('leadimage', scale=scale, alt=alt, css_class=css_class)
        return None

    def get_leadimage(self):
        if self.has_leadimage:
            return getattr(self.context, 'leadimage')

        return None

    def set_leadimage(self, data):
        field = _NamedBlobImage(filename=u'leadimage')
        field.data = data
        self.context.leadimage = field