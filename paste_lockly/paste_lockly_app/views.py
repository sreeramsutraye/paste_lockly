from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils.crypto import get_random_string
from .models import Snippet
import base64

def create_snippet(request):
    if request.method == 'POST':
        content = request.POST['content']
        secret_key = request.POST['secret_key']
        
        if secret_key:
            secret_key = base64.urlsafe_b64encode(secret_key.encode()).decode()

        snippet = Snippet(content=content, secret_key=secret_key)
        snippet.save()
        
        return HttpResponse(f"Your snippet has been created! View it here: /snippets/{snippet.id}/")

    return render(request, 'create_snippet.html')

def view_snippet(request, snippet_id):
    snippet = get_object_or_404(Snippet, id=snippet_id)
    secret_key = request.GET.get('key', None)
    
    if snippet.secret_key and secret_key:
        secret_key = base64.urlsafe_b64encode(secret_key.encode()).decode()
        if secret_key != snippet.secret_key:
            return HttpResponse("Invalid secret key!")

    return render(request, 'view_snippet.html', {'snippet': snippet})
