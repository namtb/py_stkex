import pandas
import config.environment as env
from tables.security import Security

def get_all_security():
    query = env.session.query(Security)
    result = pandas.read_sql(query.statement, env.session.bind)
    return result

def get_security_by_ticketId(ticket_id):
    query = env.session.query(Security).filter(Security.ticker_id == ticket_id)
    result = pandas.read_sql(query.statement, env.session.bind)
    return result

def get_security_by_sub_industry_id (sub_industry_id):
    query = env.session.query(Security).filter(Security.sub_industry_id == sub_industry_id)
    result = pandas.read_sql(query.statement, env.session.bind)
    return result

def get_security_by_industry_id (industry_id):
    match_string = industry_id+"%"
    query = env.session.query(Security).filter(Security.sub_industry_id.like(match_string))
    result = pandas.read_sql(query.statement, env.session.bind)
    return result


def get_security_by_industry_group(industry_group):
    match_string = industry_group+"%"
    query = env.session.query(Security).filter(Security.sub_industry_id.like(match_string))
    result = pandas.read_sql(query.statement, env.session.bind)
    return result


def get_security_by_sector(sector):
    match_string = sector+"%"
    query = env.session.query(Security).filter(Security.sub_industry_id.like(match_string))
    result = pandas.read_sql(query.statement, env.session.bind)
    return result

def get_all_security_hose():
    query = env.session.query(Security).filter(Security.exchange_id == 1)
    result = pandas.read_sql(query.statement, env.session.bind)
    return result