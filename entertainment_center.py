import fresh_tomatoes
import media

# data info supplied below to the fresh_tomatoes program


toy_story = media.Movie("toy story", " a story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.come/watch?v=vwyZH85NQC4", "11/22/95" )

grand_budapest_hotel = media.Movie("The Grand Budapest Hotel",
                         "A man takes care of a hotel during a war",
                         "http://www.impawards.com/2014/thumbs/sq_grand_budapest_hotel.jpg",
                         "https://www.youtube.com/watch?v=1Fg5iWmQjwk", "3/7/14" )
                     
goodfellas = media.Movie("Goodfellas",
                        "Crime doesn't pay in the end",
                        "http://thumbs4.ebaystatic.com/d/l225/m/myYZ7AGmxrSYS8b4V9CBKLw.jpg",
                        "https://www.youtube.com/watch?v=2ilzidi_J8Q", "9/19/90")                        

frozen = media.Movie("Frozen",
                         "Two sisters win the day",
                         "http://img1.wikia.nocookie.net/__cb20130917150207/disney/images/1/11/Frozen_Poster.jpg",
                         "https://www.youtube.com/watch?v=bQRLVxZHKPs", "11/27/13")

shawshank_redemption = media.Movie("Shawshank Redemption",
                        "A good man finally gets out of prison",
                        "http://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                        "https://www.youtube.com/watch?v=NmzuHjWmXOc", "9/23/94")


cinema_paradiso = media.Movie("Cinema Paradiso",
                        "A boy grows up to live his dreams",
                        "http://www.atodmagazine.com/wp-content/uploads/2014/11/Cinema-Paradiso-Poster.jpg",
                        "https://www.youtube.com/watch?v=maV1ZYdAExw", "2/2/90")

movies = [toy_story, grand_budapest_hotel, goodfellas, frozen, shawshank_redemption, cinema_paradiso]
fresh_tomatoes.open_movies_page(movies)



