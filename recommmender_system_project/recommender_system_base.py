from abc import ABC, abstractmethod
import pandas


class RecommenderSystemBase(ABC):
    """The base class for the recommender system

    Attributes
    ----------
    movies_dataframe : pandas.DataFrame
        A dataframe with all the movies metadata (movies_metadata, keywords, credits, descriptions, etc).
        This dataframe is indexed on the `movie_id` column (refer to the the `__create_movies_dataframe` for
        more informations)

    ratings_dataframe : pandas.DataFrame
        A dataframe with the users ratings.

    Methods
    -------
    __create_movies_dataframe
        Merges all the movie informations in a single dataframe and indexes it with a new column `movie_id`

    recommend_movies_to_user
        Given a user with a watch history, it recommends the k movies that he will most likely watch.

    recommend_similar_movies
        Recommends the k most similar of the movie with the id 'movie_id'.

    get_movies_embeddings
        Returns the embedding of the movies with movie_id in movie_ids.


    Notes
    -----
    - You can add other attributes and methods to this class.
    - In the constructor parameters, you can add other datasets if you need them.
    """

    def __init__(self, ratings_dataframe: pandas.DataFrame, movies_metadata_dataframe: pandas.DataFrame,
                 keywords_dataframe: pandas.DataFrame, credits_dataframe: pandas.DataFrame) -> None:
        """Sets the movies_dataframe and ratings_dataframe attributes.

        Parameters
        ----------
        ratings_dataframe : pandas.DataFrame
            The movie ratings of users.
        movies_metadata_dataframe : pandas.DataFrame
            The movies metadata.
        keywords_dataframe : pandas.DataFrame
            The movies keywords.
        credits_dataframe : pandas.DataFrame
            The movies credits.
        """
        self.movies_dataframe = self.__create_movies_dataframe(ratings_dataframe, movies_metadata_dataframe,
                                                               keywords_dataframe, credits_dataframe)
        self.ratings_dataframe = ratings_dataframe

    def __create_movies_dataframe(self, ratings_dataframe: pandas.DataFrame,
                                  movies_metadata_dataframe: pandas.DataFrame,
                                  keywords_dataframe: pandas.DataFrame,
                                  credits_dataframe: pandas.DataFrame) -> pandas.DataFrame:
        """Merges all the movie information in a single dataframe and indexes it with a new column `movie_id`.

        The columns `title` and `original_title` contains duplicates so they can not be used as an identifier
        of the movies. We can use the `id` column as an identifier but we want to have a user friendly id.
        Therefore, you need to create a new column `movie_id` where you will append multiple informations
        (title, original_title, release_year, language). This column should have the following format :
        title-original_title-language-release_year

        Example :
            title = The Promise, original_title = Das Versprechen, release_year = 1995-02-16,
            original_language = de ====> movie_id = the_promise-das_versprechen-en-1995


        Parameters
        ----------


        Returns
        -------
        A dataframe that groups all the movie informations.
        """
        pass

    @abstractmethod
    def recommend_movies_to_user(self, user_id: int, k: int) -> pandas.DataFrame:
        """Given a user with a watch history, it recommends the k movies that he will most likely watch.

        user_favourite_movies = the set of movies that the user watched and liked.

        If len(user_favourite_movies) = 0:
            Recommend k random movies from the set of highly rated movies in the dataset.
            These k movies should be chosen randomly. So if the function is executed 2 times, it should
            return different results.

        If k < len(user_favourite_movies):
            Select a random set of movies from the user_favourite_movies set and recommend a movie for each item.

        If k > len(user_favourite_movies):
            Select n movies for each movie the user liked.
            Example :
                k = 10 and len(user_favourite_movies) = 1
                    Recommend 10 movies that are similar to the movie the user watched.
                k = 10 and len(user_favourite_movies) = 3
                    Recommend:
                        3 movies that are similar the 1st movie the user liked.
                        3 movies that are similar the 2nd movie the user liked.
                        4 movies that are similar the 3rd movie the user liked.

        Parameters
        ----------
        user_id : int
            The id of the user
        k : int
            The number of movies to recommend

        Returns
        -------
        pandas.DataFrame
            A subset of the movies_dataframe with the k movies that the user may like.
        """
        pass

    @abstractmethod
    def recommend_similar_movies(self, movie_id: str, k: int) -> pandas.DataFrame:
        """Recommends the k most similar movies of the movie with the id 'movie_id'.

        Parameters
        ----------
        movie_id : str
            The id of the movie.
        k : int
            The number of similar movies to recommend.

        Returns
        -------
        pandas.DataFrame
            A subset of the movies_dataframe with the k similar movies of the target movie (movie_id).
        """
        pass

    @abstractmethod
    def get_movies_embeddings(self, movie_ids: [str]) -> pandas.DataFrame:
        """Returns the embedding of the movies with movie_id in movie_ids.

        Parameters
        ----------
        movie_ids : [str]
            List of the movies movie_id.

        Returns
        -------
        pandas.DataFrame
            The embeddings of the movies with movie_id in movie_ids.
        """
        pass
