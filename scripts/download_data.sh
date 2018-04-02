#!/bin/bash

wget -r http://prezydent2000.pkw.gov.pl/gminy/obwody.html -A xls -np -P ../data/
mv ../data/prezydent2000.pkw.gov.pl/gminy/ ../data/gminy/
mv ../data/gminy/obwody/ ../data/obwody/
wget -r http://prezydent2000.pkw.gov.pl/gminy/gminy.html -A xls -np -P ../data/
mv ../data/prezydent2000.pkw.gov.pl/gminy/ ../data/
rm -rf ../data/prezydent2000.pkw.gov.pl
mkdir -p ../output/województwa
mkdir -p ../output/okręgi
mkdir -p ../output/gminy

