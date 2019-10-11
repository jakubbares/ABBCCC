from marshmallow_jsonapi import Schema, fields
from marshmallow import validate
import json
not_blank = validate.Length(min=1, error='Field cannot be blank')

class LeagueSchema(Schema):
    id = fields.Integer(dump_only=True)
    instatid = fields.Integer()
    tier = fields.String()
    country_name = fields.String(validate=not_blank)
    name = fields.String(validate=not_blank)

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/data/"
        else:
            self_link = "/data/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'data'


class TaskSchema(Schema):
    id = fields.Integer(dump_only=True)
    customer_id = fields.Integer()
    position = fields.String()
    assigned_to_id = fields.Integer()

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/data/"
        else:
            self_link = "/data/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'data'


class CandidateCustomerLinkSchema(Schema):
    id = fields.Integer()
    player_id = fields.Integer()
    customer_id = fields.Integer()
    position = fields.String()
    contract_value_min = fields.Integer()
    contract_value_max = fields.Integer()

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/data/"
        else:
            self_link = "/data/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'data'

class PlayerPositionLinkSchema(Schema):
    id = fields.Integer()
    position_id = fields.Integer()
    starts = fields.Integer()

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/data/"
        else:
            self_link = "/data/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'data'


class TeamLeagueLinkSchema(Schema):
    id = fields.Integer()
    league_id = fields.Integer()
    team_id = fields.Integer()
    league_instatid = fields.Integer()
    team_instatid = fields.Integer()
    season = fields.String()
    matches = fields.Integer()
    wins = fields.Integer()
    draws = fields.Integer()
    losses = fields.Integer()
    goals = fields.Integer()
    points = fields.Integer()

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/data/"
        else:
            self_link = "/data/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'data'

class TeamSchema(Schema):
    id = fields.Integer(dump_only=True)
    instatid = fields.Integer()
    name = fields.String(validate=not_blank)

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/data/"
        else:
            self_link = "/data/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'data'

class TransferSchema(Schema):
    id = fields.Integer(dump_only=True)
    player_id = fields.Integer()
    fee = fields.Integer()
    team_from_id = fields.Integer()
    team_to_id = fields.Integer()
    value = fields.Integer()
    currency = fields.String(validate=not_blank)
    position_id = fields.Integer()
    url = fields.String(validate=not_blank)

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/data/"
        else:
            self_link = "/data/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'data'



class PlayerEvaluationSchema(Schema):
    id = fields.Integer(dump_only=True)
    player_id = fields.Integer(validate=not_blank)
    user_id = fields.Integer(validate=not_blank)
    tag = fields.String()
    score = fields.Integer()
    kind = fields.String(validate=not_blank)
    comment = fields.String()
    creation_time = fields.DateTime(dump_only=True)

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/data/"
        else:
            self_link = "/data/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'data'



class UserSchema(Schema):
    id = fields.Integer()
    role = fields.String(validate=not_blank)
    name = fields.String(validate=not_blank)
    password = fields.String(validate=not_blank)
    temporary_password = fields.Boolean()
    email = fields.String(validate=not_blank)
    creation_time = fields.DateTime(dump_only=True)

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/data/"
        else:
            self_link = "/data/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'data'

class CalculatedPlayersSchema(Schema):
    id = fields.Integer()
    instatid = fields.Integer()
    name = fields.String(validate=not_blank)
    nationality = fields.String(validate=not_blank)
    team = fields.String()
    team_id = fields.Integer()
    league = fields.String()
    league_id = fields.Integer()
    birthday = fields.String()

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/data/"
        else:
            self_link = "/data/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'data'



class PlayerSchema(Schema):
    id = fields.Integer(dump_only=True)
    instatid = fields.Integer()
    name = fields.String(validate=not_blank)
    contract = fields.String()
    nationality = fields.String(validate=not_blank)
    team_instatid = fields.Integer()
    birthday = fields.String()
    weight = fields.Integer()
    height = fields.Integer()
    left_foot = fields.Integer()
    right_foot = fields.Integer()
    creation_time = fields.DateTime(dump_only=True)
    team_id = fields.Integer()
    contract_tm = fields.String()
    team_member_since_tm = fields.String()
    market_value_tm = fields.Decimal()
    name_tm = fields.String()
    player_number_tm = fields.Integer()
    birthday_tm = fields.String()
    url_tm = fields.String()
    nationality_tm = fields.String()
    height_tm = fields.Integer()
    foot_tm = fields.String()
    position_tm = fields.String()
    creation_time_tm = fields.Date()

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/data/"
        else:
            self_link = "/data/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'data'


class PositionSchema(Schema):
    id = fields.String()
    name = fields.String(validate=not_blank)

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/data/"
        else:
            self_link = "/data/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'data'


class MatchSchema(Schema):
    id = fields.Integer()
    instatid = fields.Integer()
    league_id = fields.Integer()
    league_instatid = fields.Integer()
    league = fields.String()
    country = fields.String()
    home_team_id = fields.Integer()
    guest_team_id = fields.Integer()
    home_team_instatid = fields.Integer()
    guest_team_instatid = fields.Integer()
    season = fields.String()
    match_date = fields.String()
    upload_time = fields.Date()
    home_team = fields.String()
    guest_team = fields.String()
    match_result = fields.String()

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/data/"
        else:
            self_link = "/data/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'data'


