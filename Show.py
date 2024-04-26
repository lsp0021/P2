# Author: Suqi Lu
# Latest modified date: 4/26/2024
# Description: The Show class

from Media import Media 

class Show(Media):
    def __init__(self, id, title, average_rate, type_show, directors, actors, country_code, date_added, year_released, rating, duration, genres, description):
        super().__init__(id, title, average_rate)
        self.__type_show = type_show
        self.__directors = directors
        self.__actors = actors
        self.__country_code = country_code
        self.__date_added = date_added
        self.__year_released = year_released
        self.__rating = rating
        self.__duration = duration
        self.__genres = genres
        self.__description = description

    # Getters
    def get_type_show(self):
        return self.__type_show

    def get_directors(self):
        return self.__directors

    def get_actors(self):
        return self.__actors

    def get_country_code(self):
        return self.__country_code

    def get_date_added(self):
        return self.__date_added

    def get_year_released(self):
        return self.__year_released

    def get_rating(self):
        return self.__rating

    def get_duration(self):
        return self.__duration

    def get_genres(self):
        return self.__genres

    def get_description(self):
        return self.__description

    # Setters
    def set_type_show(self, type_show):
        self.__type_show = type_show

    def set_directors(self, directors):
        self.__directors = directors

    def set_actors(self, actors):
        self.__actors = actors

    def set_country_code(self, country_code):
        self.__country_code = country_code

    def set_date_added(self, date_added):
        self.__date_added = date_added

    def set_year_released(self, year_released):
        self.__year_released = year_released

    def set_rating(self, rating):
        self.__rating = rating

    def set_duration(self, duration):
        self.__duration = duration

    def set_genres(self, genres):
        self.__genres = genres

    def set_description(self, description):
        self.__description = description

    # override the print function
    def __str__(self):
        message = ""
        message += "Title:\n"
        message += self.get_title() + "\n"
        message += "Directors:\n"
        message += self.get_directors() + "\n"
        message += "Average Rating:\n"
        message += self.get_average_rate() + "\n"
        message += "Actors:\n"
        message += self.get_actors() + "\n"
        message += "Country Code:\n"
        message += self.get_country_code() + "\n"
        message += "Date Added:\n"
        message += self.get_date_added() + "\n"
        message += "Released Year:\n"
        message += self.get_year_released() + "\n"
        message += "Rating:\n"
        message += self.get_rating() + "\n"
        message += "Duration:\n"
        message += self.get_duration() + "\n"
        message += "Genres:\n"
        message += self.get_genres() + "\n"
        message += "Description:\n"
        message += self.get_description()
        return message

