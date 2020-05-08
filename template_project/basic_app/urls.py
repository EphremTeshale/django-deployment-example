from django.urls import path

from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('',views.index,name='index_page'),
    path('other/', views.other,name='other_page'),
    path('relative/', views.relative,name='relative_url_page'),
]