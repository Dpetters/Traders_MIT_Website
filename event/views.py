from core.decorators import render_to

from event.models import Event


@render_to("events.html")
def events(request, extra_context=None):
    context = {}
    context['events'] = Event.objects.all()
    return context