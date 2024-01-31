from django.urls import path
from .views import upload_image, generated,upload_list,agent_generate,GeneratePDF,PDFView,clear,Add_Data

urlpatterns = [
    path('', upload_image, name='upload_image'),
    path('generated/<int:pk>/', generated, name='generated'),
    path('upload_list/',upload_list,name="upload_list"),
    path('agent_generate/<int:pk>/',agent_generate,name="agent_generate"),
    path('generate-pdf/', GeneratePDF.as_view(), name='generate_pdf'),
    path('pdf_view/<int:pk>',PDFView.as_view(),name='pdf_view'),
    path('clean/',clear,name='clear'),
    path('sec_gene/',Add_Data.as_view(),name="sec_gene")
]
