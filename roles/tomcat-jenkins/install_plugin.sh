#!/bin/bash
while read plugins.txt i;
do
    java -jar jenkins-cli.jar -s http://ci.upskillable.com/ install-plugin $i;
done
