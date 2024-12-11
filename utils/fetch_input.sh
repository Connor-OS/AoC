
# Check if year and day arguments are provided
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <year> <day>"
  exit 1
fi

YEAR=$1
DAY=$2

# Construct the URL
URL="https://adventofcode.com/$YEAR/day/$DAY/input"

# Set the output file name
OUTPUT_FILE="../${YEAR}/resources/day_${DAY}.txt"

# Fetch the data and export it to the file
curl -s "$URL" --cookie 'session=53616c7465645f5fc34da317fb53487d006eb5f3d62ff2216e50f80cc80378d1430f278c6ed57184ea9852cc07d77850e33637d252c893033a8f99ba6572b8e2' -o "$OUTPUT_FILE"

if [ $? -eq 0 ]; then
  echo "Data successfully fetched and saved to $OUTPUT_FILE"
else
  echo "Failed to fetch data from $URL"
  exit 1
fi