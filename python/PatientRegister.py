import pickle, os

class Patient(object):
    def __init__(self, name = None, address = None, Health = None, PatientID = None):
        self.name = name
        self.address = address
        self.Health = Health
        self.PatientID = PatientID
        self.contacts = {}
        self.filename = 'Register'

    def __str__(self):
        return '[Patient Name: {0} | Address: {1} | Health Status: {2} | PatientID: {3}]'.format(self.name, self.address, self.Health, self.PatientID)

    def __repr__(self):
        return '[Patient Name: {0} | Address: {1} | Health Status: {2} | PatientID: {3}]'.format(self.name, self.address, self.Health, self.PatientID)

    # Adding contact provided by the user in our Address Book
    def addPatient(self):
        try:
            if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
                PatientRegister = open(self.filename, 'rb')
                data = pickle.load(PatientRegister)
                PatientRegister.close()
            else:
                PatientRegister = open(self.filename, 'wb')
                data = {}

            contact = self.getcontactFromUser()
            data[contact['Patient Name']] = contact
            PatientRegister = open(self.filename, 'wb')
            pickle.dump(data, PatientRegister)
            PatientRegister.close()
            print('contact Added Successfully!')
        except:
            print('There was an error! Patient was not added.')
        finally:
            PatientRegister.close()

   
    def getcontactFromUser(self):
        try:
            self.contacts['Patient Name'] = str(input('Enter Patient\'s Full Name: '))
            self.contacts['Address'] = str(input('Enter  Patient\'s Address: '))
            self.contacts['Health Status'] = str(input('Enter  Patient\'s Health Status: '))
            self.contacts['PatientID'] = int(input('Enter PatientID : '))
            return self.contacts
        except KeyboardInterrupt as error:
            raise error

   
    def displayPatientcontact(self):
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            PatientRegister = open(self.filename, 'rb')
            data = pickle.load(PatientRegister)
            PatientRegister.close()
            if data:
                for records in data.values():
                    print(records)
            PatientRegister.close()
        else:
            print('No Record in database.')

   
    def searchPatient(self):
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            PatientRegister = open(self.filename, 'rb')
            data = pickle.load(PatientRegister)
            PatientRegister.close()
            try:
                contactToSearch = input('Enter the name of Patient:')
                counter = 0
                for contact in data.values():
                    if contactToSearch in contact['Patient Name']:
                        print(data[contact['Patient Name']])
                        counter += 1
                if counter == 0:
                    print('No record found whose name is:', contactToSearch)
            except:
                print('Error occured!')
        else:
            print('No Record in database.')

   
    def modifyPatientcontact(self):
        if os.path.exists(self.filename) and os.path.getsize(self.filename) > 0:
            PatientRegister = open(self.filename, 'rb')
            data = pickle.load(PatientRegister)
            PatientRegister.close()
            try:
                PatientToModify = input('Enter the name of the Patient to modify (Only enter full name): ')
                # Search for the record to update
                for contact in data.values():
                    if PatientToModify == contact['Patient Name']:
                        contact = data[PatientToModify]
                        break
                
                
                
                contact['Health Status'] = input('Enter Health Status to modify: ')
                del data[PatientToModify]
                data[PatientToModify] = contact
                print('Successful')
                
                
            except:
                print('Error occured. No such record found. Try Again!')
            finally:
                PatientRegister = open(self.filename, 'wb')
                pickle.dump(data, PatientRegister)
                PatientRegister.close()
        else:
            print('No Record in database.')

if __name__ == '__main__':
    register = Patient()
    print('Enter 1.Add Patient 2.Search a Patient 3.Modifying a Patient Health Status 4. Display Patient List 5. To Exit')
    while True:
        choice = int(input('Enter your choice: '))
        if choice == 1:
            register.addPatient()
        elif choice == 2:
            register.searchPatient()
        elif choice == 3:
            register.modifyPatientcontact()
        elif choice == 4:
            register.displayPatientcontact()
        elif choice == 5:
            exit()
        else:
            print('Invalid Option. Try Again!')