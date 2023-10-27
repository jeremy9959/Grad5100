import pandas as pd
import sqlalchemy as sqla
import os
import glob

## reads the csv files of the top chef data and uploads them to tables in the RDS instance

print("pandas version = {}".format(pd.__version__))
print("sqlalchemy version = {}".format(sqla.__version__))
files = glob.glob("csv/*.csv")
tab = {}
for x in files:
    df = pd.read_csv(x)
    header = list(df.columns)
    try:
        header.remove("Unnamed: 0")
    except:
        pass
    tab[x.split(".")[0]] = df[header].set_index("index")

engine = sqla.create_engine(
    "mysql+pymysql://admin:HMSHotspur16guns@database-1.cwvjklnp4wu3.us-east-1.rds.amazonaws.com",
    echo=False,
)

with engine.connect() as conn:
    conn.execute(sqla.text("create database topChef;"))
    conn.execute(sqla.text("use topChef;"))
    for x in tab:
        tab[x].to_sql(x, conn, if_exists="replace")

# %%
