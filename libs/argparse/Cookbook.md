
**Example**
```
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print args.accumulate(args.integers)
```


**Parse String and int**

```
parser = argparse.ArgumentParser('usage %prog -H <target host> -p <target port>')
parser.add_argument('-H', type=str, dest='targetHost', help='Specify target host')
parser.add_argument('-p', type=int, dest='targetPort', help='Specify target port')

args = parser.parse_args()
print(args.targetHost)
print(args.targetPort)
```