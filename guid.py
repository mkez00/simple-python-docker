import uuid
import sys

count = 4
if len(sys.argv)>1:
	count = int(sys.argv[1])

for num in range(0,count):
	print(uuid.uuid4())