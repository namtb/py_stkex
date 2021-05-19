import pandas
import config.environment as env
from models.models import AlgorithmParameter



def get_all_algorithm_parameters ():
    query = env.session.query(AlgorithmParameter)
    result = pandas.read_sql(query.statement, env.session.bind)
    return result

def get_algorithm_parameters_for_tickerid (ticker_id=None):
    if (ticker_id is None):
        return False

    query = env.session.query(AlgorithmParameter).filter(AlgorithmParameter.ticker_id == ticker_id)
    result = pandas.read_sql(query.statement, env.session.bind)
    return result