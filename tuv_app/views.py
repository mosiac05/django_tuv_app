import os
from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView
from django.conf import settings
from django.templatetags.static import static
from django.urls import reverse
from tuv_app.models import Logo,Banner,Album,Song,FeaturedSong,Video,FeaturedVideo,GalleryImage,Contact,Footer
from tuv_app.forms import ContactForm
# Create your views here.
footer = Footer.objects.all()
banner = Banner.objects.order_by('?')
albums = Album.objects.all()

context = {}

class HomePage(TemplateView):
    """
    Displays the homepage of the site
    """
    template_name = 'index.html';


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['footer'] = footer[:1]
        context['banner'] = banner[:1]
        context['song_albums'] = albums

        featured_song = FeaturedSong.objects.first()
        context['featured_song'] = featured_song

        videos = Video.objects.order_by('?')[:5]
        context['videos'] = videos

        songs = Song.objects.all()[:4]
        context['songs'] = songs

        gallery_images = GalleryImage.objects.order_by('?')[:7]
        context['gallery_images'] = gallery_images

        return context

class AboutPage(TemplateView):
    """
    Displays the about page
    """

    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['footer'] = footer[:1]
        context['banner'] = banner[:1]
        context['song_albums'] = albums

        featured_video = FeaturedVideo.objects.first()
        context['featured_video'] = featured_video

        gallery_images = GalleryImage.objects.all()[:13]
        context['gallery_images'] = gallery_images

        return context

class TracksPage(ListView):
    """
    Displays the Our Tracks page
    """
    model = Song
    template_name = 'tracks.html'
    context_object_name = 'songs'
    paginate_by = 6
    songs = Song.objects.order_by('song_upload_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['footer'] = footer[:1]
        context['banner'] = banner[:1]
        context['song_albums'] = albums

        videos = Video.objects.order_by('?')[:5]
        context['videos'] = videos

        return context

##########################################################
##                  FUNCTION BASED VIEWS                ##
#########################################################
def contact(request):

    submitted = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = Contact()
            contact.contact_name = form.cleaned_data['name']
            contact.contact_email = form.cleaned_data['email']
            contact.contact_subject = form.cleaned_data['subject']
            contact.contact_message = form.cleaned_data['message']
            contact.save()
            submitted = True
            return render(request, 'contact.html', {'submitted': submitted, 'footer': footer[:1], 'banner': banner[:1], 'song_albums': albums})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form, 'song_albums': albums, 'submitted': submitted, 'footer': footer[:1], 'banner': banner[:1],})


def album(request, pk):
    songs = Song.objects.filter(album=pk).order_by('song_upload_date')
    return render(request, 'tracks.html', {'songs': songs, 'banner': banner[:1], 'footer': footer[:1], 'song_albums': albums})

def lyrics(request, pk):
    single_song = Song.objects.filter(pk=pk).first()
    songs = Song.objects.order_by('song_upload_date')[:5]
    return render(request, 'lyrics.html', {'single_song': single_song, 'songs': songs, 'banner': banner[:1]})
