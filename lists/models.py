from django.db import models

class Item(models.Model):
   text = models.TextField(
default=''
)
   priority = models.TextField(
default=''
)
   list = models.ForeignKey(
       List,
       on_delete=models.SET_DEFAULT,default=None
)
