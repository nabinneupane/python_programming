class ParentClass:
    def __init__(self, Name, Email, Phone):
        self.Name = Name; 
        self.Email = Email; 
        self.Phone = Phone;
    def getName(self):
        return self.Name;
    def getEmail(self):
        return self.Email
    def getPhone(self): 
        return self.Phone;
    def setName(self,name):
        self.Name= name;
    def setEmail(self,email):
        self.Email = email; 
    def setPhone(self, phone):
        self.Phone = phone; 
    def printValue(self):
        print("\t ========================")
        print("\t Name: ", self.Name , "    Email: ", self.Email , "     Phone: ", self.Phone);
        
