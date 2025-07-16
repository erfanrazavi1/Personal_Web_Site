from django.urls import path
from main.views import (
    home,
    about,
    contact,
    portfolio,
)



urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('portfolio/', portfolio, name='portfolio'),

]
