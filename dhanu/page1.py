from django.http import HttpResponse
from django.shortcuts import render
import operator

def ram(request):


    return render(request,'wel.html')


def about(request):


    return render(request,'about1.html')



def ram1(request):

    mess=request.GET['message']

    w1=mess.split()

    wlcount={}
    for word in w1:
        if word in wlcount:
            wlcount[word] +=1
        else:
            wlcount[word]=1
    sort1=sorted(wlcount.items(),key=operator.itemgetter(1),reverse=True)           

    return render(request,'wel1.html',{'msg':mess,'length':len(w1),'abc':wlcount, 'cba':sort1})     