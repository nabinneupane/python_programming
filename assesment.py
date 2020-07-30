from  Contacts import Contacts; 
from Leads import Leads; 
import  json; 

#creating Contact class objects... 

print("\n Creating Contact class objects........\n")
contactObject = Contacts("Alice Brown", "None", "1231112223"); 
contactObject2 = Contacts("Bob Crown", "bob@crowns.com", "None")
contactObject3 = Contacts("Carlos Drew", "carl@drewess.com","3453334445")
contactObject4 = Contacts("Doug Emerty", "None", "4564445556")
contactObject5 = Contacts("Egan Fair","eg@fairness.com","5675556667")

print("\n Completed......\n")
#list to store contact class objects. 
contactList=[]; 


contactList.extend((contactObject,contactObject2,contactObject3,contactObject4,contactObject5))

print("\n\n List of Contact class object created.... printing it...\n\n")

for i in range(len(contactList)):
    contactList[i].printValue()

#creating Leads class objects... 
print("\n\n Creating Leads class objects........\n\n")
leadsObject = Leads("None", "kevin@keith.com", "None"); 
leadsObject2 = Leads("Lucy", "lucy@liu.com", "None")
leadsObject3 = Leads("Mary Middle", "mary@middle.com","3331112223")
leadsObject4 = Leads("None", "None", "4442223334")
leadsObject5 = Leads("None","ole@olson.com","None")

# list to store leads class objects. 
leadsList= []
leadsList.extend((leadsObject,leadsObject2,leadsObject3,leadsObject4,leadsObject5))
print("\n\n List of Leads class object created.... printing it...\n\n")

for i in range(len(contactList)):
    leadsList[i].printValue()



print("\n\n Now opening JSON file and printing the values........\n\n")
#opening JSON file
file = open('registrant.json')



data = json.load(file); 

for i in data['registrant']:
    print(i)


print ("\n\n all set for modifying values \n\n")
for i in data['registrant']:
    
    flag = True
    flag2 = True
                
    for j in range(0,len(contactList)):
        if(i["email"] == contactList[j].getEmail() and i["email"] != "None"):
            if ( contactList[j].getName == "None" and i["name"] !="None"):
                contactList[j].setName(i["name"])
            if ( contactList[j].getPhone == "None" and i["phone"] !="None"):
                contactList[j].setPhone(i["phone"])
            flag = False
            break
        elif (i["phone"] == contactList[j].getPhone() and i["phone"] != "None"):
            if (contactList[j].getName =="None" and i["name"] != "None"):
                contactList[j].setName(i["name"])
            if (i["email"] !="None" and contactList[j].getEmail == "None"):
                contactList[j].setEmail(i["email"])            
            flag = False
            break
        
    if(flag):
        
        for k in range(0,len(leadsList)):
            if(i["email"] == leadsList[k].getEmail() and i["email"] != "None"):
                
                #remomve it from leads list if matched
                leadsList.remove(leadsList[k])
                contactList.append(Contacts(i["name"],i["email"],i["phone"]))
                flag2 = False
                break
            elif (i["phone"] ==  leadsList[k].getPhone() and i["phone"] != "None"): 
                #remove if from leads list if matched
                leadsList.remove(leadsList[k])
                contactList.append(Contacts(i["name"],i["email"],i["phone"]))
                flag2= False
                break
    if(flag2 and flag):
        contactList.append(Contacts(i["name"],i["email"],i["phone"])) 

       

        
print("\n\nModification done.......Printing values in contactList and LeadsList\n\n")

file.close()

print("\n\n Printing values in contact list...\n\n")
for i in range(len(contactList)):
    contactList[i].printValue()

print("\n\n printing values in Leads list... \n\n")
for i in range(len(leadsList)):
    leadsList[i].printValue()
