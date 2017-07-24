from register.models import jfuser,jfcompany,jfadmin,usercompany
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect, HttpResponse

# Create your views here.
