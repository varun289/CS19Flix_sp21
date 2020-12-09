# CS19Flix
#What problem is your project trying to solve?

Deciding which movie to watch, game to play, or show to binge is not as straightforward as it seems in 2020. People have more free time to consume entertainment than ever before, as well as more entertainment options, yet there is no unified interface to access recommendations on content curated from multiple services, etc.

Most recommender systems today are platform-specific (example: Netflix and Amazon). However, due to the large number of entertainment sources, these recommender systems don’t recommend where users should be allocating their time to consume media.

TECH STACK
User Interface - Vue JS is a front-end framework. It is great to use for simple web pages.

Server - We used a python flask server to provide fastAI data to the front-end

Model - We used fast ai for our collaborative filtering model

Dataset used for the project: https://www.kaggle.com/rounakbanik/the-movies-dataset

Branches:

Master Branch: 

Frontend folder contains the code for the swiping feature (seperate from movie list final product)
To Run: Yarn install
	  Yarn serve

Notebooks folder: contains a collaborative filtering file that trains and exports the model. Also contains a file to create a csv with all the movie reviews from users that will be used in the future for the NLP model. 
To Run: Google Collab

Ignore Backend folder (utilized in different branch)


Movie List Branch:
Frontend folder: contains code to view list of movies generated from the TMDB movies API and the predicted ratings generated from the collaborative filtering model
Make sure to run the server before running this.
To Run: Yarn install
	  Yarn serve


Backend folder contains the code for the server to run. Server routes API POST requests and returns data to the UI.
Ignore Procfile (it was for deploying the server, but we ran into issues with that).
To Run: 
Open Backend Folder in code editor
pip install -r requirements.txt
   	  pip install IPython if needed
Run server.py
Ignore list-view folder: is the initial clean looking list we tried to incorporate API request with but doesn’t work

(ignore the getPost and storeData branches)


