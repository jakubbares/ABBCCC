from flask import Blueprint, request, jsonify, make_response
from app.data.models import db, Event, Match, League, Player, Team, Position
from app.data.schemas import EventSchema, MatchSchema, LeagueSchema, PlayerSchema, TeamSchema, TransferSchema, PositionSchema
from marshmallow import ValidationError
import json
import pandas as pd

data = pd.read_csv('data', delimiter=',')

def decimal_default(obj):
    if isinstance(obj, Decimal):
        if Decimal(obj) % 1 == 0:
            return int(obj)
        elif Decimal(obj) % 1 != 0:
            return str(round(obj, 4))
    elif isinstance(obj, int):
        return int(obj)
    elif isinstance(obj, str):
        return str(obj)
    else:
        return str(obj)
    raise TypeError


class EventList(Resource):
    @staticmethod
    def getNewEvents(index):
        events_query = Event.query.filter(Event.team_id == team_id).all()
        results = schema.dump(events_query, many=True).data
        return json.dumps(results)

    @staticmethod
    def getPoints():
        events_query = Event.query.filter(Event.player_instatid == player_instatid).all()
        results = schema.dump(events_query, many=True).data
        return json.dumps(results)

    @staticmethod
    def getEventsForMatch(match_id):
        events_query = Event.query.filter(Event.match_id == match_id).all()
        results = schema.dump(events_query, many=True).data
        return json.dumps(results)

    @staticmethod
    def post():
        raw_dict = request.get_json(force=True)
        try:
                schema.validate(raw_dict)
                event_dict = raw_dict['data']['attributes']
                event = Event(event_dict['end'], event_dict['half'], event_dict['match_id'], event_dict['order_i'], event_dict['player_id'], event_dict['pos_x'], event_dict['pos_y'], event_dict['team_id'], event_dict['type'])
                event.add(event)
                query = Event.query.get(event.id)
                results = schema.dump(query).data
                return json.dumps(results), 201

        except ValidationError as err:
                resp = jsonify({"error": err.messages})
                resp.status_code = 403
                return resp

        except SQLAlchemyError as e:
                db.session.rollback()
                resp = jsonify({"error": str(e)})
                resp.status_code = 403
                return resp

class EventUpdate(Resource):
    @staticmethod
    def patch(id):
        event = Event.query.get_or_404(id)
        raw_dict = request.get_json(force=True)

        try:
            schema.validate(raw_dict)
            event_dict = raw_dict['data']['attributes']
            for key, value in event_dict.items():

                setattr(event, key, value)

            event.update()
            return event

        except ValidationError as err:
                resp = jsonify({"error": err.messages})
                resp.status_code = 401
                return resp

        except SQLAlchemyError as e:
                db.session.rollback()
                resp = jsonify({"error": str(e)})
                resp.status_code = 401
                return resp

    @staticmethod
    def delete(id):
        event = Event.query.get_or_404(id)
        try:
            delete = event.delete(event)
            response = make_response()
            response.status_code = 204
            return response
            
        except SQLAlchemyError as e:
                db.session.rollback()
                resp = jsonify({"error": str(e)})
                resp.status_code = 401
                return resp
        

# api.add_resource(EventList, '.json')
# api.add_resource(EventUpdate, '/<int:id>.json')