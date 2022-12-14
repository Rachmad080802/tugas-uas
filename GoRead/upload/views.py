from django.shortcuts import render
from upload.models import Upload

# Create your views here.
def index(request):

    posting = Upload.objects.all()

    return render(request, 'upload/index.html', {'posting':posting} )
