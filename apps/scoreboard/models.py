from django.db import models
from apps.content.models import Event
from .management.read_csv import wow


class Contestant(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    country = models.ForeignKey("Country", null=False, blank=False, on_delete=models.CASCADE)
    ruler = models.ForeignKey("Ruler", null=False, blank=False, on_delete=models.CASCADE)
    rank = models.IntegerField(null=False, blank=False)

    event_tier = models.ForeignKey("ContestTier", null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + " - " + self.event_tier


class Country(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name


class Ruler(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name


class ProblemScore(models.Model):
    p_id = models.IntegerField(null=False, blank=False, unique=True)
    score = models.FloatField(null=False, blank=False)
    contestant = models.ForeignKey("Contestant", related_name="problem_scores", null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.p_id + ": " + self.score + " - " + self.contestant


class ContestTier(models.Model):
    persian_name = models.CharField(max_length=50, null=False, blank=False)
    english_name = models.CharField(max_length=50, null=False, blank=False)
    event = models.ForeignKey(Event, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.engish_name + " - " + self.event + " : " + self.pk


class CSV(models.Model):
    contest_tier = models.ForeignKey(ContestTier, on_delete=models.CASCADE, null=False, blank=False)
    csv_file = models.FileField(upload_to='scoreboard', null=False, blank=False)

    def save(self, *args, **kwargs):
        wow(self.csv_file.url, self.contest_tier.id)
        super(CSV, self).save(*args, **kwargs)
