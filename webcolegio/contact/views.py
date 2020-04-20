from django.shortcuts import render,redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
# Create your views here.

def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)#Optiene los datos del formulario
        if contact_form.is_valid():
            nombre = request.POST.get('nombre','')
            email = request.POST.get('email','')
            contenido = request.POST.get('contenido','')
            # ENVIAMOS EL CORREO
            email = EmailMessage(
                "Sitio Web - Academico El Poblado", #Asunto del mensaje
                "Remitente: {} \nEmail: <{}> \n\nEscribio: \n\n{} ".format(nombre, email, contenido),#estructura del mensaje
                "testing.developer.404@gmail.com", #email de origen
                ["narvaez.jhoan@correounivalle.edu.co"], #email de destino
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact')+"?ok")
            except:
                return redirect(reverse('contact')+"?fail")

            

    return render(request,'contact/contact.html',{'formulario':contact_form})