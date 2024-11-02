# urls.py (fichier principal du projet)
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from forum import views  # Importation des vues de l'application principale

urlpatterns = [
    path('admin/', admin.site.urls),  # Accès à l'interface d'administration
    path('', views.home, name='home'),  # Page d'accueil de l'application
    path('create/', views.create_publication, name='create_publication'),  # Créer une publication
    path('like/<int:publication_id>/', views.like_publication, name='like_publication'),  # Aimer une publication
    path('send_message/<int:receiver_id>/', views.send_message, name='send_message'),  # Envoyer un message
    path('inbox/', views.inbox, name='inbox'),  # Boîte de réception
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Page de connexion
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Page de déconnexion
    path('register/', views.register, name='register'),  # Page d'inscription
    path('user/<int:user_id>/', views.user_profile, name='user_profile'),  # Profil utilisateur
    path('forum/', include(('forum.urls', 'forum'), namespace='forum')),  # Inclure les routes du forum
    path('forum/', include('forum.urls', namespace='forum')),

]

# Servir les fichiers médias en mode développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)