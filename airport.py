import mysql.connector
import datetime
# Added the username and password to change out faster
USERNAME='kdh85'
PASSWORD='~Csc4449'
def displayMenu():
 print("Airport Information Database")
 print("****************************")
 print("1-Insert a new Technician")
 print("2-Delete an existing airplane")
 print("3-Update the expertise of an existing technician")
 print("4-List the details of the technician whose salary is greater than 
the average of the salary of all technicians")
 print("5-List all the model numbers that a given technician has the 
expertise, along with their capacity and weight")
 print("6-List the total number of technicians who are experts in each 
model")
 print("7-List the details (test number, test name, maximum score, etc.) 
of the FAA tests for a given airplane, sorted by the maximum scores")
 print("8-List the most recent annual medical examination and his/her 
union membership number for each traffic controller")
 print("9-List the total number of tests done by each technician for a 
given airplane.")
 print("10-List the name of the technician, the registration number of the 
airplane, and the FAA number of those tests done between September2005 and 
December2005, sortedbythe FAA numbers")
 print("11-Quit")
 print()
24
def getChoice():
 choice = eval(input(">>"))
 return choice
def main():
 cnx = mysql.connector.connect(host='square.law.miami.edu',user=USERNAME, 
password=PASSWORD, database='{0}_FINAL_PROJECT'.format(USERNAME))
 cursor = cnx.cursor()
 displayMenu()
 choice = getChoice()
 while(choice!=11):
 if (choice==1):
 query = ("INSERT INTO Technicians (emplSSN, fname, lname, 
address, phoneNo, salary) " +
 "VALUES ('101010101', 'Karysse', 'Hay', '123 Main St', 
'3059304043', '100000')")
 cursor.execute(query)
 print("Record inserted successfully.")
 cursor.execute("SELECT * FROM Technicians")
 print("{:<12} {:<12} {:<12} {:<15} {:<12} {:<10}".format(
 "SSN", "First Name", "Last Name", "Address", "Phone No", 
"Salary"))
 print("="*80)
 for (emplSSN, fname, lname, address, phoneNo, salary) in cursor:
 print("{:<12} {:<12} {:<12} {:<15} {:<12} {:<10}".format(
25
 emplSSN, fname, lname, address, phoneNo, salary))
 print()
 displayMenu()
 choice=getChoice()
 elif (choice==2):
 query = ("DELETE FROM airplane " +
 "WHERE registrationNo = %s")
 regNo = input("Enter a Registration No: ")
 cursor.execute(query, (regNo,))
 if cursor.rowcount > 0:
 print("Airplane with Registration No {} was deleted 
successfully.".format(regNo))
 else:
 print("Airplane with Registration No {} does not 
exist.".format(regNo))
 print()
 displayMenu()
 choice=getChoice()
 elif (choice==3):
 emplSSN = input("Enter the technician's SSN: ")
 modelNo = input("Enter the new Model Number: ")
 query = "UPDATE technicianExpertise SET modelNo = %s WHERE 
emplSSN = %s"
26
 cursor.execute(query, (modelNo, emplSSN))
 query = "SELECT emplSSN, modelNo FROM technicianExpertise WHERE 
emplSSN = %s"
 cursor.execute(query, (emplSSN,))
 print("{:<12} {:<8}".format("SSN", "Model No"))
 print("="*25)
 for row in cursor.fetchall():
 print("{:<12} {:<8}".format(*row))
 print()
 displayMenu()
 choice=getChoice()
 elif (choice==4):
 result=cursor.execute("SELECT * " +
 "FROM Technicians " +
 "WHERE salary > (SELECT AVG(salary) FROM Technicians)")
 print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
 "SSN", "First Name", "Last Name", "Address", "Phone #", 
"Salary"))
 # Print a line to separate the headers from the data
 print("="*110)
 # Print each row of data from the database
 for row in cursor.fetchall():
27
 print("{:<15} {:<15} {:<15} {:<15} {:<15} 
${:<15,.2f}".format(*row))
 print()
 displayMenu()
 choice=getChoice()
 elif (choice==5):
 query = ("SELECT A.modelNo, A.capacity, A.weight " +
 "FROM airplaneModel A " +
 "JOIN technicianExpertise T ON T.modelNo = A.modelNo "+
 "WHERE T.emplSSN = %s")
 ssn = input("Enter a Technician's SSN: ")
 cursor.execute(query, (ssn,))
 print("{:<15} {:<15} {:<15}".format(
 "Model No", "Capacity", "Weight"))
 print("="*50)
 for row in cursor.fetchall():
 print("{:<15} {:<15} {:<15}".format(*row))
 print()
 displayMenu()
 choice=getChoice()
28
 elif (choice==6):
 query = ("SELECT modelNo, COUNT(emplSSN) AS numExperts " +
 "FROM technicianExpertise "+
 "GROUP BY modelNo")
 result = cursor.execute(query)
 print("{:<12} {:<15}".format(
 "Model No", "Number of Experts"))
 print("="*45)
 for row in cursor.fetchall():
 print("{:<12} {:<15}".format(*row))
 print()
 displayMenu()
 choice=getChoice()
 elif (choice==7):
 query = ("SELECT T.registrationNo, T.emplSSN, I.testName, 
T.noHours, T.date, T.maxScore " +
 "FROM testRecords T "+
 "JOIN testingInfo I ON T.faaNo = I.faaNo "+
 "WHERE T.registrationNo = %s " +
 "ORDER BY T.maxScore ASC")
 regNo = input("Enter your desrired registration number: ")
29
 cursor.execute(query, (regNo,))
 print("{:<20} {:<15} {:<15} {:<10} {:<15} {:<15}".format(
 "Registration No", "SSN", " Test Name", "Hours", "Date", 
"Max Score"))
 print("="*100)
 for row in cursor.fetchall():
 print("{:<20} {:<15} {:<15} {:<10} {:<15} 
{:<15}".format(row[0], row[1], row[2], row[3], row[4].strftime('%d %b %Y'), 
row[5]))
 print()
 displayMenu()
 choice=getChoice()
 elif (choice==8):
 query = ("SELECT T.emplSSN, T.recentDate, E.memberNo " +
 "FROM trafficController T "+
 "LEFT JOIN employeeUnion E ON T.emplSSN = E.emplSSN "+
 "ORDER BY E.memberNo ASC")
 cursor.execute(query)
 print("{:<15} {:<15} {:<15}".format(
 "SSN", "Recent Date", "Member No"))
 print("="*50)
30
 for row in cursor.fetchall():
 print("{:<15} {:<15} {:<15}".format(row[0], 
row[1].strftime('%d %b %Y'), row[2]))
 print()
 displayMenu()
 choice=getChoice()
 elif (choice==9):
 query = ("SELECT emplSSN, COUNT(*) AS numTests " +
 "FROM testRecords "+
 "WHERE registrationNo = %s "+
 "GROUP BY emplSSN " +
 "ORDER BY numTests ASC")
 regNo = input("Enter your desrired registration number: ")
 cursor.execute(query, (regNo,))
 print("{:<15} {:<15}".format(
 "SSN", "Number of Tests"))
 print("="*35)
 for row in cursor.fetchall():
 print("{:<15} {:<15}".format(*row))
31
 print()
 displayMenu()
 choice=getChoice()
 elif (choice==10):
 query = ("SELECT T.fname, T.lname, R.registrationNo, R.faaNo " +
 "FROM Technicians T "+
 "INNER JOIN testRecords R ON T.emplSSN = R.emplSSN "+
 "WHERE R.date BETWEEN '2005-09-01' AND '2005-12-31'" +
 "ORDER BY R.faaNo ASC")
 cursor.execute(query)
 print("{:<12} {:<12} {:<20} {:<10}".format(
 "First Name", "Last Name", "Registration No", "FAA No"))
 print("="*60)
 for row in cursor.fetchall():
 print("{:<12} {:<12} {:<20} {:<10}".format(*row))
 print()
 displayMenu()
 choice=getChoice()
 elif (choice==11):
 cursor.close()
32
 cnx.close()
if __name__ == "__main__":
 main()
