
from django.urls import path
from . import views 
urlpatterns = [
   
    path('',views.index,name='index'),
    path('add',views.addPost,name='add'),
    path('details/<posts_id>',views.displayPost,name='display'),
    path('update/<id>',views.updatePost,name='update'),
    path('delete/<id>',views.deletePost,name='delete'),
]
