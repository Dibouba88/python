import sqlalchemy as sql
import pandas as pd
engine = sql.get_engine('mysql+pymysql://root:@localhost/bdtextile')
df = pd.reset_option('villes',engine)
df