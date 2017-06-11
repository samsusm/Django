from django.shortcuts import render
# from django.http import HttpResponse
from .forms import SignUpForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index_page(request):
    # if request.user.is_authenticated():
    #     body_msg = "Welcome %s!" % (request.user)
    # else:
    #     body_msg = "Welcome Guest, Please Register"

    Form = SignUpForm(request.POST or None)
    if Form.is_valid():
        instance = Form.save(commit=False)
        context = {
                    "body_text":"ThankYou for Registering!"
        }

        # mail(instance)
        # After confirming the Link only, we should save the data in DB by executing below line, but as of now, it is temp enabled
        instance.save()
    else:
        context = {
                "body_text": "Please Register",
                "form":Form
        }

    return render(request,"form.html",context)
    # return HttpResponse("Yo Samsu!")


def mail(request_data):
        # Dummy Link
        activation_link = "https://www.google.com"
        title = "Confirmation Mail from XYZ.com"
        message = """
                    Hi %s,
                    Thanks for registering XYZ.com, please click the below link to activate your account
                    %s
        """         %(request_data.full_name, activation_link)
        send_mail(
            title,
            message,
            settings.EMAIL_HOST_USER,
            [request_data.email],
            fail_silently=False,
        )
