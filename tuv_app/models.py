from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

class Logo(models.Model):
    """
    Model for Logo Images
    """
    logo_image = models.ImageField(upload_to='uploads/logos')

    def clean(self):
        if Logo.objects.exists() and not self.pk:
            raise ValidationError("You can only edit the logo!")

    def save(self, *args, **kwargs):
        # Saves the record
        return super(Logo, self).save(*args, **kwargs)

    def __str__(self):
        return 'Logo';


class Banner(models.Model):
    banner_image = models.ImageField(upload_to='uploads/banners')
    banner_text = models.CharField(max_length=50)

    def __str__(self):
        return self.banner_text


class Album(models.Model):
    album_name = models.CharField(max_length=50)

    def __str__(self):
        return self.album_name

class Song(models.Model):
    song_title = models.CharField(max_length=50)
    song_file = models.FileField(upload_to='uploads/songs')
    song_upload_date = models.DateTimeField(auto_now=True)
    song_image = models.ImageField(upload_to='uploads/songs')
    album = models.ForeignKey('Album', on_delete=models.CASCADE)

    def __str__(self):
        return self.song_title

class FeaturedSong(models.Model):
    song = models.ForeignKey('Song', on_delete=models.CASCADE)

    def clean(self):
        if FeaturedSong.objects.exists() and not self.pk:
            raise ValidationError("You can only edit the featured song!")

    def save(self, *args, **kwargs):
        # Saves the record
        return super(FeaturedSong, self).save(*args, **kwargs)

    def __str__(self):
        return 'FeaturedSong';


class Video(models.Model):
    video_title = models.CharField(max_length=50)
    video_event_name = models.CharField(max_length=100)
    video_link = models.URLField(max_length=254)
    video_image = models.ImageField(upload_to='uploads/videos')

    def __str__(self):
        return self.video_title

class FeaturedVideo(models.Model):
    video = models.ForeignKey('Video', on_delete=models.CASCADE)

    def clean(self):
        if FeaturedVideo.objects.exists() and not self.pk:
            raise ValidationError("You can only edit the logo!")

    def save(self, *args, **kwargs):
        # Saves the record
        return super(FeaturedVideo, self).save(*args, **kwargs)

    def __str__(self):
        return 'FeaturedVideo';

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='uploads/gallery')
    image_description = models.CharField(max_length=50)

    def __str__(self):
        return self.image_description


class Contact(models.Model):
    contact_message = models.TextField()
    contact_name = models.CharField(max_length=50)
    contact_email = models.EmailField(max_length=254)
    contact_subject = models.CharField(max_length=100)

    def __str__(self):
        return self.contact_subject + ' - ' + self.contact_name

class Footer(models.Model):
    about_us = models.TextField()
    about_image = models.ImageField(upload_to='uploads/about')
    footer_text = models.CharField(max_length=254)
    email_address = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=50)
    call_time = models.CharField(max_length=100)
    resident_address = models.CharField(max_length=254)
    postal_code = models.CharField(max_length=50)
    facebook_link = models.URLField(max_length=254)
    twitter_link = models.URLField(max_length=254)
    youtube_link = models.URLField(max_length=254)
    instagram_link = models.URLField(max_length=254)


    def clean(self):
        if Footer.objects.exists() and not self.pk:
            raise ValidationError("You can only edit the footer!")

    def save(self, *args, **kwargs):
        # Saves the record
        return super(Footer, self).save(*args, **kwargs)

    def __str__(self):
        return 'Footer';
