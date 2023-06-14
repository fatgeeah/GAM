from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Gamer(models.Model):
    gamer_username = models.CharField(max_length=50)
    gamer_first_name = models.CharField(max_length=50)
    gamer_last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    gamer_games = models.CharField(max_length=100)

    def __str__(self):
        return f'Gamer: {self.gamer_id} {self.gamer_username}'

class Games(models.Model):
    game_names = models.CharField(max_length=100)
    gameThumbnails = models.ImageField(_("Games Thumbnails"),upload_to='thumbnail/',help_text=".jpg,.png ,.jpeg, .gif, .svg supported")
    video = models.FileField(_("Video"), upload_to='videos/', help_text=".mp4 spported only")

    def __str__(self):
        return self.game_names