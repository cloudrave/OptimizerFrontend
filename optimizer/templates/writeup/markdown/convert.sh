#!/bin/bash

echo "Converting $1 into HTML and moving to writeup templates directory"

# e.g.  "final.md"  -->  "final"
prefix=${1%\.md}

htmlending=".html"
tofile="../$prefix$htmlending"

printf %"s\n" "Converting to ../$prefix$htmlending"

printf %"s\n" "{% extends \"writeup/base.html\" %}" "{% block writeup %}" > $tofile
multimarkdown $1 >> $tofile
printf %"s\n" "{% endblock %}" >> $tofile

echo "Complete"
