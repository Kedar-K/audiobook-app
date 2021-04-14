from rest_framework import routers, serializers, viewsets
from audios.models import Song, AudioBook, Podcast, Participant

# Serializers define the API representation.
class SongSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'song_name', 'duration_in_seconds', 'uploaded_time']

# ViewSets define the view behavior.
class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


# Serializers define the API representation.
class PodcastSerializer(serializers.HyperlinkedModelSerializer):
    participants = serializers.StringRelatedField(many=True)
    class Meta:
        model = Podcast
        fields = ['id', 'podcast_name', 'duration_in_seconds', 'uploaded_time', 'host', 'participants']

# ViewSets define the view behavior.
class PodcastViewSet(viewsets.ModelViewSet):
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer

# Serializers define the API representation.
class AudiobookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AudioBook
        fields = ['id', 'title', 'duration_in_seconds', 'uploaded_time', 'author', 'narrator']

# ViewSets define the view behavior.
class AudiobookViewSet(viewsets.ModelViewSet):
    queryset = AudioBook.objects.all()
    serializer_class = AudiobookSerializer


# Serializers define the API representation.
class ParticipantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Participant
        fields = ['name', 'podcast']

# ViewSets define the view behavior.
class ParticipantbookViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'songs', SongViewSet)
router.register(r'podcasts', PodcastViewSet)
router.register(r'audiobooks', AudiobookViewSet)
router.register(r'participant', ParticipantbookViewSet)
