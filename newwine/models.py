from django.db import models
from tinymce import HTMLField


# Index
class Carousel(models.Model):
    image = models.FileField('File', upload_to='carousel/')
    caption = models.TextField(max_length=300)
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Carousel'
        verbose_name_plural = 'Carousel'

    def __str__(self):
        return self.caption


class MainEvent(models.Model):
    image = models.FileField('File', upload_to='event/')
    name = models.CharField(max_length=100)
    details = models.TextField(max_length=500)
    added = models.DateTimeField(auto_now_add=True)
    event_time = models.CharField(max_length=150, default="January 01 1999 00:00:00")

    class Meta:
        verbose_name = 'Main Event'
        verbose_name_plural = 'Main Event'

    def __str__(self):
        return self.name


class Quote(models.Model):
    quote = models.TextField(max_length=300)
    author = models.CharField(max_length=100)
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Quote'
        verbose_name_plural = 'Quotes'

    def __str__(self):
        return self.author + " - " + self.quote


class LatestSermons(models.Model):
    added = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    summary = HTMLField('Sermon summary')
    #   summary = models.TextField(max_length=500)

    class Meta:
        verbose_name = 'Latest Sermon'
        verbose_name_plural = 'Latest Sermons'

    def __str__(self):
        return self.title


class Announcements(models.Model):
    added = models.DateTimeField(auto_now_add=True)
    title = models.TextField(default='None')
    announcement = models.TextField(max_length=1000)

    class Meta:
        verbose_name = 'Announcements'
        verbose_name_plural = 'Announcements'

    def __str__(self):
        return self.title

# Index END


# ABOUT

# ABOUT END


# EXECUTIVES
class ExecutivesThumbnail(models.Model):
    profile = models.FileField('File', upload_to='excom/')
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Executives Thumbnails'
        verbose_name_plural = 'Executives Thumbnails'

    def __str__(self):
        return self.name + " - " + self.position


class ExecutivesDetails(models.Model):
    executive = models.ForeignKey(ExecutivesThumbnail, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    hostel = models.CharField(max_length=100)
    course = models.CharField(max_length=150)
    contact = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Executives Details'
        verbose_name_plural = 'Executives Details'

    def __str__(self):
        return self.name + " - " + self.position
# EXECUTIVES END


# IMAGES 2
class Gallery(models.Model):
    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'

    added = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=150)
    album_pic = models.FileField('File', upload_to='album_thumbnails')
    caption = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Images(models.Model):
    file = models.FileField('File', upload_to='gallery_images/')
    gallery = models.ForeignKey(Gallery, blank=True, null=True, on_delete='CASCADE')

    def __str__(self):
        return self.filename

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    @property
    def filename(self):
        return self.file.name.rsplit('/', 1)[-1]

# 'File', upload_to='images/'
#   IMAGES 2 END


class RegisteredMembers(models.Model):
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(max_length=20)
    date_of_birth = models.CharField(max_length=50)
    course = models.CharField(max_length=150)
    year = models.CharField(max_length=10)
    hall_or_hostel = models.CharField(max_length=100)
    room = models.CharField(max_length=10)
    department = models.CharField(max_length=70)
    covenant_family = models.CharField(max_length=100)
    home_temple = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Registered Members'
        verbose_name_plural = 'Registered Members'

    def __str__(self):
        return self.first_name + " " + self.surname + " - " + self.phone


#   DEPARTMENTS


class Departments(models.Model):
    department_image = models.FileField('File', upload_to='department_image/')
    department_name = models.CharField(max_length=100)
    department_about = models.TextField(max_length=1000)
    department_function = models.TextField(max_length=1000)
    department_meeting_day_1 = models.CharField(max_length=50)
    department_meeting_day_2 = models.CharField(max_length=50)
    department_meeting_time_1 = models.CharField(max_length=50)
    department_meeting_time_2 = models.CharField(max_length=50)
    department_venue_1 = models.CharField(max_length=50)
    department_venue_2 = models.CharField(max_length=50)
    department_leader_image = models.FileField('File', upload_to='leaders/')
    department_leader_name = models.CharField(max_length=150)
    department_leader_hostel = models.CharField(max_length=100)
    department_leader_course = models.CharField(max_length=150, null=True)
    department_leader_contact = models.CharField(max_length=100)
    department_deputy_image = models.FileField('File', upload_to='leaders/')
    department_deputy_name = models.CharField(max_length=150)
    department_deputy_hostel = models.CharField(max_length=100)
    department_deputy_course = models.CharField(max_length=150, null=True)
    department_deputy_contact = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'

    def __str__(self):
        return self.department_name

#   DEPARTMENTS END

#   SERMONS


class Sermons(models.Model):
    image = models.FileField('File', upload_to='sermons/')
    audio = models.FileField('File', upload_to='sermons/')
    title = models.CharField(max_length=100)
    minister = models.CharField(max_length=150)
    day_of_message = models.CharField(max_length=50)
    is_playing = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Sermon'
        verbose_name_plural = 'Sermons'

    def __str__(self):
        return self.minister + " - " + self.title
#   SERMONS END


#   COVENANT FAMILY

