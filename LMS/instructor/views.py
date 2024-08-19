from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from homeapp.models import User

def instructor_dashboard(request):
    template = loader.get_template('dashboard.html')

    request.session["userid"] = 1

    userid = request.session.get("userid")

    user_details = User.objects.get(user_id=userid)

    context = {
        'userid' : userid,
        "user_details" : user_details,
    }

    return HttpResponse(template.render(context, request))