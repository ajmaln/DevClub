from home.forms import ContactForm


def contact_processor(request):
    return {'form': ContactForm(None)}
