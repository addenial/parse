# nmap-xml2csv-OSinfo.py
Script to parse nmap XML fields related to enumerated OS information into CSV file.

Fields of interested parsed into following:

`IP,OS family,vendor,osgen,type,os match name,accuracy`


#Examples

Parse and print to screen only:
>python ./nmap-xml2csv-OSinfo.py -f nmap-output.xml -p

Parse and save result to CSV:
>python ./nmap-xml2csv-OSinfo.py -f nmap-output.xml -csv parsed-OS-info.csv

# nmap-xml2csv-services.py

`IP,port,proto,service,product,version,extra info,os type,hostname`

#Examples

Parse and print to screen only:
>python ./nmap-xml2csv-services.py -f nmap-sv.xml -p

Parse and save result to CSV:
>python ./nmap-xml2csv-services.py -f nmap-sv.xml -csv services.csv



# nmap-xml2csv-icmp.py

`IP` or `subnet-/24`

#Examples

Parse and print to screen only:
>python ./nmap-xml2csv-icmp.py -f nmap-pings.xml -p

Parse and save result to CSV:
>python ./nmap-xml2csv-icmp.py -f nmap-pings.xml -csv pingz.csv

Parse and find active subnets:
>python ./nmap-xml2csv-icmp.py -f nmap-pings.xml -subs

Parse and find active subnets, save to csv:
>python ./nmap-xml2csv-icmp.py -f nmap-pings.xml -subs -csv active-subnets.csv



