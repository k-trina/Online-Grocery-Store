"""
-------------------------------------------------------
Author:  David Brown
ID:      999999999
Email:   dbrown@wlu.ca
__updated__ = "2022-09-30"
-------------------------------------------------------
Runs simple test code against the DCRIS database with both
direct connections and SSH tunneling.
-------------------------------------------------------
"""
# pylint: disable=broad-except

# Imports
from Connect import Connect
from Tunnel import Tunnel
import sys

# Constants - connection definition files
DCRIS_FILE = "dcris.txt"
HOPPER_FILE = "hopper.txt"


def get_test_data():
    """
    -------------------------------------------------------
    Reads data from the DCRIS 'broad' table.
    Use: get_test_data()
    -------------------------------------------------------
    """
    # Connect to the DCRIS database with an option file
    conn = Connect(DCRIS_FILE)
    # Get the connection cursor object
    cursor = conn.cursor
    # Define a SQL query
    sql = "SELECT * FROM employee"
    # Execute the query from the connection cursor
    cursor.execute(sql)
    # Print the column names from the query result
    print("Columns:")
    print(cursor.column_names)
    print()
    # Get and print the contents of the query results (raw results)
    rows = cursor.fetchall()
    print(f"Row count: {cursor.rowcount}")
    print()

    print("Data:")
    for row in rows:
        print(row)
    # Close the Connect object
    conn.close()
    return

def insert_data(cursor):
    
    return

#Add all data to tables
def fill_tables(mycursor):
    print("Filling tables")
    mycursor.execute("""
    INSERT INTO `faro8180`.`employee` ();
    """)

def drop_table(cursor):
    cursor.execute("""
    DROP TABLE customer;
    DROP TABLE department;
    DROP TABLE employee;
    DROP TABLE inventory;
    DROP TABLE order;
    DROP TABLE product;
    DROP TABLE store;
    DROP TABLE supplier;""")
    return;

