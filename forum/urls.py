from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views  # Importation des vues de l'application

app_name = 'forum'  # Namespace pour éviter les conflits de nom dans le projet

urlpatterns = [
    # Routes pour les publications
    path('', views.home, name='home'),  # Page d'accueil
    path('create/', views.create_publication, name='create_publication'),  # Créer une publication
    path('like/<int:publication_id>/', views.like_publication, name='like_publication'),  # Aimer une publication
    path('send_message/<int:receiver_id>/', views.send_message, name='send_message'),  # Envoyer un message
    path('inbox/', views.inbox, name='inbox'),  # Boîte de réception
    path('login/', views.login_view, name='login'),  # Page de connexion
    path('logout/', views.logout_view, name='logout'),  # Page de déconnexion
    path('register/', views.register, name='register'),  # Page d'inscription
    path('user/<int:user_id>/', views.user_profile, name='user_profile'),  # Profil utilisateur
    path('edit-profile/', views.edit_profile_view, name='edit_profile'),  # Édition du profil

 
]

# Ajouter cette ligne pour servir les fichiers médias en mode développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