class Family(models.Model):
    cov_img = models.FileField('File', upload_to='covenant_family/')
    cov_name = models.CharField(max_length=150)
    cov_day = models.CharField(max_length=20)
    cov_time = models.CharField(max_length=10)
    cov_location = models.CharField(max_length=60)
    cov_head = models.CharField(max_length=200)
    cov_head_image = models.FileField('File', upload_to='leaders/')
    cov_course = models.CharField(max_length=150, null=True)
    cov_hostel = models.CharField(max_length=150, null=True)
    cov_contact = models.CharField(max_length=100)
    dept_cov_head = models.CharField(max_length=200)
    dept_head_image = models.FileField('File', upload_to='leaders/')
    dept_cov_course = models.CharField(max_length=150, null=True)
    dept_cov_hostel = models.CharField(max_length=150, null=True)
    dept_cov_head_contact = models.CharField(max_length=150)

    class Meta:
        verbose_name = 'Covenant Family'
        verbose_name_plural = 'Covenant Families'

    def __str__(self):
        return self.cov_name

#   COVENANT FAMILY END

#   INITIATORS


class Initiators(models.Model):
    initiators_img = models.FileField('File', upload_to='initiators_images')
    initiators_name = models.CharField(max_length=200)
    initiators_portfolio = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Initiator'
        verbose_name_plural = 'Initiators'

    def __str__(self):
        return self.initiators_name

#   INITIATORS END


#   TEAMS

class Teams(models.Model):
    team_name = models.CharField(max_length=300)
    team_role = HTMLField('Team Role')

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

    def __str__(self):
        return self.team_name

#   TEAMS END


#   THEME
class Theme(models.Model):
    theme_name = models.CharField(max_length=400, null=True)
    theme_verse_body = HTMLField('Theme Verse Body', null=True)
    theme_verse_scripture = models.CharField(max_length=150, null=True)
    theme_body = HTMLField('Theme Body', null=True)
    theme_tenets = HTMLField('Theme Tenets', null=True)

    class Meta:
        verbose_name = 'Theme'
        verbose_name_plural = 'Themes'

    def __str__(self):
        return self.theme_name

#   THEME END


#   COORDINATOR
class Coordinator(models.Model):
    coord_portfolio = models.CharField(max_length=200)
    coord_img = models.FileField('File', upload_to='coordinators')
    coord_name = models.CharField(max_length=200)
    coord_course = models.CharField(max_length=200)
    coord_hostel = models.CharField(max_length=200)
    coord_contact = models.CharField(max_length=100)
    coord_role = HTMLField('Coordinator Role')

    class Meta:
        verbose_name = 'Coordinator'
        verbose_name_plural = 'Coordinators'

    def __str__(self):
        return self.coord_name+" - "+self.coord_portfolio

#   COORDINATOR END


#   GENDER COORDINATORS
class Gender(models.Model):
    men_coord_portfolio = models.CharField(max_length=200)
    men_coord_img = models.FileField('File', upload_to='coordinators')
    men_coord_name = models.CharField(max_length=200)
    men_coord_course = models.CharField(max_length=200)
    men_coord_hostel = models.CharField(max_length=200)
    men_coord_contact = models.CharField(max_length=100)
    women_coord_portfolio = models.CharField(max_length=200)
    women_coord_img = models.FileField('File', upload_to='coordinators')
    women_coord_name = models.CharField(max_length=200)
    women_coord_course = models.CharField(max_length=200)
    women_coord_hostel = models.CharField(max_length=200)
    women_coord_contact = models.CharField(max_length=100)
    gender_coord_role = HTMLField('Gender Coodrinators Role')

    class Meta:
        verbose_name = 'Gender Coordinators'
        verbose_name_plural = 'Gender Coordinators'

    def __str__(self):
        return "Gender Coordinators"

#   GENDER COORDINATORS END


#   ARTICLES
class Articles(models.Model):
    article_img = models.FileField('Article Image', upload_to='article_images')
    article_title = models.CharField(max_length=100)
    article_overview = models.CharField(max_length=200)
    article_body = HTMLField('Article Body')
    article_owner_name = models.CharField(max_length=200)
    article_owner_title = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.article_title

#   ARTICLES END


#   TESTIMONIES
class Testimonies(models.Model):
    testimony_img = models.FileField('Testimony Image', upload_to='testimony_images')
    testimony_title = models.CharField(max_length=100)
    testimony_overview = models.CharField(max_length=200)
    testimony_body = HTMLField('Testimony Body')
    testimony_owner_name = models.CharField(max_length=200)
    testimony_owner_title = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Testimony'
        verbose_name_plural = 'Testimonies'

    def __str__(self):
        return self.testimony_title

#   TESTIMONIES END


#   TEACHINGS
class Notes(models.Model):
    note_img = models.FileField('Notes Image', upload_to='notes_images')
    note_title = models.CharField(max_length=100)
    note_overview = models.CharField(max_length=200)
    note_body = HTMLField('Note Body')
    note_owner_name = models.CharField(max_length=200)
    note_owner_title = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Teachings'
        verbose_name_plural = 'Teachings'

    def __str__(self):
        return self.note_title

#   TEACHINGS END


#   BIBLE STUDY OUTLINES
class Outlines(models.Model):
    outline_img = models.FileField('Study Outline Image', upload_to='oultline_images')
    outline_title = models.CharField(max_length=100)
    outline_overview = models.CharField(max_length=200)
    outline_body = HTMLField('Note Body')
    outline_owner_name = models.CharField(max_length=200)
    outline_owner_title = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Bible Study Outline'
        verbose_name_plural = 'Bible Study Outlines'

    def __str__(self):
        return self.outline_title

#   BIBLE STUDY OUTLINES END
