"""This module presents favorite movies in a HTML form."""
import media
import fresh_tomatoes

A_FEW_GOOD_MEN = media.Movie("A Few Good Men",
                             "A lawyer defends two US Marines charged with the murder of a"\
                                     " fellow Marine",
                             "https://upload.wikimedia.org/wikipedia/en/4/45/"\
                                     "A_Few_Good_Men_poster.jpg",
                             "https://www.youtube.com/watch?v=ePo91pMcu94")

LION_KING = media.Movie("The Lion King",
                        "A lion cub who cannot wait to be king, searches for his destiny",
                        "https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg",
                        "https://www.youtube.com/watch?v=4sj1MT05lAA")

GOD_FATHER = media.Movie("God Father",
                         "A story about fictional New York crime family",
                         "https://upload.wikimedia.org/wikipedia/en/1/1c/Godfather_ver1.jpg",
                         "https://www.youtube.com/watch?v=sY1S34973zA")

DEPARTED = media.Movie("Departed",
                       "A crime drama with double agents on both sides, in police crime"\
                            " branch and mob syndicate",
                       "https://upload.wikimedia.org/wikipedia/en/5/50/Departed234.jpg",
                       "https://www.youtube.com/watch?v=SGWvwjZ0eDc")

LOST_ARK = media.Movie("Raiders of the Lost Ark",
                       "An archaeologist is hire by US government to find the lost ark"\
                              " before Nazis get hold of it",
                       "https://upload.wikimedia.org/wikipedia/en/4/4c/Raiders_of_the_Lost_Ark.jpg",
                       "https://www.youtube.com/watch?v=XkkzKHCx154")

DIE_HARD = media.Movie("Die Hard",
                       "A New York City cop gets trapped in a Los Angeles high-rise occupied"\
                               "by terrorists on Christmas Eve",
                       "https://upload.wikimedia.org/wikipedia/en/7/7e/Die_hard.jpg",
                       "https://www.youtube.com/watch?v=-qxBXm7ZUTM")

MOVIES = [A_FEW_GOOD_MEN, LION_KING, GOD_FATHER, DEPARTED, LOST_ARK, DIE_HARD]
fresh_tomatoes.open_movies_page(MOVIES)
