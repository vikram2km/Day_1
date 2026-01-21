import logging
from collections import Counter

logging.basicConfig(level=logging.INFO,format='%(asctime)s, - %(levelname)s - %(message)s')

rotation_count=4
day1_list = [5, 3, 8, 3, 9, 1, 5, 7, 2, 8]
numbers_list = [12, 45, 2, 67, 45, 89, 34, 67, 23]
day1_nested_list = [[1, 2, [3, 4]], [5, 6], [7, [8, 9]]]
list_a = [1, 2, 3, 4, 5, 6, 7]
list_b = [5, 6, 7, 8, 9]
freq_list = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple', 'kiwi', 'kiwi', 'mango']
dict1 = {'a':3, 'b':2}
dict2 = {'b':1, 'c':5}


#Remove duplicates from a list
def remove_duplicates(lst_obj):
    logging.info(f'1.List After Removing Duplicates: {list(dict.fromkeys(lst_obj).keys())}')
   
#Find the second largest number   
def second_largest(lst_obj):
    unq=list(set(lst_obj))
    if len(unq)==1:
        logging.info(f'2.There is NO second largest element')
    else:
        logging.info(f'2.Second Largest: {sorted(unq)[-2]}')

#Reverse a list without slicing
def reverse_list(lst_obj):
    logging.info(f'3.Reversed List: {[lst_obj[i] for i in range(len(lst_obj)-1,-1,-1)]}')

#Rotate a list k times
def rotate_list(lst_obj,k):
    k=k%len(lst_obj) if k>len(lst_obj) else k
    logging.info(f'4.Rotated List {k} times: {lst_obj[-k:]+lst_obj[:-k]}')
    
#Flatten a nested list
def flatten_list(lst_obj):
    for i in lst_obj:
        (yield from flatten_list(i)) if isinstance(i,list) else (yield i)

#Set Problems:
        
#Find common elements between two lists
def common_elements(lst_obj1,lst_obj2):
    logging.info(f'6.Common Elements: {set(lst_obj1).intersection(set(lst_obj2))}')

#Find elements present in only one list
def onlyin_oneset(lst_obj1,lst_obj2):
    logging.info(f'7.Only in List A: {set(lst_obj1)-(set(lst_obj2))}')

#Check if one list is a subset of another
def subset(lst_obj1,lst_obj2):
    logging.info(f'8.List A is sublist of List B : {set(lst_obj1).issubset(set(lst_obj2))}')

#Count frequency of elements
def dict_frequency(freq_list):
    logging.info(f'9.Frequency Count : {dict(Counter(freq_list))}')

#Find first non-repeating element
def dict_first_unique(freq_list):
    unq=dict(Counter(freq_list))
    for k,v in unq.items():
        if v==1:
            logging.info(f'10.First Unique Element : {k}')
            break

#Group elements by frequency
def dict_freq_grp(freq_list):
    d={}
    unq=dict(Counter(freq_list))
    for k,v in unq.items():
        d.setdefault(v,[]).append(k)
    logging.info(f'11.Frequency Group : {d}')

#Merge two dictionaries (sum values if keys overlap)
def dict_merge(dict1,dict2):
    k={x:dict1.get(x,0)+dict2.get(x,0) for x in set(dict1)|set(dict2)}
    logging.info(f'12.Merging Dictionary {k}')
    
def main():
    try:
        remove_duplicates(day1_list)
        second_largest(numbers_list)
        reverse_list(day1_list)
        rotate_list(numbers_list,rotation_count)
        logging.info(f'5.Flattened List: {list(flatten_list(day1_nested_list))}')
        common_elements(list_a,list_b)
        onlyin_oneset(list_a,list_b)
        subset(list_a,list_b)

        dict_first_unique(freq_list)
        dict_freq_grp(freq_list)
        dict_merge(dict1,dict2)
    except Exception as e:
        logging.exception(f'Exception : {e}')
        
    
if __name__=='__main__':
    main()