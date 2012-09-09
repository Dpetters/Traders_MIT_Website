from core.decorators import render_to
from core.models import ExecMember

@render_to("about.html")
def about(request, extra_context=None):
    context = {}
    context['current_exec_members'] = ExecMember.objects.filter(left__isnull=True).order_by("-co_president", "boardmember_ptr__user__first_name")
    context['past_exec_members'] = ExecMember.objects.filter(left__isnull=False).order_by("left")
    return context


@render_to("home.html")
def home(request, extra_context=None):
    context = {}
    return context
