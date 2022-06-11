from django.urls import path
from testapp import views

urlpatterns = [
    path('add_item_view/',views.add_item_view,name='add_item_view'),
    path('display_item_view/',views.display_item_view,name='display_item_view')
]