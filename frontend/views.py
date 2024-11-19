from django.shortcuts import render

def home_view(request):
    return render(request,'frontend/index.html')

def article_details_view(request):
    return render(request,'frontend/article-details.html')

def privacy_policy_view(request):
    return render(request,'frontend/privacy-policy.html')

def terms_conditions_view(request):
    return render(request,'frontend/terms-conditions.html')

