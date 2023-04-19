
import os
import openai
import time
import io
import uuid
import pyttsx3
import ffmpeg
import requests
import speech_recognition as sr
import random
import string
import boto3
import secrets
import string

import re
import email.utils
import json

from email_validator import validate_email, EmailNotValidError
from botocore.exceptions import ClientError
from django.views.decorators.cache import cache_control
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils import timezone
from django.views.generic import View
from django.utils.decorators import method_decorator

from slickrpc import Proxy
from django_corsheaders.decorators import cors_headers
from gtts import gTTS
from datetime import datetime, timedelta

from authlib.integrations.django_client import OAuth
from .models import User, UserProfile, ChatRoom, ChatMessage

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

from django.contrib.auth.hashers import make_password
from django.core.cache import cache
from django.core.files.base import ContentFile
from django.utils.crypto import get_random_string
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.db.models import Q
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_control

from django.shortcuts import render, redirect
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt


from .models import *
from .forms import *


# Create your views here.
MODEL = "gpt-3.5-turbo-0301"


def talkgpt(request):
    voice_options = get_voice_options()
    completion = openai.ChatCompletion.create(
        model=MODEL,
        max_tokens=3000,
        n=1,
        stop=None,
        temperature=0.6,
        messages=[{"type": "user", "text": "Hello!"}]
    )
    response = (completion.choices[0].message)
    return render(request, "talkgpt.html", {"response": response})


def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[
            {"type": "user", "text": prompt}
        ],
        temperature=0.5,
        max_tokens=3000,
        n=1,
        stop=None,
    )
    return response.choices[0].message.content
    return response


def send_message(request):
    message = request.POST.get("message")
    response = generate_response(message)
    return JsonResponse({"message": response})


def stream_response(prompt):
    def generate():
        time.sleep(0.5)  # add delay to allow user input to be sent first
        yield "data: {}\n\n".format("Hello! How can I assist you today?")

        while True:
            completions = openai.ChatCompletion.create(
                model=MODEL,
                prompt=prompt,
                max_tokens=3000,
                n=1,
                stop=None,
                temperature=0.5,
            )

            message = completions.choices[0].message
            prompt += message

            yield "data: {}\n\n".format(message)

    return HttpResponse(generate(), content_type="text/event-stream")


