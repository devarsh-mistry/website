from django.shortcuts import render

# Create your views here.
# def qr_code(r):
#     return render(r,'')




# from django.shortcuts 
# import render
import qrcode
import qrcode.image.svg
from io import BytesIO
def index(request): 
    context = {}
    if request.method == "POST": 
        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(request.POST.get("qr_text",""),image_factory=factory, box_size=20) 
        stream = BytesIO() 
        img.save(stream) 
        context["svg"] = stream.getvalue().decode()     
    return render(request, "qr_code_demo/index.html", context=context)

def forms(r):
    return render(r,"qr_code_demo/form.html")