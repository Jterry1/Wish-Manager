from django.db import models
from login_and_reg_app.models import User
from django.contrib import messages


# Create your models here.
class WishManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        if len(post_data['name']) < 3:
            errors['name'] = 'Wish name must be at least 3 characters long.'
        if len(post_data['description']) < 3:
            errors['descriptionf'] = 'Wish description must be at least 3 characters long.'
        return errors


class GrantedManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        if len(post_data['name']) < 3:
            errors['name'] = 'Wish name must be at least 3 characters long.'
        return errors


class Wish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    wished_by = models.ForeignKey(User, related_name='wishes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = WishManager()



class Granted(models.Model):
    name = models.CharField(max_length=255)
    wished_by = models.ForeignKey(User, related_name='granteds', on_delete=models.CASCADE)
    og_created_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = GrantedManager()