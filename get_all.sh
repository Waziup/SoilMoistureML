
SENSORS=`curl -X GET "http://api.waziup.io/api/v1/sensors?limit=1000" | jq -r ".[].id"`

for i in $SENSORS; do

  MEAS=`curl -X GET "http://api.waziup.io/api/v1/sensors/$i/measurements" | jq -r ".[].id"`
  
  for j in $MEAS; do
    echo "\n\nGetting data for sensor $i measurement $j"
    ./get_data.sh $i $j
  done

done
