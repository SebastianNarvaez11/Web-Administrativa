from .models import Link


def ctx_dict(request):
    ctx = {}
    links = Link.objects.all()
    for link in links:
        if link.estado:
            ctx[link.key] = link.url
    return ctx
