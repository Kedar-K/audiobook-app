from django.db import models

MAX_PODCAST_USER_ALLOWED = 10

class Song(models.Model):
    song_name = models.CharField(max_length=100)
    duration_in_seconds = models.PositiveIntegerField()
    uploaded_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.song_name


class AudioBook(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    narrator = models.CharField(max_length=100)
    duration_in_seconds = models.PositiveIntegerField()
    uploaded_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - By: ({self.narrator})"


class Podcast(models.Model):
    podcast_name = models.CharField(max_length=100)
    host = models.CharField(max_length=100)
    duration_in_seconds = models.PositiveIntegerField()
    uploaded_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.podcast_name} - By: ({self.host})"

    
    def get_participants(self, id):
        parti = Podcast.objects.get(pk=id).participants.all()
        p = []
        for x in parti:
            p.append(x.name)
        return p


class Participant(models.Model):
    name = models.CharField(max_length=100)
    podcast = models.ForeignKey(to=Podcast, related_name='participants', on_delete=models.CASCADE)


    def save(self, *args, **kwargs):
        podcast_user__count = Participant.objects.filter(podcast=self.podcast).count()
        if podcast_user__count >= MAX_PODCAST_USER_ALLOWED and not self.pk:
            raise Exception(f"Max number of participants allowed are {MAX_PODCAST_USER_ALLOWED}")
        else:
            super(Participant, self).save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.name}"
