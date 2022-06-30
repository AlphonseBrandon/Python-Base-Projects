#Define the "HealthInsurance" class
class HealthInsurance:
    #Initialize the object's attributes
  def __init__(self, company_name, foundation_year, founder_name,  company_slogan, num_of_employees, num_of_clients):    
    self.company_name = company_name
    self.foundation_year = foundation_year
    self.founder_name = founder_name
    self.company_slogan = company_slogan
    self.num_of_employees = num_of_employees
    self.num_of_clients = num_of_clients



    #Define the print_report method
  def print_report(self):
    print(f"""The {self.company_name}, was founded in {self.foundation_year}. The founder of the company is {self.founder_name}. 

  Company slogan: {self.company_slogan}

  Number of employees: {self.num_of_employees}

  Number of clients: {self.num_of_clients}""")  

    #Define the sup_health_insurance method
  def sub_health_insurance(self, age, chronic_disease, income):  
      #if-else statements to check whether person can get supplemental insurance or not
      if age < 60 and chronic_disease == True  and income < 5000:
        print('Sorry! you are not eligible to the sub health insurance')
      elif age >= 60 and chronic_disease == False or income < 5000:
        print('Congratulations, you are eligible for sub health insurance') 

    #Define the update_num_clients method
  def update_num_clients(self, new_number):
    num_of_clients = new_number
    print(f'The number of clients have been updated to {num_of_clients}')  
    
#Create the object "HI_company1" with it's attributes
HI_company1 = HealthInsurance('Healthy', 2012, 'Bob Mayer', 'We care for you', 3500, 13230 )

#Call the print_report method for HI_company1
HI_company1.print_report()

