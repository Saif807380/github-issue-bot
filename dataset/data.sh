#!/bin/bash

declare -a languages=("python" "javascript" "java")
declare -a labels=("bug" "documentation" "docs" "enhancement" "feature" "question" "design" "improvement" "help")

for language in "${languages[@]}"
do
  echo "Current Language: ${language}"
  for label in "${labels[@]}"
  do
    echo "Current Label: ${label}"
    python data.py $language $label
  done
done
