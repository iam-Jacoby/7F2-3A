from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def instructor_dashboard(request):
    template = loader.get_template('dashboard.html')

    request.session["userid"] = 100

    userid = request.session.get("userid")
    print(userid)


    context = {
        'userid' : userid,
    }

    return HttpResponse(template.render(context, request))