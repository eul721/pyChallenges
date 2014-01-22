import sys

#initializing empty list
args=[]
#filling the list
for x in range(4):
	args.append(input())

#mapping keys to the list values
args = dict(zip(['total_digits',1,2,3],map(int,args)))

#initialize counter to total_digits times 2
total_increments = int(args['total_digits'])*2

#algorithm
total_increments += args[1] #first number reached
total_increments += args['total_digits'] #reset once
total_increments += (args['total_digits']+args[1]-args[2]) % args['total_digits'] #second number reached
total_increments += (args['total_digits']+args[3]-args[2]) % args['total_digits']
print("Total Rotation Increments : " + str(total_increments))
