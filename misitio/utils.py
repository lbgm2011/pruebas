import os
import re
import Image
from django.db import models
from django import forms
from django.conf import settings
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe
from django.template.loader import render_to_string
from django.contrib.admin.widgets import AdminFileWidget
from tinymce import models as tinymce_models
from urlparse import urljoin
from BeautifulSoup import BeautifulSoup, Comment

def sanitizeHtml(value, base_url=None):
    rjs = r'[\s]*(&#x.{1,7})?'.join(list('javascript:'))
    rvb = r'[\s]*(&#x.{1,7})?'.join(list('vbscript:'))
    re_scripts = re.compile('(%s)|(%s)' % (rjs, rvb), re.IGNORECASE)
    validTags = 'p i strong b u a h1 h2 h3 blockquote br ul ol li'.split()
    validAttrs = 'href src width height'.split()
    urlAttrs = 'href src'.split() # Attributes which should have a URL
    soup = BeautifulSoup(value)
    for comment in soup.findAll(text=lambda text: isinstance(text, Comment)):
        # Get rid of comments
        comment.extract()
    for tag in soup.findAll(True):
        if tag.name not in validTags:
            tag.hidden = True
        attrs = tag.attrs
        tag.attrs = []
        for attr, val in attrs:
            if attr in validAttrs:
                val = re_scripts.sub('', val) # Remove scripts (vbs & js)
                if attr in urlAttrs:
                    val = urljoin(base_url, val) # Calculate the absolute url
                tag.attrs.append((attr, val))
 
    return soup.renderContents().decode('utf8')

class CustomHTMLField(tinymce_models.HTMLField):
    def clean(self, value, *args, **kwargs):
        return sanitizeHtml(value)
