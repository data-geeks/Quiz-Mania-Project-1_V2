from django.db import models

# Create your models here.

# Questions table is made to insert the Test Questions , various tables will be made for each kind of test
# Table Columns are: Question,Option1,Option2,Option3,Option4,Answer(Option no that is A/B/C/D)

# BASIC
# Docker
class Docker_B(models.Model):
    Question = models.CharField(max_length=100)
    Option1 = models.CharField(max_length=100)
    Option2 = models.CharField(max_length=100)
    Option3 = models.CharField(max_length=100)
    Option4 = models.CharField(max_length=100)
    Answer = models.CharField(max_length=5)

    def __str__(self):
        return f'''
        {self.id} Question: {self.Question}
        1. {self.Option1}
        2. {self.Option2}
        3. {self.Option3}
        4. {self.Option4}
        Answer: {self.Answer }
        '''

# Aws
class AWS_B(models.Model):
    Question = models.CharField(max_length=1000)
    Option1 = models.CharField(max_length=1000)
    Option2 = models.CharField(max_length=1000)
    Option3 = models.CharField(max_length=1000)
    Option4 = models.CharField(max_length=1000)
    Answer = models.CharField(max_length=1000)

    def __str__(self):
        return f'''
        {self.id} Question: {self.Question}
        1. {self.Option1}
        2. {self.Option2}
        3. {self.Option3}
        4. {self.Option4}
        Answer: {self.Answer }
        '''

# Redhat
class Redhat_B(models.Model):
    Question = models.CharField(max_length=100)
    Option1 = models.CharField(max_length=100)
    Option2 = models.CharField(max_length=100)
    Option3 = models.CharField(max_length=100)
    Option4 = models.CharField(max_length=100)
    Answer = models.CharField(max_length=5)

    def __str__(self):
        return f'''
        {self.id} Question: {self.Question}
        1. {self.Option1}
        2. {self.Option2}
        3. {self.Option3}
        4. {self.Option4}
        Answer: {self.Answer }
        '''

# Python
class Python_B(models.Model):
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

# Tensorflow
class Tensorflow_B(models.Model):
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

# Computer Vision
class ComputerVision_B(models.Model):
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

# Kubernetes
class Kubernetes_B(models.Model):
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

# Scikit Learn
class ScikitLearn_B(models.Model):
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

# INTERMEDIATE
# Docker
class Docker_I(models.Model):
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

# Aws
class AWS_I(models.Model):
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

# Redhat
class Redhat_I(models.Model):
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

# Python
class Python_I(models.Model):
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

# Tensorflow
class Tensorflow_I(models.Model):
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

# Computer Vision
class ComputerVision_I(models.Model):
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

# Kubernetes
class Kubernetes_I(models.Model):
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

# Scikit Learn
class ScikitLearn_I(models.Model):
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

# ADVANCE
# Docker
class Docker_A(models.Model):
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

# Aws
class AWS_A(models.Model):
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

# Redhat
class Redhat_A(models.Model):
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

# Python
class Python_A(models.Model):
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

# Tensorflow
class Tensorflow_A(models.Model):
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

# Computer Vision
class ComputerVision_A(models.Model):
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

# Kubernetes
class Kubernetes_A(models.Model):
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

# Scikit Learn
class ScikitLearn_A(models.Model):
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


# SCOREBOARD
class Score(models.Model):
    Email = models.CharField(max_length=100)
    TestName = models.CharField(max_length=100)
    Score = models.CharField(max_length=20)
    Date = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f'''
        Email: {self.Email}
        Test Name: {self.TestName}
        Score: {self.Score}
        Date: {self.Date}
        '''
        
