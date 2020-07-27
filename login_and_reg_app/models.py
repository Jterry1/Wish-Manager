from django.db import models
import re

# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, post_data):
        errors = {}
        if len(post_data['first_name']) < 2:
            errors['first_name'] = 'First name should be at least 2 characters.'
        if len(post_data['last_name']) < 2:
            errors['last_name'] = 'Last name should be at least 2 characters.'
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):         
            errors['email'] = "Invalid email address."
        if len(User.objects.filter(email=post_data['email'])) > 0:
            errors['email'] = 'Email is already registered'
        if len(post_data['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters.'
        if post_data['password'] != post_data['confirm_pw']:
            errors['confirm_pw'] = 'Passwords do not match!'
        return errors
        


class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()