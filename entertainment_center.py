import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
    "http://www.impawards.com/1995/posters/toy_story_ver1.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

gran_torino = media.Movie("Gran Torino",
                          "http://www.impawards.com/2008/posters/gran_torino.jpg",
                          "https://www.youtube.com/watch?v=3WkGaPMInMc")

band_of_brothers = media.Movie("Band of Brothers",
                            "http://img.moviepostershop.com/band-of-brothers-movie-poster-2001-1010195949.jpg",
                            "https://www.youtube.com/watch?v=kyDkHvi9yeI")

harry_potter = media.Movie("Harry Potter",
                            "http://harrypotterfanzone.com/wp-content/2015/07/chamber-of-secrets-theatrical-poster.jpg",
                            "https://www.youtube.com/watch?v=PbdM1db3JbY")

o_brother = media.Movie("O Brother Where Art Thou?",
                        "https://images-na.ssl-images-amazon.com/images/I/51Z2g-KN03L._AC_UL320_SR216,320_.jpg",
                        "https://www.youtube.com/watch?v=eW9Xo2HtlJI")

godfather = media.Movie("The Godfather",
                        "http://fontmeme.com/images/The-Godfather-Poster.jpg",
                        "https://www.youtube.com/watch?v=sY1S34973zA")

movies = [toy_story, gran_torino, band_of_brothers, harry_potter, o_brother, godfather]

fresh_tomatoes.open_movies_page(movies)
