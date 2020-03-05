#! /bin/bash

output=$1
doc1=$2
doc2=$3

pdftk merge $2 $3 cat output $1
