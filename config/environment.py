import config.connectDB as connectDB
from sqlalchemy.orm import sessionmaker

engine = connectDB.connect_db_sqlalchemy()
Session = sessionmaker(bind=engine)
session = Session()

default_url = "https://iboard.ssi.com.vn/bang-gia/vn30"