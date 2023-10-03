from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import Download
from .forms import DownloadForm

@login_required
def index(request):
    if request.method == 'POST':
        form = DownloadForm(request.POST)
        if form.is_valid():
            dl_data = form.save(commit=False)
            dl_data.user = request.user
            dl_data.save()
            return redirect(index)
    
    download_list = Download.objects.all()
    form = DownloadForm()
    context = {"download_list":download_list,"form":form}
    return render(request,"index.html",context)

def delete(request, item_id):
    download_item = Download.objects.get(pk=item_id)
    download_item.delete()
    return redirect(index)
