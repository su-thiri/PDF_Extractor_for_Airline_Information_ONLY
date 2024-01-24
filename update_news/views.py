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
            return redirect('generate_pdf')  # This should match the name in your urls.py
        return render(request, 'entry_pannel.html', {'form': form})
    
class PDFView(View):
    def get(self, request,pk):
        user_data = UserData.objects.get(id = pk)
        template_path = 'output_file.html'  # Replace with the actual template path
        date_list =user_data.travel_date.split(',')
        depaturetime_list = user_data.departure_time.split(',')
        arrival_time_list = user_data.arrival_time.split(',')
        class_list = user_data.ar_class.split(',')
        flight_list = user_data.flight.split(',')
        destination_list = user_data.flight.split(',')

        context = {'date': user_data.travel_date,'destination':user_data.desination,'depaturetime':user_data.departure_time,
                   'arrivaltime':user_data.arrival_time,'flight':user_data.flight,
                   'class':user_data.ar_class,'baggage_allowance':user_data.baggage_allowance,'date_list':date_list,
                   'depaturetime_list':depaturetime_list,'arrival_time_list':arrival_time_list,'class_list':class_list,
                   'flight_list':flight_list,'destination_list': destination_list
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
    

class PDFView2(View):
    def get(self, request,pk):
        user_data = UserData.objects.get(id = pk)
        template_path = 'output_file2.html'  # Replace with the actual template path
        date_list =user_data.travel_date.split(',')
        depaturetime_list = user_data.departure_time.split(',')
        arrival_time_list = user_data.arrival_time.split(',')
        class_list = user_data.ar_class.split(',')
        flight_list = user_data.flight.split(',')
        destination_list = user_data.flight.split(',')

        len_date = len(date_list)
        len_departure = len(depaturetime_list)
        len_arrival = len(arrival_time_list)
        len_flight = len(flight_list)

        context = {'date_list':date_list,
                   'depaturetime_list':depaturetime_list,'arrival_time_list':arrival_time_list,'class_list':class_list,
                   'flight_list':flight_list,'destination_list': destination_list, 'len_date':len_date,'len_dep':len_departure,
                   'len_arrival':len_arrival,'len_flight':len_flight
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

