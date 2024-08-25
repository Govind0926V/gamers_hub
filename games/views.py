# games/views.py

from django.shortcuts import render, redirect
from .models import User, Game, Review, GameList

def home(request):
    # Logic for the homepage
    return render(request, 'games/home.html')

def profile(request, username):
    
    user = User.nodes.get(username=username)
    return render(request, 'games/profile.html', {'user': user})

def game_detail(request, game_id):
    game = Game.nodes.get(id=game_id)
    return render(request, 'game_detail.html', {'game': game})

def add_review(request, game_id):
    if request.method == 'POST':
        content = request.POST['content']
        rating = request.POST['rating']
        user = User.nodes.get(id=request.user.id)
        game = Game.nodes.get(id=game_id)
        review = Review(content=content, rating=rating).save()
        review.reviewer.connect(user)
        review.game.connect(game)
        return redirect('game_detail', game_id)

def add_friend(request, user_id):
    user = User.nodes.get(id=request.user.id)
    friend = User.nodes.get(id=user_id)
    user.friends.connect(friend)
    return redirect('profile', user_id)

def recommendations(request):
    user = User.nodes.get(id=request.user.id)
    recommendations = recommend_games(user)  # type: ignore # Assuming recommend_games is defined
    return render(request, 'recommendations.html', {'recommendations': recommendations})
