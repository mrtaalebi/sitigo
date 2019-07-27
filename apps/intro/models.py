from django.db import models
from apps.content.models import resize


class HomePage(models.Model):
    sponsor_name_persian = models.CharField(max_length=200)
    sponsor_name_english = models.CharField(max_length=200)
    organizer_name_persian = models.CharField(max_length=200)
    organizer_name_english = models.CharField(max_length=200)
    organizer_image = models.ImageField(upload_to='organizer')
    sponsor_image = models.ImageField(upload_to='sponsor')

    def save(self, *args, **kwargs):
        if not self.id:
            self.sponsor_image = resize(self.sponsor_image, 200, 200)
            self.organizer_image = resize(self.organizer_image, 200, 200)
        super(HomePage, self).save(*args, **kwargs)


class HomePageImage(models.Model):
    image = models.ImageField(upload_to='home_page_slideshow')
    persian_caption = models.CharField(max_length=300, null=True, blank=True)
    english_caption = models.CharField(max_length=300, null=True, blank=True)
    homePage = models.ForeignKey(HomePage, related_name='home_page_image', on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.id:
            self.image = resize(self.image, 500, 400)
        super(HomePageImage, self).save(*args, **kwargs)


