from django.shortcuts import render, get_object_or_404
from .models import Grops, Bahosi
import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
# Create your views here.

def render_pdf_view(request, pk):
    template_path = 'index.html'
    baho=get_object_or_404(Bahosi, id=pk)
    talababoholash=baho.talababaholash_set.all()
    context = {'baho': baho, 'talababoholash':talababoholash}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def Home(request):
    grops=Grops.objects.all()
    print(grops[0])
    return render(request, 'home.html', {'grops':grops})