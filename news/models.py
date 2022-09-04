from django.db import models
from news.consts import MAX_RATE
# Create your models here.




CATEGORY = (('business', 'ビジネス'), ('science ・Technology', '科学・テクノロジー'), ('Humanities ・ ideas', '人文・思想'), ('computer・IT', 'コンピュータ・IT'))
RATE_CHOICES = [(x, str(x))for x in range(0, MAX_RATE + 1)]

class Book(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(
        max_length = 100,
        choices = CATEGORY
    )
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(to=Book, on_delete=models.CASCADE, related_name='reviews')
    title = models.CharField(max_length=100)
    text = models.TextField()
    rate = models.IntegerField(choices=RATE_CHOICES)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


