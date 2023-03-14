from django.urls import path

from debitors.views import DebitorViews

urlpatterns = [
    path('', DebitorViews.as_view()),
]
