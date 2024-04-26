from Book import Book
from Show import Show
import tkinter
import tkinter.filedialog as filedialog
import os

class Recommender():

    def __init__(self):
        self.book_dic = {}
        self.show_dic = {}
        self.ass_dic = {}

    def loadBooks(self):

        # read the file
        while 1:
            filepath = filedialog.askopenfilename(title="", initialdir=os.getcwd())

            if os.path.exists(filepath):
                break
            else:
                print("The file is not exist")
                continue
        try:
            with open(filepath, "r") as file:
                next(file)

                for line in file:
                    line = line.split(",")

                    if len(line) != 11:
                        raise ValueError("The input file is not the standard shows input file")
                    
                    id = line[0]
                    title = line[1]
                    authors = line[2]
                    average_rate = line[3]
                    isbn = line[4]
                    isbn13 = line[5]
                    language_code  = line[6]
                    num_pages = line[7]
                    num_ratings = line[8]
                    publication_date = line[9]
                    publisher = line[10]

                    newBook = Book(id, title, average_rate, authors, isbn, isbn13, language_code, num_pages, num_ratings, publication_date, publisher)

                    self.book_dic[id] = newBook
        except Exception as e:
            print(e)
            # if encounter any error, set the dictionary as empty
            self.book_dic = {}
    
    def loadShows(self):

        # read the file
        while 1:
            filepath = filedialog.askopenfilename(title="", initialdir=os.getcwd())

            if os.path.exists(filepath):
                break
            else:
                print("The file is not exist")
                continue
        try:
            with open(filepath, "r", encoding='utf-8') as file:
                next(file)

                for line in file:
                    line = line.split(",")

                    if len(line) != 13:
                        raise ValueError("The input file is not the standard shows input file")
                    
                    id = line[0]
                    type = line[1]
                    title = line[2]
                    directors = line[3]
                    cast = line[4]
                    average_rate = line[5]
                    country_code = line[6]
                    date_added = line[7]
                    year_released = line[8]
                    rating = line[9]
                    duration = line[10]
                    genres = line[11]
                    description = line[12]

                    newShow = Show(id, title, average_rate, type, directors, cast, country_code, date_added, year_released, rating, duration, genres, description)

                    self.show_dic[id] = newShow
        except Exception as e:
            print(e)
            # if encounter any error, set the dictionary as empty
            self.show_dic= {}

    def loadAssociations(self):

        # read the file
        while 1:
            filepath = filedialog.askopenfilename(title="", initialdir=os.getcwd())

            if os.path.exists(filepath):
                break
            else:
                print("The file is not exist")
                continue

        try:
            with open(filepath, "r") as file:

                for line in file:
                    line = line.split(",")

                    if len(line) != 2:
                        raise ValueError("The input file is not the standard shows input file")
                        
                    id1 = line[0]
                    id2 = line[1]

                    # store id1 and id2
                    if id1 in self.ass_dic:
                        if id2 in self.ass_dic[id1]:
                            self.ass_dic[id1][id2] += 1
                        else:
                            self.ass_dic[id1][id2] = 1
                    else:
                        self.ass_dic[id1] = {}
                        self.ass_dic[id1][id2] = 1
                    
                    # reversal store
                    if id2 in self.ass_dic:
                        if id1 in self.ass_dic[id2]:
                            self.ass_dic[id2][id1] += 1
                        else:
                            self.ass_dic[id2][id1] = 1
                    else:
                        self.ass_dic[id2] = {}
                        self.ass_dic[id2][id1] = 1

        except Exception as e:
            print(e)
            # if encounter any error, set the dictionary as empty
            self.show_dic= {}

    def getMovieList(self):

        maxTitle = 5
        maxRuntime = 7

        # get max length
        for movie in self.show_dic:

            if movie.get_type_show().lower() == "movie":
                title = movie.get_title()
                duration = movie.get_duration()

                if maxTitle < len(title):
                    maxTitle = len(title)
                
                if maxRuntime < len(duration):
                    maxRuntime = len(duration)
        
        # print header
        message = "Title"

        if 5 < maxTitle:
            for i in range(maxTitle - 5):
                message += " "

        message += "Runtime"
        if 7 < maxRuntime:
            for i in range(maxRuntime - 7):
                message += " "
        print(message)
        
        # print information of each movie
        for movie in self.show_dic:

            if movie.get_type_show().lower() == "movie":

                message = ""

                title = movie.get_title()
                duration = movie.get_duration()

                message += title

                # add extra spaces
                if maxTitle < len(title):
                    for i in range(maxTitle - len(title)):
                        message += " "

                message += duration

                # add extra spaces
                if maxRuntime < len(duration):
                    for i in range(maxRuntime - len(duration)):
                        message += " "
                
                print(message)

    def getBookList(self):

        maxTitle = 5
        maxAuthor = 9

        for book in self.book_dic:

            title = book.get_title()
            authors = book.get_authors()

            if maxTitle < len(title):
                maxTitle = len(title)
                
            if maxAuthor < len(authors):
                maxAuthor = len(authors)
        
        # print header
        message = "Title"

        if 5 < maxTitle:
            for i in range(maxTitle - 5):
                message += " "

        message += "Author(s)"
        if 9 < maxAuthor:
            for i in range(maxAuthor - 9):
                message += " "
        
        print(message)

        # print information of books        
        for book in self.book_dic:

            message = ""

            title = book.get_title()
            authors = book.get_authors()

            message += title

            # add extra spaces
            if maxTitle < len(title):
                for i in range(maxTitle - len(title)):
                     message += " "

            message += authors

            # add extra spaces
            if maxAuthor < len(authors):
                for i in range(maxAuthor - len(authors)):
                    message += " "
                
            print(message)
    
    def getTVList(self):

        maxTitle = 5
        maxSeasons = 7

        for movie in self.show_dic:

            if movie.get_type_show().lower() == "tv show":
                title = movie.get_title()
                seasons = movie.get_duration()

                if maxTitle < len(title):
                    maxTitle = len(title)
                
                if maxSeasons < len(seasons):
                    maxSeasons = len(seasons)
        
        # print header
        message = "Title"

        if 5 < maxTitle:
            for i in range(maxTitle - 5):
                message += " "

        message += "Author(s)"
        if 7 < maxSeasons:
            for i in range(maxSeasons - 7):
                message += " "
        
        print(message)
        
        # print tv shows inforamtions
        for movie in self.show_dic:

            if movie.get_type_show().lower() == "tv show":

                message = ""

                title = movie.get_title()
                seasons = movie.get_duration()

                message += title

                # add extra spaces
                if maxTitle < len(title):
                    for i in range(maxTitle - len(title)):
                        message += " "

                message += seasons

                # add extra spaces
                if maxSeasons < len(seasons):
                    for i in range(maxSeasons - len(seasons)):
                        message += " "
                
                print(message)
    
    def getMovieStats(self):
        
        
        rating_count = {} # count number of movie based on their rating
        director_count = {} # count who has directed the most movie
        actor_count = {} # count who has acted in the most movies
        genres_count = {} # count most frequent movie genre
        count = 0 # count how many movies
        average_duration = 0

        for id, movie in self.show_dic.items():

            if movie.get_type_show().lower().strip() == "movie":
                
                count +=1

                if movie.get_rating() in rating_count:
                    rating_count[movie.get_rating()] += 1
                else:
                    rating_count[movie.get_rating()] = 1

                average_duration += int(movie.get_duration().split(" ")[0])

                directors = movie.get_directors().strip().split("\\")
                for director in directors:
                    if director in director_count:
                        director_count[director] += 1
                    else:
                        director_count[director] = 1
                
                actors = movie.get_actors().strip().split("\\")
                for actor in actors:
                    if actor in actor_count:
                        actor_count[actor] += 1
                    else:
                        actor_count[actor] = 1

                genres = movie.get_genres().strip().split("\\")
                for genre in genres:
                    if genre in genres_count:
                        genres_count[genre] += 1
                    else:
                        genres_count[genre] = 1
                
        message = "Ratings:"
        print(message)

        for rating, count_current in rating_count.items():

            percent = count_current * 100/ count
            message = f"{rating}  {percent:.2f}"
            print(message)
        
        if count != 0:
            average_duration = average_duration / count
            print("Average duration: " + str(average_duration))

        print("most director: " + self.getMost(director_count))
        print("most director: " + self.getMost(actor_count))
        print("most genres: " + self.getMost(genres_count))


            
    def getTVStats(self):
        
        rating_count = {} # count number of movie based on their rating
        average_duration = 0 # count number of seasons
        genres_count = {} # count most frequent movie genre
        count = 0 # count how many movies
        

        for id, tvshow in self.show_dic.items():

            if tvshow.get_type_show().lower() == "tv show":
                 
                count +=1

                if tvshow.get_rating() in rating_count:
                    rating_count[tvshow.get_rating()] += 1
                else:
                    rating_count[tvshow.get_rating()] = 1
                
                average_duration += int(tvshow.get_duration().split(" ")[0])
                
                genres = tvshow.get_genres().strip().split("\\")
                for genre in genres:
                    print(genre)
                    if genre in genres_count:
                        genres_count[genre] += 1
                    else:
                        genres_count[genre] = 1

        
        message = "Ratings:"
        print(message)

        for rating, count_current in rating_count.items():

            percent = count_current * 100/ count
            message = f"{rating}  {percent:.2f}"
            print(message)

        average_duration = average_duration / count
        print("average seasons: " + str(average_duration))
        print("most tv: " + self.getMost(genres_count))
    
    def getBookStats(self):
        
        average_page = 0 # count average number of pages
        author_count = {} # count number of written book by one author
        publisher_count = {} # count number of tv shows
        count = 0 # count how many movies
        

        for id, book in self.book_dic.items():
            
            count +=1

            average_page += int(book.get_num_pages())

            authors = book.get_authors().strip().split("\\")
            for author in authors:
                if author in author_count:
                    author_count[author] += 1
                else:
                    author_count[author] = 1

            if book.get_publisher() in publisher_count:
                publisher_count[book.get_publisher()] += 1
            else:
                publisher_count[book.get_publisher()] = 1

        
        average_page = average_page / count
        print("average pages: " + str(average_page))
        print("most author: " + self.getMost(author_count))
        print("most publisher: " + self.getMost(publisher_count))

    def getMost(self,dic):

        most_object_count = 0
        most_object = ""

        for object, count_current in dic.items():

            if count_current > most_object_count:
                 most_object_count = count_current
                 most_object = object

        return most_object

aa = Recommender()
#aa.loadShows()
#aa.getMovieStats()
#aa.getTVStats()


aa.loadBooks()
aa.getBookStats()