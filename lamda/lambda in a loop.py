lsit_of_lambdas = []
for i in range(5):
    lsit_of_lambdas.append(lambda a=i:a)
    
for j in lsit_of_lambdas:
    print(j())