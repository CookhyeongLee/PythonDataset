import cx_Oracle
import pandas as pd
import xml.etree.ElementTree as ET

# Connect to Oracle database
dsn = cx_Oracle.makedsn("localhost", 1521, sid="orcl8276")
connection = cx_Oracle.connect(
    user="yj", password="1", dsn=dsn, encoding="UTF-8")

print('Connected to localhost:1521')

# Cursor to tune the number of rows
cur = connection.cursor()

# Reading xml file
xml_data = open(r'C:\xmlfile.xml').read()

# Save the file as root
root = ET.XML(xml_data)

# Loop all tags in the file
for child in root:
    for x in root.findall(child.tag+"/*"):

        # Save data in dict with corresponding headers
        data = dict(
            Geography=x.attrib['Geography'],
            Age_group=x.attrib['Age_group'],
            Highest_certificatediploma_or_degree=x.attrib['Highest_certificate__diploma_or_degree'],
            VECTOR_ID=x.attrib['VECTOR_ID'],
            SCALAR_FACTOR=x.attrib['SCALAR_FACTOR'],
            NB_DECIMAL=x.attrib['NB_DECIMAL'],
            DGUID=x.attrib['DGUID'],
            UOM=x.attrib['UOM'])

        # Insert the values to the Oracle table
        sql_insert = """insert into emp_sal 
        (Geography, Age_group, Highest_certificatediploma_or_degree, 
        VECTOR_ID, SCALAR_FACTOR, NB_DECIMAL, DGUID, UOM) 
        values (:Geography,:Age_group,:Highest_certificatediploma_or_degree, 
        :VECTOR_ID,:SCALAR_FACTOR,:NB_DECIMAL,:DGUID,:UOM)
        """

        # Execute the query
        cur.execute(sql_insert, data)

# Commit
connection.commit()

# End connection
connection.close()