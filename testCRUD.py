import unittest, json, os, sys, inspect, configparser, time

from mongodbconnector import mongodbconnector

##########################################################
#                PROPERTIES PART START
##########################################################

thisfolder = os.path.dirname(os.path.abspath(__file__))
initfile = os.path.join(thisfolder, 'config.properties')

config = configparser.ConfigParser()
config.read(initfile)

##########################################################
#                PROPERTIES PART END
##########################################################

##########################################################
#                DB PART START
##########################################################

hostPort  = config.get("MONGODB", "hostPort")
userName = config.get("MONGODB", "user")
password = config.get("MONGODB", "password")
isCloud = config.get("MONGODB", "isCloud")
queryParam = config.get("MONGODB", "queryParam")
databaseName = config.get("MONGODB", "databaseName")

print("Connecting to mongo:")
mongodbcon = mongodbconnector(hostPort, userName, password, queryParam, databaseName, isCloud)
print("Connected")

##########################################################
#                DB PART END
##########################################################


class TestLoadBep20TokenTrfToMongoDB(unittest.TestCase):
    
    def test_crud_indb(self):
      example1= {}
      example1["firstName"]= "John"
      example1["lastName"]= "Doe"
      example1["Address"]= "First addresss"
      
      _id_example1 = mongodbcon.insertintoSample(example1)

      example2= {}
      example2["firstName"]= "Brandon"
      example2["lastName"]= "Don"
      example2["Address"]= "Second addresss"

      _id_example2 = mongodbcon.insertintoSample(example2)

      
      input("Verify that the two records are inserted and then press any key")

      #DELETE SECOND
      mongodbcon.deleteSample(_id_example2)

      input("Verify that the second records is not present anymore and then press any key")

      #UPDATE FIRST
      example1["firstName"]= "Marc"
      mongodbcon.UpdateSample(example1, _id_example1)


if __name__ == '__main__':
    unittest.main()