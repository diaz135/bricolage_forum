from django.shortcuts import render, redirect, get_object_or_404
from .models import Publication, Like, Message
from .forms import PublicationForm, CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm
from .models import Profile
from .forms import ProfileForm


def home(request):
    publications = Publication.objects.all()
    liked_publications = Like.objects.filter(user=request.user).values_list('publication_id', flat=True) if request.user.is_authenticated else []
    return render(request, 'forum/home.html', {
        'publications': publications,
        'liked_publications': liked_publications,
    })

@login_required
def create_publication(request):
    if request.method == 'POST':
        form = PublicationForm(request.POST, request.FILES)
        if form.is_valid():
            publication = form.save(commit=False)
            publication.author = request.user
            publication.save()
            messages.success(request, 'Publication créée avec succès.')
            return redirect('home')
    else:
        form = PublicationForm()
    return render(request, 'forum/create_publication.html', {'form': form})

@login_required
def like_publication(request, publication_id):
    publication = get_object_or_404(Publication, id=publication_id)
    like, created = Like.objects.get_or_create(publication=publication, user=request.user)
    if not created:
        like.delete()
    return redirect('home')

@login_required
def send_message(request, receiver_id):
    receiver = get_object_or_404(User, id=receiver_id)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            message = Message(sender=request.user, receiver=receiver, content=content)
            message.save()
            messages.success(request, 'Message envoyé avec succès.')
            return redirect('home')
        else:
            messages.error(request, 'Le message ne peut pas être vide.')
    return render(request, 'forum/send_message.html', {'receiver': receiver})

@login_required
def inbox(request):
    received_messages = Message.objects.filter(receiver=request.user)
    return render(request, 'forum/inbox.html', {'messages': received_messages})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Inscription réussie ! Bienvenue.')
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def user_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    users = User.objects.exclude(id=user.id)
    return render(request, 'user_profile.html', {'user': user, 'users': users})

def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

def login_view(request):
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirige vers la page d'accueil ou une autre page
            else:
                form.add_error(None, 'Nom d’utilisateur ou mot de passe incorrect.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)  # Connecte l'utilisateur après l'inscription
            return redirect('forum:home')  # Redirige vers la page d'accueil
    else:
        form = RegistrationForm()
    return render(request, 'registration.html', {'form': form})

@login_required
def edit_profile_view(request):
    profile = request.user.profile  # Récupère le profil de l'utilisateur
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('forum:home')  # Redirige vers la page d'accueil
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})
