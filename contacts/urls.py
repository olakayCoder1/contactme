from django.urls import path
from . import views









urlpatterns = [ 
    path('', views.index, name='index'),
    path('contact/about/<str:id>', views.about_contact, name='about-contact'),
    path('contact/add', views.add_contact, name='add-contact'),
    path('contact/about/edit/<str:id>', views.edit_contact, name='edit-contact'),
    path('contact/about/delete/<str:id>', views.delete_contact, name='delete-contact'),
    path('contact/search', views.search_contact, name='search-contact')
]