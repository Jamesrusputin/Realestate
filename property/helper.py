from .models import Property
from datetime import datetime, timezone
from django.shortcuts import get_object_or_404
import base64
import requests
from realestate import decode_jwt
from decouple import config

def get_properties(top=False):
    """
    This Robust fucnction is used to get the properties for home page and properties page.
    """
    property_list = Property.objects.order_by('-id')
    if len(property_list) >= 3 and top == True:
        property_list = property_list[:3]
    context_result = []
    for property in property_list:
        id = property.id
        price = property.price
        address = property.address
        city = property.city
        state = property.state
        zipcode = property.zipcode
        photo_main = property.photo_main
        sqft = property.sqft
        bedrooms = property.bedrooms
        bathrooms = int(property.bathrooms)
        garage = property.garage
        name = property.name
        diff_date = datetime.now(timezone.utc) - property.property_date
        days = diff_date.days
        if days == 0:
            days_text = "Few Hours ago"
        else:
            days_text = f"{days} days ago"
        property_result = dict(id=id,price=price, address=address, city=city, state=state, zipcode=zipcode, photo_main=photo_main, sqft=sqft, bedrooms=bedrooms, bathrooms=bathrooms, garage=garage, name=name, days=days_text)
        context_result.append(property_result)
    return context_result

def get_property_details(id):
    """
    This function is used to get the property details.
    """
    property_details = get_object_or_404(Property, pk=id)
    return property_details

def get_token(code):
    """
    This function is used to get the user details after contacting AWS Cognito.
    """
    token_endpoint = config('token_endpoint')
    redirect_url = config('redirect_url')
    client_id = config('client_id')
    client_secret = config('client_secret')

    encode_data = base64.b64encode(bytes(f'{client_id}:{client_secret}', "ISO-8859-1")).decode("ascii")

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': f'Basic {encode_data}'
    }

    body = {
        'grant_type': 'authorization_code',
        'client_id': client_id,
        'code': code,
        'redirect_uri': redirect_url
    }

    response = requests.post(token_endpoint, headers=headers, data=body)

    id_token = response.json()['id_token']
    user_data = decode_jwt.lambda_handler(id_token, None)
    if not user_data:
        return False
    
    user = {
        'id_token' : id_token,
        'name': user_data['name'],
        'email': user_data['email']
    }

    return user

def get_session(request):
    """
    This function is used to get the session token.
    """
    try:
        response = request.COOKIES['sessiontoken']
        return response
    except Exception:
        return None