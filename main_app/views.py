from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from .models import Beyonce, Tour, Photo
from .forms import ShowsForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin



S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'beyoncecollector-0217'


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def beyonces_index(request):
    beyonces = Beyonce.objects.filter(user=request.user)
    return render(request, 'beyonce/index.html', {'beyonces': beyonces})

@login_required
def beyonces_detail(request, beyonce_id):
  beyonce = Beyonce.objects.get(id=beyonce_id)
  
  shows_form = ShowsForm() 
  # create a list of toys the cat doesn't have
#   tours_beyonce_doesnt_have = Tour.objects.exclude(id__in=beyonce.tours.all().values_list('id'))
  return render(request, 'beyonces/detail.html', {
    'beyonce': beyonce,
    'shows_form': shows_form,
    # 'tours': tours_beyonce_doesnt_have
  })

@login_required
def add_shows(request, beyonce_id):
  # capture submitted form inputs
  form = ShowsForm(request.POST)
  # validate form inputs
  if form.is_valid():
  # save a temp copy of a new feeding using the form submission
    new_shows = form.save(commit=False)
  # associate the new feeding to the cat using the corresponding cat id
    new_shows.beyonce_id = beyonce_id
  # save the new feeding to the database
    new_shows.save()
  # return with a response to redirect
  # NOTE: we need to import the built-in redirect function/method
  return redirect('detail', beyonce_id=beyonce_id)

@login_required
def add_photo(request, beyonce_id):
  # capture the photo file from the form submission
  photo_file = request.FILES.get('photo-file', None)
  # check if a file was included
  if photo_file:
    # if a file is included
    # initialize a s3 client object
    s3 = boto3.client('s3')
    # create a unique identifier for our photo file
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    # 5683h3.png 
    try:
    # attempt to upload the photo to aws s3
      s3.upload_fileobj(photo_file, BUCKET, key)
      # generate a special url to access the photo remotely
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      # instantiate an instance of the photo model - also associate the cat to the photo
      photo = Photo(url=url, beyonce_id=beyonce_id)
      # save the photo model instance
      photo.save()
    # if something goes wrong, print the error
    except Exception as error:
      print('something went wrong uploading to s3')
      print(error)
  # return a response as a redirect back to the cat show page
  return redirect('detail', beyonce_id=beyonce_id)
@login_required
def assoc_tours(request, beyonce_id):
  Beyonce.objects.get(id=beyonce_id).tours.add(tour_id)
  return redirect('detail', beyonce_id=beyonce_id)

  # the same django view function can handle BOTH POST or GET requests
  # GET -> present the user with a signup form
  # POST -> handle the submission of the signup form
def signup(request):
  error_message = ''
  if request.method == 'POST':
    # handle the creation of the new user
    # capture form inputs from the submission
    form = UserCreationForm(request.POST)
    # validate form inputs
    if form.is_valid():
      # save the new user
      user = form.save()
      # login the new user
      login(request, user)
      # redirect to the cats index
      return redirect('index')
    # if the user inputs are invalid
    else:
      # generate error message to present to the screen
      error_message = 'invalid credentials'
  # send a new form to the template
  form = UserCreationForm()
  return render(request, 'registration/signup.html', {
    'form': form,
    'error': error_message
  })


class BeyonceCreate(LoginRequiredMixin, CreateView):
  model = Beyonce  
  fields = ('city', 'state', 'age', 'tour')
  success_url = '/beyonces/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class BeyonceUpdate(LoginRequiredMixin, UpdateView):
  model = Beyonce
  fields = ('state', 'description', 'age')

class BeyonceDelete(LoginRequiredMixin, DeleteView):
  model = Beyonce
  success_url = '/beyonces/'

class TourIndex(LoginRequiredMixin, ListView):
  model = Tour

class ToursDetail(LoginRequiredMixin, DetailView):
  model = Tour

class TourCreate(LoginRequiredMixin, CreateView):
  model = Tour
  fields = '__all__'

class TourUpdate(LoginRequiredMixin, UpdateView):
  model = Tour
  fields = '__all__'

class TourDelete(LoginRequiredMixin, DeleteView):
  model = Tour
  success_url = '/tours/'