class EventSchema(Schema):
    id = fields.Integer(dump_only=True)
    instatid = fields.Integer()
    match_instatid = fields.Integer()
    player_instatid = fields.Integer()
    player_id = fields.Integer()
    player_name = fields.String()
    team_instatid = fields.Integer()
    team_id = fields.Integer()
    # match_id = fields.Integer()
    order_i = fields.Integer()
    end = fields.Decimal()
    half = fields.Integer()
    pos_x = fields.Decimal()
    pos_y = fields.Decimal()
    type = fields.Integer()
    creation_time = fields.DateTime(dump_only=True)

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/data/"
        else:
            self_link = "/data/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'data'


class ExpectedGoalsSchema(Schema):
    id = fields.Integer(dump_only=True)
    pos_x = fields.Integer()
    pos_y = fields.Integer()
    season = fields.Integer()
    position_id = fields.Integer()
    team_id = fields.Integer()
    league_id = fields.Integer()
    total_shots = fields.Integer()
    total_goals = fields.Integer()
    creation_time = fields.DateTime(dump_only=True)

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/data/"
        else:
            self_link = "/data/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'data'
class PlayerStatsCalculatedSchema(Schema):
    id = fields.Integer(dump_only=True)
    player_id = fields.Integer()
    player_instatid = fields.Integer()
    league_id = fields.Integer()
    # league_id = fields.Integer()
    # team_id = fields.Integer()
    # season = fields.Integer()
    goals = fields.Decimal()
    assists = fields.Decimal()
    yellow_cards = fields.Decimal()
    red_cards = fields.Decimal()
    total_actions = fields.Decimal()
    successful_total_actions = fields.Decimal()
    shots = fields.Decimal()
    successful_shots = fields.Decimal()
    passes = fields.Decimal()
    successful_passes = fields.Decimal()
    key_passes = fields.Decimal()
    successful_key_passes = fields.Decimal()
    crosses = fields.Decimal()
    successful_crosses = fields.Decimal()
    challenges = fields.Decimal()
    successful_challenges = fields.Decimal()
    air_challenges = fields.Decimal()
    successful_air_challenges = fields.Decimal()
    dribbles = fields.Decimal()
    successful_dribbles = fields.Decimal()
    tackles = fields.Decimal()
    successful_tackles = fields.Decimal()
    lost_balls = fields.Decimal()
    received_balls = fields.Decimal()
    fouls = fields.Decimal()
    player_fouls = fields.Decimal()

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/data/"
        else:
            self_link = "/data/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'data'


class PlayerStatsTotalSchema(Schema):
    id = fields.Integer(dump_only=True)
    player_id = fields.Integer()
    player_instatid = fields.Integer()
    league_id = fields.Integer()
    # league_id = fields.Integer()
    # team_id = fields.Integer()
    # season = fields.Integer()
    minutes = fields.Integer()
    # minutes_per_90 = fields.Decimal()
    goals = fields.Integer()
    assists = fields.Integer()
    yellow_cards = fields.Integer()
    red_cards = fields.Integer()
    total_actions = fields.Integer()
    successful_total_actions = fields.Integer()
    shots = fields.Integer()
    successful_shots = fields.Integer()
    passes = fields.Integer()
    successful_passes = fields.Integer()
    key_passes = fields.Integer()
    successful_key_passes = fields.Integer()
    crosses = fields.Integer()
    successful_crosses = fields.Integer()
    challenges = fields.Integer()
    successful_challenges = fields.Integer()
    air_challenges = fields.Integer()
    successful_air_challenges = fields.Integer()
    dribbles = fields.Integer()
    successful_dribbles = fields.Integer()
    tackles = fields.Integer()
    successful_tackles = fields.Integer()
    lost_balls = fields.Integer()
    received_balls = fields.Integer()
    fouls = fields.Integer()
    player_fouls = fields.Integer()
    # ran_distance_x = fields.Decimal()
    # ran_distance_y = fields.Decimal()
    # goals = fields.Integer()
    # assists = fields.Integer()
    # non_penalty_total_goals = fields.Integer()
    # shots = fields.Integer()
    # box_shots = fields.Integer()
    # outside_penalty_box_shots = fields.Integer()
    # touches_in_box = fields.Integer()
    # key_passes = fields.Integer()
    # throughballs = fields.Integer()
    # lost_balls = fields.Integer()
    # passes = fields.Integer()
    # gain = fields.Integer()
    # passes_to_the_box = fields.Integer()
    # danger_zone_entries = fields.Integer()
    # long_balls_attempted = fields.Integer()
    # long_balls_made = fields.Integer()
    # crosses_attempted = fields.Integer()
    # crosses_made = fields.Integer()
    # dribbles_attempted = fields.Integer()
    # dribbles_made = fields.Integer()
    # space_defending = fields.Integer()
    # tackles_attempted = fields.Integer()
    # tackles_made = fields.Integer()
    # padj_tackles = fields.Integer()
    # interceptions = fields.Integer()
    # padj_interceptions = fields.Integer()
    # won_balls = fields.Integer()
    # won_balls_on_opposition_half = fields.Integer()
    # challenges_attempted = fields.Integer()
    # challenges_made = fields.Integer()
    # long_balls_received = fields.Integer()
    # touches_on_opposition_half = fields.Integer()
    # touches_on_own_half = fields.Integer()
    # second_balls_picked = fields.Integer()
    # creation_time = fields.DateTime(dump_only=True)

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/data/"
        else:
            self_link = "/data/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'data'


