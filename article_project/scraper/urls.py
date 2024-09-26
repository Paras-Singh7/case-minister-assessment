from django.urls import path
from .views import ScrapeAPIView

urlpatterns = [
    path("article/", ScrapeAPIView.as_view(), name="scrape"),
]
