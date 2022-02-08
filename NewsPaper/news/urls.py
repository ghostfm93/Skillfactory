from django.urls import path
from .views import NewsList, NewsDetail, SearchList, PostCreate, PostDelete, PostUpdate

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', NewsDetail.as_view()),
    path('search', SearchList.as_view()),
    path('create/', PostCreate.as_view()),
    path('delete/<int:pk>', PostDelete.as_view()),
    path('update/<int:pk>',PostUpdate.as_view()),
]