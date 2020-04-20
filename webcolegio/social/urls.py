from django.urls import path
from .views import LinkListView, LinkUpdateView

link_urldash = ([
    path('list/', LinkListView.as_view(), name='list'),
    path('update/<int:pk>/', LinkUpdateView.as_view(), name='update'),
], 'link_urldash')
