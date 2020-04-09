from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """Тема, которую изучет пользователь"""
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        """Возвращает строковое представление модели"""
        return self.text
    
class Entry(models.Model):
    """Информация выученная пользователем по теме"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    def __str__(self):
            """Возвращает строковое представление модели"""
            return self.text[:50] + "..."

    class Meta:
        verbose_name_plural = 'entries'

        
            