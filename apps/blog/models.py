from django.db import models
from ckeditor.fields import RichTextField
from django.core.mail import send_mail, EmailMessage
from django.utils.translation import ugettext, ugettext_lazy as _

from igo import settings

import math
import threading


class BlogDir(models.Model):
    name = models.CharField(max_length=30, unique=True, null=False, blank=False)
    lang = models.CharField(max_length=2, choices=(("en", _("en")),("fa", _("fa"))), default="fa")

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    dir = models.ForeignKey('BlogDir', on_delete=models.CASCADE, related_name='posts', null=False, blank=False)

    title = models.CharField(max_length=50, unique=True, null=False, blank=False)
    headline = models.TextField(max_length=200, null=False, blank=False)
    text = RichTextField()
    image = models.ImageField()
    date_created = models.DateTimeField(auto_now=True)

    def send_subscriber_blog_post_mail(self, mail_list):
        subject = _('New blog post in igo-official.ir') + str(self.title)
        message = '{}\n{}\n{}\n{}'.format(
                self.title,
                self.headline,
                '{}/blog/{}/{}'.format(settings.SITE_URL, self.dir.id, self.id),
                _('Check the above link')
                )
        html_message = '<body><h1>{}</h1><br><p>{}</p><br><a href="{}">{}</a></body>'.format(
                self.title,
                self.headline,
                '{}/blog/{}/{}'.format(settings.SITE_URL, self.dir.id, self.id),
                _('Click on this link to see this post on igo-official.ir')
                )

        print(mail_list)
        for x in mail_list:
            print(send_mail(
                    subject=subject,
                    message=message,
                    html_message=message,
                    from_email='national.igo@gmail.com',
                    recipient_list=[x],
                    ))

    def save(self, *args, **kwargs):
        l = [i.email for i in Subscriber.objects.all()]
        super(BlogPost, self).save(*args, **kwargs)
        threading.Thread(target=self.send_subscriber_blog_post_mail,
                args=[l]
                ).start()

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    post = models.ForeignKey('BlogPost', on_delete=models.CASCADE, related_name='comments', null=False, blank=False)

    author = models.CharField(max_length=20, null=False, blank=True, default="Unknown")
    text = models.TextField(max_length=200, null=False, blank=False)
    date = models.DateTimeField(auto_now=True)


class BlogImage(models.Model):
    image = models.ImageField(upload_to='blog/')

    def __str__(self):
        return str(self.image.url)



class Subscriber(models.Model):
    email = models.EmailField(unique=True, null=False, blank=False)

    def save(self, *args, **kwargs):
        try:
            super().save(*args, **kwargs)
        except:
            pass

