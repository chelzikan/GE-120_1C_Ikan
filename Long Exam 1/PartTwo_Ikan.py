print ("Leveling Computation")

# create a sentinnel controlled loop
counter = 1 
lines = []

levelling_table = 0
total_distance = 0
tp_counter = 0


def floatInput (prompt):
    '''
    makes your value in float type

    input - int, float

    output - float
    '''
prompt = float ()


counter = 1 
lines = []

while True:
    print()
    print("Line {}".format(counter))  




#
    invalid_input = False
    while not (invalid_input):
        Elevation = input("Elevation: ")
        if invalid_input:
            print ("Invalid Input")
            continue
        if not (invalid_input):
            break
    Foresight = float (input("Foresight: "))
    Backsight = float (input("Backsight: "))
    
    
    if Elevation >= 0 and Backsight >= 0:
        HI = 'HI'.format(Elevation + Backsight)
    elif HI >= 0 and Foresight >= 0 :
        RunningElevation = 'Running Elev'.format(float(HI - Foresight))
    else:
        HT1  = "INVALID"

    
    line = (''.format(counter, counter + 1), '{:.3f}'.format(float(Foresight)), Backsight)
    lines.append(line)

   
    yn = input("Add new line? (y/n): ")
    if yn.lower() == "yes" or yn.lower() == "y":
        counter += 1
        continue
    else:
        break


print("\n\n")
print('{: ^20}'.format("LEVELING COMPUTATION"))



    
# (TT) idkkk (TT)