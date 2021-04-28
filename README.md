

The Package for Click can be found at KelleClark/database_project (github.com) . One way to run the system locally on your computer:

	1. You will need to have the following on your computer:
Python 
PyCharm 2019 or later 
Neo4j Desktop v.4 or later
Git

Note where you store Python and Git within your File System, you will need to set the location of the .exe files when setting up your project.

2. Open PyCharm and select NewProjec Figure 11.1t:
choose a location for your new project on your computer
set the location of your Python Interpreter: New Virtual Environment to your Python.exe
create 
Figure 11.1 Set up new project


3. Under Files/Settings/Version Control select Git and fill in the location on your computer of your Git.exe file, see Figure 11.2

Figure 11.2 Set up the Git for the project


4. In the top navigation bar, select the Version Control System VCS and choose Git. From the Github address above, grab the url to clone the repository and paste in the url of the git repository.  It is a good idea to use the Test button to see if Git is connected.
You should now be able to use the Git features like commit (green check) , commit/push (green up arrow) and pull (blue arrow) on the top right and to checkout and create branches on the bottom left as shown in Figure 11.3















Figure 11.3  The Git features in PyCharm



5. Now we need to make sure our python virtual environment that you set up in step 2 has all of the required packages and libraries.  Go to the python terminal on the bottom of the interface and use the cli $ (venv) somelocation > pip install -r requirements.txt, see Figure 11.4

Figure 11.4 To install required packages and libraries


Now minimize PyCharm for a second and open Neo4j Desktop.  

Within the Desktop, go to Project and create a New Project...and then add a Database.  Start the Database and Open the Neo4j Browser.  Connect to the database by using the cli cypher statement on the command line at the top of the Neo4j Browser enter  $ :server connect
Open the DB menu from the left and add find :user server add.  Add yourself as a user, for me my username is kelle and password is 111. We will need that in our database set up.  

Minimize Neo4j Desktop and Neo4j Browser.  Open PyCharm back up and set the Configuration near the top in the navigation bar. Then name the configuration...I named mine app and set the location to the file you want to run the application...app.py.  As in Figure 11.5, make sure you have the path of the Python venv set to the one for your project… and apply.   

Figure 11.5  Set up the PyCharm configuration to run the ClickApp











Before we run the system, find the file for our configuration of the graph databases as highlighted in Figure 11.6

Figure 11.6: Find the configuration file for Graph neo4j object 

Update your username and password that you just added to the Neo4j Database within your new project as shown in Figure 11.7.


Figure 11.7  : Make sure to change user and password to your information from your Neo4j Project Database
from py2neo import Graph


def db_auth():
   user = 'kelle'
   pword = '111'
   #graph = Graph("bolt://127.0.0.1:7687/db/data/", username=user, password=pword)
   graph = Graph("http://127.0.0.1:7474/db/data/", username=user, password=pword)
   return graph

 You should now be able to press the green “play” button and run the system or use the run button on the bottom. Errors will be shown in the run terminal at the bottom, but you should be able to open your web browser (Edge is good) and navigate to 127.0.0.1:5000, which is the default flask port.








Figure 11.8 The rendering of home/index.html rendered by @app.route(“/”) within the app.py file using flask



Section 11.2 The Model

We used two different graph databases, one to authenticate the user and issue a token so that a request to the server would not return information unless the token could be decoded and determined to be signed.  The other graph database is for the Person and Event node objects and the interestedIn and postedEvent relationships between two Persons or a Person and an Event.  

The schema for User, Figure 11.9, defined as a python class and used within the Graph object,  is  defined in the classes.py file of the Model directory. 




The email attribute of User will serve as the primary key (and is thus required).  The label for the node in the Graph associated with an instance of a User will be the name attribute.  When a user registers, their password is encrypted and stored within their user node.  This is the method used to ensure that the user’s information is only available to them during their session and could also be used to set views and permissions within the system.  If the system were to have used a token for a user, then a token would be generated with each login of the user, and would be encoded (not encrypted). The token is included with all requests to the server and checked to see if when decoded returns “signed.”  If signed, then the get request continues; otherwise, an error of invalid user is returned in the terminal.   We chose to use a dictionary data type and the idea of a session.  The user’s email is included in the session and if the user’s email is a key of the dictionary...then the system uses the values of the dictionary.

 
Figure 11.9     The User Model for session and authenticating login
 


