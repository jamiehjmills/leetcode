
#!/usr/bin/env bash

# to read files
csvFile=/Users/hyojoomills/Development/shell/text.csv
txtFile=/Users/hyojoomills/Development/shell/test.txt

# to save into a new csv file
location=$(pwd)
updatedFile=$location/updated.csv
rm -rf $updatedFile
touch $updatedFile && chmod u+x $updatedFile


  #  for i in $(seq 0 ${#list[@]});
  #   do
  #     if [[ ${list[$i]} == $domain ]]; then
  #      #echo ${list[$i]}
  #      firstLetter=${list[$i]:0:1}
  #      index=$i
  #      while [[ $firstLetter != "#" && $index != 0 ]]
  #      do
  #        index=$((index-1))
  #        firstLetter=${list[$index]:0:1}
  #      done

  #       echo ${list[$index]}
  #       break

  #     fi
  #  done