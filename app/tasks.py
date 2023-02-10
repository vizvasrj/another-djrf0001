import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djrf.settings")
django.setup()

from celery import shared_task
import pandas as pd
import io
from app.models import DemoModel

@shared_task
def someting(file_obj):
    print("Herer", file_obj)
    df = pd.read_csv(file_obj)

    print(df.columns)
    for i, row in df.iterrows():
        try:
            # print(i, row["Year"], row["Value"], row["levels"], row["code"], row["name"], row["Units"], row["Variable_code"], row["Variable_name"] )
            year = row.get("Year")
            levels = row.get("levels")
            code = row.get("code")
            name = row.get("name")
            units = row.get("Units")
            variable_code = row.get("Variable_code")
            variable_name = row.get("Variable_name")

            demo = DemoModel.objects.create(
                year=year, levels=levels, code=code,
                name=name, units=units, 
                variable_code=variable_code, 
                variable_name=variable_name,
            )
            print(demo)

            pass
        except KeyError:
            print(row)

    return True
