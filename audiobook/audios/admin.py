from django.contrib import admin
from .models import Song, AudioBook, Podcast, Participant
# Register your models here.
admin.site.register(Song)
admin.site.register(AudioBook)
admin.site.register(Podcast)
admin.site.register(Participant)
