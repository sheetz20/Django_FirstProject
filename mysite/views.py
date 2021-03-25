from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def capital(request):
    djtext = request.POST.get('text','default')
    capText = request.POST.get('captext','off')
    punctext = request.POST.get('punc','off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if capText == 'on':
        djtext = djtext.upper()
        params = {'msg': 'Upper Text:','value': djtext}
    if punctext == 'on':
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'msg': 'Punctuation Removed:', 'value': analyzed}
        djtext = analyzed
    if newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
        params = {'msg': 'New Line Removed:', 'value': analyzed}
        djtext = analyzed
        # return render(request, 'capital.html', params)
    if extraspaceremover == "on" :
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'msg': 'New Line Removed:', 'value': analyzed}
        djtext = analyzed
        # return render(request, 'capital.html', params)
    if charcount == 'on':
        total = 0
        for word in djtext.split():
            total = total + len(word)
        params = {'msg': 'Total Character Count:', 'value': total}
        # return render(request, 'capital.html', params)
    if(capText != 'on' and punctext != 'on' and newlineremover != 'on' and extraspaceremover != 'on' and charcount != 'on'):
        return HttpResponse('<h1>Error</h1>')
    return render(request, 'capital.html', params)
    # else:
    #     return HttpResponse("<h1>Error</h1>")

def navigation(request):
    return render(request,'nav.html')

def demo(request):
    return HttpResponse("ooops! press Back")
