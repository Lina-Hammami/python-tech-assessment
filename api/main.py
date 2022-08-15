from fastapi import FastAPI
from api.scraper import FBScraper 

app = FastAPI()
fbposts = FBScraper()

@app.get("/")
async def read_all_posts():
    return {"Welcome to the facebook scraper API !"}

@app.get("/posts")
async def read_all_posts():
    # return stored fb posts from database  
    return fbposts.get_all_posts_from_db()

@app.get("/scrapemeta")
async def scrape_meta():
    # scrape the meta fb page 
    return fbposts.scrape_meta()

@app.get("/highlikes")
async def highest_likes():
    # returns the highest number of likes
    return fbposts.highlikes()

@app.get("/highcomments")
async def highest_comments():
    # returns the highest number of comments
    return fbposts.highcomments()

# ps: the test is on the meta facebook profile for the first 3 pages 