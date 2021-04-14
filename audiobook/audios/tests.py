from django.test import TestCase
from audios.models import Song, AudioBook, Podcast, Participant
# Create your tests here.

class SongTestCase(TestCase):
    def setUp(self):
        print("******************************************")
        print("Testing Song")
        print("Creating Song1")
        Song.objects.create(song_name="song_test_shell1", duration_in_seconds=250)
        print("Creating Song2")
        Song.objects.create(song_name="song_test_shell2", duration_in_seconds=250)


    def test_song_created_fields_check(self):
        """tests for song"""

        print("Test for first entry")
        #Test for first entry
        song_one = Song.objects.get(song_name="song_test_shell1")
        self.assertEqual(song_one.song_name,"song_test_shell1","song_name doesnot match") 
        self.assertEqual(song_one.duration_in_seconds,250,"duration_in_seconds doesnot match")
        id = song_one.id
        assert id != None,"This field should not be empty"
        uploaded_time = song_one.uploaded_time
        assert uploaded_time != None, "This field should not be empty"

        print("Test for second entry")
        #Test for second entry
        song_two = Song.objects.get(song_name="song_test_shell2")
        self.assertEqual(song_two.song_name,"song_test_shell2","song_name doesnot match") 
        self.assertEqual(song_two.duration_in_seconds,250,"duration_in_seconds doesnot match")
        id = song_two.id
        assert id != None,"This field should not be empty"
        uploaded_time = song_two.uploaded_time
        assert uploaded_time != None, "This field should not be empty"

        print("try to get wrong song")
        #try to get wrong song
        count = Song.objects.filter(song_name="song_test_shell3").count()
        self.assertEqual(count,0,"There should not be an bobect with song_name='song_test_shell3'")


class AudioBookCase(TestCase):
    
    def setUp(self):
        print("******************************************")
        print("tests for audiobook")
        print("creating first audiobook")
        AudioBook.objects.create(title="audiobook_test_shell1", author="book1",narrator="n_book1",duration_in_seconds=250)


    def test_audiobook_created_fields_check(self):
        """tests for audiobook"""
        print("Test for first entry")
        #Test for first entry
        audiobook_one = AudioBook.objects.get(title="audiobook_test_shell1")
        self.assertEqual(audiobook_one.title,"audiobook_test_shell1","title doesnot match") 
        self.assertEqual(audiobook_one.duration_in_seconds,250,"duration_in_seconds doesnot match")
        self.assertEqual(audiobook_one.narrator,"n_book1","narrator doesnot match") 
        self.assertEqual(audiobook_one.author,"book1","author doesnot match")
        id = audiobook_one.id
        assert id != None,"id field should not be empty"
        uploaded_time = audiobook_one.uploaded_time
        assert uploaded_time != None, "uploaded_time field should not be empty"

        print("try to get wrong audiobook")
        #try to get wrong audiobook
        count = AudioBook.objects.filter(title="audiobook_test_shell2").count()
        self.assertEqual(count,0,"There should not be an object with title='audiobook_test_shell1'")

class PodcastCase(TestCase):
    def setUp(self):
        print("******************************************")
        print("tests for podcasts")
        print("creating first for podcast")
        Podcast.objects.create(podcast_name="podcast_test_shell1", host="book1",duration_in_seconds=250)
        podcast_one = Podcast.objects.get(podcast_name="podcast_test_shell1")
        print("adding new participant to this podcast")
        Participant.objects.create(name="parti_test_shell1", podcast=podcast_one)


    def test_podcast_created_fields_check(self):
        """tests for podcasts"""
        print("Test for first entry")
        #Test for first entry
        podcast_one = Podcast.objects.get(podcast_name="podcast_test_shell1")
        self.assertEqual(podcast_one.podcast_name,"podcast_test_shell1","title doesnot match") 
        self.assertEqual(podcast_one.duration_in_seconds,250,"duration_in_seconds doesnot match")
        self.assertEqual(podcast_one.host,"book1","narrator doesnot match") 
        id = podcast_one.id
        assert id != None,"id field should not be empty"
        uploaded_time = podcast_one.uploaded_time
        assert uploaded_time != None, "uploaded_time field should not be empty"

        print("added participant check")
        #added participant check
        participant1=podcast_one.participants.all()[0]
        assert podcast_one.participants.all()[0]==participant1,"participant should be available"

        print("try to get wrong podcast")
        #try to get wrong song
        count = Podcast.objects.filter(podcast_name="podcast_test_shell2").count()
        self.assertEqual(count,0,"There should not be an object with podcast_name='podcast_test_shell1'")



