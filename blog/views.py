from django.http.response import HttpResponse

from django.template import Context, loader

from .models import Tag

def greeting(request):
    return HttpResponse('Greetings from Blog!')

def homepage(request):
    tag_list = Tag.objects.all()
    template = loader.get_template('blog/tag_list.html')
    context = Context({'tag_list': tag_list})
    output = template.render(context)
    return HttpResponse(output)

def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    template = loader.get_template('blog/tag_detail.html')
    context = Context({'tag': tag})
    return HttpResponse(template.render(context))