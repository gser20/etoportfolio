from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')
def second_page(request):
    return render(request, 'second_page.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Here you can send an email or save the data
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # For example, send an email (requires email settings)
            # send_mail('Contact Form Submission', message, email, ['your_email@example.com'])
            return render(request, 'portfolio/contact_success.html')
    else:
        form = ContactForm()

    return render(request, 'portfolio/contact.html', {'form': form})