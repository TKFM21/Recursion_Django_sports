from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views import View
from .models import Game, Pickup, Link


class Index(View):
    def get(self, request, *args, **kwargs):
        gameId = self.kwargs['pk'] if 'pk' in self.kwargs else None
        game_data = None
        if gameId:
            game_data = get_object_or_404(Game, id=gameId)
        else:
            game_data = Game.objects.order_by('?')[0]
        return render(request, 'app/index.html', {
            'game_data': game_data,
        })

class RuleIndex(View):
    def get(self, request, *args, **kwargs):
        game_data = get_object_or_404(Game, id=self.kwargs['pk'])
        return render(request, 'app/rule.html', {
            'game_data': game_data,
        })

class PickupsIndex(View):
    def get(self, request, *args, **kwargs):
        pickup_data = get_list_or_404(Pickup, game=self.kwargs['pk'])
        game_data = get_object_or_404(Game, id=self.kwargs['pk'])
        return render(request, 'app/pickups.html', {
            'game_data': game_data,
            'pickup_data': pickup_data,
        })

class PickupDetail(View):
    def get(self, request, *args, **kwargs):
        pickup_data = get_object_or_404(Pickup, id=self.kwargs['id'])
        game_data = get_object_or_404(Game, id=self.kwargs['pk'])
        return render(request, 'app/pickup_detail.html', {
            'game_data': game_data,
            'pickup_data': pickup_data,
        })

class Links(View):
    def get(self, request, *args, **kwargs):
        link_data = get_list_or_404(Link, game=self.kwargs['pk'])
        game_data = get_object_or_404(Game, id=self.kwargs['pk'])
        return render(request, 'app/links.html', {
            'game_data': game_data,
            'link_data': link_data,
        })
