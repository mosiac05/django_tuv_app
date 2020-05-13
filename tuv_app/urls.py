from django.urls import path
from tuv_app import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "tuv_app"

urlpatterns = [
    path('', views.HomePage.as_view(),name='home'),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('tracks/', views.TracksPage.as_view(), name='tracks'),
    path('contact/', views.contact, name='contact'),
    path('album/<pk>', views.album, name='album'),
    path('lyrics/<pk>', views.lyrics, name='lyrics'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
