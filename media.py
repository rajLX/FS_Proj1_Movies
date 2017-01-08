#!/usr/bin/env python
"""Module that implements Movie class. """

import webbrowser

class Movie:
    """ Abstracts the movie in a simple manner. """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """ Constuctor for the class.

        Args:
            movie_title: The exact title of the movie
            movie_storyline: A brief note on storyline
            poster_image: Popular poster to depict the movie
            trailer_youtube: Link to movie trailer
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Play the movie trailer. """
        webbrowser.open(self.trailer_youtube_url)

    def print_story(self):
        """Print the movie story line. """
        print(self.storyline)

    def __str__(self):
        """Print movie name. """
        print(self.title)
