# General Information
  IGO(Iranian Geometry Olympiad)
  currently served at [igo-official.ir](https://igo-official.ir)

# Technologies
  * [Django](https://github.com/django/django)
  * [Semantic UI](https://github.com/Semantic-Org/Semantic-UI)

# Getting Started
1- Install virtualenv and activate venv following instruction in the link blow
  * [How to install virtualenv](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b)

2- Inside the activated venv, install projcet requirements
  * `pip install -r requirements.txt`

3- Run the development server
  * `./manage.py runsever 0.0.0.0:8000`

# Production
1- Simply build and run with docker
  * `docker-compose -f deploy/docker-compose.yml up -d`

2- You may also want to transfer media files and apply database dump from old server
  (I'm not really in the mood to explain. Sorry!)

# Docs
  * You can find the following under [docs](https://github.com/mrtaalebi/sitigo/tree/master/docs)
    * CODE_OF_CONDUCT
    * CONTRIBUTING
    * README
  * LICENSE
  * ISSUE_TEMPLATE
