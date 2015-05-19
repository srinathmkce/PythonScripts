__author__ = 'user'
import movies
import fresh_tomatoes

sathileelavathi = movies.Movie("Sathileelavathi", "Comedy Script", "http://www.tamilyogi.tv/wp-content/uploads/2014/08/sati.jpg",
                               "https://www.youtube.com/watch?v=iYesV4sJ-C8")
singaravelan = movies.Movie("Singaravelan", "Comedy Movie", "http://www.starmusiq.com/movieimages/Singaravelan_B.jpg",
                            "https://www.youtube.com/watch?v=Jn6H0WT2huw")
vasoolraja = movies.Movie("vasoolraja", "Comedy", "http://tamilgun.com/wp-content/uploads/2014/09/main.jpg",
                         "https://www.youtube.com/watch?v=r-_tVHECCvY")
movies_list = [sathileelavathi, singaravelan, vasoolraja]
fresh_tomatoes.open_movies_page(movies_list)