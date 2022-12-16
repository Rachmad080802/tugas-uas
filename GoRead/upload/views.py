from django.shortcuts import render
from upload.models import Upload
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):

    posting = Upload.objects.all()

    return render(request, 'upload/index.html', {'posting':posting} )
class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

