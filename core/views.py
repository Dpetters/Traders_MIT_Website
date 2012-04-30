from core.decorators import render_to
from core.models import ExecMember

@render_to("about_us.html")
def about_us(request, extra_context=None):
    context = {'current_exec_members':ExecMember.objects.current()}
    return context


@render_to("home.html")
def home(request, extra_context=None):
    context = {}
    return context