# I HAVE CREATED THIS FILE - NILESH RUDRA
from django.http import HttpResponse
from django.shortcuts import render

# lecture - 6

# def index(request):
#     return HttpResponse('''<h1>MAANG Companies</h1> <a href="https://www.apple.com/in/">www.apple.com</a><br>
#     <a href="https://www.facebook.com/">www.facebook.com</a><br>
#     <a href="https://www.netflix.com/in/">www.netflix.com</a><br>
#     <a href="https://www.amazon.in/">www.amazon.com</a><br>
#     <a href="https://www.google.co.in/">www.google.com</a>''')
#
#
# def about(request):
#     return HttpResponse("My first django website!!")

# lecture - 7 making pipeline
def index(request):
    # b = {'name':"Nilesh Rudra",'place':"West Bengal"}
    return render(request,'index.html')


def analyzed(request):
    txtt = request.POST.get('text', 'default')
    djText = txtt
    removepunc = request.POST.get('removepunc', 'default')
    capitalizeFirst = request.POST.get('capitalizeFirst', 'default')
    eraseNewLine = request.POST.get('eraseNewLine', 'default')
    countChar = request.POST.get('countChar', 'default')
    extraspaceremover = request.POST.get('extraspaceremover', 'default')
    res_text = ""
    puncuation = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''

    def removePunc(a):
        rem_em = ""
        for i in a:
            if i not in puncuation:
                rem_em += i
        return rem_em

    if removepunc == 'on':
        djText = removePunc(djText)

    def capitalizefirst(b):
        cap_em = ""
        for char in b:
                cap_em += char.upper()
        return cap_em

    if capitalizeFirst == 'on':
        djText = capitalizefirst(djText)

    def erasnewline(c):
        er_em = ""
        for ii in c:
            if (ii != '\n') and (ii != '\r'):
                er_em += ii
        print(er_em)
        return er_em

    if eraseNewLine == 'on':
        djText = erasnewline(djText)

    def extraspacereRemover(d):
        exspace_em = ""
        for idx, char in enumerate(d):
            if d[idx] == " " and d[idx+1] == " ":
                pass
            else:
                exspace_em += char
        return exspace_em

    if extraspaceremover == 'on':
        djText = extraspacereRemover(djText)
    if(len(djText)):
        c = {'sentence': djText}
    else:
        c = {'sentence': "Error"}
    if(countChar=='on'):
        h = {'sentence':djText,'charac':len(djText),'NoofCharacter':"No of Character. after analyzation:"}
        return render(request, 'analyzed.html',h)

    return render(request, 'analyzed.html', c)

