from django.db import models


class Game(models.Model):
    name = models.CharField('name', max_length=100)
    desc = models.TextField('desc')
    imgUrl = models.URLField('imgUrl')
    rule = models.TextField('rule')

    def __str__(self):
        return self.name


class Pickup(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField('name', max_length=200)
    desc = models.TextField('desc')
    imgUrl = models.URLField('imgUrl')
    status = models.CharField('status', max_length=20)

    def __str__(self):
        return self.game.name + '/' + self.name


class Link(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField('name', max_length=200)
    desc = models.TextField('desc')
    url = models.URLField('url')

    def __str__(self):
        return self.game.name + '/' + self.name
