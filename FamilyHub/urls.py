from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(), name='login'), 
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # App URLs - All namespaces are correct
    path('', include('core.urls')), 
    path('gallery/', include('gallery.urls', namespace='gallery')), 
    path('blog/', include('blog.urls', namespace='blog')),
    path('calendar/', include('calendar_app.urls', namespace='calendar_app')),
    path('contacts/', include('contacts.urls', namespace='contacts')),
    path('recipes/', include('recipes.urls', namespace='recipes')),
]

# 🟢 CRITICAL FIX: STATIC AND MEDIA FILES IN DEVELOPMENT MODE 🟢
if settings.DEBUG:
    # 🌟 THIS LINE IS CRITICAL FOR CSS/JS TO LOAD 🌟
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
    # Media Files (Images, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
