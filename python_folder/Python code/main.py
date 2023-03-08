#Experession calculator
#By Santino J. Tomasi
#Beta


list_beta = []


def First_half():
    
    inital_in = input()
    
    inc = 0 
    
    length = len(inital_in)
    
    temp_front = None
    
    while length > inc:
        
        
        try:
            
            if inital_in[inc] != ".":
                
                int(inital_in[inc])
            
            if temp_front == None:
                
                temp_front = inc
            
            if inc+1 == length:
                
                list_beta.append(inital_in[temp_front:inc+1])
                
                break
                
            
            inc+=1
            
        except ValueError:
            
            list_beta.append(inital_in[temp_front:inc])
            
            temp_front = None
            
            list_beta.append(inital_in[inc])
            
            
            inc+=1
            
            
def main():
    First_half()
    
    print(list_beta)
    

if __name__ == "__main__":
    main()