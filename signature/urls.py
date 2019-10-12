from django.urls import path
from .views import SignAPIView, SignOutputView

app_name = 'sign'

urlpatterns = [
    path('input', SignAPIView.as_view(), name='input'),
    path('output/<int:model>', SignOutputView.as_view(), name='output')
]