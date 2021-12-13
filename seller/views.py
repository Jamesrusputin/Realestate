from django.shortcuts import render
from django.http import JsonResponse
from django.core import exceptions
from .models import Seller
from django.contrib.auth.models import User
from django.contrib import auth
from property.helper import get_session
from realestate import decode_jwt

# Create your views here.
def get_contact_info(request):
    if request.method == 'GET':
        token = get_session(request)
        if token is not None:
            user_data = decode_jwt.lambda_handler(token, None)
            seller_name = request.GET.get('seller_name').strip()
            try:
                seller_obj = Seller.objects.get(name=seller_name)
                json_response = dict(status=True, seller_name=seller_obj.name, seller_email=seller_obj.email_id, seller_contact=seller_obj.contact_no)
                return JsonResponse(json_response)
            except exceptions.ObjectDoesNotExist:
                return JsonResponse({'status': False, 'message': 'No seller found'})
        else:
            return JsonResponse({'status': False, 'message': 'Login'})
    else:
        return JsonResponse({'status': False, 'message': 'Request Method Invalid'})