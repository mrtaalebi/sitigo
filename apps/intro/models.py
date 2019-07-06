from django.db import models
# from django.utils.translation import ugettext_lazy as _
#
# # Singleton model HomePageData
# class HomePageData(models.Model):
#
#     class Meta:
#         abstract = True
#
#     def save(self, *args, **kwargs):
#         self.pk = 1
#         super(HomePageData, self).save(*args, **kwargs)
#
#     def delete(self, *args, **kwargs):
#         pass
#
#
#
# class Organizer(models.Model):
#
#     role_choices = (('Organizer', _('Organizer')),
#                     ('Sponser', _('Sponser')))
#
#     role = models.CharField(max_length=50, choices=role_choices, null=False, blank=False)
#     name = models.CharField(max_length=50, null=False, blank=False)
#     image = models.ImageField(null=False, blank=False)
#
#     home_page_data = models.ManyToManyField('HomePageData', related_name='organizers')
#
#
# class Slide(models.Model):
#
#     title = models.CharField(max_length=50, null=False, blank=False)
#     image = models.ImageField(null=False, blank=False)
#
#     home_page_data = models.ManyToManyField('HomePageData', related_name='slides')
from apps.content.models import resize


class HomePageImage(models.Model):
    image = models.ImageField(upload_to='home_page_slideshow')

    def save(self, *args, **kwargs):
        if not self.id:
            self.image = resize(self.image, 500, 400)
        super(HomePageImage, self).save(*args, **kwargs)


class HomePage(models.Model):
    images = models.ManyToManyField(HomePageImage)
