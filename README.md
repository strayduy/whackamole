# whackamole

This is an app to keep politicians honest.

To run the server run "python manage.py runserver"

The data is being loaded into the rsync_data directory using the following command:
rsync -avz --delete --delete-excluded --exclude-from=rsync_data/exclusions.txt govtrack.us::govtrackdata/congress/113/votes rsync_data/.

The data is being parsed by running:
python load_db/load_votes.py

The data is being uploaded to the db using the following commands:

mongoimport -h $WHACKAMOLE_DB_HOST -d $WHACKAMOLE_DB_NAME -c senate_votes -u $WHACKAMOLE_DB_USER -p $WHACKAMOLE_DB_PASSWORD --file /tmp/votes/senate.json

mongoimport -h $WHACKAMOLE_DB_HOST -d $WHACKAMOLE_DB_NAME -c senate_reps -u $WHACKAMOLE_DB_USER -p $WHACKAMOLE_DB_PASSWORD --file /tmp/reps/senate.json
