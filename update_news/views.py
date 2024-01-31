# pdf_generator/views.py

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.views import View
from update_news.models import UserImage,UserData
from .forms import UserImageForm,UserDataForm
from .utils import generate_pdf,generate_agent
from django.templatetags.static import static
from xhtml2pdf import pisa

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

class GeneratePDF(View):
    def get(self, request):
        form = UserDataForm()
        return render(request, 'entry_pannel.html', {'form': form})

    def post(self, request):
        form = UserDataForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('generate_pdf')
         # This should match the name in your urls.py
        return render(request, 'entry_pannel.html', {'form': form})

class Add_Data(View):

    def get(self,request):
        data = UserData.objects.raw("select * from update_news_userdata")
        return render(request, 'entry_pannel2.html', {'data': data})
    
    def post(self,request):
        data = UserData.objects.all()
        data.travel_date = request.POST.get("date")
        data.desination = request.POST.get("destination")
        data.departure_time = request.POST.get("departuretime")
        data.arrival_time = request.POST.get("arrivaltime")
        data.flight = request.POST.get("flightname")
        data.ar_class = request.POST.get("class")
        data.baggage_allowance = request.POST.get("baggage_allowance")

        if data:
            data.save()
            return redirect('generate_pdf')
        
        return render(request, 'entry_pannel2.html', {'data': data})

def clear(request):
    UserData.objects.all().delete()
    return redirect('generate_pdf')

class PDFView(View):
    def get(self, request,pk):
        user_data = UserData.objects.get(id = pk)
        template_path = 'output_file.html'
        flight_data = UserData.objects.get_queryset()
        count = 0
        for i in flight_data:
            count += 1

        flight_data1 = []
        flight_data2 = []
        flight_data3 = []
        flight_data4 = []

        if count == 1:
            flight_data = flight_data
        elif count == 2:
            flight_data1.append(flight_data[0])
            flight_data2.append(flight_data[1])
        elif count == 3:
            flight_data1.append(flight_data[0])
            flight_data2.append(flight_data[1])
            flight_data3.append(flight_data[2])
        elif count == 4:
            flight_data1.append(flight_data[0])
            flight_data2.append(flight_data[1])
            flight_data3.append(flight_data[2])
            flight_data4.append(flight_data[3])

        context = {'name':user_data.passenger_name,'pp_num':user_data.passport_num,
                   'flight_data':flight_data,'count':count,
                   'flight_data1':flight_data1,'flight_data2':flight_data2,
                   'flight_data3':flight_data3,'flight_data4':flight_data4
                   }

        # Render the HTML template to a string
        template = get_template(template_path)
        html = template.render(context)

        # Create a PDF file
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="generated_file.pdf"'

        # Generate PDF using xhtml2pdf
        pisa_status = pisa.CreatePDF(html, dest=response)

        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response