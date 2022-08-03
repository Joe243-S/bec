from django.shortcuts import render

# Create your views here.
def home_page(request):
    """Home page's view"""
    my_title = "bassie expert cleaning"
    template_name = "main.html"
    context = {
        'title': my_title,
    }
    return render(request, template_name, context)

def gallery_page(request):
    """Gallery page's view"""
    my_title = "Gallery"
    template_name = "gallery.html"
    context = {
        'title': my_title,
    }
    return render(request, template_name, context)