from . models import Category

def get_links(request):
    links = Category.objects.all()
    print(links)
    return dict(links=links)