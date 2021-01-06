from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.



tag_list = ['hn','div','p','a','ul','ol','input','exam']             #Database


# Create your views here.
def sampleIndex(request):
    context = {
        'tags': tag_list
    }
    return render(request, 'sample/index.html', context)

def sampleTemp(request, pattern):
    return render(request, 'sample/temp.html')

def sampleYear(request, year):
    context = {
        'data': year
    }
    return render(request, 'sample/year.html', context)

def sampleMonth(request, month):
    context = {
        'data': month
    }
    return render(request, 'sample/month.html', context)

def sampleDay(request, day):
    context = {
        'data': day
    }
    return render(request, 'sample/day.html', context)

def sampleWords(request, word):
    context = {
        'data': word
    }
    return render(request, 'sample/words.html', context)


def sampleHtml(request, tag):
    context = {
        'title': tag
    }

    if tag in tag_list:
        template = 'sample/{}.html'.format(tag)
    else:
        template = 'sample/Not_Exist_Page.html'

    return render(request, template, context)


def sampleInput(request):                                   #인자 안에 있는 모든 값을 서버로 전송 
    print(request.POST.get('text'))
    print(request.POST.get('pass'))
    print(request.POST.get('date'))
    return HttpResponse('응답 완료')



def sampleExam(request):
    print(request.POST.get('tv'))
    print(request.POST.get('internet'))
    print(request.POST.get('sancheck'))
    print(request.POST.get('game'))
    print(request.POST.get('music'))
    print(request.POST.get('health'))
    print(request.POST.get('calling'))
    print(request.POST.get('nap'))
    print(request.POST.get('moutaining'))
    print(request.POST.get('sports'))
    
    return HttpResponse('complete!')