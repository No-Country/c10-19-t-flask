import collections
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import ColumnProperty, RelationshipProperty, InstrumentedAttribute

db = SQLAlchemy()

class BaseModelMixin:
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self, data: dict):
        for k, v in data.items():
            #print(f'{k} = {v}\n')
            setattr(self, k, v)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()       

    @classmethod
    def get_all(cls, limit = None, page = None):
        query = cls.query # type: ignore
        if limit is not None:
            query = query.limit(limit)
        if page is not None:
            query = query.offset(int(page)*int(limit)) # type: ignore

        return query.all()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id) # type: ignore
        
    @classmethod
    def simple_filter_all(cls, **kwargs):
        return cls.query.filter_by(**kwargs).all() # type: ignore

    @classmethod
    def simple_filter(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first() # type: ignore

    @classmethod
    def avanze_filter_all(cls, json, limit = None, page = None):
        query = cls.query # type: ignore
        q = False
        for arg, value in json.items():
            key=None
            if '__' in arg:
                arg = arg.split('__')
                if len(arg) >= 2:
                    key = arg[1]
                    arg = arg[0]
            column = getattr(cls, arg, None)
            if isinstance(column, InstrumentedAttribute):
                q = True
                if isinstance(column.property, ColumnProperty):
                    sub_query = query.filter(column == value)
                    try :
                        value = datetime.strptime(value, r'%Y-%m-%d')
                        if key == 'desde': 
                            sub_query = query.filter(column > value)
                        elif key == 'hasta':
                            sub_query = query.filter(column < value)
                        else:
                            sub_query = query.filter(column == value)
                    except Exception:
                        pass
                    query = sub_query
                elif isinstance(column.property, RelationshipProperty):
                    model = column.property.entity.class_
                    query = query.join(model).filter(getattr(model, key).like(f'{value}%')) # type: ignore
        if limit is not None:
            query = query.limit(limit)
        if page is not None:
            query = query.offset(int(page)*int(limit)) # type: ignore
        return query.all() if q else []