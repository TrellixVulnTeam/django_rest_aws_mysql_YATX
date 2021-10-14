from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    # admin의 컬럼명
    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
