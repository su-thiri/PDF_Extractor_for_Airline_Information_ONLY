# pdf_generator/utils.py

from PIL import Image
from reportlab.pdfgen import canvas
from io import BytesIO
import requests
from reportlab.lib.utils import ImageReader

def generate_pdf(image_path,default_logo_url):
    # Crop user-uploaded image using PIL
    img = Image.open(image_path)
    cropped_img = img.crop((0, 580, 2510, 1700))  # Adjust coordinates as needed

    # Create PDF using ReportLab
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)
    pdf.setFont("Helvetica", 16)
    pdf.drawString(9,720, "Passenger Information")

    default_logo_response = requests.get(default_logo_url)
    default_logo_response2 = requests.get(default_logo_url)
    default_logo_response3 = requests.get(default_logo_url)

    default_logo_img = Image.open(BytesIO(default_logo_response.content))
    default_logo_img2 = Image.open(BytesIO(default_logo_response2.content))
    default_logo_img3 = Image.open(BytesIO(default_logo_response3.content))




    default_logo_cropped = default_logo_img.crop((0,0,7500,780))
    default_logo_cropped2 = default_logo_img2.crop((0,2300,7500,3450))
    default_logo_cropped3 = default_logo_img3.crop((0,1500,7500,2200))

    default_logo_buffer = BytesIO()
    default_logo_buffer2 = BytesIO()
    default_logo_buffer3 = BytesIO()
    default_logo_cropped.save(default_logo_buffer, format="PNG")
    default_logo_cropped2.save(default_logo_buffer2, format="PNG")
    default_logo_cropped3.save(default_logo_buffer3, format="PNG")

    default_logo_buffer.seek(0)
    default_logo_buffer2.seek(0)
    default_logo_buffer3.seek(0)

    # Use ImageReader to open the image from the buffer
    default_logo_reader = ImageReader(default_logo_buffer)
    default_logo_reader2 = ImageReader(default_logo_buffer2)
    default_logo_reader3 = ImageReader(default_logo_buffer3)

    # Add user-uploaded and default images to the PDF
    pdf.drawInlineImage(cropped_img, 5,350, width=600, height=300)
    pdf.drawImage(default_logo_reader, 0,760,width=700,height=90)
    pdf.drawImage(default_logo_reader2,0,0,width=700, height=90)
    pdf.drawImage(default_logo_reader3,6,100,width=700,height=80)


    pdf.showPage()
    pdf.save()

    buffer.seek(0)
    return buffer

def generate_agent(image_path,default_logo_url):
    # Crop user-uploaded image using PIL
    img = Image.open(image_path)
    cropped_img = img.crop((0, 580, 2510, 1700))  # Adjust coordinates as needed

    # Create PDF using ReportLab
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer)
    pdf.setFont("Helvetica", 16)
    pdf.drawString(9,720, "Passenger Information")

    default_logo_response = requests.get(default_logo_url)
    default_logo_response2 = requests.get(default_logo_url)
    


    default_logo_img = Image.open(BytesIO(default_logo_response.content))
    default_logo_img2 = Image.open(BytesIO(default_logo_response2.content))
    




    default_logo_cropped = default_logo_img.crop((0,0,100,780))
    default_logo_cropped2 = default_logo_img2.crop((0,2300,100,3450))
   

    default_logo_buffer = BytesIO()
    default_logo_buffer2 = BytesIO()
    default_logo_buffer3 = BytesIO()
    default_logo_cropped.save(default_logo_buffer, format="PNG")
    default_logo_cropped2.save(default_logo_buffer2, format="PNG")
    

    default_logo_buffer.seek(0)
    default_logo_buffer2.seek(0)
 

    # Use ImageReader to open the image from the buffer
    default_logo_reader = ImageReader(default_logo_buffer)
    default_logo_reader2 = ImageReader(default_logo_buffer2)
   

    # Add user-uploaded and default images to the PDF
    pdf.drawInlineImage(cropped_img, 5,350, width=600, height=300)
    pdf.drawImage(default_logo_reader, 0,760,width=700,height=90)
    pdf.drawImage(default_logo_reader2,0,0,width=700, height=90)
  


    pdf.showPage()
    pdf.save()

    buffer.seek(0)
    return buffer
