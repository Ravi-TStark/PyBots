import imdb
import json
from speech import speak, speakLimited
   
# creating instance of IMDb 
ia = imdb.IMDb() 

def moviePlotQuery(mname):
    # getting the movie with name 
    search = ia.search_movie(mname) 
  
    # getting movie year 
    year = search[0]['year'] 
  
    # printing movie name and year 
    print(search[0]['title'] + " : " + str(year))

    movie = ia.get_movie(search[0].movieID, info =['plot']) 

    movie.infoset2keys

    plot = movie['plot'][0]
    plot = plot.split('::')[0]

    print(plot)
    speakLimited(search[0]['title'] + ": " + str(year))
    speakLimited(plot)

def movieSummaryQuery(mname):
    # getting the movie with name 
    search = ia.search_movie(mname) 
  
    # getting movie year 
    year = search[0]['year'] 
  
    # printing movie name and year 
    print(search[0]['title'] + " : " + str(year))

    movie = ia.get_movie(search[0].movieID, info =['synopsis']) 

    movie.infoset2keys

    synopsis = movie['synopsis'][0]

    print(synopsis)
    speakLimited(search[0]['title'] + ": " + str(year))
    speak(synopsis)

query = input("Enter Query: ")
moviePlotQuery(query)