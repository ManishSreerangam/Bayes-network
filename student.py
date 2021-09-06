
import sys
import csv
import uuid
import argparse 
import math
def naivebayes():
    args = parser.parse_args()
    file = args.data
    with open( file ,  'r') as file:
        csvFile = csv.reader ( file , delimiter= ',' ) 
        data=[row for row in csvFile]
        target_variable , x1 , x2  = [] , [] , [] 
        rows = len(data) 
        columns = len(data[0])
        for i in range(0 , rows) :
            a1 = [ ]
            b1 = [ ]
            dependent_variable = []
            counter = 0      
            for j in data[i] :  
                counter += 1
                if counter == 1 :       
                    dependent_variable.append(j)
                elif counter == columns  :
                    b1.append(float(j))  
                else:
                    a1.append(float(j))
            target_variable.append(dependent_variable)        
            x1.append(a1)
            x2.append(b1)
            # data is loaded and converted as required 
        count_class_a = 0
        for i in range(0 , rows):     
            if(target_variable[i][0] == 'A' ):
                count_class_a += 1
        #print( "total number of classes with label 'A' :{} ".format(count_class_a))
        count_class_b = 0
        for i in range(0 , rows):     
            if(target_variable[i][0] == 'B' ):
                count_class_b += 1
        #print( "total number of classes with label 'B' :{} ".format(count_class_b))
        """
        finding mean 
        """
        x1_a = float(0)
        x2_a = float(0)
        x1_b = float(0)
        x2_b = float(0)
        mean_x1_a = float(0)
        mean_x2_a = float(0)
        mean_x1_b = float(0)
        mean_x2_b = float(0)
        counter_a = 0
        counter_b = 0
        v_x1_a = float(0)
        v_x2_a = float(0)
        v_x1_b = float(0)
        v_x2_b = float(0)
        variance_x1_a = float(0)
        variance_x2_a = float(0)
        variance_x1_b = float(0)
        variance_x2_b = float(0)
        for i in range(0,rows):
            if(target_variable[i][0] == 'A' ):
                counter_a += 1
                x1_a += x1[i][0]
                x2_a += x2[i][0]
            else:
                counter_b += 1
                x1_b += x1[i][0]
                x2_b += x2[i][0]
        mean_x1_a = x1_a / counter_a
        mean_x2_a = x2_a / counter_a
        mean_x1_b = x1_b / counter_b
        mean_x2_b = x2_b / counter_b

        """
        Probabilities 
        """
        prob_a = counter_a / (counter_a + counter_b )
        prob_b = counter_b / (counter_a + counter_b )

        """
        finding variance.
        """
        for i in range(0,rows):
            if(target_variable[i][0] == 'A' ):
                v_x1_a += (x1[i][0] - mean_x1_a) * (x1[i][0] - mean_x1_a)
                v_x2_a += (x2[i][0] - mean_x2_a) * (x2[i][0] - mean_x2_a)
            else:
                v_x1_b += (x1[i][0] - mean_x1_b) * (x1[i][0] - mean_x1_b)
                v_x2_b += (x2[i][0] - mean_x2_b) * (x2[i][0] - mean_x2_b)
        variance_x1_a = (v_x1_a / (counter_a - 1) )
        variance_x2_a = (v_x2_a / (counter_a - 1) )
        variance_x1_b = (v_x1_b / (counter_b - 1) )
        variance_x2_b = (v_x2_b / (counter_b - 1) )
        #print("variance_x1_a = {} , variance_x2_a = {} ,variance_x1_b  = {} , variance_x2_b = {} ".format(variance_x1_a , variance_x2_a , variance_x1_b,  variance_x2_b ))            
        #first_line
        print(mean_x1_a , end =',' )
        print(variance_x1_a , end =',' )
        print(mean_x2_a , end =',' )
        print(variance_x2_a , end =',' )
        print(prob_a )
        #2nd line 
        print(mean_x1_b , end =',' )
        print(variance_x1_b , end =',' )
        print(mean_x2_b , end =',' )
        print(variance_x2_b , end =',' )
        print(prob_b  )
        #function for apriori algorithm
        def apriori (x1 , variance_x1_a , mean_x1_a , x2 , variance_x2_a , mean_x2_a , prob):
            part1_x1 = ((2 * 3.14 * variance_x1_a) ** 0.5 )
            part1_x1 = 1 / part1_x1
            part2_x1 = ( x1 - mean_x1_a ) ** 2
            part2_x1 = (part2_x1 / (2 * variance_x1_a))
            part2_x1 = math.exp(- part2_x1 )
            part_x1 = part1_x1 * part2_x1
            part1_x2 = ((2 * 3.14 * variance_x2_a) ** 0.5 )
            part1_x2 = 1 / part1_x2
            part2_x2 = ( x2 - mean_x2_a ) ** 2
            part2_x2 = (part2_x2 / (2 * variance_x2_a) )
            part2_x2 = math.exp(- part2_x2 )
            part_x2 = part1_x2 * part2_x2
            #probability of a 
            fullpart_a = part_x1 * part_x2 * prob
            return fullpart_a
        count = 0
        for i in range(0 , rows):
            apriori_a = apriori (x1[i][0] , variance_x1_a , mean_x1_a , x2[i][0] , variance_x2_a , mean_x2_a , prob_a)
            apriori_b = apriori (x1[i][0] , variance_x1_b , mean_x1_b , x2[i][0] , variance_x2_b , mean_x2_b , prob_b)
            if (apriori_a > apriori_b):
                if(target_variable[i][0] == "A"):
                    pass
                else:
                    count += 1
            else:
                if(target_variable[i][0] == "B"):
                    pass
                else:
                    count += 1
        print(count)
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--data", help="Data File")
    naivebayes()
           
        
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    