from django.urls import reverse_lazy
from django.views import generic
from .forms import ContactForm
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.core.mail import send_mail
# Create your views here.

class Top(generic.FormView):
    form_class = ContactForm
    success_url = reverse_lazy('contact:thanks')
    template_name = 'contact/top.html'

    def form_valid(self,form):
        subject = 'お問い合わせがありました'
        message = render_to_string('contact/mail.txt',form.cleaned_data,self.request)
        from_email = 'toritoritorina@gmail.com'
        reciepient_email = ['toritoritorina@gmail.com']
        send_mail(subject,message,from_email,reciepient_email)
        return redirect('contact:thanks')

class Thanks(generic.TemplateView):
    template_name = 'contact/thanks.html'