from django.db import models

# Create your models here.


class Poll(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.title


# class Category(models.Model):

#    name = models.CharField(max_length=128)
#    description = models.TextField(blank = True)
#    polls = models.ManyToManyField(Poll, blank = True, related_name = 'categories')
