#!/bin/bash
# $(date +%F) gives the date in YYYY-MM-DD format
# output="summary_$(date +%F).txt"

while true
do
echo "--------------------------------------------------------"
echo "1. Analyze .log and .txt files for errors in a directory"
echo "2. Exit"
echo "--------------------------------------------------------"
read -p "Choose an option: " opt

if [ "$opt" == 1 ]
then

read -p "Enter a path: " path
read -p "Enter a path to save the results: " spath

output="$spath/summary_$(date +%F).txt"
echo "Error summary: " > "$output"

# Add .txt and .log detection before starting and exit if none found
# echo "No .txt or .log files found! Returning to menu."

for file in "$path"/*.txt "$path"/*.log
do
# Skips the output file to prevent an infinite loop
if [ "$file" == "$output" ]
then
continue
fi

while read line
do

if [[ "$line" == *Error* ]] || [[ "$line" == *error* ]] || [[ "$line" == *ERROR* ]] || [[ "$line" == *Failed* ]] || [[ "$line" == *failed* ]] || [[ "$line" == *FAILED* ]]
then
echo "$file: $line" >> "$output"
fi
done < "$file"
done

echo "Analysis completed. Results have been saved to $output"

elif [ "$opt" == 2 ]
then exit

else echo "Wrong input"
fi
done
