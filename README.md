# nmap-xml2csv-OSinfo.py
Script to parse nmap XML fields related to enumerated OS information into CSV file.

Fields of interested parsed into following:

`IP,OS family,vendor,osgen,type,os match name,accuracy`


#Examples

Parse and print to screen only:

python ./nmap-xml2csv-OSinfo.py -f nmap-output.xml -p

Parse and save result to CSV:

python ./nmap-xml2csv-OSinfo.py -f nmap-output.xml -csv parsed-OS-info.csv



