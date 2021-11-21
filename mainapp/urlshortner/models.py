from django.db import models
from .utils import generate_shortened_url
# Create your models here.

class Shortner(models.Model):
  created_on=models.DateTimeField(auto_now_add=True)
  original_url=models.URLField(max_length=1000)
  short_url= models.CharField(max_length=15, unique=True, blank=True)
  def __str__(self) -> str:
      return f'{self.original_url} to {self.short_url}'
  def save(self,*args,**kwargs):
    if not self.short_url:
      self.short_url = generate_shortened_url(self)
    super().save(*args, **kwargs)
