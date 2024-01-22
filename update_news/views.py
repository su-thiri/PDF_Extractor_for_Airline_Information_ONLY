# pdf_generator/views.py

from django.http import HttpResponse
from django.shortcuts import render, redirect

from update_news.models import UserImage
from .forms import UserImageForm
from .utils import generate_pdf,generate_agent
from django.templatetags.static import static

def upload_image(request):
    if request.method == 'POST':
        form = UserImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('generated', pk=form.instance.pk)
    else:
        form = UserImageForm()

    return render(request, 'upload_image.html', {'form': form})

def upload_list(request):
    images = UserImage.objects.all()
    return render(request,'upload_file_list.html',{"images":images})

def generated(request, pk):
    user_image = UserImage.objects.get(id=pk)
    default_logo_url = request.build_absolute_uri(static("image/banner.jpg"))
    pdf_file = generate_pdf(user_image.image.path, default_logo_url)
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="generated.pdf"'
    return response

def agent_generate(request,pk):
    user_image = UserImage.objects.get(id=pk)
    default_logo_url = request.build_absolute_uri(static("image/banner.jpg"))
    pdf_file = generate_agent(user_image.image.path, default_logo_url)
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="generated.pdf"'
    return response