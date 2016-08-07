from sqlalchemy.engine import create_engine
from sqlalchemy import schema, types

engine = create_engine('sqlite:///:memory:', echo=True)
metadata = schema.MetaData(bind=engine, reflect=False)

schema.Table('sugar_content', metadata, 'drink_name', 'sugar', 'serving_size', 'num_servings')