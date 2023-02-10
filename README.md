# Step 1

there is `sample.csv` file here

`./manage.py runserver` to start django server

`celery -A djrf worker -B -l info` to start celery for parsing `csv`

`curl -F "image=@sample.csv" http://localhost:8000/upload/sample.csv -X PUT` by curl you can upload csv file

# Step 2

`http://localhost:8000/demo/` go to this location and you will find filter change it so
