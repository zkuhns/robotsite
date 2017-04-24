from django.http import Http404
from django.shortcuts import render

from .models import Member


def index(request):
    members = Member.objects.filter(member_accessibility=True).order_by('last_name')
    context = {'members': members}
    return render(request, 'members/index.html', context)


def detail(request, member_id):
    try:
        member = Member.objects.get(pk=member_id)
        if not member.member_accessibility:
            raise Http404("Member does not exist")
    except Member.DoesNotExist:
        raise Http404("Member does not exist")
    if member.contact_accessibility:
        return render(request, 'members/detail.html', {'member': member,
                                                       'public': 1})
    else:
        return render(request, 'members/detail.html', {'member': member})
