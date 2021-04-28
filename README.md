<!--
*** The Best-README-Template at https://github.com/othneildrew/Best-README-TemplateIf 
-->



<!-- PROJECT SHIELDS -->
<!--
*** Can use markdown "reference style" links for readability or html if needed
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/KelleClark/database_project" alt="Logo" width="80" height="80"><img src="https://github.com/KelleClark/database_project/blob/main/ClickApp/static/img/clik.PNG">
  </a>

  <h3 align="center">Clik</h3>

  <p align="center">
    project_description
    <br />
    <a href="https://github.com/KelleClark/database_project"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/KelleClark/database_project">View Demo</a>
    ·
    <a href="https://github.com/KelleClark/database_project">Report Bug</a>
    ·
    <a href="https://github.com/KelleClark/database_project">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

An objective of social media platforms is to connect members with individuals and groups who share similar interests or connections. While FB, Twitter, LI, Reddit and Instagram provide users with an enjoyable and useful service, many believe that these social media sites make users less social. Current social applications available indirectly promote more time behind the screen, encourage individuals to make large and superficial connections, and enable the consumption of curated information that does not reflect reality. This project aims to provide users with some of the functionality of benchmark social media applications but with a focus on a design that improves real interaction between users.  The proposed system would include a three tier design implemented as a locally hosted web application for the scope of this semester-long project. 

The overarching goal for the system, as viewed by the team, is to bring people together in authentic ways that foster real relationships off screen. The application's use cases will be constructed in early stages of development as the team explores the personas of typical users and the tasks and goals of those users. Possible use cases are to enable the user to create small social circles and to enable the user to engage in face-to-face interactions in real-time.

### Built With

