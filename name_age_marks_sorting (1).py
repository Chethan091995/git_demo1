# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 19:16:32 2021

@author: Dell
"""
"""

You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers. The tuples are input by console. The sort criteria is:

1: Sort based on name;

2: Then sort based on age;

3: Then sort by score.

The priority is that name > age > score.

If the following tuples are given as input to the program:

Tom,19,80

John,20,90

Jony,17,91

Jony,17,93

Json,21,85

Then, the output of the program should be:

[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

"""
class sorting:
    
    user_details=[]
    
    def name(self):
        
        return (input('Enter your name :'))

    def age(self):
        
        while True:
            self.s_age=input('Enter your age :')
            
            if self.s_age.isdigit() and self.s_age>'0':
                return self.s_age
            else:
                print('Enter valid age')
                
    def height(self):
        
        while True:
            self.s_height=input('Enter your height :')
            
            if self.s_height.replace('.','',1).isdigit() and self.s_height>'0':
                return self.s_height
            else:
                print('Enter valid height')
                
                
    def user_info(self):
        
        u_name=self.name()
        u_age=self.age()
        u_height=self.height()
        
        self.user_details.append((u_name,u_age,u_height))
        
    def multiple_users_info(self):
        
        while True:
            
            veri=input('Enter S to add students ,E for Exit :')[0].upper()
            
            if veri=='E':
                break
                
            if veri=='S':
                self.user_info()
                
        print('------------------------------------------------------------',end='\n\n')
                
        print('The original user_details is :',end='\n\n')
        
        print(self.user_details,end='\n\n')
        
        print('------------------------------------------------------------',end='\n\n')
        
        print('The user details in the acsending order :',end='\n\n')
        
        print(sorted(self.user_details))
        
        print('------------------------------------------------------------',end='\n\n')
        
        print('The user details in the descending order :',end='\n\n')
        
        print(sorted(self.user_details ,reverse=True))
        
        
                
        
def main_program():
    
    s=sorting()
    
    s.multiple_users_info()
    
main_program()
    
    