class ChancesModelSchema(Schema):
    id = fields.Integer(dump_only=True)
    match_instatid = fields.Integer()
    player_instatid = fields.Integer()
    team_instatid = fields.Integer()
    from_pos_x = fields.Decimal()
    from_pos_y = fields.Decimal()
    to_pos_x = fields.Decimal()
    to_pos_y = fields.Decimal()
    time = fields.Decimal()
    type = fields.String()
    creation_time = fields.DateTime(dump_only=True)

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/data/"
        else:
            self_link = "/data/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'data'


class XMLModelsSeasonTeamSchema(Schema):
    id = fields.Integer(dump_only=True)
    team_instatid = fields.Integer()
    league_instatid = fields.Integer()
    season = fields.String()
    minutes = fields.Decimal()
    points = fields.Integer()
    xPoints = fields.Integer()
    xPoints_ours = fields.Integer()
    goals_for = fields.Decimal()
    goals_against = fields.Decimal()
    xG_for_p90 = fields.Decimal()
    xG_against_p90 = fields.Decimal()
    shots_for = fields.Decimal()
    shots_against = fields.Decimal()
    shots_on_target = fields.Decimal()
    shots_on_target_againts = fields.Decimal()
    headed_shots = fields.Decimal()
    dangerzone_shots_p90 = fields.Decimal()
    dangerzone_shots_against_p90 = fields.Decimal()
    xG_per_shot = fields.Decimal()
    average_distance_of_shots = fields.Decimal()
    average_distance_of_shots_against = fields.Decimal()
    passes_p90 = fields.Decimal()
    passes_succes_rate = fields.Decimal()
    average_direction_of_pass = fields.Decimal()
    passes_to_the_box_p90 = fields.Decimal()
    passes_to_the_box_against_p90 = fields.Decimal()
    dangerzone_entries_p90 = fields.Decimal()
    crosses_p90 = fields.Decimal()
    shots_from_crosses = fields.Decimal()
    avg_number_of_passes_before_shot = fields.Decimal()
    passes_in_buildup = fields.Decimal()
    passes_in_middle_third = fields.Decimal()
    passes_in_final_third = fields.Decimal()
    long_balls = fields.Decimal()
    lost_balls = fields.Decimal()
    buildup = fields.Decimal()
    maintenance = fields.Decimal()
    counter_attacking = fields.Decimal()
    sustainable_threat = fields.Decimal()
    fast_tempo = fields.Decimal()
    high_press = fields.Decimal()
    tts_for = fields.Decimal()
    tts_against = fields.Decimal()
    tts_difference = fields.Decimal()
    tts_tackle = fields.Decimal()
    tts_interception = fields.Decimal()
    tts_turnover = fields.Decimal()
    won_balls_opp_half = fields.Decimal()
    won_balls_final_third = fields.Decimal()
    won_balls_middle_third = fields.Decimal()
    won_balls_own_third = fields.Decimal()
    avg_height_of_turnover = fields.Decimal()
    tackles_total = fields.Decimal()
    tackles_success_rate = fields.Decimal()
    headers_total = fields.Decimal()
    headers_success_rate = fields.Decimal()
    challenges_total = fields.Decimal()
    challenges_success_rate = fields.Decimal()
    lost_headers_in_own_box = fields.Decimal()
    won_headers_in_opp_box = fields.Decimal()
    interceptions = fields.Decimal()
    tackles_padj = fields.Decimal()
    interceptions_padj = fields.Decimal()

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/data/"
        else:
            self_link = "/data/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'data'


class MatchTeamStatsTotalSchema(Schema):
    id = fields.Integer(dump_only=True)
    match_id = fields.Integer()
    match_instatid = fields.Integer()
    team_id = fields.Integer()
    team_instatid = fields.Integer()
    creation_time = fields.DateTime(dump_only=True)
    goals = fields.Integer()
    assists = fields.Integer()
    yellow_cards = fields.Integer()
    red_cards = fields.Integer()
    total_actions = fields.Integer()
    successful_total_actions = fields.Integer()
    shots = fields.Integer()
    successful_shots = fields.Integer()
    passes = fields.Integer()
    successful_passes = fields.Integer()
    key_passes = fields.Integer()
    successful_key_passes = fields.Integer()
    crosses = fields.Integer()
    successful_crosses = fields.Integer()
    challenges = fields.Integer()
    successful_challenges = fields.Integer()
    air_challenges = fields.Integer()
    successful_air_challenges = fields.Integer()
    dribbles = fields.Integer()
    successful_dribbles = fields.Integer()
    tackles = fields.Integer()
    successful_tackles = fields.Integer()
    lost_balls = fields.Integer()
    received_balls = fields.Integer()
    fouls = fields.Integer()

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/data/"
        else:
            self_link = "/data/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'data'

    
