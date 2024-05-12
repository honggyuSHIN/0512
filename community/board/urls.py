from django.urls import path
from .views import *

app_name='board'

urlpatterns=[
    path('',board_list),
    path('<int:pk>/',board_detail),

    path('post/create/',board_third),
    path('post/detail/<int:pk>/',board_detail),
    path('post/update/<int:pk>/',board_fix),
    path('post/delete/<int:pk>/',board_delete),
    path('comment/create/<int:post_id>/',create_comment),
    path('comment/list/<int:post_id>/',get_comments),

    
    
    
]