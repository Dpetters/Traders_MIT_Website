from django.forms.formsets import formset_factory
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from core.decorators import render_to
from core.models import ExecMember, ApplicantPoll, Applicant
from core.forms import ApplicantForm
from event.models import Event


@render_to("about.html")
def about(request, extra_context=None):
    context = {}
    context['current_exec_members'] = ExecMember.objects.filter(left__isnull=True).order_by("-co_president", "joined")
    context['past_exec_members'] = ExecMember.objects.filter(left__isnull=False).order_by("left")
    return context

@render_to("home.html")
def home(request, extra_context=None):
    context = {'applicant_poll':ApplicantPoll.objects.filter(active=True).exists()}
    return context

@render_to("photos.html")
def photos(request, extra_context=None):
    context = {'events_with_photos':Event.objects.filter(slideshow__isnull=False).exclude(slideshow=u'').order_by("-end_datetime")}
    return context

@login_required
@render_to("applicant_poll.html")
def applicant_poll(request, extra_context=None):
    context = {}
    ApplicantFormSet = formset_factory(ApplicantForm)
    applicantPoll = list(ApplicantPoll.objects.all())[-1]

    done = False
    currentExecMember = ExecMember.objects.get(user=request.user)
    if currentExecMember in applicantPoll.completed_by.all():
        done = True
    context["done"] = done
   
    execMembersLeft = []
    completed = True
    for execMember in ExecMember.objects.filter(left__isnull=True):
        if not execMember in applicantPoll.completed_by.all():
            completed = False
            execMembersLeft.append(execMember.user.username)
    context["completed"] = completed
    context["execMembersLeft"] = "Still waiting on %s" % " ".join(execMembersLeft)
    applicants = Applicant.objects.filter(applicantPoll = applicantPoll)

    if not completed:
        applicants = Applicant.objects.filter(applicantPoll = applicantPoll)
        if request.method == 'POST':
            formset = ApplicantFormSet(request.POST, request.FILES)
            if formset.is_valid():
                for form in formset:
                    id = form.cleaned_data.get("id")
                    if id:
                        applicant = Applicant.objects.get(id=id)
                        if not applicant.positives:
                            applicant.positives = ""
		        positive1 = form.cleaned_data.get("positive1")
		        if positive1: 
	                    applicant.positives += "; %s" % positive1
                        positive2 = form.cleaned_data.get("positive2")
                        if positive2: 
                            applicant.positives += "; %s" % positive2
                        positive3 = form.cleaned_data.get("positive3")
                        if positive3:
                            applicant.positives += "; %s" % positive3
                        if not applicant.negatives:
                            applicant.negatives = ""
                        negative1 = form.cleaned_data.get("negative1")
                        if negative1: 
                            applicant.negatives += "; %s" % negative1
                        negative2 = form.cleaned_data.get("negative2")
                        if negative2: 
                            applicant.negatives += "; %s" % negative2
                        negative3 = form.cleaned_data.get("negative3")
                        if negative3: 
                            applicant.negatives += "; %s" % negative3
                        applicant.score += int(form.cleaned_data.get("rating"))
                        applicant.save()
                print currentExecMember
                applicantPoll.completed_by.add(currentExecMember)
                applicantPoll.save()
                return HttpResponseRedirect(reverse("applicant_poll"))
        else:
            formset = ApplicantFormSet(initial = applicants.values())
        context['management_form'] = formset.management_form
        context['formset'] = zip(formset.forms, applicants)
    else:
        context['applicants'] = applicants.order_by("-score") 
    return context
