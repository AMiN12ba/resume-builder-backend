from turtle import home
from main import views
from main.views import IndexView
from django.urls import path


app_name = 'main'


urlpatterns = [
    path('', views.IndexView.as_view(), name="home"),
	path('contact/', views.ContactView.as_view(), name="contact"),
	path('blog/', views.BlogView.as_view(), name="blogs"),
	path('blog/<slug:slug>', views.BlogDetailView.as_view(), name="blog"),
]
