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




Parsing multiple files at once, print to screen  
>python3 .\nmap-xml2csv-services.py -f nmaps-sv.xml nmap-sv2.xml nmap-sv3.xml -p

Parse every .xml file in current directory, print to screen
>python3 ./nmap-xml2csv-services.py -f '*' -p
>
>python ./nmap-xml2csv-services.py -f * -p

Parse every .xml file in current directory and save results to CSV 
>python3 ./nmap-xml2csv-services.py -f '*' -csv services.csv
>
>python ./nmap-xml2csv-services.py -f * -csv services.csv

#.
#remove duplicates example 
linux...
>cat services.csv | sort -r | uniq 

#windows
>type services.csv | sort /r /unique


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


Parse every .xml file in current directory, print to screen:
>python3 ./nmap-xml2csv-icmp.py -f '*' -p

>python ./nmap-xml2csv-icmp.py -f * -subs


Parse every .xml file in current directory, round to nearest /24, save results to CSV: 
>python3 ./nmap-xml2csv-icmp.py -f '*' -subs -csv active-subnets.csv

>python ./nmap-xml2csv-icmp.py -f * -subs -csv active-subnets.csv

#to remove any remaining duplicates..

#linux
>cat active-subnets.csv | sort -r | uniq 

#windows
>type active-subnets.csv | sort /r /unique

#
# ports.py
displays open ports from hosts. saves results to "f1____.log"

`python ports.py -f * -p `


linux - show sorted uniques, prep csv for other tooling example:

`cat f1____.log | sort -n | uniq`

`cat f1____.log | sort -n | uniq | tr '\r' ',' | tr --delete '\n'`

`cat f1____.log | sort -n | uniq  | tr '\n' ',' `


windows - show uniques:

`type f1____.log | sort /unique `



#



# masscan_parse_full.py
Parse masscan xml output into CSV 

examples-

single file parse:
>python masscan_parse_full.py -f massPP.xml

single file parse, display to screen, also save in CSV output file
>python masscan_parse_full.py -f massPP.xml -o outt.csv

parse every .xml masscan result file in current directory, display combined output
>python masscan_parse_full.py -f '*'

>python masscan_parse_full.py -f '*' -o outt.csv

#good luck!
