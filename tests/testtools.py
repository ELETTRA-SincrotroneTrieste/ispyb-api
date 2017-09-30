from ispyb.connection import Connection, get_connection_class
import os

def get_connection(dict_cursor=False):
    ConnClass = get_connection_class(Connection.ISPYBMYSQLSP)
    conf_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../conf/config.cfg'))
    return ConnClass(conf='dev', dict_cursor=dict_cursor, conf_file=conf_file)
