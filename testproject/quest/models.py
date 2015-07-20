from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    def __str__(self):
	return self.question_text

class Category(models.Model):
    question = models.ForeignKey(Question)
    category_text = models.CharField(max_length=200)
    def __str__(self):
	return self.category_text

# Create your models here.
