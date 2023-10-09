from sqlalchemy import Column, Integer, String, ForeignKey, Uuid, Boolean
from sqlalchemy.orm import declarative_base, relationship
import json
from sqlalchemy.ext.declarative import DeclarativeMeta

base = declarative_base()

class Users(base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    public_id = Column(Uuid)
    email = Column(String(50))
    password = Column(String(250))
    first_name = Column(String(250))
    last_name = Column(String(250))
    org_name = Column(String(250))
    admin = Column(Boolean, default=False)
    image = Column(String(1000))
    banner = Column(String(1000))
    desc = Column(String(250)) 
    phone = Column(String(250)) 


class AlchemyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields

        return json.JSONEncoder.default(self, obj)
