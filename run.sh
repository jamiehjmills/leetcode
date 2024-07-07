#!/bin/bash
echo "running the shell script"

#list=(`git diff -U0 src/Udemy/LinkedList/time.py | grep '^[+-]' | grep -Ev '^(--- a/|\+\+\+ b/)'`)
list=(`git diff -U0 origin/master HEAD src/Udemy/LinkedList/test.py | grep '^[+-]' | grep -Ev '^(--- a/|\+\+\+ b/)'`)
length=${#list[@]}
#echo ${length}

new_list=()

for i in $(seq 0 $length);
do
  echo ${list[$i]}
  value=${list[$i]}
  char1=${value:1:1}

  if [[ $value == +* ]]; then
    if [[ $char1 != "" && $char1 != "#" ]]; then
      if [[ $char1 == "." ]]; then
         new_list+=(${value:2})
         #echo "correct"
      else
        new_list+=(${value:1})
        #echo "correct"
      fi
    fi
  fi
done

echo ${new_list[@]}