class MatchPlayerStatsTotalSchema(Schema):
    id = fields.Integer(dump_only=True)
    match_id = fields.Integer()
    match_instatid = fields.Integer()
    player_id = fields.Integer()
    player_instatid = fields.Integer()
    team_id = fields.Integer()
    team_instatid = fields.Integer()
    creation_time = fields.DateTime(dump_only=True)
    position = fields.String()
    minutes = fields.Integer()
    goals = fields.Integer()
    assists = fields.Integer()
    yellow_cards = fields.Integer()
    red_cards = fields.Integer()
    total_actions = fields.Integer()
    successful_total_actions = fields.Integer()
    shots = fields.Integer()
    successful_shots = fields.Integer()
    passes = fields.Integer()
    successful_passes = fields.Integer()
    key_passes = fields.Integer()
    successful_key_passes = fields.Integer()
    crosses = fields.Integer()
    successful_crosses = fields.Integer()
    challenges = fields.Integer()
    successful_challenges = fields.Integer()
    air_challenges = fields.Integer()
    successful_air_challenges = fields.Integer()
    dribbles = fields.Integer()
    successful_dribbles = fields.Integer()
    tackles = fields.Integer()
    successful_tackles = fields.Integer()
    lost_balls = fields.Integer()
    received_balls = fields.Integer()
    fouls = fields.Integer()
    player_fouls = fields.Integer()
    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/data/"
        else:
            self_link = "/data/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'data'


class ShotsModelSchema(Schema):
    id = fields.Integer()
    match_instatid = fields.Integer()
    team_instatid = fields.Integer()
    type = fields.String()
    action = fields.String()
    px = fields.Decimal()
    py = fields.Decimal()
    xG = fields.Decimal()
    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/data/"
        else:
            self_link = "/data/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'data'


class XMLModelsSeasonPlayerAggSchema(Schema):
    id = fields.Integer()   
    league_name = fields.String()
    league_country = fields.String()
    league_tier = fields.Integer()
    league_instatid = fields.Integer()    
    player_instatid = fields.Integer()
    team_instatid = fields.Integer()
    team_name = fields.String()
    player_name = fields.String()
    nationality = fields.String()
    birthday = fields.Date()
    height = fields.Integer()
    weight = fields.Integer()
    left_foot = fields.Integer()
    right_foot = fields.Integer()   
    season = fields.String()
    league_id = fields.Integer()       
    team_id = fields.Integer()
    player_id = fields.Integer()
    instat_creation_time = fields.Date()
    transfermarkt_creation_time = fields.Date()
    instat_contract = fields.String()
    transfermarkt_contract = fields.String()
    market_value_tm = fields.Float()
    matches_count = fields.Integer()
    average_minutes = fields.Float()
    minutes = fields.Float()
    xG_minutes = fields.Float()
    padj_tackles_minutes = fields.Float()
    padj_interceptions_minutes = fields.Float()
    primary_position = fields.String()
    secondary_position = fields.String()
    primary_position_percentage = fields.Float()
    secondary_position_percentage = fields.Float()
    total_goals = fields.Integer()
    average_x = fields.Float()
    average_y = fields.Float()
    shots_p90 = fields.Float()
    box_shots_p90 = fields.Float()
    outside_box_shots_p90 = fields.Float()
    scoring_contribution_p90 = fields.Float()
    percentage_of_own_created_shots = fields.Float()
    scoring_percentage = fields.Float()
    touches_in_box = fields.Float()
    assists_p90 = fields.Float()
    key_passes_acc_p90 = fields.Float()
    throughballs_p90 = fields.Float()
    lost_balls_p90 = fields.Float()
    passes_p90 = fields.Float()
    passes_completion = fields.Float()
    acc_passes_to_the_box_p90 = fields.Float()
    passes_to_the_box_p90 = fields.Float()
    danger_zone_entries_p90 = fields.Float()
    long_balls_p90 = fields.Float()
    long_balls_completion = fields.Float()
    crosses_succ_p90 = fields.Float()
    crosses_completion = fields.Float()
    dribbles_succ_p90 = fields.Float()
    dribbles_completion = fields.Float()
    space_defending_p90 = fields.Float()
    tackles_completion = fields.Float()
    padj_tackles_p90 = fields.Float()
    padj_interceptions_p90 = fields.Float()
    won_balls_p90 = fields.Float()
    won_balls_opp_half_p90 = fields.Float()
    challenges_p90 = fields.Float()
    challenges_succ_rate = fields.Float()
    challenges_succ_p90 = fields.Float()
    long_balls_received_p90 = fields.Float()
    air_challenges_succ_rate = fields.Float()
    air_challenges_p90 = fields.Float()
    air_challenges_succ_p90 = fields.Float()
    own_created_shots_p90 = fields.Float()
    acc_passes_p90 = fields.Float()
    crosses_p90 = fields.Float()
    dribbles_p90 = fields.Float()
    won_challenges_p90 = fields.Float()
    won_air_challenges_p90 = fields.Float()
    opp_half_touches = fields.Float()
    opp_half_touches_ratio = fields.Float()
    non_penalty_goals = fields.Float()
    long_balls_succ_p90 = fields.Float()
    conversion_rate = fields.Float()
    picking_up_second_balls_p90 = fields.Float()
    xG = fields.Float()
    xG_p90 = fields.Float()
    xG_per_shot = fields.Float()
    np_xG = fields.Float()
    np_xG_p90 = fields.Float()
    np_xG_per_shot = fields.Float()
    version = fields.Float()
    padj_air_challenges_p90 = fields.Float()
    patch_average_time_duration_p90 = fields.Float()
    patch_time_duration_sum_p90 = fields.Float()
    patch_position_gain_sum_p90 = fields.Float()
    patch_value_p90 = fields.Float()
    patch_total_offensive_actions_p90 = fields.Float()
    patch_defensive_rectangularity_p90 = fields.Float()
    patch_defensive_yrange_p90 = fields.Float()
    patch_defensive_xrange_p90 = fields.Float()
    patch_defensive_area_p90 = fields.Float()
    throughballs_shot_p90 = fields.Float()
    cross_shot_p90 = fields.Float()
    long_balls_shot_p90 = fields.Float()
    opp_half_touches_p90 = fields.Float()

    def get_top_level_links(self, data, many):
        if many:
            self_link = "/data/"
        else:
            self_link = "/data/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'data'

