# FamilyHub/urls.py (CORRECTED)

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views # Login/Logout के लिए

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(), name='login'), 
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # App URLs - 🌟 NOTE: Added 'namespace' to all app includes 🌟
    path('', include('core.urls')), # Home Page
    
    # gallery में namespace पहले से था, यह सही है
    path('gallery/', include('gallery.urls', namespace='gallery')), 
    
    # blog में namespace जोड़ा गया
    path('blog/', include('blog.urls', namespace='blog')),
    
    # calendar_app में namespace जोड़ा गया
    path('calendar/', include('calendar_app.urls', namespace='calendar_app')),
    
    # contacts में namespace जोड़ा गया
    path('contacts/', include('contacts.urls', namespace='contacts')),
    
    # recipes में namespace जोड़ा गया
    path('recipes/', include('recipes.urls', namespace='recipes')),
]

# Media Files in Development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)