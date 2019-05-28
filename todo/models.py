from django.db import models

class TodoItem(models.Model):
    content = models.TextField()
    # context2 =models.TextField()


    # //After this i makemigration and migrate
    # //date create and who create add here

# class TodoItem(models.Model):
#     names = models.TextField(max_length=200)
#     # //This is demo model to just check migration working or not4
#     # and see this is not dome