class XMLModelsMatchPlayerSchema(Schema):
    id = fields.Integer()
    match_instatid = fields.Integer()
    player_instatid = fields.Integer()
    player_id = fields.Integer()
    match_id = fields.Integer()
    team_instatid = fields.Integer()
    team_id = fields.Integer()
    first_event_time = fields.Decimal()
    last_event_time = fields.Decimal()
    minutes = fields.Integer()
    match_date = fields.DateTime()
    season = fields.String()
    creation_time = fields.DateTime(dumponly=True)
    goals = fields.Integer()
    average_x = fields.Decimal()
    average_y = fields.Decimal()
    shots_p90 = fields.Decimal()
    box_shots_p90 = fields.Decimal()
    outside_penalty_box_shots_p90 = fields.Decimal()
    scoring_contribution_p90 = fields.Decimal()
    percentage_of_own_created_shots = fields.Decimal()
    scoring_percentage = fields.Decimal()
    touches_in_box = fields.Decimal()
    assists_p90 = fields.Decimal()
    key_passes_acc_p90 = fields.Decimal()
    throughballs_p90 = fields.Decimal()
    lost_balls_p90 = fields.Decimal()
    passes_p90 = fields.Decimal()
    passes_completion = fields.Decimal()
    passes_to_the_box = fields.Decimal()
    danger_zone_entries_p90 = fields.Decimal()
    long_balls_p90 = fields.Decimal()
    long_balls_completion = fields.Decimal()
    crosses_successful_p90 = fields.Decimal()
    crosses_completion = fields.Decimal()
    dribbles_successful_p90 = fields.Decimal()
    dribbles_completion = fields.Decimal()
    average_space_defending_p90 = fields.Decimal()
    successful_tackles_p90 = fields.Decimal()
    tackles_completion = fields.Decimal()
    interceptions_p90 = fields.Decimal()
    padj_tackles_p90 = fields.Decimal()
    padj_interceptions_p90 = fields.Decimal()
    won_balls_p90 = fields.Decimal()
    won_balls_on_opposition_half_p90 = fields.Decimal()
    challenges_p90 = fields.Decimal()
    challenges_success_rate = fields.Decimal()
    air_challenges_success_rate = fields.Decimal()
    air_challenges_p90 = fields.Decimal()
    own_created_shots_p90 = fields.Decimal()
    accurate_passes_p90 = fields.Decimal()
    crosses_p90 = fields.Decimal()
    dribbles_p90 = fields.Decimal()
    tackles_p90 = fields.Decimal()
    won_challenges_p90 = fields.Decimal()
    won_air_challenges_p90 = fields.Decimal()
    opp_half_touches = fields.Decimal()
    opp_half_touches_ratio = fields.Decimal()
    non_penalty_goals = fields.Decimal()
    long_balls_successful_p90 = fields.Decimal()
    long_balls_received_p90 = fields.Decimal()
    conversion_rate = fields.Decimal()
    picking_up_second_balls_p90 = fields.Decimal()
    position = fields.String()
    
    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/data/"
        else:
            self_link = "/data/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'data'


