from sqlite3 import Connection as SQLite3Connection
from datetime import datetime
from sqlalchemy import event
from sqlalchemy.engine import Engine
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# app
app = Flask(__name__)

# set up database configuration for our application
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sqlitedb.file" #local file with our data 
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = 0

# configure sqlite3 to enforce foreign key constraints

@event.listens_for(Engine, "connect")
def _set_sqlite_pragma(dbapi_connection, connection_record):
	if isinstance(dbapi_connection, SQLite3Connection):
		cursor = dbapi_connection.cursor()
		cursor.execute("PRAGMA foreign_keys=ON")
		cursor.close()

# create an instance of our database by passing in our app
db = SQLAlchemy(app)
now = datetime.now()


# Models/ tables for our api
# User table 
class User(db.Model):
	__tablename__ = "user"
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(50))
	email= db.Column(db.String(50))
	address = db.Column(db.String(200))
	phone = db.Column(db.String(50))
	posts = db.relationship("BlogPost", cascade="all, delete")

#  blogPost table 
class BlogPost(db.Model):
	__tablename__ = "blog_post"
	id = db.Column(db.Integer, primary_key = True)
	title = db.Column(db.String(50))
	body = db.Column(db.String(200))
	date = db.Column(db.Date)
	user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable = False) 


#Create routes for api
# create a new user
@app.route("/user", methods=["POST"])
def create_user():
	pass
	

# return all users in descending order
@app.route("/user/descending_id", methods=["GET"])
def get_all_users_descending():
	pass

# return all users in ascending order 
@app.route("/user/ascending_id", methods=["GET"])
def get_all_users_ascending():
	pass

# return specific user with gven id
@app.route("/user/<user_id>", methods=["GET"])
def get_one_user(user_id):
	pass

# delete a user
@app.route("/user/<user_id>", methods=["DELETE"])
def delete_user(user_id):
	pass

# create blog post for specific user id
@app.route("/blog_post/<user_id>", methods=["POST"])
def create_blog_post(user_id):
	pass

# get all posts by user 
@app.route("/blog_post/<user_id>", methods=["GET"])
def get_all_blog_posts(user_id):
	pass

# get one blog post
@app.route("/blog_posts/<blog_post_id>", methods=["GET"])
def get_one_blog_post(blog_post_id):
	pass

# delete blog post
@app.route("/blog_posts/<blog_post_id>", methods=["DELETE"])
def delete_blog_post(blog_post_id):
	pass

# if running  this file as our main application (running file directly)
if __name__ == "__main__":
	app.run(debug=True)

		



