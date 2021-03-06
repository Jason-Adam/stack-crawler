# StackOverflow Web Crawler  
The repository holds all the necessary components to run a web-scraper on the StackOverflow website. The scraper is currently configured to write the documents to a local MongoDB, but it can easily be changed by commenting out the pipeline in  
```bash
stack/stack/settings.py
```  
The scraper currently has two spiders that run sequentially. The stack spider will pull the URLs and titles of questions for a given SO tag. These will be loaded to the Mongo Database. The second crawler will query the URLs from Mongo and proceed to scrape them for the actual question text and other data. The pipeline will perform an upsert on the Mongo database. The script can be run using the following:  
```bash
cd stack  
python3 run_spiders.py
```  
## Setting Up MongoDB  
This project utilizes a local MongoDB instance. Instructions for setting one up can be found [here](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/). To start the database instance, open the terminal and type (assumes you're using Homebrew):  
```bash
brew services start mongodb-community
```  
I also recommend using **MongoDB Compass** to view your database. It can be downloaded [here](https://www.mongodb.com/products/compass).  
## Python Environment  
You will need the following environment variables for the crawler to run:  
```bash
MONGO_DB="stackoverflow"
MONGO_COLLECTION="ai_questions"
MONGO_HOST="localhost"
MONGO_PORT=27017
SO_TAG="artificial-intelligence"
```
