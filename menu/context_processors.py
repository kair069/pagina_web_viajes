from django.urls import get_resolver

def menu_routes(request):
    """
    Obtiene todas las rutas registradas en Django y las devuelve como un contexto.
    """
    resolver = get_resolver()
    urls = []
    for pattern in resolver.url_patterns:
        if hasattr(pattern, 'name') and pattern.name:
            urls.append({'name': pattern.name, 'url': pattern.pattern.describe()})
    return {'menu_routes': urls}
