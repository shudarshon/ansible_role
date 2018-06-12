#!/bin/bash
ipaddr=`cat ./hosts | cut -d ' ' -f 3- | grep -oE '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' | sed 's/^/"/' |sed 's/$/:8301",/' | sed '$ s/.$//'`
file=./templates/bootstrap.json.j2
#cat ./hosts | cut -d ' ' -f 3- | grep -oE '[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+' | sed 's/^/"/' |sed 's/$/:8301",/' | sed '$ s/.$//' > ./ip
#ipaddr=`cat ./ip`

sed -i '/start.*/,$d' $file
echo -e '\t"start_join": [\n' >> $file
echo "${ipaddr} ]}" >> $file
`which jq` . < $file | `which tee` ./tmp
mv ./tmp $file
#rm ./ip

# this script will result in the replacing and formatting private ip addresses from ansible hosts file as json format in specific file.
#"192.168.1.11:8301",
#"192.168.1.12:8301",
#"192.168.1.13:8301",
#"192.168.1.14:8301"
