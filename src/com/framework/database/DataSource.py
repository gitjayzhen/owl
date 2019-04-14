import cx_Oracle
import logging, time


class Database(object):
  '''
  Use this method to for DML SQLS :
  Inputs - Sql to be executed. Data related to that sql
  Returns - The last inserted, updated, deleted ID.
  '''

  def __init__(self, user, password, host, port, service_name, mode, *args):
    #mode should be 0 if not cx_Oracle.SYSDBA
    self.user = user
    self.password = password
    self.host = host
    self.port = port
    self.user = user
    self.service_name = service_name
    self.logger = logging.getLogger(__name__)
    try:
      self.mode = mode
    except:
      self.mode = 0
      self.logger.info(" Mode is not mentioned while creating database object")
    self.connection = None
    dsn = cx_Oracle.makedsn(self.host, self.port, self.service_name)
    self.connect_string = self.user + '/' + self.password + '@' + dsn
    try:
      self.connection = cx_Oracle.connect(self.connect_string, mode=self.mode,
                                          threaded=True)
      self.connection.stmtcachesize = 1000
      self.connection.client_identifier = 'my_app'
      self.cursor = self.connection.cursor()
      self.idVar = self.cursor.var(cx_Oracle.NUMBER)
    except cx_Oracle.DatabaseError, exc:
      error, = exc
      self.logger.exception(
        'Exception occured while trying to create database object : %s',
        error.message)
      raise exc

  def query(self, q):
    try:
      self.cursor.execute(q)
      return self.cursor.fetchall()
    except cx_Oracle.DatabaseError, exc:
      error, = exc
      self.logger.info(
        "Error occured while trying to run query: %s, error : %s", q,
        error.message)
      return error.message

  def dml_query(self, sql):
    try:
      self.cursor.execute(sql)
      self.connection.commit()
      return 1
    except Exception as e:
      self.logger.exception(e)
      return 0

  def dml_query_with_data(self, sql, data):
    """
    Use this method to for DML SQLS :
    Inputs - Sql to be executed. Data related to that sql
    Returns - The last inserted, updated, deleted ID.
    """
    try:
      self.cursor.execute(sql, data)
      self.connection.commit()
      return 1
    except Exception as e:
      self.logger.exception(e)
      return 0

  def update_output(self, clob, job_id, flag):
    try:
      q = "Select output from my_table where job_id=%d" % job_id
      self.cursor.execute(q)
      output = self.cursor.fetchall()
      # Checking if we already have some output in the clob for that job_id
      if output[0][0] is None:
        if flag == 1:
          self.cursor.execute("""UPDATE my_table
                                 SET OUTPUT = :p_clob
                                 ,job_status=:status WHERE  job_id = :p_key""",
                                 p_clob=clob, status="COMPLETED", p_key=job_id)
        else:
          self.cursor.execute("""UPDATE my_table
                                 SET OUTPUT = :p_clob
                                 ,job_status=:status WHERE  job_id = :p_key""",
                                 p_clob=clob, status="FAILED", p_key=job_id)
      else:
        self.cursor.execute("""UPDATE my_table
                               SET OUTPUT = OUTPUT || ',' || :p_clob
                               WHERE  job_id = :p_key""", p_clob=clob, p_key=job_id)
      self.connection.commit()
      rows_updated = self.cursor.rowcount
      return rows_updated
    except Exception as e:
      self.logger.exception(e)
      return 0

  def __del__(self):
    try:
      if self.connection is not None:
        self.connection.close()
    except Exception as e:
      self.logger.exception(
        "Exception while trying to close database connection object : %s", e)


  '''
  if __name__ == '__main__':
    db = Database('test', 'test', 'my_host', '1000', 'my_db', 0)
    columns = db.query('select * from my-table')
    print columns
  '''