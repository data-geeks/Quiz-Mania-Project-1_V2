from django.contrib import admin
from . import models
# Register your models here.

# Models for all Basic Test
admin.site.register(models.Docker_B)
admin.site.register(models.AWS_B)
admin.site.register(models.Redhat_B)
admin.site.register(models.Python_B)
admin.site.register(models.Tensorflow_B)
admin.site.register(models.ComputerVision_B)
admin.site.register(models.Kubernetes_B)
admin.site.register(models.ScikitLearn_B)

# Models for all Intermediate Test
admin.site.register(models.Docker_I)
admin.site.register(models.AWS_I)
admin.site.register(models.Redhat_I)
admin.site.register(models.Python_I)
admin.site.register(models.Tensorflow_I)
admin.site.register(models.ComputerVision_I)
admin.site.register(models.Kubernetes_I)
admin.site.register(models.ScikitLearn_I)

# Models for all Advance Test
admin.site.register(models.Docker_A)
admin.site.register(models.AWS_A)
admin.site.register(models.Redhat_A)
admin.site.register(models.Python_A)
admin.site.register(models.Tensorflow_A)
admin.site.register(models.ComputerVision_A)
admin.site.register(models.Kubernetes_A)
admin.site.register(models.ScikitLearn_A)

# Score
admin.site.register(models.Score)
admin.site.register(models.Data)
