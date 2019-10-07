from django.urls import path
from . import views

urlpatterns = [
    path('Docker_B',views.docker_B,name='Docker_B'),
    path('Docker_I',views.docker_I,name='Docker_I'),
    path('Docker_A',views.docker_A,name='Docker_A'),

    path('AWS_B',views.aws_B,name='AWS_B'),
    path('AWS_I',views.aws_I,name='AWS_I'),
    path('AWS_A',views.aws_A,name='AWS_A'),

    path('Redhat_B',views.redhat_B,name='Redhat_B'),
    path('Redhat_I',views.redhat_I,name='Redhat_I'),
    path('Redhat_A',views.redhat_A,name='Redhat_A'),

    path('Python_B',views.python_B,name='Python_B'),
    path('Python_I',views.python_I,name='Python_I'),
    path('Python_A',views.python_A,name='Python_A'),

    path('Tensorflow_B',views.tensorflow_B,name='Tensorflow_B'),
    path('Tensorflow_I',views.tensorflow_I,name='Tensorflow_I'),
    path('Tensorflow_A',views.tensorflow_A,name='Tensorflow_A'),

    path('ComputerVision_B',views.computervision_B,name='ComputerVision_B'),
    path('ComputerVision_I',views.computervision_I,name='ComputerVision_I'),
    path('ComputerVision_A',views.computervision_A,name='ComputerVision_A'),

    path('Kubernetes_B',views.kubernetes_B,name='Kubernetes_B'),
    path('Kubernetes_I',views.kubernetes_I,name='Kubernetes_I'),
    path('Kubernetes_A',views.kubernetes_A,name='Kubernetes_A'),

    path('ScikitLearn_B',views.scikitlearn_B,name='ScikitLearn_B'),
    path('ScikitLearn_I',views.scikitlearn_I,name='ScikitLearn_I'),
    path('ScikitLearn_A',views.scikitlearn_A,name='ScikitLearn_A')
]