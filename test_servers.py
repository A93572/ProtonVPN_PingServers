#!/usr/bin/python
import argparse, os, random, re, pyping, operator, sys

# ping function - REQUIRES pyping
# install with pip install pyping
def do_ping(host):
    phost = pyping.ping(host)
    return phost.avg_rtt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("region", type=str,
            help="ProtonVPN Region Code - Use ALL for ALL files")
    parser.add_argument("-c", "--connect", help="Connect to VPN",
            action="store_true")
    parser.add_argument("-v", "--verbose", help="Increase output verbosity",
            action="store_true")
    args = parser.parse_args()
    print("Testing latencey for '%s' Servers" % (args.region.lower()))
    if (args.region.lower()) == "all":
       region = ""
    else:
       region = (args.region.lower())
    # list for tuples
    case_list = []
    # create list of all files in current dir
    files = [f for f in os.listdir('.') if os.path.isfile(f) if f.endswith('.ovpn')]
    # iterate through file list
    for f in files:
        if (region) in f:
            with open(f,'r') as inF:
                for line in inF:
                    # find line containing ip
                    if 'remote ' in line:
                        # extract only the ip
                        ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', line )
                        # convert to str
                        ip = ''.join(ip)
                        # create tuple from collected data (filename, ipm latency
                        case = ( str(f), str(ip), do_ping(ip) )
                        print(case)
                        # append the list
                        case_list.append(case)
    # sort list of tuples for lowest latency
    result = sorted(case_list, key=lambda case: float(case[2]))
    # add lowest list item and convert to string
    if len(result) == 0:
        sys.exit("No servers match %s. Region is case sensitive, check region" % (args.region.lower()))
    result = str(result[0])
    # convert to tuple so you can get the corresponding hostname
    lowest = eval(result)
    #print lowest latency 
    print(lowest[0])
    print(lowest[1])
    print(lowest[2])
    
    if args.connect:
        print("Connecting")

if __name__ == "__main__":
    main()
