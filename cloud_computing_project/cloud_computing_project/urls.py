"""cloud_computing_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from book.views import books_json, book_json, book_html
from counter.views import increase_counter, get_count
urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', books_json),
    path('books/<int:id>', book_json),
    path('bookh/<int:id>', book_html),
    path('counter/increase', increase_counter),
    path('counter/', get_count)
]