class XMLModelsSeasonPlayerSchema(Schema):
    id = fields.Integer()
    player_instatid = fields.Integer()
    team_instatid = fields.Integer()
    league_instatid = fields.Integer()
    league_name = fields.String()
    team_name = fields.String()
    player_name = fields.String()
    birthday = fields.Date()
    height = fields.Integer()
    weight = fields.Integer()
    nationality = fields.String()
    left_foot = fields.Integer()
    right_foot = fields.Integer()
    tier = fields.Integer()
    season = fields.String()
    season_half = fields.Integer()
    total_goals = fields.Integer()
    average_x = fields.Decimal()
    average_y = fields.Decimal()
    shots_p90 = fields.Decimal()
    box_shots_p90 = fields.Decimal()
    outside_penalty_box_shots_p90 = fields.Decimal()
    scoring_contribution_p90 = fields.Decimal()
    percentage_of_own_created_shots = fields.Decimal()
    scoring_percentage = fields.Decimal()
    touches_in_box = fields.Decimal()
    assists_p90 = fields.Decimal()
    key_passes_acc_p90 = fields.Decimal()
    throughballs_p90 = fields.Decimal()
    lost_balls_p90 = fields.Decimal()
    passes_p90 = fields.Decimal()
    passes_completion = fields.Decimal()
    passes_to_the_box = fields.Decimal()
    danger_zone_entries_p90 = fields.Decimal()
    long_balls_p90 = fields.Decimal()
    long_ball_completion = fields.Decimal()
    crosses_successful_p90 = fields.Decimal()
    crosses_completion = fields.Decimal()
    dribbles_successful_p90 = fields.Decimal()
    dribbles_completion = fields.Decimal()
    space_defending_p90 = fields.Decimal()
    successful_tackles_p90 = fields.Decimal()
    tackles_completion = fields.Decimal()
    interceptions_p90 = fields.Decimal()
    padj_tackles_p90 = fields.Decimal()
    padj_interceptions_p90 = fields.Decimal()
    won_balls_p90 = fields.Decimal()
    won_balls_on_opposition_half_p90 = fields.Decimal()
    challenges_total_p90 = fields.Decimal()
    challenges_success_rate = fields.Decimal()
    long_balls_success = fields.Decimal()
    long_balls_received_p90 = fields.Decimal()
    air_challenges_success_rate = fields.Decimal()
    air_challenges_p90 = fields.Decimal()
    own_created_shots_p90 = fields.Decimal()
    accurate_passes_p90 = fields.Decimal()
    crosses_p90 = fields.Decimal()
    dribbles_p90 = fields.Decimal()
    tackles_p90 = fields.Decimal()
    won_challenges_p90 = fields.Decimal()
    won_air_challenges_p90 = fields.Decimal()
    opp_half_touches = fields.Decimal()
    opp_half_touches_ratio = fields.Decimal()
    non_penalty_goals = fields.Decimal()
    long_balls_successful_p90 = fields.Decimal()
    conversion_rate = fields.Decimal()
    picking_up_second_balls_p90 = fields.Decimal()
    matches_count = fields.Decimal()
    average_minutes = fields.Decimal()
    minutes = fields.Decimal()
    xG_total = fields.Decimal()
    xG_assists_total = fields.Decimal()
    xG_p90 = fields.Decimal()
    xG_per_shot = fields.Decimal()
    xG_goals_and_assists_p90 = fields.Decimal()
    primary_position = fields.String()
    secondary_position = fields.String()


    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/data/"
        else:
            self_link = "/data/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'data'


class XMLAvgTierPositionSchema(Schema):
    id = fields.Integer()
    position = fields.String()
    tier = fields.Integer()
    player_instatid = fields.Integer()
    player_id = fields.Integer()
    team_instatid = fields.Integer()
    team_id = fields.Integer()
    season = fields.String()
    season_half = fields.Integer()
    creation_time = fields.DateTime(dumponly=True)
    total_goals = fields.Integer()
    average_x = fields.Decimal()
    average_y = fields.Decimal()
    shots_p90 = fields.Decimal()
    box_shots_p90 = fields.Decimal()
    outside_penalty_box_shots_p90 = fields.Decimal()
    scoring_contribution_p90 = fields.Decimal()
    percentage_of_own_created_shots = fields.Decimal()
    scoring_percentage = fields.Decimal()
    touches_in_box = fields.Decimal()
    assists_p90 = fields.Decimal()
    key_passes_acc_p90 = fields.Decimal()
    throughballs_p90 = fields.Decimal()
    lost_balls_p90 = fields.Decimal()
    passes_p90 = fields.Decimal()
    passes_completion = fields.Decimal()
    passes_to_the_box = fields.Decimal()
    danger_zone_entries_p90 = fields.Decimal()
    long_balls_p90 = fields.Decimal()
    long_balls_completion = fields.Decimal()
    crosses_successful_p90 = fields.Decimal()
    crosses_completion = fields.Decimal()
    dribbles_successful_p90 = fields.Decimal()
    dribbles_completion = fields.Decimal()
    space_defending_p90 = fields.Decimal()
    successful_tackles_p90 = fields.Decimal()
    tackles_completion = fields.Decimal()
    interceptions_p90 = fields.Decimal()
    padj_tackles_p90 = fields.Decimal()
    padj_interceptions_p90 = fields.Decimal()
    won_balls_p90 = fields.Decimal()
    won_balls_on_opposition_half_p90 = fields.Decimal()
    challenges_p90 = fields.Decimal()
    challenges_success_rate = fields.Decimal()
    long_balls_success = fields.Decimal()
    long_balls_received_p90 = fields.Decimal()
    air_challenges_success_rate = fields.Decimal()
    air_challenges_p90 = fields.Decimal()
    per90 = fields.Decimal()
    own_created_shots_p90 = fields.Decimal()
    accurate_passes_p90 = fields.Decimal()
    crosses_p90 = fields.Decimal()
    dribbles_p90 = fields.Decimal()
    tackles_p90 = fields.Decimal()
    won_challenges_p90 = fields.Decimal()
    won_air_challenges_p90 = fields.Decimal()
    opp_half_touches = fields.Decimal()
    opp_half_touches_ratio = fields.Decimal()
    non_penalty_goals = fields.Decimal()
    long_balls_successful_p90 = fields.Decimal()
    conversion_rate = fields.Decimal()
    picking_up_second_balls = fields.Decimal()
    matches_count = fields.Decimal()
    average_minutes = fields.Decimal()

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/data/"
        else:
            self_link = "/data/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'data'



