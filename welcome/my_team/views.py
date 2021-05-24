from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'input.html')

def welcome(request):
    team = request.GET['team']
    team_member = request.GET['member']
    memberlist = team_member.split(', ')
    member = []
    for mem in memberlist:
        if mem not in member:
            member.append(mem) 
    return render(request, 'welcome.html', {'team':team,'count':len(member),'fullmember':team_member,'member':member})