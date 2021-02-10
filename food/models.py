from django.db import models
from django.conf import settings


class Category(models.Model):
    name = models.CharField(max_length=400)
    url = models.CharField(max_length=400)

    def __str__(self):

        return self.name


class Food(models.Model):
    name = models.CharField(max_length=400)
    nameFr = models.CharField(max_length=400)
    genericNameFr = models.CharField(max_length=400)
    url = models.CharField(max_length=400)
    nutritionGrade = models.CharField(max_length=3)
    countries = models.CharField(max_length=400)
    purchasePlaces = models.CharField(max_length=400)
    manufacturingPlaces = models.TextField()
    ingredientsText = models.TextField()
    image_link = models.URLField(max_length=450, null=True)

    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):

        return self.nameFr


class MyFood(models.Model):
    """ A class who store the users favorites foods """

    userId = models.IntegerField()  # the user's id

    food = models.ForeignKey('Food', on_delete=models.CASCADE)

    def __str__(self):
        return self.food.nameFr


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
