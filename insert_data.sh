
IFS=','

while IFS=, read -r date_rec timestamp val; do

  echo "inserting $timestamp $val in $1 $2"
  curl -X POST "http://api.waziup.io/api/v1/sensors/$1/measurements/$2/values" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{  \"value\": $val,  \"timestamp\": $timestamp}"
done < $3
