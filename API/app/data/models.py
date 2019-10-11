from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError

db = SQLAlchemy()
Base = declarative_base()


class CRUD():
    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()

    def update(self):
        return db.session.commit()

    def update2(self, obj, id, attrs):
        db.session.query(obj).filter(obj.id == id).update(attrs)
        return db.session.commit()

    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()


class CalculatedPlayers(db.Model, CRUD):
    id = db.Column(db.Integer,  primary_key=True)
    instatid = db.Column(db.Integer)
    name = db.Column(db.String(255))
    nationality = db.Column(db.String(255))
    team = db.Column(db.String(255))
    team_id = db.Column(db.Integer)
    league = db.Column(db.String(255))
    league_id = db.Column(db.Integer)
    birthday = db.Column(db.String(255))

    def __init__(self, team_id, league_id, team, league, nationality, birthday, name, instatid):
        self.id = id
        self.instatid = instatid
        self.team_id = team_id
        self.league_id = league_id
        self.league = league
        self.team = team
        self.nationality = nationality
        self.birthday = birthday
        self.name = name

class TeamLeagueLink(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    league_id = db.Column(db.Integer, db.ForeignKey('league.id'))
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    league_instatid = db.Column(db.Integer)
    team_instatid = db.Column(db.Integer)
    season = db.Column(db.String,  primary_key=True)
    matches = db.Column(db.Integer)
    wins = db.Column(db.Integer)
    draws = db.Column(db.Integer)
    losses = db.Column(db.Integer)
    goals = db.Column(db.Integer)
    points = db.Column(db.Integer)

    def __init__(self, team_id, league_id, team_instatid, league_instatid):
        self.id = team_id
        self.league_id = league_id
        self.team_instatid = team_instatid
        self.league_instatid = league_instatid


class League(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    instatid = db.Column(db.Integer)
    tier = db.Column(db.String(50))
    country_name = db.Column(db.String(50))
    name = db.Column(db.String(50))

    def __init__(self, country_name, name):
        self.country_name = country_name
        self.name = name


class User(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    creation_time = db.Column(db.Date, server_default=db.func.current_timestamp(), nullable=False)
    name = db.Column(db.String(100))
    role = db.Column(db.String(70))
    password = db.Column(db.String(70))
    email = db.Column(db.String(70))
    temporary_password = db.Column(db.Boolean)

    def __init__(self, name, role, password, email, temporary_password):
        self.name = name
        self.role = role
        self.password = password
        self.email = email
        self.temporary_password = temporary_password



class Team(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    instatid = db.Column(db.Integer)
    name = db.Column(db.String(50))
    # players = db.relationship("Player", back_populates="team")
    # events = db.relationship("Event", back_populates="team")
    # total_stats = db.relationship("TeamStatsTotal", uselist=False, back_populates="team")
    # leagues = db.relationship('League', secondary='team_league_link')
    # candidates = db.relationship("Player", secondary='candidate_customer_link')

    def __init__(self, name, instatid):
        self.name = name
        self.instatid = instatid


class Transfer(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    player_instatid = db.Column(db.Integer)
    # player = db.relationship("Player", back_populates="transfers")
    fee = db.Column(db.Integer)
    position_id = db.Column(db.Integer, db.ForeignKey('position.id'))
    value = db.Column(db.Integer)
    currency = db.Column(db.String(20))
    team_from_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    team_to_id = db.Column(db.Integer, db.ForeignKey('team.id'))

    def __init__(self, player_id, fee, position, value, currency, team_from_id, team_to_id):
        self.player_id = player_id
        self.fee = fee
        self.position = position
        self.value = value
        self.currency = currency
        self.team_from_id = team_from_id
        self.team_to_id = team_to_id


class PlayerPositionLink(db.Model, CRUD):
    id = db.Column(db.Integer, db.ForeignKey('player.id'), primary_key=True)
    position_id = db.Column(db.Integer, db.ForeignKey('position.id'), primary_key=True)
    starts = db.Column(db.Integer)
    # player = db.relationship("Player", back_populates="player_assoc")
    # position = db.relationship("Position", back_populates="position_assoc")

    def __init__(self, player_id, position_id, starts):
        self.id = player_id
        self.position_id = position_id
        self.starts = starts


class Player(db.Model, CRUD):
    id = db.Column(db.Integer)
    instatid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    contract = db.Column(db.String(100))
    nationality = db.Column(db.String(50))
    team_instatid = db.Column(db.Integer)
    birthday = db.Column(db.String(255))
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    left_foot = db.Column(db.Integer)
    right_foot = db.Column(db.Integer)
    creation_time = db.Column(db.Date, server_default=db.func.current_timestamp(), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    contract_tm = db.Column(db.String)
    team_member_since_tm = db.Column(db.String)
    market_value_tm = db.Column(db.Float)
    name_tm = db.Column(db.String)
    player_number_tm = db.Column(db.Integer)
    birthday_tm = db.Column(db.String)
    url_tm = db.Column(db.String)
    nationality_tm = db.Column(db.String)
    height_tm = db.Column(db.Integer)
    foot_tm = db.Column(db.String)
    position_tm = db.Column(db.String)
    creation_time_tm = db.Column(db.Date)


    def __init__(self, name, instatid, contract, nationality, team_id, birthday, height, weight, left_foot, right_foot):
        self.instatid = instatid
        self.name = name
        self.contract = contract
        self.nationality = nationality
        self.team_id = team_id
        self.height = height
        self.weight = weight
        self.birthday = birthday
        self.left_foot = left_foot
        self.right_foot = right_foot



class Position(db.Model, CRUD):
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(50))
    # players = db.relationship("Player", secondary='player_position_link')

    def __init__(self, name, shortcut):
        self.name = name
        self.shortcut = shortcut


class Match(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    instatid = db.Column(db.Integer)
    league_id = db.Column(db.Integer, db.ForeignKey('league.id'))
    league_instatid = db.Column(db.Integer)
    league = db.Column(db.String)
    country = db.Column(db.String)
    # league = db.relationship("League", back_populates="matches")
    home_team_instatid = db.Column(db.Integer)
    guest_team_instatid = db.Column(db.Integer)
    home_team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    guest_team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    home_team = db.Column(db.String)
    guest_team = db.Column(db.String)
    season = db.Column(db.String)
    match_date = db.Column(db.String)

    match_result = db.Column(db.String)
    # match_team_stats = db.relationship("MatchTeamStats", back_populates="match")
    # match_player_stats = db.relationship("MatchPlayerStats", back_populates="match")
    # events = db.relationship("Event", back_populates="match")

    def __init__(self, league_id, instatid, season, team_home_id, team_guest_id, match_date):
        self.league_id = league_id
        self.instatid = instatid
        self.season = season
        self.team_home_id = team_home_id
        self.team_guest_id = team_guest_id
        self.match_date = match_date


class Event(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    instatid = db.Column(db.Integer)
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'))
    match_instatid = db.Column(db.Integer)
    # match = db.relationship("Match", back_populates="events")
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    player_instatid = db.Column(db.Integer)
    player_name = db.Column(db.String(300))
    # player = db.relationship("Player", back_populates="events")
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    team_instatid = db.Column(db.Integer)
    # team = db.relationship("Team", backref=db.backref("events"))
    end = db.Column(db.Float)
    half = db.Column(db.Integer)
    pos_x = db.Column(db.Float)
    pos_y = db.Column(db.Float)
    type = db.Column(db.String(300))
    creation_time = db.Column(db.Date, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, instatid, player_instatid, match_instatid, team_instatid, end, half, match_id, order_i, player_id, pos_x, pos_y, team_id, type):
        self.end = end
        self.instatid = instatid
        self.half = half
        self.order_i = order_i
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.player_id = player_id
        self.player_instatid = player_instatid
        self.match_id = match_id
        self.match_instatid = match_instatid
        self.team_id = team_id
        self.team_instatid = team_instatid
        self.type = type



class PlayerEvaluation(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    creation_time = db.Column(db.Date, server_default=db.func.current_timestamp(), nullable=False)
    tag = db.Column(db.String(50))
    kind = db.Column(db.String(50))
    comment = db.Column(db.String(2000))
    score = db.Column(db.Integer)

    def __init__(self, player_id, user_id, tag, kind, score, comment, edit):
        self.player_id = player_id
        self.user_id = user_id
        self.tag = tag
        self.kind = kind
        self.score = score
        self.comment = comment
        self.edit = edit

class CandidateCustomerLink(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    customer_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    position = db.Column(db.String(10))
    contract_value_min = db.Column(db.Integer())
    contract_value_max = db.Column(db.Integer())

    def __init__(self, customer_id, player_id, position):
        self.customer_id = customer_id
        self.player_id = player_id
        self.position = position

class Task(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    position = db.Column(db.String(10))
    assigned_to_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, customer_id, position, user_id):
        self.customer_id = customer_id
        self.position = position
        self.assigned_to_id = user_id


class ExpectedGoals(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    pos_x = db.Column(db.Integer)
    pos_y = db.Column(db.Integer)
    position_id = db.Column(db.Integer, db.ForeignKey('position.id'))
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    league_id = db.Column(db.Integer, db.ForeignKey('league.id'))
    season = db.Column(db.Integer)
    total_shots = db.Column(db.Integer)
    total_goals = db.Column(db.Integer)
    creation_time = db.Column(db.Date, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, pos_x, pos_y, season, position_id, team_id, league_id, total_shots, total_goals):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.season = season
        self.position_id = position_id
        self.team_id = team_id
        self.league_id = league_id
        self.total_goals = total_goals
        self.total_shots = total_shots

class PlayerStatsCalculatedAcross(db.Model, CRUD):
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), primary_key=True)
    player_instatid = db.Column(db.Integer)
    # player = db.relationship("Player", back_populates="calc_stats")
    goals = db.Column(db.Float)
    assists = db.Column(db.Float)
    yellow_cards = db.Column(db.Float)
    red_cards = db.Column(db.Float)
    total_actions = db.Column(db.Float)
    successful_total_actions = db.Column(db.Float)
    shots = db.Column(db.Float)
    successful_shots = db.Column(db.Float)
    passes = db.Column(db.Float)
    successful_passes = db.Column(db.Float)
    key_passes = db.Column(db.Float)
    successful_key_passes = db.Column(db.Float)
    crosses = db.Column(db.Float)
    successful_crosses = db.Column(db.Float)
    challenges = db.Column(db.Float)
    successful_challenges = db.Column(db.Float)
    air_challenges = db.Column(db.Float)
    successful_air_challenges = db.Column(db.Float)
    dribbles = db.Column(db.Float)
    successful_dribbles = db.Column(db.Float)
    tackles = db.Column(db.Float)
    successful_tackles = db.Column(db.Float)
    lost_balls = db.Column(db.Float)
    received_balls = db.Column(db.Float)
    fouls = db.Column(db.Float)
    player_fouls = db.Column(db.Float)

class PlayerStatsCalculated(db.Model, CRUD):
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), primary_key=True)
    player_instatid = db.Column(db.Integer)
    league_id = db.Column(db.Integer, db.ForeignKey('league.id'), primary_key=True)
    # player = db.relationship("Player", back_populates="calc_stats")
    goals = db.Column(db.Float)
    assists = db.Column(db.Float)
    yellow_cards = db.Column(db.Float)
    red_cards = db.Column(db.Float)
    total_actions = db.Column(db.Float)
    successful_total_actions = db.Column(db.Float)
    shots = db.Column(db.Float)
    successful_shots = db.Column(db.Float)
    passes = db.Column(db.Float)
    successful_passes = db.Column(db.Float)
    key_passes = db.Column(db.Float)
    successful_key_passes = db.Column(db.Float)
    crosses = db.Column(db.Float)
    successful_crosses = db.Column(db.Float)
    challenges = db.Column(db.Float)
    successful_challenges = db.Column(db.Float)
    air_challenges = db.Column(db.Float)
    successful_air_challenges = db.Column(db.Float)
    dribbles = db.Column(db.Float)
    successful_dribbles = db.Column(db.Float)
    tackles = db.Column(db.Float)
    successful_tackles = db.Column(db.Float)
    lost_balls = db.Column(db.Float)
    received_balls = db.Column(db.Float)
    fouls = db.Column(db.Float)
    player_fouls = db.Column(db.Float)

#     def __init__(self, player_id):
#         self.player_id = player_id
#
#

class LeagueStatsCalculated(db.Model, CRUD):
    league_id = db.Column(db.Integer, db.ForeignKey('league.id'), primary_key=True)
    goals = db.Column(db.Integer)
    assists = db.Column(db.Integer)
    yellow_cards = db.Column(db.Integer)
    red_cards = db.Column(db.Integer)
    total_actions = db.Column(db.Integer)
    successful_total_actions = db.Column(db.Integer)
    shots = db.Column(db.Integer)
    successful_shots = db.Column(db.Integer)
    passes = db.Column(db.Integer)
    successful_passes = db.Column(db.Integer)
    key_passes = db.Column(db.Integer)
    successful_key_passes = db.Column(db.Integer)
    crosses = db.Column(db.Integer)
    successful_crosses = db.Column(db.Integer)
    challenges = db.Column(db.Integer)
    successful_challenges = db.Column(db.Integer)
    air_challenges = db.Column(db.Integer)
    successful_air_challenges = db.Column(db.Integer)
    dribbles = db.Column(db.Integer)
    successful_dribbles = db.Column(db.Integer)
    tackles = db.Column(db.Integer)
    successful_tackles = db.Column(db.Integer)
    lost_balls = db.Column(db.Integer)
    received_balls = db.Column(db.Integer)
    fouls = db.Column(db.Integer)
    player_fouls = db.Column(db.Integer)

class PlayerStatsTotalAcross(db.Model, CRUD):
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), primary_key=True)
    player_instatid = db.Column(db.Integer)
    # player = db.relationship("Player", back_populates="total_stats")
    minutes = db.Column(db.Integer)
    # minutes_per_90 = db.Column(db.Float)
    goals = db.Column(db.Integer)
    assists = db.Column(db.Integer)
    yellow_cards = db.Column(db.Integer)
    red_cards = db.Column(db.Integer)
    total_actions = db.Column(db.Integer)
    successful_total_actions = db.Column(db.Integer)
    shots = db.Column(db.Integer)
    successful_shots = db.Column(db.Integer)
    passes = db.Column(db.Integer)
    successful_passes = db.Column(db.Integer)
    key_passes = db.Column(db.Integer)
    successful_key_passes = db.Column(db.Integer)
    crosses = db.Column(db.Integer)
    successful_crosses = db.Column(db.Integer)
    challenges = db.Column(db.Integer)
    successful_challenges = db.Column(db.Integer)
    air_challenges = db.Column(db.Integer)
    successful_air_challenges = db.Column(db.Integer)
    dribbles = db.Column(db.Integer)
    successful_dribbles = db.Column(db.Integer)
    tackles = db.Column(db.Integer)
    successful_tackles = db.Column(db.Integer)
    lost_balls = db.Column(db.Integer)
    received_balls = db.Column(db.Integer)
    fouls = db.Column(db.Integer)
    player_fouls = db.Column(db.Integer)

class PlayerStatsTotal(db.Model, CRUD):
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'), primary_key=True)
    player_instatid = db.Column(db.Integer)
    league_id = db.Column(db.Integer, db.ForeignKey('league.id'), primary_key=True)
    # player = db.relationship("Player", back_populates="total_stats")
    minutes = db.Column(db.Integer)
    # minutes_per_90 = db.Column(db.Float)
    goals = db.Column(db.Integer)
    assists = db.Column(db.Integer)
    yellow_cards = db.Column(db.Integer)
    red_cards = db.Column(db.Integer)
    total_actions = db.Column(db.Integer)
    successful_total_actions = db.Column(db.Integer)
    shots = db.Column(db.Integer)
    successful_shots = db.Column(db.Integer)
    passes = db.Column(db.Integer)
    successful_passes = db.Column(db.Integer)
    key_passes = db.Column(db.Integer)
    successful_key_passes = db.Column(db.Integer)
    crosses = db.Column(db.Integer)
    successful_crosses = db.Column(db.Integer)
    challenges = db.Column(db.Integer)
    successful_challenges = db.Column(db.Integer)
    air_challenges = db.Column(db.Integer)
    successful_air_challenges = db.Column(db.Integer)
    dribbles = db.Column(db.Integer)
    successful_dribbles = db.Column(db.Integer)
    tackles = db.Column(db.Integer)
    successful_tackles = db.Column(db.Integer)
    lost_balls = db.Column(db.Integer)
    received_balls = db.Column(db.Integer)
    fouls = db.Column(db.Integer)
    player_fouls = db.Column(db.Integer)

    # ran_distance_x = db.Column(db.Float)
    # ran_distance_y = db.Column(db.Float)
    # non_penalty_total_goals = db.Column(db.Integer)
    # shots = db.Column(db.Integer)
    # box_shots = db.Column(db.Integer)
    # outside_penalty_box_shots = db.Column(db.Integer)
    # touches_in_box = db.Column(db.Integer)
    # key_passes = db.Column(db.Integer)
    # throughballs = db.Column(db.Integer)
    # lost_balls = db.Column(db.Integer)
    # passes = db.Column(db.Integer)
    # gain = db.Column(db.Integer)
    # passes_to_the_box = db.Column(db.Integer)
    # danger_zone_entries = db.Column(db.Integer)
    # long_balls_attempted = db.Column(db.Integer)
    # long_balls_made = db.Column(db.Integer)
    # crosses_attempted = db.Column(db.Integer)
    # crosses_made = db.Column(db.Integer)
    # dribbles_attempted = db.Column(db.Integer)
    # dribbles_made = db.Column(db.Integer)
    # space_defending = db.Column(db.Integer)
    # tackles_attempted = db.Column(db.Integer)
    # tackles_made = db.Column(db.Integer)
    # padj_tackles = db.Column(db.Integer)
    # interceptions = db.Column(db.Integer)
    # padj_interceptions = db.Column(db.Integer)
    # won_balls = db.Column(db.Integer)
    # won_balls_on_opposition_half = db.Column(db.Integer)
    # challenges_attempted = db.Column(db.Integer)
    # challenges_made = db.Column(db.Integer)
    # long_balls_received = db.Column(db.Integer)
    # touches_on_opposition_half = db.Column(db.Integer)
    # touches_on_own_half = db.Column(db.Integer)
    # second_balls_picked = db.Column(db.Integer)
    # creation_time = db.Column(db.Date, server_default=db.func.current_timestamp(), nullable=False)
    def __init__(self, player_id):
        self.player_id = player_id


class MatchTeamStatsTotal(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'))
    match_instatid = db.Column(db.Integer)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    team_instatid = db.Column(db.Integer)
    creation_time = db.Column(db.Date, server_default=db.func.current_timestamp(), nullable=False)
    goals = db.Column(db.Integer)
    assists = db.Column(db.Integer)
    yellow_cards = db.Column(db.Integer)
    red_cards = db.Column(db.Integer)
    total_actions = db.Column(db.Integer)
    successful_total_actions = db.Column(db.Integer)
    shots = db.Column(db.Integer)
    successful_shots = db.Column(db.Integer)
    passes = db.Column(db.Integer)
    successful_passes = db.Column(db.Integer)
    key_passes = db.Column(db.Integer)
    successful_key_passes = db.Column(db.Integer)
    crosses = db.Column(db.Integer)
    successful_crosses = db.Column(db.Integer)
    challenges = db.Column(db.Integer)
    successful_challenges = db.Column(db.Integer)
    air_challenges = db.Column(db.Integer)
    successful_air_challenges = db.Column(db.Integer)
    dribbles = db.Column(db.Integer)
    successful_dribbles = db.Column(db.Integer)
    tackles = db.Column(db.Integer)
    successful_tackles = db.Column(db.Integer)
    lost_balls = db.Column(db.Integer)
    received_balls = db.Column(db.Integer)
    fouls = db.Column(db.Integer)

    def __init__(self, match_id, team_id):
        self.match_id = match_id
        self.team_id = team_id

class MatchPlayerStatsTotal(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    match_id = db.Column(db.Integer, db.ForeignKey('match.id'))
    match_instatid = db.Column(db.Integer)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    player_instatid = db.Column(db.Integer)
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'))
    team_instatid = db.Column(db.Integer)
    creation_time = db.Column(db.Date, server_default=db.func.current_timestamp(), nullable=False)
    position = db.Column(db.String)
    minutes = db.Column(db.Integer)
    goals = db.Column(db.Integer)
    assists = db.Column(db.Integer)
    yellow_cards = db.Column(db.Integer)
    red_cards = db.Column(db.Integer)
    total_actions = db.Column(db.Integer)
    successful_total_actions = db.Column(db.Integer)
    shots = db.Column(db.Integer)
    successful_shots = db.Column(db.Integer)
    passes = db.Column(db.Integer)
    successful_passes = db.Column(db.Integer)
    key_passes = db.Column(db.Integer)
    successful_key_passes = db.Column(db.Integer)
    crosses = db.Column(db.Integer)
    successful_crosses = db.Column(db.Integer)
    challenges = db.Column(db.Integer)
    successful_challenges = db.Column(db.Integer)
    air_challenges = db.Column(db.Integer)
    successful_air_challenges = db.Column(db.Integer)
    dribbles = db.Column(db.Integer)
    successful_dribbles = db.Column(db.Integer)
    tackles = db.Column(db.Integer)
    successful_tackles = db.Column(db.Integer)
    lost_balls = db.Column(db.Integer)
    received_balls = db.Column(db.Integer)
    fouls = db.Column(db.Integer)
    player_fouls = db.Column(db.Integer)

    def __init__(self, match_id, player_id):
        self.match_id = match_id
        self.player_id = player_id


class XMLModelsMatchPlayer(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    match_instatid = db.Column(db.Integer, db.ForeignKey('match.instatid'))
    player_instatid = db.Column(db.Integer, db.ForeignKey('player.instatid'))
    player_id = db.Column(db.Integer)
    match_id = db.Column(db.Integer)
    team_instatid = db.Column(db.Integer, db.ForeignKey('team.instatid'))
    team_id = db.Column(db.Integer)
    first_event_time = db.Column(db.Float)
    last_event_time = db.Column(db.Float)
    minutes = db.Column(db.Integer)
    match_date = db.Column(db.Date)
    season = db.Column(db.String)
    creation_time = db.Column(db.Date, server_default=db.func.current_timestamp(), nullable=False)
    goals = db.Column(db.Integer)
    average_x = db.Column(db.Float)
    average_y = db.Column(db.Float)
    shots_p90 = db.Column(db.Float)
    box_shots_p90 = db.Column(db.Float)
    outside_penalty_box_shots_p90 = db.Column(db.Float)
    scoring_contribution_p90 = db.Column(db.Float)
    percentage_of_own_created_shots = db.Column(db.Float)
    scoring_percentage = db.Column(db.Float)
    touches_in_box = db.Column(db.Float)
    assists_p90 = db.Column(db.Float)
    key_passes_acc_p90 = db.Column(db.Float)
    throughballs_p90 = db.Column(db.Float)
    lost_balls_p90 = db.Column(db.Float)
    passes_p90 = db.Column(db.Float)
    passes_completion = db.Column(db.Float)
    passes_to_the_box = db.Column(db.Float)
    danger_zone_entries_p90 = db.Column(db.Float)
    long_balls_p90 = db.Column(db.Float)
    long_balls_completion = db.Column(db.Float)
    crosses_successful_p90 = db.Column(db.Float)
    crosses_completion = db.Column(db.Float)
    dribbles_successful_p90 = db.Column(db.Float)
    dribbles_completion = db.Column(db.Float)
    average_space_defending_p90 = db.Column(db.Float)
    successful_tackles_p90 = db.Column(db.Float)
    tackles_completion = db.Column(db.Float)
    interceptions_p90 = db.Column(db.Float)
    padj_tackles_p90 = db.Column(db.Float)
    padj_interceptions_p90 = db.Column(db.Float)
    won_balls_p90 = db.Column(db.Float)
    won_balls_on_opposition_half_p90 = db.Column(db.Float)
    challenges_p90 = db.Column(db.Float)
    challenges_success_rate = db.Column(db.Float)
    air_challenges_success_rate = db.Column(db.Float)
    air_challenges_p90 = db.Column(db.Float)
    own_created_shots_p90 = db.Column(db.Float)
    accurate_passes_p90 = db.Column(db.Float)
    crosses_p90 = db.Column(db.Float)
    dribbles_p90 = db.Column(db.Float)
    tackles_p90 = db.Column(db.Float)
    won_challenges_p90 = db.Column(db.Float)
    won_air_challenges_p90 = db.Column(db.Float)
    opp_half_touches = db.Column(db.Float)
    opp_half_touches_ratio = db.Column(db.Float)
    non_penalty_goals = db.Column(db.Float)
    long_balls_successful_p90 = db.Column(db.Float)
    long_balls_received_p90 = db.Column(db.Float)
    conversion_rate = db.Column(db.Float)
    picking_up_second_balls_p90 = db.Column(db.Integer)
    position = db.Column(db.String)
    xG = db.Column(db.Float)
    xG_assist = db.Column(db.Float)
    np_xG = db.Column(db.Float)
    np_xG_assist = db.Column(db.Float)

    def __init__(self):
        pass


class XMLModelsMatchTeam(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    match_instatid = db.Column(db.Integer, db.ForeignKey('match.instatid'))
    team_instatid = db.Column(db.Integer, db.ForeignKey('team.instatid'))
    league_instatid = db.Column(db.Integer, db.ForeignKey('league.instatid'))
    season = db.Column(db.String)
    creation_time = db.Column(db.Date, server_default=db.func.current_timestamp(), nullable=False)
    match_date = db.Column(db.Date)
    minutes = db.Column(db.Float)
    points = db.Column(db.Integer)
    xPoints = db.Column(db.Integer)
    xPoints_ours = db.Column(db.Integer)
    goals_for = db.Column(db.Integer)
    goals_against = db.Column(db.Integer)
    xG_for_p90 = db.Column(db.Float)
    xG_against_p90 = db.Column(db.Float)
    shots_for_p90 = db.Column(db.Float)
    shots_against_p90 = db.Column(db.Float)
    shots_for = db.Column(db.Integer)
    shots_against = db.Column(db.Integer)
    shots_on_target = db.Column(db.Integer)
    shots_on_target_againts = db.Column(db.Integer)
    headed_shots = db.Column(db.Integer)
    dangerzone_shots_p90 = db.Column(db.Float)
    dangerzone_shots = db.Column(db.Float)
    dangerzone_shots_against_p90 = db.Column(db.Float)
    xG_per_shot = db.Column(db.Float)
    xG_per_shot_against = db.Column(db.Float)
    average_distance_of_shots = db.Column(db.Float)
    average_distance_of_shots_against = db.Column(db.Float)
    passes_p90 = db.Column(db.Float)
    passes_succes_rate = db.Column(db.Float)
    forward_passes = db.Column(db.Float)
    backward_passes = db.Column(db.Float)
    total_passes_into_the_box_p90 = db.Column(db.Float)
    total_passes_into_the_box = db.Column(db.Float)
    acc_passes_into_the_box_p90 = db.Column(db.Float)
    acc_passes_into_the_box = db.Column(db.Float)
    passes_to_the_box_against_p90 = db.Column(db.Float)
    dangerzone_entries_p90 = db.Column(db.Float)
    dangerzone_entries = db.Column(db.Float)
    crosses_p90 = db.Column(db.Float)
    shots_from_crosses = db.Column(db.Float)
    avg_number_of_passes_before_shot = db.Column(db.Float)
    passes_in_buildup = db.Column(db.Float)
    passes_in_middle_third = db.Column(db.Float)
    passes_in_final_third = db.Column(db.Float)
    long_balls = db.Column(db.Float)
    lost_balls = db.Column(db.Float)
    touches_inside_box = db.Column(db.Float)
    touches_inside_box_p90 = db.Column(db.Float)
    events_inside_box = db.Column(db.Float)
    buildup = db.Column(db.Float)
    maintenance = db.Column(db.Float)
    counter_attacking = db.Column(db.Float)
    sustainable_threat = db.Column(db.Float)
    fast_tempo = db.Column(db.Float)
    high_press = db.Column(db.Float)
    tts_for = db.Column(db.Float)
    tts_against = db.Column(db.Float)
    tts_difference = db.Column(db.Float)
    tts_tackle = db.Column(db.Float)
    tts_interception = db.Column(db.Float)
    tts_turnover = db.Column(db.Float)
    won_balls_opp_half = db.Column(db.Float)
    won_balls_final_third = db.Column(db.Float)
    won_balls_middle_third = db.Column(db.Float)
    won_balls_own_third = db.Column(db.Float)
    avg_height_of_turnover = db.Column(db.Float)
    tackles_total = db.Column(db.Float)
    tackles_success_rate = db.Column(db.Float)
    headers_total = db.Column(db.Float)
    headers_success_rate = db.Column(db.Float)
    challenges_total = db.Column(db.Float)
    challenges_success_rate = db.Column(db.Float)
    tackles_padj = db.Column(db.Float)
    interceptions = db.Column(db.Float)
    interceptions_padj = db.Column(db.Float)

    def __init__(self):
        pass

class XMLModelsSeasonPlayerAgg(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)    
    league_name = db.Column(db.String)
    league_country = db.Column(db.String)
    league_tier = db.Column(db.Integer)
    league_instatid = db.Column(db.Integer, db.ForeignKey('league.instatid'))    
    player_instatid = db.Column(db.Integer, db.ForeignKey('player.instatid'))
    team_instatid = db.Column(db.Integer)
    team_name = db.Column(db.String)
    player_name = db.Column(db.String)
    nationality = db.Column(db.String)
    birthday = db.Column(db.Date)
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    left_foot = db.Column(db.Integer)
    right_foot = db.Column(db.Integer)   
    season = db.Column(db.String)
    league_id = db.Column(db.Integer)
    team_id = db.Column(db.Integer)
    player_id = db.Column(db.Integer)
    instat_creation_time = db.Column(db.Date)
    transfermarkt_creation_time = db.Column(db.Date)
    instat_contract = db.Column(db.String)
    transfermarkt_contract = db.Column(db.String)
    market_value_tm = db.Column(db.Float)   
    matches_count = db.Column(db.Integer)
    average_minutes = db.Column(db.Float)
    minutes = db.Column(db.Float)
    xG_minutes = db.Column(db.Float)
    padj_tackles_minutes = db.Column(db.Float)
    padj_interceptions_minutes = db.Column(db.Float)
    primary_position = db.Column(db.String)
    secondary_position = db.Column(db.String)
    primary_position_percentage = db.Column(db.Float)
    secondary_position_percentage = db.Column(db.Float)
    total_goals = db.Column(db.Integer)
    average_x = db.Column(db.Float)
    average_y = db.Column(db.Float)
    shots_p90 = db.Column(db.Float)
    box_shots_p90 = db.Column(db.Float)
    outside_box_shots_p90 = db.Column(db.Float)
    scoring_contribution_p90 = db.Column(db.Float)
    percentage_of_own_created_shots = db.Column(db.Float)
    scoring_percentage = db.Column(db.Float)
    touches_in_box_p90 = db.Column(db.Float)
    assists_p90 = db.Column(db.Float)
    key_passes_acc_p90 = db.Column(db.Float)
    throughballs_p90 = db.Column(db.Float)
    lost_balls_p90 = db.Column(db.Float)
    passes_p90 = db.Column(db.Float)
    passes_completion = db.Column(db.Float)
    acc_passes_to_the_box_p90 = db.Column(db.Float)
    passes_to_the_box_p90 = db.Column(db.Float)
    danger_zone_entries_p90 = db.Column(db.Float)
    long_balls_p90 = db.Column(db.Float)
    long_balls_completion = db.Column(db.Float)
    crosses_succ_p90 = db.Column(db.Float)
    crosses_completion = db.Column(db.Float)
    dribbles_succ_p90 = db.Column(db.Float)
    dribbles_completion = db.Column(db.Float)
    space_defending_p90 = db.Column(db.Float)
    tackles_completion = db.Column(db.Float)
    padj_tackles_p90 = db.Column(db.Float)
    padj_interceptions_p90 = db.Column(db.Float)
    won_balls_p90 = db.Column(db.Float)
    won_balls_opp_half_p90 = db.Column(db.Float)
    challenges_p90 = db.Column(db.Float)
    challenges_succ_rate = db.Column(db.Float)
    challenges_succ_p90 = db.Column(db.Float)
    long_balls_received_p90 = db.Column(db.Float)
    air_challenges_succ_rate = db.Column(db.Float)
    air_challenges_p90 = db.Column(db.Float)
    air_challenges_succ_p90 = db.Column(db.Float)
    own_created_shots_p90 = db.Column(db.Float)
    acc_passes_p90 = db.Column(db.Float)
    crosses_p90 = db.Column(db.Float)
    dribbles_p90 = db.Column(db.Float)
    won_challenges_p90 = db.Column(db.Float)
    won_air_challenges_p90 = db.Column(db.Float)
    opp_half_touches = db.Column(db.Float)
    opp_half_touches_ratio = db.Column(db.Float)
    non_penalty_goals = db.Column(db.Float)
    long_balls_succ_p90 = db.Column(db.Float)
    conversion_rate = db.Column(db.Float)
    picking_up_second_balls_p90 = db.Column(db.Float)
    xG = db.Column(db.Float)
    xG_p90 = db.Column(db.Float)
    xG_per_shot = db.Column(db.Float)
    np_xG = db.Column(db.Float)
    np_xG_p90 = db.Column(db.Float)
    np_xG_per_shot = db.Column(db.Float)
    version = db.Column(db.Float)
    padj_air_challenges_p90 = db.Column(db.Float)
    patch_average_time_duration_p90 = db.Column(db.Float)
    patch_time_duration_sum_p90 = db.Column(db.Float)
    patch_position_gain_sum_p90 = db.Column(db.Float)
    patch_value_p90 = db.Column(db.Float)
    patch_total_offensive_actions_p90 = db.Column(db.Float)
    patch_defensive_rectangularity_p90 = db.Column(db.Float)
    patch_defensive_yrange_p90 = db.Column(db.Float)
    patch_defensive_xrange_p90 = db.Column(db.Float)
    patch_defensive_area_p90 = db.Column(db.Float)
    throughballs_shot_p90 = db.Column(db.Float)
    cross_shot_p90 = db.Column(db.Float)
    long_balls_shot_p90 = db.Column(db.Float)
    opp_half_touches_p90 = db.Column(db.Float)
    def __init__(self):
        pass

		
class ShotsModel(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    match_instatid = db.Column(db.Integer, db.ForeignKey('match.instatid'))
    team_instatid = db.Column(db.Integer, db.ForeignKey('team.instatid'))
    type = db.Column(db.String(30))
    action = db.Column(db.String(30))
    px = db.Column(db.Float)
    py = db.Column(db.Float)
    xG = db.Column(db.Float)


class XMLModelsPass(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    match_instatid = db.Column(db.Integer, db.ForeignKey('match.instatid'))
    team_instatid = db.Column(db.Integer, db.ForeignKey('team.instatid'))
    player_instatid = db.Column(db.Integer, db.ForeignKey('player.instatid'))
    zone = db.Column(db.String(10))
    zone_target = db.Column(db.String(10))
    time = db.Column(db.Float)
    time_target = db.Column(db.Float)
    type = db.Column(db.String(20))
    pos_x = db.Column(db.Integer)
    pos_x_target = db.Column(db.Integer)
    pos_y = db.Column(db.Integer)
    pos_y_target = db.Column(db.Integer)
    creation_time = db.Column(db.Date, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self):
        pass

class XMLModelsTeamPassCluster(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    team_instatid = db.Column(db.Integer, db.ForeignKey('team.instatid'))
    cluster_id = db.Column(db.Integer, db.ForeignKey('xml_models_pass_cluster.id'))
    count = db.Column(db.Integer)
    creation_time = db.Column(db.Date, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, team_instatid, cluster_id, count):
        self.cluster_id = cluster_id
        self.team_instatid = team_instatid
        self.count = count

class XMLModelsPassCluster(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    # league_instatid = db.Column(db.Integer, db.ForeignKey('league.instatid'))
    pos_x = db.Column(db.Integer)
    pos_x_target = db.Column(db.Integer)
    pos_y = db.Column(db.Integer)
    pos_y_target = db.Column(db.Integer)
    creation_time = db.Column(db.Date, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self, pos_x, pos_y, pos_x_target, pos_y_target):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_x_target = pos_x_target
        self.pos_y_target = pos_y_target


class XMLModelsPassTeam(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    match_instatid = db.Column(db.Integer, db.ForeignKey('match.instatid'))
    team_instatid = db.Column(db.Integer, db.ForeignKey('team.instatid'))
    zone = db.Column(db.String(10))
    zone_target = db.Column(db.String(10))
    type = db.Column(db.String(20))
    count = db.Column(db.Integer)
    creation_time = db.Column(db.Date, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self):
        pass


class XMLModelsCategories(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    model_name = db.Column(db.String)
    category = db.Column(db.String)

    def __init__(self):
        pass

class ChancesModel(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    match_instatid = db.Column(db.Integer)
    player_instatid = db.Column(db.Integer)
    team_instatid = db.Column(db.Integer)
    from_pos_x = db.Column(db.Float)
    from_pos_y = db.Column(db.Float)
    to_pos_x = db.Column(db.Float)
    to_pos_y = db.Column(db.Float)
    time = db.Column(db.Float)
    type = db.Column(db.String)
    creation_time = db.Column(db.Date, server_default=db.func.current_timestamp(), nullable=False)

    def __init__(self):
        pass


class XMLAvgTierPosition(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.String)
    tier = db.Column(db.Integer)
    creation_time = db.Column(db.Date, server_default=db.func.current_timestamp(), nullable=False)
    total_goals = db.Column(db.Float)
    average_x = db.Column(db.Float)
    average_y = db.Column(db.Float)
    shots_p90 = db.Column(db.Float)
    box_shots_p90 = db.Column(db.Float)
    outside_penalty_box_shots_p90 = db.Column(db.Float)
    scoring_contribution_p90 = db.Column(db.Float)
    percentage_of_own_created_shots = db.Column(db.Float)
    scoring_percentage = db.Column(db.Float)
    touches_in_box = db.Column(db.Float)
    assists_p90 = db.Column(db.Float)
    key_passes_acc_p90 = db.Column(db.Float)
    throughballs_p90 = db.Column(db.Float)
    lost_balls_p90 = db.Column(db.Float)
    passes_p90 = db.Column(db.Float)
    passes_completion = db.Column(db.Float)
    passes_to_the_box = db.Column(db.Float)
    danger_zone_entries_p90 = db.Column(db.Float)
    long_balls_p90 = db.Column(db.Float)
    long_balls_completion = db.Column(db.Float)
    crosses_successful_p90 = db.Column(db.Float)
    crosses_completion = db.Column(db.Float)
    dribbles_successful_p90 = db.Column(db.Float)
    dribbles_completion = db.Column(db.Float)
    space_defending_p90 = db.Column(db.Float)
    successful_tackles_p90 = db.Column(db.Float)
    tackles_completion = db.Column(db.Float)
    interceptions_p90 = db.Column(db.Float)
    padj_tackles_p90 = db.Column(db.Float)
    padj_interceptions_p90 = db.Column(db.Float)
    won_balls_p90 = db.Column(db.Float)
    won_balls_on_opposition_half_p90 = db.Column(db.Float)
    challenges_p90 = db.Column(db.Float)
    challenges_success_rate = db.Column(db.Float)
    long_balls_success = db.Column(db.Float)
    long_balls_received_p90 = db.Column(db.Float)
    air_challenges_success_rate = db.Column(db.Float)
    air_challenges_p90 = db.Column(db.Float)
    own_created_shots_p90 = db.Column(db.Float)
    accurate_passes_p90 = db.Column(db.Float)
    crosses_p90 = db.Column(db.Float)
    dribbles_p90 = db.Column(db.Float)
    tackles_p90 = db.Column(db.Float)
    won_challenges_p90 = db.Column(db.Float)
    won_air_challenges_p90 = db.Column(db.Float)
    opp_half_touches = db.Column(db.Float)
    opp_half_touches_ratio = db.Column(db.Float)
    non_penalty_goals = db.Column(db.Float)
    long_balls_successful_p90 = db.Column(db.Float)
    conversion_rate = db.Column(db.Float)
    picking_up_second_balls = db.Column(db.Float)
    matches_count = db.Column(db.Float)
    average_minutes = db.Column(db.Float)
    minutes = db.Column(db.Float)

    def __init__(self):
        pass


class XMLAvgPosition(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.String)
    creation_time = db.Column(db.Date, server_default=db.func.current_timestamp(), nullable=False)
    total_goals = db.Column(db.Float)
    average_x = db.Column(db.Float)
    average_y = db.Column(db.Float)
    shots_p90 = db.Column(db.Float)
    box_shots_p90 = db.Column(db.Float)
    outside_penalty_box_shots_p90 = db.Column(db.Float)
    scoring_contribution_p90 = db.Column(db.Float)
    percentage_of_own_created_shots = db.Column(db.Float)
    scoring_percentage = db.Column(db.Float)
    touches_in_box = db.Column(db.Float)
    assists_p90 = db.Column(db.Float)
    key_passes_acc_p90 = db.Column(db.Float)
    throughballs_p90 = db.Column(db.Float)
    lost_balls_p90 = db.Column(db.Float)
    passes_p90 = db.Column(db.Float)
    passes_completion = db.Column(db.Float)
    passes_to_the_box = db.Column(db.Float)
    danger_zone_entries_p90 = db.Column(db.Float)
    long_balls_p90 = db.Column(db.Float)
    long_balls_completion = db.Column(db.Float)
    crosses_successful_p90 = db.Column(db.Float)
    crosses_completion = db.Column(db.Float)
    dribbles_successful_p90 = db.Column(db.Float)
    dribbles_completion = db.Column(db.Float)
    space_defending_p90 = db.Column(db.Float)
    successful_tackles_p90 = db.Column(db.Float)
    tackles_completion = db.Column(db.Float)
    interceptions_p90 = db.Column(db.Float)
    padj_tackles_p90 = db.Column(db.Float)
    padj_interceptions_p90 = db.Column(db.Float)
    won_balls_p90 = db.Column(db.Float)
    won_balls_on_opposition_half_p90 = db.Column(db.Float)
    challenges_p90 = db.Column(db.Float)
    challenges_success_rate = db.Column(db.Float)
    long_balls_success = db.Column(db.Float)
    long_balls_received_p90 = db.Column(db.Float)
    air_challenges_success_rate = db.Column(db.Float)
    air_challenges_p90 = db.Column(db.Float)
    own_created_shots_p90 = db.Column(db.Float)
    accurate_passes_p90 = db.Column(db.Float)
    crosses_p90 = db.Column(db.Float)
    dribbles_p90 = db.Column(db.Float)
    tackles_p90 = db.Column(db.Float)
    won_challenges_p90 = db.Column(db.Float)
    won_air_challenges_p90 = db.Column(db.Float)
    opp_half_touches = db.Column(db.Float)
    opp_half_touches_ratio = db.Column(db.Float)
    non_penalty_goals = db.Column(db.Float)
    long_balls_successful_p90 = db.Column(db.Float)
    conversion_rate = db.Column(db.Float)
    picking_up_second_balls = db.Column(db.Float)
    matches_count = db.Column(db.Float)
    average_minutes = db.Column(db.Float)
    minutes = db.Column(db.Float)

    def __init__(self):
        pass


class XMLModelsSeasonTeam(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    team_instatid = db.Column(db.Integer)
    league_instatid = db.Column(db.Integer)
    season = db.Column(db.String)
    minutes = db.Column(db.Float)
    points = db.Column(db.Integer)
    xPoints = db.Column(db.Integer)
    xPoints_ours = db.Column(db.Integer)
    goals_for = db.Column(db.Float)
    goals_against = db.Column(db.Float)
    xG_for_p90 = db.Column(db.Float)
    xG_against_p90 = db.Column(db.Float)
    shots_for = db.Column(db.Float)
    shots_against = db.Column(db.Float)
    shots_on_target = db.Column(db.Float)
    shots_on_target_againts = db.Column(db.Float)
    headed_shots = db.Column(db.Float)
    dangerzone_shots_p90 = db.Column(db.Float)
    dangerzone_shots_against_p90 = db.Column(db.Float)
    xG_per_shot = db.Column(db.Float)
    average_distance_of_shots = db.Column(db.Float)
    average_distance_of_shots_against = db.Column(db.Float)
    passes_p90 = db.Column(db.Float)
    passes_succes_rate = db.Column(db.Float)
    average_direction_of_pass = db.Column(db.Float)
    passes_to_the_box_against_p90 = db.Column(db.Float)
    dangerzone_entries_p90 = db.Column(db.Float)
    crosses_p90 = db.Column(db.Float)
    shots_from_crosses = db.Column(db.Float)
    avg_number_of_passes_before_shot = db.Column(db.Float)
    passes_in_buildup = db.Column(db.Float)
    passes_in_middle_third = db.Column(db.Float)
    passes_in_final_third = db.Column(db.Float)
    long_balls = db.Column(db.Float)
    lost_balls = db.Column(db.Float)
    buildup = db.Column(db.Float)
    maintenance = db.Column(db.Float)
    counter_attacking = db.Column(db.Float)
    sustainable_threat = db.Column(db.Float)
    fast_tempo = db.Column(db.Float)
    high_press = db.Column(db.Float)
    tts_for = db.Column(db.Float)
    tts_against = db.Column(db.Float)
    tts_difference = db.Column(db.Float)
    tts_tackle = db.Column(db.Float)
    tts_interception = db.Column(db.Float)
    tts_turnover = db.Column(db.Float)
    won_balls_opp_half = db.Column(db.Float)
    won_balls_final_third = db.Column(db.Float)
    won_balls_middle_third = db.Column(db.Float)
    won_balls_own_third = db.Column(db.Float)
    avg_height_of_turnover = db.Column(db.Float)
    tackles_total = db.Column(db.Float)
    tackles_success_rate = db.Column(db.Float)
    headers_total = db.Column(db.Float)
    headers_success_rate = db.Column(db.Float)
    challenges_total = db.Column(db.Float)
    challenges_success_rate = db.Column(db.Float)
    lost_headers_in_own_box = db.Column(db.Float)
    won_headers_in_opp_box = db.Column(db.Float)
    interceptions = db.Column(db.Float)
    tackles_padj = db.Column(db.Float)
    interceptions_padj = db.Column(db.Float)

    def __init__(self):
        pass

class XMLSeasonPercentiles(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    league_tier = db.Column(db.Integer)
    season = db.Column(db.String)
    percentile = db.Column(db.Float)
    primary_position = db.Column(db.String)
    total_goals = db.Column(db.Integer)
    average_x = db.Column(db.Float)
    average_y = db.Column(db.Float)
    shots_p90 = db.Column(db.Float)
    box_shots_p90 = db.Column(db.Float)
    outside_box_shots_p90 = db.Column(db.Float)
    scoring_contribution_p90 = db.Column(db.Float)
    percentage_of_own_created_shots = db.Column(db.Float)
    scoring_percentage = db.Column(db.Float)
    touches_in_box = db.Column(db.Float)
    assists_p90 = db.Column(db.Float)
    key_passes_acc_p90 = db.Column(db.Float)
    throughballs_p90 = db.Column(db.Float)
    lost_balls_p90 = db.Column(db.Float)
    passes_p90 = db.Column(db.Float)
    passes_completion = db.Column(db.Float)
    acc_passes_to_the_box_p90 = db.Column(db.Float)
    passes_to_the_box_p90 = db.Column(db.Float)
    danger_zone_entries_p90 = db.Column(db.Float)
    long_balls_p90 = db.Column(db.Float)
    long_balls_completion = db.Column(db.Float)
    crosses_succ_p90 = db.Column(db.Float)
    crosses_completion = db.Column(db.Float)
    dribbles_succ_p90 = db.Column(db.Float)
    dribbles_completion = db.Column(db.Float)
    space_defending_p90 = db.Column(db.Float)
    tackles_completion = db.Column(db.Float)
    padj_tackles_p90 = db.Column(db.Float)
    padj_interceptions_p90 = db.Column(db.Float)
    won_balls_p90 = db.Column(db.Float)
    won_balls_opp_half_p90 = db.Column(db.Float)
    challenges_p90 = db.Column(db.Float)
    challenges_succ_p90 = db.Column(db.Float)
    challenges_succ_rate = db.Column(db.Float)
    long_balls_received_p90 = db.Column(db.Float)
    air_challenges_succ_rate = db.Column(db.Float)
    air_challenges_p90 = db.Column(db.Float)
    air_challenges_succ_p90 = db.Column(db.Float)
    own_created_shots_p90 = db.Column(db.Float)
    acc_passes_p90 = db.Column(db.Float)
    crosses_p90 = db.Column(db.Float)
    dribbles_p90 = db.Column(db.Float)
    won_challenges_p90 = db.Column(db.Float)
    won_air_challenges_p90 = db.Column(db.Float)
    opp_half_touches = db.Column(db.Float)
    opp_half_touches_ratio = db.Column(db.Float)
    non_penalty_goals = db.Column(db.Float)
    long_balls_succ_p90 = db.Column(db.Float)
    conversion_rate = db.Column(db.Float)
    picking_up_second_balls_p90 = db.Column(db.Float)
    xG = db.Column(db.Float)
    xA = db.Column(db.Float)
    xG_p90 = db.Column(db.Float)
    xG_per_shot = db.Column(db.Float)
    xGA_p90 = db.Column(db.Float)
    np_xG = db.Column(db.Float)
    np_xA = db.Column(db.Float)
    np_xG_p90 = db.Column(db.Float)
    np_xG_per_shot = db.Column(db.Float)
    np_xGA_p90 = db.Column(db.Float)

    def __init__(self):
        pass


class JSONPassingCentersMatchTeam(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    league_instatid = db.Column(db.Integer)
    season = db.Column(db.String)
    match_instatid = db.Column(db.Integer)
    team_instatid = db.Column(db.Integer)
    passes = db.Column(db.String)
    players = db.Column(db.String)

    def __init__(self):
        pass


class JSONChallengesMatchTeam(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    league_instatid = db.Column(db.Integer)
    season = db.Column(db.String)
    match_instatid = db.Column(db.Integer)
    team_instatid = db.Column(db.Integer)
    json = db.Column(db.String)

    def __init__(self):
        pass


class JSONChancesSeasonPlayer(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    league_instatid = db.Column(db.Integer)
    season = db.Column(db.String)
    player_name = db.Column(db.String)
    player_instatid = db.Column(db.Integer)
    team_instatid = db.Column(db.Integer)
    json = db.Column(db.String)

    def __init__(self):
        pass


class JSONChancesMatchTeam(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    league_instatid = db.Column(db.Integer)
    season = db.Column(db.String)
    match_instatid = db.Column(db.Integer)
    team_instatid = db.Column(db.Integer)
    json = db.Column(db.String)

    def __init__(self):
        pass


class JSONShotsMatchTeam(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    league_instatid = db.Column(db.Integer)
    season = db.Column(db.String)
    match_instatid = db.Column(db.Integer)
    team_instatid = db.Column(db.Integer)
    json = db.Column(db.String)

    def __init__(self):
        pass


class JSONShotsSeasonPlayer(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    league_instatid = db.Column(db.Integer)
    season = db.Column(db.String)
    team_instatid = db.Column(db.Integer)
    player_instatid = db.Column(db.Integer)
    player_name = db.Column(db.String)
    json = db.Column(db.String)

    def __init__(self):
        pass


class XMLPassesSonarSeasonPlayer(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    league_instatid = db.Column(db.Integer)
    season = db.Column(db.String)
    team_instatid = db.Column(db.Integer)
    player_instatid = db.Column(db.Integer)
    data = db.Column(db.String)

    def __init__(self):
        pass
