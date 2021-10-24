from django.shortcuts import render
# from django.http import HttpResponse
# Create your views here.

# request will be called automatically when Django calls this function in urls.py in 'project folder'
def index(request):
    meetups = [
        {'title': 'First meetup', 'location':'Bucharest', 'slug':'a-first-meetup'},
        {'title': 'Second meetup', 'location' : 'London', 'slug':'a-first-meetup'}

    ]
    # return HttpResponse("<h1> Hello </h1>")
    # second argument = path as seen form templates
    return render(request, 'meetups/index.html', {
        'meetups':meetups, # first arg = names to pass to use in our template file, second arg = value for those names
        'show_meetups': True

    }) # render returns template files


# THERE IS ANOTHER WAY OF ADDING VIEWS (OTHER THAN A FUNCTION)
# another view (which is just a function)
def meetup_details(request):
    selected_meetup = {
        'title':'My first meetup',
         'description':'This is the first meetup'}
    return render(request, 'meetups/meetup-details.html',{
        'meetup_title': selected_meetup['title'],
        'meetup_desctiption' :  selected_meetup['description']
    })    