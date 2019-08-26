from django.template import RequestContext
from django.urls import reverse
from django.utils.translation import ugettext as _
from django.utils import translation

def navbar(request):

    context = {
        'navbar': [
            ['/', _('Home')],
            ['/blog', _('Blog')],
            ['/events', _('Events')],
            ['/articles', _('Articles')],
            ['/staff', _('Staff')],
            ['/gallery', _('Gallery')],
            ['/faq', _('FAQ')],
            ['/contact_us', _('Contact Us')],
        ]
    }

    if translation.get_language() == "en":
        context['navbar'].remove(['/articles', _('Articles')])
        context['navbar'].remove(['/faq', _('FAQ')])
    

    page_dir = '/' + request.path.split('/')[1]
    for x in context['navbar']:
        if x[0] == page_dir:
            x.append('active')
        else:
            x.append('')

    return context

