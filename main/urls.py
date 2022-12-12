from .yasg import urlpatterns as swagger
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')),
    path('blogs/', include('blog.urls')),
    path('core/', include('core.urls')),
    path('users/', include('my_users.urls')),
    path('todo-app/', include('todo_app.urls'))
] + swagger