def create_tables(cursor):
    cursor.execute("""
    CREATE TABLE `store` (
      `storeID` int NOT NULL,
      `businessHours` varchar(45) NOT NULL,
      `address` varchar(45) NOT NULL,
      `phone` varchar(45) NOT NULL,
      PRIMARY KEY (`storeID`),
      UNIQUE KEY `storeID_UNIQUE` (`storeID`),
      UNIQUE KEY `phone_UNIQUE` (`phone`),
      UNIQUE KEY `address_UNIQUE` (`address`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
    
    CREATE TABLE `customer` (
      `username` varchar(20) NOT NULL,
      `password` varchar(45) NOT NULL,
      `email` varchar(100) NOT NULL,
      PRIMARY KEY (`username`,`email`),
      UNIQUE KEY `email_UNIQUE` (`email`),
      UNIQUE KEY `username_UNIQUE` (`username`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
    
    CREATE TABLE `department` (
      `departmentID` int NOT NULL,
      `departmentName` enum('Produce','Dairy','Meat','Bakery','Frozen') DEFAULT NULL,
      PRIMARY KEY (`departmentID`),
      UNIQUE KEY `departmentID_UNIQUE` (`departmentID`),
      UNIQUE KEY `departmentName_UNIQUE` (`departmentName`),
      KEY `idx_department_departmentName` (`departmentName`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
    
    CREATE TABLE `employee` (
      `EmployeeID` int NOT NULL AUTO_INCREMENT,
      `Salary` int NOT NULL,
      `Hours` int unsigned DEFAULT NULL COMMENT 'Number of Hours per wek ',
      `Phone` varchar(20) NOT NULL COMMENT 'Phone number inculding area code (10 + 2)',
      `Roles` enum('Manager','Part-time','Full-time') DEFAULT NULL,
      `EmpName` varchar(100) NOT NULL,
      `Bank Info` varchar(100) NOT NULL,
      `DepartmentID` int DEFAULT NULL,
      PRIMARY KEY (`EmployeeID`),
      UNIQUE KEY `EmployeeID_UNIQUE` (`EmployeeID`),
      UNIQUE KEY `Bank Info_UNIQUE` (`Bank Info`),
      KEY `DepartmentID_idx` (`DepartmentID`),
      CONSTRAINT `DepartmentID` FOREIGN KEY (`DepartmentID`) REFERENCES `department` (`departmentID`)
    ) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

    CREATE TABLE `inventory` (
      `availableStock` int NOT NULL,
      `supplier ID` int NOT NULL,
      `productID` int NOT NULL,
      PRIMARY KEY (`productID`),
      KEY `supplierID_idx` (`supplier ID`),
      CONSTRAINT `productID` FOREIGN KEY (`productID`) REFERENCES `product` (`productID`),
      CONSTRAINT `supplier ID` FOREIGN KEY (`supplier ID`) REFERENCES `supplier` (`supplierID`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
    
    CREATE TABLE `order` (
      `orderID` int NOT NULL,
      `paymentmethod` varchar(45) NOT NULL,
      `pickupDate` datetime DEFAULT NULL,
      `totalBill` decimal(7,2) NOT NULL,
      `totalQuantity` int NOT NULL,
      `username` varchar(45) NOT NULL,
      `employeeID` int NOT NULL,
      `storeID` int NOT NULL,
      PRIMARY KEY (`orderID`),
      UNIQUE KEY `orderID_UNIQUE` (`orderID`),
      KEY `username_idx` (`username`),
      KEY `employee ID_idx` (`employeeID`),
      KEY `storeID_idx` (`storeID`),
      KEY `username_idx1` (`username`),
      KEY `employee ID_idx1` (`employeeID`),
      KEY `storeID_idx1` (`storeID`),
      CONSTRAINT `employee ID` FOREIGN KEY (`employeeID`) REFERENCES `employee` (`EmployeeID`),
      CONSTRAINT `storeID1` FOREIGN KEY (`storeID`) REFERENCES `store` (`storeID`),
      CONSTRAINT `username` FOREIGN KEY (`username`) REFERENCES `customer` (`username`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
    
    CREATE TABLE `product` (
      `productID` int NOT NULL,
      `productName` varchar(64) NOT NULL,
      `price` decimal(10,2) NOT NULL,
      `expiryDate` date NOT NULL,
      `supplierID` int NOT NULL,
      `storeID` int NOT NULL,
      `Department ID` int NOT NULL,
      PRIMARY KEY (`productID`),
      UNIQUE KEY `productID_UNIQUE` (`productID`),
      KEY `departmentID_idx` (`Department ID`),
      KEY `supplierID_idx` (`supplierID`),
      KEY `storeID_idx` (`storeID`),
      CONSTRAINT `Department ID` FOREIGN KEY (`Department ID`) REFERENCES `department` (`departmentID`),
      CONSTRAINT `storeID` FOREIGN KEY (`storeID`) REFERENCES `store` (`storeID`),
      CONSTRAINT `supplierID` FOREIGN KEY (`supplierID`) REFERENCES `supplier` (`supplierID`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci COMMENT='                ';

    CREATE TABLE `supplier` (
      `supplierID` int NOT NULL,
      `phone` varchar(20) DEFAULT NULL,
      `address` varchar(45) DEFAULT NULL,
      `supplierName` varchar(100) DEFAULT NULL,
      PRIMARY KEY (`supplierID`),
      UNIQUE KEY `supplierID_UNIQUE` (`supplierID`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

    
    
""");
    return;


def test_connect():
    """
    -------------------------------------------------------
    Direct database server connection.
    -------------------------------------------------------
    """
    print("Standard Connection")
    print()

    try:
        # Connect to the DCRIS database with an option file
        conn = Connect(DCRIS_FILE)
        # Get the connection cursor object
        cursor = conn.cursor
        get_test_data(cursor)
    except Exception as e:
        print(str(e))


def test_connect_tunnel():
    """
    -------------------------------------------------------
    Database server connection using ssh tunneling.
    -------------------------------------------------------
    """
    print("SSH Tunnel Connection")
    print()

    try:
        tunnel = Tunnel(HOPPER_FILE)

        with tunnel.tunnel:
           
            get_test_data()
            
    except Exception as e:
        print(str(e))
        
def list_options():
    print("""Please select one of the following options:

    1. Drop all tables
    2. Create all tables
    3. Add data to tables
    4. Query Tables
    Q. Quit Program
    """)
    x = input("Options: ")
    return x
    
        


# for testing
if __name__ == "__main__":
    # Test both connections
    test_connect()
    print()
    print("-" * 80)
    print()
    test_connect_tunnel()
    # Connect to the DCRIS database with an option file
    conn = Connect(DCRIS_FILE)
    # Get the connection cursor object
    cursor = conn.cursor
    x = list_options()
    if (x=='1'):
        drop_table(cursor)
    elif (x =='2'):        
        create_tables(cursor)
    # elif (x=='3'):
    #     add_data(cursor)
    # elif (x=='4'):
    #     queries(cursor)     
    elif (x=='Q'):
        print("You've successfully exited the program")
        sys.exit()
    else:
        print("Invalid option")
        sys.exit()
        