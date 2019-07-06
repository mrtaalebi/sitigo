from django.db import models
from ckeditor.fields import RichTextField
from django.core.mail import send_mail

import math


class BlogDir(models.Model):
    name = models.CharField(max_length=30, unique=True, null=False, blank=False)

    def __str__(self):
        self.name


class BlogPost(models.Model):
    dir = models.ForeignKey('BlogDir', on_delete=models.CASCADE, related_name='posts', null=False, blank=False)

    title = models.CharField(max_length=50, unique=True, null=False, blank=False)
    headline = models.TextField(max_length=200, null=False, blank=False)
    text = RichTextField()
    image = models.ImageField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super(BlogPost, self).save(*args, **kwargs)
        send_subscriber_blog_post_mail(self, [i.email for i in Subscriber.objcets.all()])

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
        for x in range(math.ceil(len(mail_list) / 20)):
            send_mail(
                    subject=subjcet,
                    message=message,
                    html_message=message,
                    from_email='igoiiggooiiigggooo@gmail.com',
                    recipient_list=['national.igo@gmail.com'],
                    bcc=mail_list[x * 20 : x * 20 + 20]
                    )

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    post = models.ForeignKey('BlogPost', on_delete=models.CASCADE, related_name='comments', null=False, blank=False)

    author = models.CharField(max_length=20, null=False, blank=True, default="Unknown")
    text = models.TextField(max_length=200, null=False, blank=False)


class Subscriber(models.Model):
    email = models.EmailField(null=False, blank=False)

