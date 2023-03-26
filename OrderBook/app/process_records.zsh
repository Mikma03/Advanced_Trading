#!/bin/zsh

# Function to clear the content of data.json
clear_data_json() {
    echo '[]' > data.json
    python3 order_book.py
}

# Function to remove a specific record based on the id
remove_record() {
    local file=$1
    local id=$2

    local records=$(cat $file | jq "map(select(.order.id != $id))")
    echo "${records}" > $file
    python3 order_book.py
}

# Function to edit a specific record based on the id and new attribute values
edit_record() {
    local file=$1
    local id=$2
    local updated_record=$3

    local records=$(cat $file | jq "map(if .order.id == $id then ${updated_record} else . end)")
    echo "${records}" > $file
    python3 order_book.py
}

# Function to append data to a JSON file
append_data() {
    local file=$1
    local formatted_line=$2

    content=$(cat $file)
    content=${content%?} # Remove the trailing closing square bracket

    if [[ $content != '[' ]]; then
        content="${content},"
    fi

    content="${content}${formatted_line}]"
    echo "${content}" > $file
}

# Create data.json and history.json with an empty JSON array if they do not already exist
[[ ! -f "data.json" ]] && echo '[]' > data.json
[[ ! -f "history.json" ]] && echo '[]' > history.json

# Read data from standard input constantly
while read -r line; do

    # Clear data.json if the input is 'clear'
    if [[ $line == "clear" ]]; then
        clear_data_json
        continue
    fi

    
    if [[ $line == "remove"* ]]; then
        id=$(echo $line | jq '.id')
        remove_record "data.json" "$id"
        remove_record "history.json" "$id"
        continue
    fi


    if [[ $line == "edit"* ]]; then
        id=$(echo $line | jq '.id')
        updated_record=$(echo $line | jq '.record')
        edit_record "data.json" "$id" "$updated_record"
        edit_record "history.json" "$id" "$updated_record"
        continue
    fi

    # Format the input line
    formatted_line=$(echo $line | perl -pe 's/"type":\s*"(\w+)"/"type": "\u$1"/' | perl -pe 's/"direction":\s*"(\w+)"/"direction": "\u$1"/')


    # Append the new record to data.json and history.json
    append_data "data.json" "$formatted_line"
    append_data "history.json" "$formatted_line"
    python order_book.py

done
