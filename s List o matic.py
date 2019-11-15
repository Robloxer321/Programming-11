animal_list = ["cat", "dog", "rat", "salmon"]
print ("Look at this list of animals"+str(animal_list))

def list_o_matic(animalcode):
  if animalcode == "":
    animalcode=animal_list.pop()
    print (animalcode, "was popped from da list")
  elif animalcode in animal_list:
    print (animalcode, "was removed from da list")
    return animal_list.remove(animalcode)
  else:
    print (animalcode, "was appended to da list")
    return animal_list.append(animalcode)

while animal_list:
  program_flow=input("Enter a animal name or 'quit': ")
  if program_flow.startswith ("q"):
    break
  else:
    print("Look at da list of animals"+str(animal_list))
    pump=list_o_matic(program_flow.upper())
    print (animal_list)

print ("It has ended, Bye Bye")
               
               
               
        
