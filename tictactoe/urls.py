from django.urls import path
from django.views.generic.base import TemplateView
app_name = 'ttt'

urlpatterns = [
    path("",  TemplateView.as_view(template_name="tictactoe.html"), name='tictactoe')
]