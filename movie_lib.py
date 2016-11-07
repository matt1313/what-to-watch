import csv

#STEP ONE


# Note that you will need to make associations between users and ratings, and ratings and movies.

# Specifically, you will need to be able to:
# Find all ratings for a movie by id
# Find the average rating for a movie by id
# Find the name of a movie by id
# Find all ratings for a user

# Write methods to handle the above use cases, and then write some tests and load in some test data to ensure they work.


#  row["movie"], get_avg(row))


class Movies:

    with open('ml-100k/u.item', encoding='latin_1') as i:
        reader_i = csv.DictReader(i)
        # for row in reader_i:
        #     print(row)



    # with open('ml-100k/u.genre', encoding='latin_1') as g:
    #     reader_g = csv.DictReader(g)
    #     for row in reader_g:
    #         print(row)




    def __init__(self):
        self.reader_i = reader_i

    def spliting_stuff(self, reader_i):
        row_split = reader_i.split("|")
        print(row_split)


        # def columize(Header):
        #     header = next(self.reader_g)
        #     print(header)


    # def movie_info():
    #
    #     pass



# class Users:
#
#     with open('ml-100k/u.user', encoding='latin_1') as u:
#         reader = csv.DictReader(u)
#         print(reader)
#         for row in reader:
#             print(row)
#
#     def __init__(self):
#         pass
#
#     def user_info():
#
#         pass
#
# class Rating:
#
#     with open('ml-100k/u.data', encoding='latin_1') as d:
#         reader = csv.DictReader(d)
#         print(reader)
#         for row in reader:
#              print(row)
#
#
#     def __init__(self):
#
#         pass
#
#     def rating_info():
#
#         pass

# def get_avg(**kwargs):
#     kwargs["open"] + float(kwargs["close"]) + float(kwargs["high"]) + float(kwargs["low"])
#
# def avg(self):
#     1 = (self.open,self.close,self.low,self.high)
#     return sum(1)/len(1)
