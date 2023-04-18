import sqlite3

db= sqlite3.connect('database.db')
d= db.cursor()

db.execute('drop table if exists person')

db.execute('create table person (unique_identifier int,firstname text, secondname text, email text,  program_name text, program_description text,program_category text,program_duration text, program_progress text )')
           
          

db.execute(f" INSERT INTO  person VALUES(1,'Tim','Layo', 'timothylayo27@gmail.com','db.py','Creating a database for a person' ,'any','2 hours','almost done')")
db.execute("SELECT * FROM person WHERE firstname ='Tim' ")
 
db.commit ()
db.close()          
         
          
        
          




 