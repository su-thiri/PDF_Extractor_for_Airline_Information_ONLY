from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.views import View
from update_news.models import UserImage,UserData
from .forms import UserImageForm,UserDataForm
from .utils import generate_pdf,generate_agent
from django.templatetags.static import static
from xhtml2pdf import pisa
from update_pdf import settings


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
        data = UserData.objects.all()
        return render(request, 'entry_pannel2.html', {'data': data})
    
    def post(self,request):
        form = UserData()

        form.departure_time = request.POST.get()
        form.arrival_time = request.POST.get()
        form.ar_class = request.POST.get()
        form.flight = request.POST.get()
        form.baggage_allowance = request.POST.get()
        form.save()

        return redirect('generate_pdf')

def clear(request):
    UserData.objects.all().delete()
    return redirect('generate_pdf')

class PDFView(View):
    def get(self, request):
        user_data = UserData.objects.all()
        separate_data = UserData.objects.first()
        template_path = 'output_file.html'
        name = separate_data.passenger_name
        pass_num = separate_data.passport_number
        booking_code = separate_data.booking_code
        eticket = separate_data.eticket
        price = separate_data.price
        image_file = request.build_absolute_uri(static("images/baner.png"))
        image_file2 = request.build_absolute_uri(static("images/banner2.png"))


        context = {

            'flight_data_lists': user_data,
            'name':name,
            'pass_num':pass_num,
            'booking_code':booking_code,
            'eticket':eticket,
            'price':price,
            'image_file':image_file,
            'image_file2':image_file2

 
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
    def get(self, request):
        user_data = UserData.objects.all()
        separate_data = UserData.objects.first()
        template_path = 'output_file2.html'
        name = separate_data.passenger_name
        pass_num = separate_data.passport_number
        booking_code = separate_data.booking_code
        eticket = separate_data.eticket
        price = separate_data.price
        

        context = {

            'flight_data_lists': user_data,
            'name':name,
            'pass_num':pass_num,
            'booking_code':booking_code,
            'eticket':eticket,
            'price':price
 
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