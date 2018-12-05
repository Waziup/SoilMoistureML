
SENSORS=`curl --silent -X GET "http://api.waziup.io/api/v1/sensors?limit=1000" | jq -r ".[].id" 2>/dev/null`

N=`echo "$SENSORS" | wc -l`

echo "********** Getting data from $N sensors *********"
COUNTER=1

for i in $SENSORS; do
  
  MEAS=`curl --silent -X GET "http://api.waziup.io/api/v1/sensors/$i/measurements" | jq -r ".[].id" 2>/dev/null`
  COUNTER=$[$COUNTER +1]
  for j in $MEAS; do
    echo "$COUNTER: Getting data for sensor $i measurement $j"
    ./get_data.sh $i $j 
  done

done
