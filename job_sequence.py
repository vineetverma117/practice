#RunTime: O(n2)

class JobSequence:
    
    def sort_in_descending(self, array):
        #sort array with descending order of profit
        sorted_array = sorted(array, key= lambda x: x[2], reverse=True)
        return sorted_array
        
    def find_max_deadline(self, array):
        max_deadline = 0
        for each_job in array:
            if each_job[1] > max_deadline:
                max_deadline = each_job[1]
        return max_deadline
        
    def find_job_sequence(self, array):
        sorted_array = self.sort_in_descending(array)
        max_dead = self.find_max_deadline(sorted_array)
        
        sequence = []
        slot = [False]*(len(sorted_array)+1)
        
        #Start from max deadline and find job with deadline >=i
        #add sequence in sequence
        #As we are traversing reverse order that's why using insert to append job at front of list
        for i in range(max_dead, 1, -1):
            for index, each_job in enumerate(sorted_array):
                if(each_job[1] >= i):
                    if slot[index] == False:
                        sequence.insert(0, each_job[0])
                        slot[index] = True
        return sequence 
        
if __name__ == '__main__':
    arr = [['a', 2, 100],  # Job Array
           ['b', 1, 19],
           ['c', 2, 27],
           ['d', 1, 25],
           ['e', 3, 15]]
           
    obj = JobSequence()
    print(obj.find_job_sequence(arr))
