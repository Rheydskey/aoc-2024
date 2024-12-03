#!/bin/bash

file=$(cat "2")
regex="mul\([0-9]+,[0-9]+\)"

r=0
b=$(echo $file | grep -oE $regex)
for i in $b; do
  trstr="${i#mul(}"
  trend="${trstr%)}"
  IFS=',' read -ra mults <<< "$trend"
  op1="${mults[0]}"
  op2="${mults[1]}"
  r=$((r + (op1 * op2)))  
done

echo $r;

