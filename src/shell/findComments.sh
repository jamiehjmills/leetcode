#!/usr/bin/env bash

# to read existing files
location=$(pwd)
csvFile=$location/text.csv
txtFile=$location/test.txt

# to save into a new csv file
updatedFile=$location/updated.csv
rm -rf $updatedFile
touch $updatedFile && chmod u+x $updatedFile

# read a txt file and find comments for a given domain
findComments() {

  txtFile=$1
  domain=$2

  # make an array from the given text file
  txtList=()
  while IFS= read -r line; do
    txtList+=("$line")
  done <$txtFile

  # find the line # in the given text file
  index=$(grep -wn $domain$ $txtFile | cut -d: -f1)
  index=$((index - 1))

  if [[ $index == -1 ]]; then
    echo "No comments: the domain is NOT found in the text file"
    return 1
  fi

  stack=()

  for i in $(seq $index 0); do
    firstLetter=${txtList[$i]:0:1}
    preIndex=$((i - 1))

    # if empty line
    if [[ ! ${txtList[$i]} ]]; then
      break
    fi

    if [[ $firstLetter == "#" ]]; then
      words=$(echo ${txtList[$i]} | tr -d "#")
      stack+=("$words ")
      if [[ ${txtList[$preIndex]:0:1} != "#" ]]; then
        break
      fi
    fi

  done

  #convert the stack array to a string
  comments=""
  for i in $(seq ${#stack[*]} 0); do
    comments+=${stack[$i]}
  done

  echo $comments

}

# read a csv file and find comments for a given domain and save them to a new csv file
domainList=($(cat $csvFile))

for i in $(seq 0 ${#domainList[@]}); do
  if [[ $i -gt 0 ]]; then
    domain=($(echo ${domainList[$i]} | tr "," " ")) # .test.com.au or testtt.com.au
    echo $domain
    if [[ ! -z $domain ]]; then
      comments=$(findComments $txtFile $domain)
      echo "$domain,$comments" >>$updatedFile
    fi
  fi
done