The attributes name, email and password are input from a form that requires these fields to be filled in with type string, email and password on the client side using form control. A warning is issued to the user if the input is not valid.  There should be no user in the system with the same email.  The attributes created_on and last_logged in are not required and are not currently used.  

If the user clicks the sign up button, the system takes in the information and checks to see if the email input is already in the system and if not uses the create_user in account_services.py to add the user to the system.  Along with the passed in information, the user node also stores a hashed value of the password using the sha512_crypt function within the  passlib.handlers.sha2_crypt library. 


Figure 11.10  The register page



In the event that the email is already among the users, then a warning is flashed letting the user know that they must use a different set of values to create their account.  This check on the collection of nodes is done via a method of the User/Graph object user = User.match(graph, f"{email}")  and implements a cypher query of the graph database. 

If the user clicks the login button, then the system again performs a cypher query using the same method. If the user is found then the session is created for the user in that the email: information pair is added to the session dictionary.








Figure 11.11 The login page


The flask framework uses the provided route to browse to the user’s profile page.  On this page, the user can see the information that is stored in the user node for them. Future features would allow a user to update their profile information and to answer questions to help the system to recommend events and friends through Machine Learning algorithms.  For now, the user should select to continue to Clik. As a team, the current database that is being accessed through the py2neo driver needs to be stopped and then a new project/database started with the same credentials but that will be connected with the neovis driver to provide utility and visualize the graph database of friends and events.









Figure 11.12 The profile page








When the continue to Clik button is pressed before the other db is stopped and the new database is created, our page looks like this:

Figure 11.13 Mypage for Clik



After the new database is started on the desktop and the neo4j browser is opened for the server to connect, the div on the right side will contain the user’s friends and events using the initial cypher query. The py2neo connection does use a http:127.0.0.1:7474 url for the graph object, while the neovis connection uses a bolt:127.0.0.1:7687 url.  Within the settings file of each db are options for using different ports and protocols...but making it work seamlessly was beyond the time frame and ability currently. 
Figure 11.14  Mypage for Clik when the Friend and Event database is available

The Nodes and relationships represented in the small clik network of users have similar schema and are best viewed using the Neo4j browser (neo4j@bolt://localhost:7687) 
























Figure 11.15  The schema for a Person node and for an Event Node










The fact that information is kept in a graphical database allows many queries to be performed with only a few lines of ciphertext and we do not need joins which makes queries faster.


Figure 11.16 The relationships between Nodes and Events 


From Neo4j, we see that the email for a Person and the node id can both be used as a primary key...the choice of the primary key being the email is based on the context of many use cases.  A user would not find it convenient to rely on knowing what a friend’s node id is that is assigned to them by neo4j, id(n) where n is the friends’ node in the graphical database.  Using an email to perform tasks such as add a friend is more appropriate in this use case. In the use case where we would like to return all friends of a user, we know the user’s email address from their session key value. Using a cypher query with the match on email address and has a ‘friendsWith” relationship allows the system to generate a view of all friends of the user. This is also the case when a user would like to view all events they have posted with the relationship “postedEvent” replacing “friendsWith.”

Section 11.3 The View and The Controller
We have seen that the flask framework allows the client (and browser) to request different views for the user like the html pages with css/bootstrap/js/jquery in the templates folder of the application: login page, the create account page, the profile page, and mypage. These requests are controlled using @app.route methods of our flask application within app.py.

The needed libraries for the pages of the application are utilized by the inclusion of scripts and links to url within content delivery networks with as much of this header information included in a _layout.html file and use jinja to extend this file.  


# database_project

For a brief explaination of how to get started, this is a rough video ...sorry!
https://wingate.zoom.us/rec/share/DSFAuqfNJckwVreyvfcqalaKfNCyOzWufcYBOpg5rrPC96WmReDuDPt4cus67QA.lLP6hGVVIlivFTwf
