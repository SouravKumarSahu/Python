import random

class Apple:
    def __init__(self):
        self.weight = random.uniform(0.2, 0.5)
        
class Package:
    total_no_of_apples = 0
    max_weight_per_pack = 300
    
    def __init__(self,pack_num):
        self.pack_num = pack_num
        self.apples_in_this_pack = 0
        self.weight_of_this_pack = 0
        
    def add_apple(self,apple):
        self.weight_of_this_pack += apple.weight
        if self.weight_of_this_pack < Package.max_weight_per_pack:
            self.apples_in_this_pack += 1
            Package.total_no_of_apples += 1
            return False
        else:
            #print(f"package {self.pack_num} is full, use another !!!")
            return True
            
package_full = True

conatiner = []

i = 0

while Package.total_no_of_apples <= 1000 :
    if package_full:
        i += 1
        new_package = Package(f"package_{i}")
        conatiner.append(new_package)
        package_full = False
    else:
        package_full = new_package.add_apple(Apple())
        
print(f"Number of packages {len(conatiner)} with total apples {Package.total_no_of_apples}")

for x in conatiner:
    print(f"Package: {x.pack_num} contains {x.apples_in_this_pack} apples and weigh around {x.weight_of_this_pack}")
