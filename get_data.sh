
FILENAME=$1-$2
echo "" > plots/$FILENAME.csv

# Accumulate datapoints
for i in {0..10}; do
  RES=`curl --silent -X GET "http://api.waziup.io/api/v1/sensors/$1/measurements/$2/values?limit=1000&offset=$(($i * 1000))" -H  "accept: application/json"`
  
  if [ "$RES" == "[]" ] 
  then
     break
  fi

  echo "$RES" | jq -r '(map(keys) | add | unique) as $cols | map(. as $row | $cols | map($row[.])) as $rows | $cols, $rows[] | @csv' 2>/dev/null >> plots/$FILENAME.csv 
  
  echo -n "."
done
COUNT=`cat plots/$FILENAME.csv | wc -l`
if [ $COUNT -gt 100 ]
then
   echo "Plotting plots/$FILENAME.png"
   #plot the graph
   gnuplot -e "filename='plots/$FILENAME'" plot 
else
   echo "Not enough data"
   rm plots/$FILENAME.csv
fi
echo
