import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-start','-a')
parser.add_argument('-end','-b')
args = parser.parse_args()
print(args.a,args.b)

print('Hello World')
print('hello Shwetank')