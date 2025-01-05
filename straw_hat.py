'''
    This file contains the class definition for the StrawHat class.
'''

from crewmate import CrewMate
from heap import Heap, comp1, comp2
import treasure

def get_id(treasure):
    return treasure.id

class StrawHatTreasury:
    '''
    Class to implement the StrawHat Crew Treasury
    '''
    
    def __init__(self, m):
        l=[]
        for i in range(m):
            a = CrewMate()     #load = 0, arr = [], id = i
            a.load = 0
            a.arr = []
            a.id = i
            l.append(a)
        self.main_heap = Heap(comp1, init_array=l)
        self.completed= []
        self.loaded_crewmates = []


        '''
        Arguments:
            m : int : Number of Crew Mates (positive integer)
        Returns:
            None
        Description:
            Initializes the StrawHat
        Time Complexity:
            O(m)
        '''
        
        # Write your code here
        
    
    def add_treasure(self, treasure):
        
        a = self.main_heap.extract()
        
        size = treasure.size
        arrival = treasure.arrival_time
        a.completion_time = max(a.completion_time, arrival) + size
        if len(a.arr) == 0:
            self.loaded_crewmates.append(a)
        a.arr.append(treasure)
        # print(a.load, a.arr, a.id)
        self.main_heap.insert(a)            #yahan tak code sahi hai
        
        
        '''
        Arguments:
            treasure : Treasure : The treasure to be added to the treasury
        Returns:
            None
        Description:
            Adds the treasure to the treasury
        Time Complexity:
            O(log(m) + log(n)) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        # Write your code here
        
    
    def get_completion_time(self):
        completed = []
        for i in self.loaded_crewmates:
            l = i.arr          #l will access list of treasure in the crewmate
            p=[]
            # for k in l:
            #     print(k.id)
            # print("#####")
            treasure_heap = Heap(comp2,init_array=p)        #define comp2 here
            for j in range(len(l)):                        #j will access treasures in the list l
                rem_size = l[j].size
                if treasure_heap.top() == None:
                    treasure_heap.insert([rem_size,l[j]])     #each element of treasure heap is a list of remaining size and treasure
                else:
                    time1 = l[j-1].arrival_time
                    current_time = l[j].arrival_time
                    t = current_time - time1
                    while t>0:
                        b = treasure_heap.extract()
                        if b == None:
                            t = -1
                        else:
                            
                            if t>=b[0]:            #matlab top element naya element aane se pehle hi process ho jayega
                                t-=b[0]                      #remaining size karni hai process
                                time1 = time1 + b[0]
                                b[1].completion_time = time1 
                                completed.append(b[1])
                                #now here write a function to append this object b in main list
                            else:
                                b[0] = b[0] - t
                                treasure_heap.insert(b)
                                t= -1
                    treasure_heap.insert([rem_size,l[j]])
            time2 = l[-1].arrival_time
            for i in range(treasure_heap.length()):
                k = treasure_heap.extract()
                time2 = time2 + k[0]
                k[1].completion_time = time2
                completed.append(k[1])
        
        completed.sort(key = get_id)
        return completed
        # self.main_heap.print_heap()
        # n = self.main_heap.length()
        # for i in range(n):
        #     crew = self.main_heap[i]


        '''Arguments:
            None
        Returns:
            List[Treasure] : List of treasures in the order of their completion after updating Treasure.completion_time
        Description:
            Returns all the treasure after processing them
        Time Complexity:
            O(n(log(m) + log(n))) where
                m : Number of Crew Mates
                n : Number of Treasures
        '''
        
        # Write your code here
        
    
    # You can add more methods if required