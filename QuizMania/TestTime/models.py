from django.db import models

# Create your models here.

# Questions table is made to insert the Test Questions , various tables will be made for each kind of test
class Questions(models.Model):
    Question = models.CharField(max_length=100)
    Option1 = models.CharField(max_length=100)
    Option2 = models.CharField(max_length=100)
    Option3 = models.CharField(max_length=100)
    Option4 = models.CharField(max_length=100)
    Answer = models.CharField(max_length=2)

    def __str__(self):
        return f'''
        {self.id} Question: {self.Question}
        1. {self.Option1}
        2. {self.Option2}
        3. {self.Option3}
        4. {self.Option4}
        Answer: {self.Answer }
        '''
        