class XMLModelsPassClusterSchema(Schema):
    id = fields.Integer()
    pos_x = fields.Integer()
    pos_x_target = fields.Integer()
    pos_y = fields.Integer()
    pos_y_target = fields.Integer()
    creation_time = fields.DateTime(dumponly=True)

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/data/"
        else:
            self_link = "/data/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'data'


class XMLModelsTeamPassClusterSchema(Schema):
    id = fields.Integer()
    team_instatid = fields.Integer()
    cluster_id = fields.Integer()
    count = fields.Integer()
    creation_time = fields.DateTime(dumponly=True)

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/data/"
        else:
            self_link = "/data/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'data'


class XMLModelsPassSchema(Schema):
    id = fields.Integer()
    match_instatid = fields.Integer()
    team_instatid = fields.Integer()
    player_instatid = fields.Integer()
    zone = fields.String()
    zone_target = fields.String()
    time = fields.Decimal()
    time_target = fields.Decimal()
    type = fields.String()
    pos_x = fields.Integer()
    pos_x_target = fields.Integer()
    pos_y = fields.Integer()
    pos_y_target = fields.Integer()
    creation_time = fields.DateTime(dumponly=True)

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/data/"
        else:
            self_link = "/data/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'data'

class XMLModelsPassTeamSchema(Schema):
    id = fields.Integer()
    match_instatid = fields.Integer()
    team_instatid = fields.Integer()
    zone = fields.String()
    zone_target = fields.String()
    type = fields.String()
    count = fields.Integer()
    creation_time = fields.DateTime(dumponly=True)

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/data/"
        else:
            self_link = "/data/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'data'

class XMLModelsCategoriesSchema(Schema):
    id = fields.Integer()
    model_name = fields.String()
    category = fields.String()

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/data/"
        else:
            self_link = "/data/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'data'


class XMLSeasonPercentilesSchema(Schema):
    id = fields.Integer()
    league_tier = fields.Integer()
    season = fields.String()
    percentile = fields.Float()
    primary_position = fields.String()
    total_goals = fields.Integer()
    average_x = fields.Float()
    average_y = fields.Float()
    shots_p90 = fields.Float()
    box_shots_p90 = fields.Float()
    outside_box_shots_p90 = fields.Float()
    scoring_contribution_p90 = fields.Float()
    percentage_of_own_created_shots = fields.Float()
    scoring_percentage = fields.Float()
    touches_in_box = fields.Float()
    assists_p90 = fields.Float()
    key_passes_acc_p90 = fields.Float()
    throughballs_p90 = fields.Float()
    lost_balls_p90 = fields.Float()
    passes_p90 = fields.Float()
    passes_completion = fields.Float()
    acc_passes_to_the_box_p90 = fields.Float()
    passes_to_the_box_p90 = fields.Float()
    danger_zone_entries_p90 = fields.Float()
    long_balls_p90 = fields.Float()
    long_balls_completion = fields.Float()
    crosses_succ_p90 = fields.Float()
    crosses_completion = fields.Float()
    dribbles_succ_p90 = fields.Float()
    dribbles_completion = fields.Float()
    space_defending_p90 = fields.Float()
    tackles_completion = fields.Float()
    padj_tackles_p90 = fields.Float()
    padj_interceptions_p90 = fields.Float()
    won_balls_p90 = fields.Float()
    won_balls_opp_half_p90 = fields.Float()
    challenges_p90 = fields.Float()
    challenges_succ_p90 = fields.Float()
    challenges_succ_rate = fields.Float()
    long_balls_received_p90 = fields.Float()
    air_challenges_succ_rate = fields.Float()
    air_challenges_p90 = fields.Float()
    air_challenges_succ_p90 = fields.Float()
    own_created_shots_p90 = fields.Float()
    acc_passes_p90 = fields.Float()
    crosses_p90 = fields.Float()
    dribbles_p90 = fields.Float()
    won_challenges_p90 = fields.Float()
    won_air_challenges_p90 = fields.Float()
    opp_half_touches = fields.Float()
    opp_half_touches_ratio = fields.Float()
    non_penalty_goals = fields.Float()
    long_balls_succ_p90 = fields.Float()
    conversion_rate = fields.Float()
    picking_up_second_balls_p90 = fields.Float()
    xG = fields.Float()
    xA = fields.Float()
    xG_p90 = fields.Float()
    xG_per_shot = fields.Float()
    xGA_p90 = fields.Float()
    np_xG = fields.Float()
    np_xA = fields.Float()
    np_xG_p90 = fields.Float()
    np_xG_per_shot = fields.Float()
    np_xGA_p90 = fields.Float()
    
    
    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/data/"
        else:
            self_link = "/data/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'data'


