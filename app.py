from flask import Flask, render_template, request, jsonify
import random
from pymongo import MongoClient
from bson.objectid import ObjectId
import json
from bson import BSON
from bson import json_util
app = Flask(__name__)

connection = MongoClient("ds029638.mongolab.com", 29638) 
db = connection["api"]
db.authenticate("alokedesai","domino")


def newlist(l):
	x = []
	for i in range(0, len(l)):
		x.append({"name" : l[i]["name"], "number" : l[i]["number"], "course" : l[i]["course"], "instructor" : l[i]["teacher"], "description" : l[i]["description"], "school" : l[i]["school"]})
		# x.append({"name" : list[i]["name"]})
	return x
@app.route('/')
def results():
	
	course_list = newlist(list(db.course_col.find( {"major" : "CSCI"})))
	

	return json.dumps(course_list, sort_keys=True, indent=4, default=json_util.default)

@app.route('/<major>/')
def major_res(major):
	 course_list  = newlist(list(db.course_col.find( {"major" : (major.encode("utf8", "ignore").upper())})))
	 return json.dumps(course_list, sort_keys=True, indent=4, default=json_util.default)

@app.route('/<major>/<int:course_num>')
def course_results(major, course_num):
	course_list  = newlist(list(db.course_col.find( {"major" : (major.encode("utf8", "ignore").upper()), "number" : (course_num) })))
	return json.dumps(course_list, sort_keys=True, indent=4, default=json_util.default)

if __name__ == '__main__':
    app.run(debug=True)