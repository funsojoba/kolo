# import uuid
# from django.db import models


# def generate_uid():
#     return uuid.uuid4().hex


# class BaseAbstractModel(models.Model):
#     id = models.CharField(primary_key=True, default=generate_uid, max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)