#!/bin/bash

# Find code, title, instructor (from file)
code=$(sed -n 1p .noteinit)
title=$(sed -n 2p .noteinit)
instructor=$(sed -n 3p .noteinit)

# Find day number
day=1
dayPadded=$(seq -f "%02g" $day $day)

# Increment until date not found
while [ -e ${dayPadded}* ]
do
    day=$(expr $day + 1)
    dayPadded=$(seq -f "%02g" $day $day)
done

# Find date
date=$(date '+%Y-%m-%d')

echo -e "# $code $title with $instructor - Day $day ($date)\n\n---\n\n" > $dayPadded-$date.md
