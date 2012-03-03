from core.decorators import render_to

@render_to("home.html")
def home(request, extra_context=None):
    context = {}
    return context
