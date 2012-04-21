#!/usr/bin/python

def main(path):
    with open(path) as f:
        for line in f:
            v,i,l = [float(x) for x in line.split()]
            r=(i!=0 and v/i or 0)
            p=v*i
            print ' & '.join([str(x) for x in [v,i,l,r,p]])


if __name__=="__main__":
    import sys
    main(*sys.argv[1:]) #arquivo
