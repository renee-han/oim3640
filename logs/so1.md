# Session 1 (01/20/26) - [Course Introduction] 
 
## What I learned today 
[In today's session, I got a deep dive into this course and the expectations and operations surrounding our roles as students. I learned that this course isn’t about hard number crunching, but more so about building, collaboration, prototyping, and active trial and error. I also was happy to see heavy emphasis and hands-on work with AI technologies as these tools are just going to get increasingly powerful down the line and the only way that we can learn more about them is to learn how to dance and tussle with it.] 
 
## Code/work I'm proud of (optional) 
[N/A] 
 
## Challenges I faced 
[One challenge I faced was after class, I tried inputting my app idea and prompting Replit for the Python code, using the instructed prompt, ‘With Python’ after my one sentence description. However, it said that I needed to upgrade to the Autonomous Agent plan in order to convert the entire project idea. I then tweaked my prompting style and instead said, “Can I just see a snippet of the code?” which finally brought up an example snippet:  

import os from flask import Flask, request, jsonify from flask_sqlalchemy import SQLAlchemy from flask_cors import CORS from datetime import datetime from sqlalchemy import desc 

app = Flask(name) CORS(app) 

Database Configuration 

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False db = SQLAlchemy(app) 

Models 

class Club(db.Model): tablename = 'clubs' id = db.Column(db.Integer, primary_key=True) name = db.Column(db.String, nullable=False) description = db.Column(db.String, nullable=False) image_url = db.Column(db.String) admin_user_id = db.Column(db.String, db.ForeignKey('users.id'), nullable=False) created_at = db.Column(db.DateTime, default=datetime.utcnow) 

class Event(db.Model): tablename = 'events' id = db.Column(db.Integer, primary_key=True) club_id = db.Column(db.Integer, db.ForeignKey('clubs.id'), nullable=False) title = db.Column(db.String, nullable=False) description = db.Column(db.String, nullable=False) start_time = db.Column(db.DateTime, nullable=False) end_time = db.Column(db.DateTime, nullable=False) location = db.Column(db.String, nullable=False) capacity = db.Column(db.Integer) created_at = db.Column(db.DateTime, default=datetime.utcnow) 

API Routes 

@app.route('/api/events', methods=['GET']) def get_events(): events = db.session.query(Event, Club).join(Club).order_by(desc(Event.start_time)).all() return jsonify([{ 'id': e.id, 'clubId': e.club_id, 'title': e.title, 'description': e.description, 'startTime': e.start_time.isoformat(), 'endTime': e.end_time.isoformat(), 'location': e.location, 'capacity': e.capacity, 'club': { 'id': c.id, 'name': c.name, 'description': c.description } } for e, c in events])] 
 
## AI usage (if any) 
[I used Replit today to generate a mockup of my app idea and also attempted to prompt it with snippets of Python code I could potentially utilize if I ever wanted to pursue this idea.] 
 
## Questions for next time 
[How will mini projects operate and to what scale are these expected to be built out to?] 