class XMLModelsMatchTeamSchema(Schema):
    id = fields.Integer()
    match_instatid = fields.Integer()
    team_instatid = fields.Integer()
    season = fields.String()
    creation_time = fields.Date()
    match_date = fields.Date()
    minutes = fields.Float()
    points = fields.Integer()
    xPoints = fields.Integer()
    xPoints_ours = fields.Integer()
    goals_for = fields.Integer()
    goals_against = fields.Integer()
    xG_for_p90 = fields.Float()
    xG_against_p90 = fields.Float()
    shots_for_p90 = fields.Float()
    shots_against_p90 = fields.Float()
    shots_for = fields.Integer()
    shots_against = fields.Integer()
    shots_on_target = fields.Integer()
    shots_on_target_againts = fields.Integer()
    headed_shots = fields.Integer()
    dangerzone_shots_p90 = fields.Float()
    dangerzone_shots = fields.Float()
    dangerzone_shots_against_p90 = fields.Float()
    xG_per_shot = fields.Float()
    xG_per_shot_against = fields.Float()
    average_distance_of_shots = fields.Float()
    average_distance_of_shots_against = fields.Float()
    passes_p90 = fields.Float()
    passes_succes_rate = fields.Float()
    forward_passes = fields.Float()
    backward_passes = fields.Float()
    total_passes_into_the_box_p90 = fields.Float()
    total_passes_into_the_box = fields.Float()
    acc_passes_into_the_box_p90 = fields.Float()
    acc_passes_into_the_box = fields.Float()
    passes_to_the_box_against_p90 = fields.Float()
    dangerzone_entries_p90 = fields.Float()
    dangerzone_entries = fields.Float()
    crosses_p90 = fields.Float()
    shots_from_crosses = fields.Float()
    avg_number_of_passes_before_shot = fields.Float()
    passes_in_buildup = fields.Float()
    passes_in_middle_third = fields.Float()
    passes_in_final_third = fields.Float()
    long_balls = fields.Float()
    lost_balls = fields.Float()
    touches_inside_box = fields.Float()
    touches_inside_box_p90 = fields.Float()
    events_inside_box = fields.Float()
    buildup = fields.Float()
    maintenance = fields.Float()
    counter_attacking = fields.Float()
    sustainable_threat = fields.Float()
    fast_tempo = fields.Float()
    high_press = fields.Float()
    tts_for = fields.Float()
    tts_against = fields.Float()
    tts_difference = fields.Float()
    tts_tackle = fields.Float()
    tts_interception = fields.Float()
    tts_turnover = fields.Float()
    won_balls_opp_half = fields.Float()
    won_balls_final_third = fields.Float()
    won_balls_middle_third = fields.Float()
    won_balls_own_third = fields.Float()
    avg_height_of_turnover = fields.Float()
    tackles_total = fields.Float()
    tackles_success_rate = fields.Float()
    headers_total = fields.Float()
    headers_success_rate = fields.Float()
    challenges_total = fields.Float()
    challenges_success_rate = fields.Float()
    tackles_padj = fields.Float()
    interceptions = fields.Float()
    interceptions_padj = fields.Float()
    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/data/"
        else:
            self_link = "/data/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'data'


class JSONPassingCentersMatchTeamSchema(Schema):
    id = fields.Integer()
    league_instatid = fields.Integer()
    season = fields.String()
    team_instatid = fields.Integer()
    match_instatid = fields.Integer()
    passes = fields.String()
    players = fields.String()
    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/data/"
        else:
            self_link = "/data/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'data'


class JSONSeasonPlayerSchema(Schema):
    id = fields.Integer()
    league_instatid = fields.Integer()
    season = fields.String()
    player_name = fields.String()
    player_instatid = fields.Integer()
    team_instatid = fields.Integer()
    json = fields.String()
    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/data/"
        else:
            self_link = "/data/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'data'


class JSONMatchTeamSchema(Schema):
    id = fields.Integer()
    league_instatid = fields.Integer()
    season = fields.String()
    match_instatid = fields.Integer()
    team_instatid = fields.Integer()
    json = fields.String()
    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/data/"
        else:
            self_link = "/data/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'data'


class JSONSeasonPlayerSchema(Schema):
    id = fields.Integer()
    league_instatid = fields.Integer()
    season = fields.String()
    player_instatid = fields.Integer()
    team_instatid = fields.Integer()
    json = fields.String()
    player_name = fields.String()

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/data/"
        else:
            self_link = "/data/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'data'


class XMLPassesSonarSeasonPlayerSchema(Schema):
    id = fields.Integer()
    league_instatid = fields.Integer()
    season = fields.String()
    team_instatid = fields.Integer()
    player_instatid = fields.Integer()
    data = fields.String()

    # self links
    def get_top_level_links(self, data, many):
        if many:
            self_link = "/data/"
        else:
            self_link = "/data/{}".format(data['id'])
        return {'self': self_link}

    class Meta:
        type_ = 'data'
