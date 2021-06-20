from django.urls import path
from main_app.views import home_page

urlpatterns = [
    path("", home_page.as_view())
]
