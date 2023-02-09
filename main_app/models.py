from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Tour(models.Model):
    name = models.CharField(max_length=50)
    album = models.CharField(max_length=20)
    url = models.CharField(max_length=200)

    def __str__(self):
        return f' {self.name}'
    
    def get_absolute_url(self):
        return reverse('tours_detail', kwargs={'pk': self.id})


class Beyonce(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    age = models.IntegerField()
    tour = models.ForeignKey(Tour,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.city}, {self.state}'
    
    def get_absolute_url(self):
        return reverse("detail", kwargs={'beyonce_id': self.id})

class Shows(models.Model):
    SETS = (
        ('S', 'Solo'),
        ('G', 'Group'),
        ('D', 'Duo'),
    )
    date = models.DateField('shows date')
    sets = models.CharField(max_length=1, choices=SETS, default=SETS[0][0], verbose_name='show type')
    beyonce = models.ForeignKey(Beyonce, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_sets_display()} on {self.date}"

    class Meta:
        ordering = ('-date',)


class Photo(models.Model):
    url = models.CharField(max_length=200)
    beyonce = models.ForeignKey(Beyonce, on_delete=models.CASCADE)

    def __str__(self):
        return f" @{self.url}"