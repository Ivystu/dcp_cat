from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('second/', views.second, name='second'),
    path('quiz_cat_1/', views.quiz_cat_1, name='quiz_cat_1'),
    path('quiz_cat_2/', views.quiz_cat_2, name='quiz_cat_2'),
    path('quiz_cat_3/', views.quiz_cat_3, name='quiz_cat_3'),
    path('quiz_cat_4/', views.quiz_cat_4, name='quiz_cat_4'),
    path('quiz_cat_5/', views.quiz_cat_5, name='quiz_cat_5'),
    path('test_result_cat/', views.test_result_cat, name='test_result_cat'),
]