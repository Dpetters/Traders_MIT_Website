from core.decorators import render_to

from event.models import Event


@render_to("events_upcoming.html")
def events_upcoming(request, extra_context=None):
    context = {'upcoming_events' : filter(lambda x: not x.is_past(), Event.objects.all())}
    return context

@render_to("events_past.html")
def events_past(request, extra_context=None):
    context = {'past_events' : filter(lambda x: x.is_past(), Event.objects.all())}
    return context
