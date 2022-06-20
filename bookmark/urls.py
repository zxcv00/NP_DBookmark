from django.urls import path

from bookmark import views
from bookmark.views import BookmarkListView, BookmarkCreateView, BookmarkDetailView, BookmarkUpdateView, \
    BookmarkDeleteView

app_name = 'bookmark'

urlpatterns = [
    # path('list/', BookmarkListView.as_view(), name='list'),  # bookmark:list
    path('lsit2/', views.list_bookmark, name='list'),
    path('add/', BookmarkCreateView.as_view(), name='add'),  # bookmark:add
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),  #bookmark:detail
    path('edit/<int:pk>/', BookmarkUpdateView.as_view(), name='edit'),  #bookmark:edit
    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name='delete'),  #bookmark:delete
]
