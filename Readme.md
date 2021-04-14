## Project setup

### Creating Virtual env (optional)

Clone repo to a folder.
`cd audiobook`
then create a new virtual environment.
`python -m venv venv` then source it `source venv/bin/activate`

### project related

Dependencies
`pip install -r requirements.txt`
`cd audiobook`

steps for migrations.

- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py createsuperuser` -- then follow process (admin, admin)

`python manage.py runserver`

### Testing

`cd audiobook`
`python manage.py test`

### Admin

To Access website go to .
http://localhost:8000/

- For Admin panel: admin/
  use recently created credentials.

## RUN from UI

### Usability

\_To see currecnly added elements/ add new element (you will get form on UI to do these operations)

"songs": "http://127.0.0.1:8000/songs/",

"podcasts": "http://127.0.0.1:8000/podcasts/",

"audiobooks": "http://127.0.0.1:8000/audiobooks/",

_To see/delete/modify particular added elements (you will get form on UI to do these operations)_

"songs": "http://127.0.0.1:8000/songs/id",

"podcasts": "http://127.0.0.1:8000/podcasts/id",

"audiobooks": "http://127.0.0.1:8000/audiobooks/id",

**Optional - The GET ,POST ,PUT ,DELETE can also be tested from postman once the server is up**

### participants

TO add participants to particuar podcast you can go to "http://127.0.0.1:8000/participant/" add name and select podcast from dropdown

## Run from shell

`cd audiobook`

`python manage.py shell`

Here are the few examples to test the endpoints

- Create:
  Song.objects.create(song_name="song_test_shell2", duration_in_seconds=250)

- Delete: AudioBook.objects.filter(title="audiobook_test_shell2").delete()

- Update: AudioBook.objects.filter(title="audiobook_test_shell2").update(duration_in_seconds=250)

- Get: Podcast.objects.get(podcast_name="podcast_test_shell1").participants.all()
