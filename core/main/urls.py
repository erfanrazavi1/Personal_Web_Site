from django.urls import path
from main.views import (
    home,
)
# from django.views.generic import TemplateView

app_name = 'main'

urlpatterns = [
    path('', home, name='home'),
    # path('', TemplateView.as_view(template_name='index.html'), name='home'),

]
