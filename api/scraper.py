from facebook_scraper import get_posts
from pymongo import MongoClient
import os



class FBScraper():

    # stores and returns the posts scraped from 'Meta' facebook profile for the first 3 pages
    def scrape_meta(self):
        items=[]
        itm={}
        for post in get_posts('Meta', pages=3):
            itm['likes'] =  post['likes']
            itm['comments'] =  post['comments']
            itm['text'] =  post['text']
            items.append(itm)
        # store all into mongoDB
        self.store_many_to_db(items)
        print("scraping done")
        return self.get_all_posts_from_db()

    def highcomments(self):
        return max([post['comments'] for post in get_posts('Meta', pages=3)])

    def highlikes(self):
        return  max([post['likes'] for post in get_posts('Meta', pages=3)])


    ''' DB manips ''' 
    # establish db connection 
    def get_database(self):
        # MONGODB_CONNSTRING from environment 
        connString = os.environ['MONGODB_CONNSTRING']
        client = MongoClient(connString,connect=False) #there is an issue connecting to DB; in troubleshooting phase 
        #db name: facebook_posts_list
        return client['facebook_posts_list']

    #  stores posts into DB
    def store_many_to_db(self, items):
        # Get the database
        dbname = self.get_database()
        #create the "posts" collection into the database
        posts_collection = dbname["posts"]
        posts_collection.insert_many(items)
        return posts_collection

    # get all posts from DB
    def get_all_posts_from_db():
        posts_collection = dbname["posts"]
        posts_details = posts_collection.find()
        return posts_details
