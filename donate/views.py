from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from .forms import PaymentForm


@login_required(login_url='login')
def payment(request):
    """
    This method will create a payment request and upon successfull payment,
    it will send an confirmation email to the user.
    This method will only load this page if the user is logged in.

        :param name: request - used to generate responses(Http) depending on the request that it receives.
        :param type: HttpResponse
        :return: returns payment page
        """
    template = render_to_string(
        'online_payment/email_template.html', {'name': request.user.first_name})

    email_message = EmailMessage(
        'Payment Complete',
        template,
        settings.EMAIL_HOST_USER,
        [request.user.email],
    )

    email_message.fail_silently = False
    # email_message.send()

    form = PaymentForm()

    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(
                request, 'A payment confirmation mail has been sent to your email ' + email)
            email_message.send()

    context = {'form': form}
    return render(request, 'online_payment/payment.html', context)
