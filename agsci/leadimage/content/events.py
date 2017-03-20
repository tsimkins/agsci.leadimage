from PIL import Image
from StringIO import StringIO
from ..interfaces import ILeadImageMarker

def rescaleImage(context, event):

    max_width = 900.0
    max_height = 1200.0

    leadimage = ILeadImageMarker(context).get_leadimage()

    if leadimage:
        (w,h) = leadimage.getImageSize()

        leadimage_format =  {
            'image/jpeg' : 'JPEG',
            'image/png' : 'PNG',
            'image/gif' : 'GIF',
        }.get(leadimage.contentType, 'UNK')

        ratio = min([max_width/w, max_height/h])

        if ratio < 1.0:
            new_w = w * ratio
            new_h = h * ratio

            try:
                pil_image = Image.open(StringIO(leadimage.data))
            except IOError:
                pass
            else:
                pil_image.thumbnail([new_w, new_h], Image.ANTIALIAS)

                img_buffer = StringIO()

                pil_image.save(img_buffer, leadimage_format, quality=100)

                img_value = img_buffer.getvalue()

                leadimage._setData(img_value)


