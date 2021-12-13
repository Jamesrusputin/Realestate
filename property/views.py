from django.shortcuts import render, redirect
from .helper import get_properties, get_property_details, get_token, get_session
from django.contrib.auth.models import User
from django.contrib import auth
from realestate import decode_jwt



def home(request):
    """
    This function is used to render the home page.
    """
    try:
        code = request.GET.get('code')
        user_data = get_token(code)
        context = {
            'user_name': user_data['name'],
            'status': 1
        }
        property_list = get_properties(top=True)
        context['property_list'] = property_list
        context['home_bar'] = 'active'
        response = render(request, 'home.html', context)
        response.set_cookie('sessiontoken', user_data['id_token'], max_age=3600)
        return response
    except:
        property_list = get_properties(top=True)
        context = {}
        context['property_list'] = property_list
        context['home_bar'] = 'active'
        token = get_session(request)
        if token is not None:
            user_data = decode_jwt.lambda_handler(token, None)
            context['user_name'] = user_data['name']
            context['status'] = 1
            return render(request, 'home.html', context)
        context['status'] = 0
        return render(request, 'home.html', context)


def properties(request):
    """
    This function is used to render the properties page.
    """
    try:
        code = request.GET.get('code')
        user_data = get_token(code)
        context = {
            'user_name': user_data['name'],
            'status': 1
        }
        property_list = get_properties()
        context['property_list'] = property_list
        context['property_bar'] = 'active'
        response = render(request, 'properties.html', context)
        response.set_cookie('sessiontoken', user_data['id_token'], max_age=3600)
        return response
    except Exception as e:
        property_list = get_properties()
        context = {}
        context['property_list'] = property_list
        context['property_bar'] = 'active'
        token = get_session(request)
        if token is not None:
            user_data = decode_jwt.lambda_handler(token, None)
            context['user_name'] = user_data['name']
            context['status'] = 1
            return render(request, 'properties.html', context)
        context['status'] = 0
        return render(request, 'properties.html', context)


def property_detail(request, prop_id):
    """
    This function is used to render the property details page.
    """
    try:
        code = request.GET.get('code')
        user_data = get_token(code)
        context = {
            'user_name': user_data['name'],
            'status': 1
        }
        property_details = get_property_details(prop_id)
        context['property_details'] = property_details
        response = render(request, 'property_detail.html', context)
        response.set_cookie('sessiontoken', user_data['id_token'], max_age=3600)
        return response
    except:
        property_list = get_property_details(prop_id)
        context = {}
        context['property_details'] = property_list
        token = get_session(request)
        if token is not None:
            user_data = decode_jwt.lambda_handler(token, None)
            context['user_name'] = user_data['name']
            context['status'] = 1
            return render(request, 'property_detail.html', context)
        context['status'] = 0
        return render(request, 'property_detail.html', context)