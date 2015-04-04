import webbrowser

class Movie():
    """ This class provideds a way to store movie related information"""

# This is code for the class movie and details the instance variables 

   
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, release_date):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.release_date = release_date
        

