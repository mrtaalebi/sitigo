from django.template import RequestContext
from django.urls import reverse
from django.utils.translation import ugettext as _

def navbar(request):

    context = {
        'navbar': [
            ['/', _('Home')],
            ['/blog', _('Blog')],
            ['/events', _('Events')],
            ['/articles', _('Articles')],
            ['/staff', _('Staff')],
            ['/faq', _('FAQ')],
            ['/contact_us', _('Contact')],
        ]
    }

    page_dir = '/' + request.path.split('/')[1]
    for x in context['navbar']:
        if x[0] == page_dir:
            x.append('active')
        else:
            x.append('')

    return context