* [CSS]
* [HTML]
* [js]
* [Boostrap](https://getbootstrap.com)
* [JQuery](https://jquery.com)
* [flask](https://pypi.org/project/Flask/)
* [Neo4j](https://neo4j.com)
* [neovis]
* [py2neo]
* [PyCharm](https://www.jetbrains.com/pycharm/)


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow the steps provided in the quick start below.

### Prerequisites
You will need to have the following on your computer:
Python 
PyCharm 2019 or later 
Neo4j Desktop v.4 or later
Git


## (not quite a) Quick Start
### Installation and Local Test Setup
1. Note where you store Python and Git within your File System, you will need to set the location of the .exe files when setting up your project.

2. Open PyCharm and select NewProjec Figure 11.1t:
choose a location for your new project on your computer
set the location of your Python Interpreter: New Virtual Environment to your Python.exe
create 
Figure 11.1 Set up new project
<p><img src="https://github.com/KelleClark/database_project/blob/main/docs/images/create_new_project.PNG"></p>

3. Under Files/Settings/Version Control select Git and fill in the location on your computer of your Git.exe file, see Figure 11.2

Figure 11.2 Set up the Git for the project
<p><img src="https://github.com/KelleClark/database_project/blob/main/docs/images/set_up_vcs_git_clone.PNG"></p>

4. In the top navigation bar, select the Version Control System VCS and choose Git. From the Github address above, grab the url to clone the repository and paste in the url of the git repository.  It is a good idea to use the Test button to see if Git is connected.
You should now be able to use the Git features like commit (green check) , commit/push (green up arrow) and pull (blue arrow) on the top right and to checkout and create branches on the bottom left as shown in Figure 11.3















Figure 11.3  The Git features in PyCharm

<p><img src="https://github.com/KelleClark/database_project/blob/main/docs/images/see_git_features_in_PyCharm.PNG"></p>

5. Now we need to make sure our python virtual environment that you set up in step 2 has all of the required packages and libraries.  Go to the python terminal on the bottom of the interface and use the cli $ (venv) somelocation > pip install -r requirements.txt, see Figure 11.4

Figure 11.4 To install required packages and libraries
<p><img src="https://github.com/KelleClark/database_project/blob/main/docs/images/pip_install_requirements.PNG"></p>

Now minimize PyCharm for a second and open Neo4j Desktop.  

Within the Desktop, go to Project and create a New Project...and then add a Database.  Start the Database and Open the Neo4j Browser.  Connect to the database by using the cli cypher statement on the command line at the top of the Neo4j Browser enter  $ :server connect
Open the DB menu from the left and add find :user server add.  Add yourself as a user, for me my username is kelle and password is 111. We will need that in our database set up.  

Minimize Neo4j Desktop and Neo4j Browser.  Open PyCharm back up and set the Configuration near the top in the navigation bar. Then name the configuration...I named mine app and set the location to the file you want to run the application...app.py.  As in Figure 11.5, make sure you have the path of the Python venv set to the one for your project… and apply.   

Figure 11.5  Set up the PyCharm configuration to run the ClickApp
<p><img src="https://github.com/KelleClark/database_project/blob/main/docs/images/configure_project.PNG"></p>

Before we run the system, find the file for our configuration of the graph databases as highlighted in Figure 11.6

Figure 11.6: Find the configuration file for Graph neo4j object 
<p><img src="https://github.com/KelleClark/database_project/blob/main/docs/images/system_file_structure.PNG"></p>

Update your username and password that you just added to the Neo4j Database within your new project as shown in Figure 11.7.


Figure 11.7  : Make sure to change user and password to your information from your Neo4j Project Database
from py2neo import Graph
<p><img src="https://github.com/KelleClark/database_project/blob/main/docs/images/db_session.PNG"></p>

def db_auth():
   user = 'kelle'
   pword = '111'
   #graph = Graph("bolt://127.0.0.1:7687/db/data/", username=user, password=pword)
   graph = Graph("http://127.0.0.1:7474/db/data/", username=user, password=pword)
   return graph

 You should now be able to press the green “play” button and run the system or use the run button on the bottom. Errors will be shown in the run terminal at the bottom, but you should be able to open your web browser (Edge is good) and navigate to 127.0.0.1:5000, which is the default flask port.


Figure 11.8 The rendering of home/index.html rendered by @app.route(“/”) within the app.py file using flask
<p><img src="https://github.com/KelleClark/database_project/blob/main/docs/images/home_index_rendered.PNG"></p>


Section 11.2 The Model

We used two different graph databases, one to authenticate the user and issue a token so that a request to the server would not return information unless the token could be decoded and determined to be signed.  The other graph database is for the Person and Event node objects and the interestedIn and postedEvent relationships between two Persons or a Person and an Event.  

The schema for User, Figure 11.9, defined as a python class and used within the Graph object,  is  defined in the classes.py file of the Model directory. 




The email attribute of User will serve as the primary key (and is thus required).  The label for the node in the Graph associated with an instance of a User will be the name attribute.  When a user registers, their password is encrypted and stored within their user node.  This is the method used to ensure that the user’s information is only available to them during their session and could also be used to set views and permissions within the system.  If the system were to have used a token for a user, then a token would be generated with each login of the user, and would be encoded (not encrypted). The token is included with all requests to the server and checked to see if when decoded returns “signed.”  If signed, then the get request continues; otherwise, an error of invalid user is returned in the terminal.   We chose to use a dictionary data type and the idea of a session.  The user’s email is included in the session and if the user’s email is a key of the dictionary...then the system uses the values of the dictionary.

 
Figure 11.9     The User Model for session and authenticating login
 
<p><img src="https://github.com/KelleClark/database_project/blob/main/docs/images/Model_User.PNG"></p>

The attributes name, email and password are input from a form that requires these fields to be filled in with type string, email and password on the client side using form control. A warning is issued to the user if the input is not valid.  There should be no user in the system with the same email.  The attributes created_on and last_logged in are not required and are not currently used.  

If the user clicks the sign up button, the system takes in the information and checks to see if the email input is already in the system and if not uses the create_user in account_services.py to add the user to the system.  Along with the passed in information, the user node also stores a hashed value of the password using the sha512_crypt function within the  passlib.handlers.sha2_crypt library. 


Figure 11.10  The register page

<p><img src="https://github.com/KelleClark/database_project/blob/main/docs/images/create_an_account.PNG"></p>

In the event that the email is already among the users, then a warning is flashed letting the user know that they must use a different set of values to create their account.  This check on the collection of nodes is done via a method of the User/Graph object user = User.match(graph, f"{email}")  and implements a cypher query of the graph database. 

If the user clicks the login button, then the system again performs a cypher query using the same method. If the user is found then the session is created for the user in that the email: information pair is added to the session dictionary.

Figure 11.11 The login page
<p><img src="https://github.com/KelleClark/database_project/blob/main/docs/images/login.PNG"></p>

The flask framework uses the provided route to browse to the user’s profile page.  On this page, the user can see the information that is stored in the user node for them. Future features would allow a user to update their profile information and to answer questions to help the system to recommend events and friends through Machine Learning algorithms.  For now, the user should select to continue to Clik. As a team, the current database that is being accessed through the py2neo driver needs to be stopped and then a new project/database started with the same credentials but that will be connected with the neovis driver to provide utility and visualize the graph database of friends and events.

Figure 11.12 The profile page
<p><img src="https://github.com/KelleClark/database_project/blob/main/profile.PNG"></p>

When the continue to Clik button is pressed before the other db is stopped and the new database is created, our page looks like this:

Figure 11.13 Mypage for Clik
<p><img src="https://github.com/KelleClark/database_project/blob/main/docs/images/continue_to_clik_before_new_db.PNG"></p>


After the new database is started on the desktop and the neo4j browser is opened for the server to connect, the div on the right side will contain the user’s friends and events using the initial cypher query. The py2neo connection does use a http:127.0.0.1:7474 url for the graph object, while the neovis connection uses a bolt:127.0.0.1:7687 url.  Within the settings file of each db are options for using different ports and protocols...but making it work seamlessly was beyond the time frame and ability currently. 
Figure 11.14  Mypage for Clik when the Friend and Event database is available

<p><img src="https://github.com/KelleClark/database_project/blob/main/docs/images/continue_to_clik_after_new_db.PNG"></p>

The Nodes and relationships represented in the small clik network of users have similar schema and are best viewed using the Neo4j browser (neo4j@bolt://localhost:7687) 
Figure 11.15  The schema for a Person node and for an Event Node










The fact that information is kept in a graphical database allows many queries to be performed with only a few lines of ciphertext and we do not need joins which makes queries faster.


Figure 11.16 The relationships between Nodes and Events 


From Neo4j, we see that the email for a Person and the node id can both be used as a primary key...the choice of the primary key being the email is based on the context of many use cases.  A user would not find it convenient to rely on knowing what a friend’s node id is that is assigned to them by neo4j, id(n) where n is the friends’ node in the graphical database.  Using an email to perform tasks such as add a friend is more appropriate in this use case. In the use case where we would like to return all friends of a user, we know the user’s email address from their session key value. Using a cypher query with the match on email address and has a ‘friendsWith” relationship allows the system to generate a view of all friends of the user. This is also the case when a user would like to view all events they have posted with the relationship “postedEvent” replacing “friendsWith.”

Section 11.3 The View and The Controller
We have seen that the flask framework allows the client (and browser) to request different views for the user like the html pages with css/bootstrap/js/jquery in the templates folder of the application: login page, the create account page, the profile page, and mypage. These requests are controlled using @app.route methods of our flask application within app.py.

The needed libraries for the pages of the application are utilized by the inclusion of scripts and links to url within content delivery networks with as much of this header information included in a _layout.html file and use jinja to extend this file.  



<!-- USAGE EXAMPLES -->
## Usage


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/KelleClark/database_project) for a list of proposed features (and known issues).


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@KClarkcode](https://twitter.com/KClarkcode) - clarkke20@students.ecu.edu

Project Link: [https://github.com/KelleClark/database_project](https://github.com/KelleClark/database_project)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Kelle Clark]()
* [Greg Sutton]()






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/KelleClark/repo.svg?style=for-the-badge
[contributors-url]: https://github.com/KelleClark/repo/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/KelleClark/repo.svg?style=for-the-badge
[forks-url]: https://github.com/KelleClark/repo/network/members
[stars-shield]: https://img.shields.io/github/stars/KelleClark/repo.svg?style=for-the-badge
[stars-url]: https://github.com/KelleClark/repo/stargazers
[issues-shield]: https://img.shields.io/github/issues/KelleClark/repo.svg?style=for-the-badge
[issues-url]: https://github.com/KelleClark/repo/issues
[license-shield]: https://img.shields.io/github/license/KelleClark/repo.svg?style=for-the-badge
[license-url]: https://github.com/KelleClark/repo/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/KelleClark


# database_project

For a brief explaination of how to get started, this is a rough video ...sorry!
https://wingate.zoom.us/rec/share/DSFAuqfNJckwVreyvfcqalaKfNCyOzWufcYBOpg5rrPC96WmReDuDPt4cus67QA.lLP6hGVVIlivFTwf
