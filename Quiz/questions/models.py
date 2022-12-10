from django.db import models
from django.utils.translation import gettext as _

class Questions(models.Model):
    question_id = models.AutoField(primary_key=True)
    question_des = models.CharField(max_length=500)
    answer_true = models.CharField(max_length=500)
    answer_wrong1 = models.CharField(max_length=500)
    answer_wrong2 = models.CharField(max_length=500)
    answer_wrong3 = models.CharField(max_length=500)
    image_question = models.ImageField(_(f"{question_des}"), upload_to=None, height_field=None, width_field=None, max_length=None)