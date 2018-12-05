
FILENAME=$1-$2
echo "" > plots/$FILENAME.csv
for i in {0..10}; do
  curl -X GET "http://api.waziup.io/api/v1/sensors/$1/measurements/$2/values?limit=1000&offset=$(($i * 1000))" -H  "accept: application/json" | jq -r '(map(keys) | add | unique) as $cols | map(. as $row | $cols | map($row[.])) as $rows | $cols, $rows[] | @csv' >> plots/$FILENAME.csv 
done

gnuplot -e "filename='plots/$FILENAME'" plot 

