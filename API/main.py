#!/usr/bin/env python
from app import create_app

from datetime import datetime
from app.data.views.events import EventList, EventUpdate
from app.data.views.players import PlayerList, PlayerUpdate
from app.data.views.stats import StatsList, StatsUpdate
from app.data.views.matchstats import MatchStatsList
from app.data.views.teams import TeamList, TeamUpdate
from app.data.views.leagues import LeagueList, LeagueUpdate
from app.data.views.positions import PositionList, PositionUpdate
from app.data.views.teamleague import TeamLeagueLinkList
from app.data.views.tags import PlayerEvaluationList, PlayerEvaluationUpdate
# from app.data.views.transfers import TransferList, TransferUpdate
from app.data.views.matches import MatchList, MatchUpdate
from app.data.views.teamleague import TeamLeagueLink
from app.data.views.playerposition import PlayerPositionLink
from app.data.views.scouting import ScoutingList, ScoutingUpdate
from app.data.views.users import UserList, UserUpdate
from app.data.views.similar import SimilarList
from app.data.views.customstats import CustomStatsList
from app.data.views.charts import ChartsList
import flask

import sys, os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'venv/Lib/site-packages')))


from flask import render_template
from flask import request
app = create_app('config')
from flask_cors import CORS, cross_origin
CORS(app, resources={r"/*": {"origins": "http://www.elevenhacks.com*"}})
import re
from urllib.parse import urlparse

#Register jobmaker blueprint
# import jobmaker.jobmaker_blueprint as blueprint
# app.register_blueprint(blueprint.bp)

@app.after_request
def after_request(response):
    if request.referrer:
        ref = request.referrer.split('/')
        url = ref[0] + "//" + ref[2]
        response.headers['Access-Control-Allow-Origin'] = url
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        response.headers['Access-Control-Allow-Methods'] = 'GET, PUT, POST, DELETE, HEAD'
    return response

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"


# Scouting
@app.route('/scouting/customer/<int:team_id>/position/<string:position>', methods=['GET'])
def getCandidatesInfo(team_id, position):
    return ScoutingList.getCandidatesInfo(team_id, position)

@app.route('/scouting/candidate', methods=['POST'])
def postCandidate():
    return ScoutingList.postCandidate()


if __name__ == '__main__':
    app.run(host=app.config['HOST'],
            port=app.config['PORT'],
            debug=app.config['DEBUG'])
