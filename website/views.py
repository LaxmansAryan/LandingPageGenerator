from django.shortcuts import render, redirect
from .models import *
from .functions import *
from django.contrib import messages
from django.conf import settings
from .aigenerator import *
import time

# Create your views here.
def home(request):
    context = {}

    if request.method == 'POST':
        businessName = request.POST['businessName']
        businessDo = request.POST['businessDo']
        
        context['section1Title'] = returnsection1Title(businessDo)
        context['section1Description'] = getDescription(businessName, businessDo, 265)

        # Get The Service Titles
        services = []
        serviceTitles = return3Services(businessDo)
        for service in serviceTitles:
            obj = {}
            serviceDescription = returnServiceDescription(service)
            obj['title'] = service
            obj['description'] = serviceDescription
            services.append(obj)
            time.sleep(1)


        # Get The Feature Titles
        features = []
        featureTitles = return3Features(businessDo)
        for feature in featureTitles:
            obj = {}
            featureDescription = returnFeatureDescription(feature)
            obj['title'] = feature
            obj['description'] = featureDescription
            features.append(obj)
            time.sleep(1)


        context['service1Title'] = services[0]['title']
        context['service1Description'] = services[0]['description']
        context['service2Title'] = services[1]['title']
        context['service2Description'] = services[1]['description']
        context['service3Title'] = services[2]['title']
        context['service3Description'] = services[2]['description']
        
        context['section3Title'] = returnsection1Title(businessDo)
        context['section3Description'] = getDescription(businessName, businessDo, 265)

        context['features1Title'] = features[0]['title']
        context['features1Description'] = features[0]['description']
        context['features2Title'] = features[1]['title']
        context['features2Description'] = features[1]['description']
        context['features3Title'] = features[2]['title']
        context['features3Description'] = features[2]['description']

        return render(request, 'website/ai-seo1.html', context)
        # return render(request, 'website/ai-website.html', context)
        # return render(request, 'website/website.html', context)

    return render(request, 'website/index.html', context)

def website(request):
    context = {}
    return render(request, 'website/website.html', context)

def website1(request):
    context = {}
    return render(request, 'website/website1.html', context)