from django.shortcuts import render
from .models import netflixData
from django.db.models import Q

def netflix_search(request):
    queryset = netflixData.objects.all()

    #search bar stuff
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) |
            Q(director__icontains=query) |
            Q(cast__icontains=query)
        )





    #get's the selected generes from the user 
    selected_genre = request.GET.getlist('Genre')
    if selected_genre:
        q = Q()
        for genre in selected_genre: 
            q |= Q(listed_in__icontains=genre)  
        queryset = queryset.filter(q)


    #get's the data from the database and seperates it so it's not long string with multiple generes
    genres_raw = netflixData.objects.values_list('listed_in', flat=True)
    genre_set = set()
    for entry in genres_raw:
        if entry:
            genre_set.update([g.strip() for g in entry.split(',')])
    genres = sorted(genre_set)

    #get's the selected countries from the user 
    selected_countries = request.GET.getlist('country')
    if selected_countries:
        q = Q()
        for country in selected_countries: 
            q |= Q(country__icontains=country)
        queryset = queryset.filter(q)

    #get's the data from the database and seperates it so it's not long string with multiple countries 
    raw_countries = netflixData.objects.values_list('country', flat=True)
    split_countries = set()
    for entry in raw_countries:
        if entry:
            split_countries.update([c.strip() for c in entry.split(',')])
    countries = sorted(split_countries)

    # get's the data from the year dropdown and passes it to the query
    year = request.GET.get('year')
    if year:
        queryset = queryset.filter(release_year__year=year)





    # this reverses the years list because the data is squed towards present so starting at 1925 is less then idea
    years = list(netflixData.objects.dates('release_year', 'year'))[::-1] 


    context = {
        'results': queryset,
        'genres': genres,
        'countries': countries,
        'years': years,
        'selected_countries': selected_countries,
        'selected_genre': selected_genre,
    }

    return render(request, 'searchPage/search.html', context)
