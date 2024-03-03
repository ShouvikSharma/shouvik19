
## Check if the given list is sorted or not

list1 = [12,122,231,314]

def check_list_sorted (input_list):
    
    return all(input_list[i]<=input_list[i+1] for i in range(len(input_list)-1))

print(check_list_sorted(list1))

### Push zeros to the end

list2 = [1,1,2,12,12,12,43]

def push_zeros_to_end (input_list):
    for i in range(len(input_list)): 
        if input_list[i] == 0:
            input_list.append(input_list[i])
            input_list.remove(input_list[i])
                
            
    return  input_list

print(push_zeros_to_end(list2))


## Check if the given list is sorted or not

list1 = [12,122,231,314]

def check_list_sorted (input_list):
    
    return [input_list[i]<=input_list[i+1] for i in range(len(input_list)-1)]