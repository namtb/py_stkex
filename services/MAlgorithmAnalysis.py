import pandas
import config.environment as env
from models.models import AlgorithmAnalysis



def get_all_algorithm_analysis ():
    query = env.session.query(AlgorithmAnalysis)
    result = pandas.read_sql(query.statement, env.session.bind)
    return result