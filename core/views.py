# core/views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Home Page View
@login_required
def home(request):
    """
    यह व्यू आपके डिज़ाइन किए गए होम पेज को दिखाता है
    """
    return render(request, 'core/home.html')