from django.db import models

class Working_Test(models.Model):
    TestName = models.CharField(max_length=100)
    TestCategory = models.CharField(max_length=100)
    Duration = models.CharField(max_length=50)
    Level = models.CharField(max_length=50)

    def __str__(self):
        return f'''
        Test Name: {self.TestName}
        Category : {self.TestCategory} 
        Duration : {self.Duration} 
        Level    : {self.Level}
        '''