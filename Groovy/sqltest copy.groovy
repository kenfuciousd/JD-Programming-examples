@Grapes([ 
@Grab(group='org.xerial',module='sqlite-jdbc',version='3.7.2'), @GrabConfig(systemClassLoader=true) 
]) 
import java.sql.* 
import org.sqlite.SQLite 
import groovy.sql.Sql 
Class.forName("org.sqlite.JDBC") 
def sql = Sql.newInstance("jdbc:sqlite:sample.db", "org.sqlite.JDBC") 
println("Creating the test database\n") 
sql.execute("drop table if exists person") 
sql.execute("create table person (id integer primary key autoincrement, firstname string, middlename string, lastname string, nickname string)") 
// Load our sample data into the database 
def people = sql.dataSet("person") 
people.add(firstname:"John", middlename:"Jacob", lastname:"Schmidt", nickname:"Jingleheimer") 
people.add(firstname:"Billie", lastname:"Jean",) 
people.add(firstname:"ELEANOR", lastname:"RIGBY") 
people.add(firstname:"Slim", lastname:"Shady", nickname:"Marshal") 
people.add(firstname:"Eleanor", lastname:"Rigby") 
/* 
Exercise 1: Complete the SQL query ensuring that it lists all the users in the 'person' table 
*/ 
println("\n") 
println("Exercise 1:\n") 
def listUsers = "SELECT * from person"  /* query went here*/
sql.eachRow(listUsers) { 
println(it) 
} 
/* 
Exercise 2: Complete the SQL query to add your name to the person table */ 
println("\n") 
println("Exercise 2:\n") 
def addUser = "INSERT INTO person (firstname, lastname) VALUES ('Jason', 'Dyer')" /*added*/
sql.execute(addUser) 
// We are intentionally using the list all query from above 
sql.eachRow(listUsers) { 
println(it) 
} 
/* 
Exercise 3: Write a SQL query to remove the nickname for Mr. Shady 
*/ 
println("\n") 
println("Exercise 3:\n") 
def updateUser = "UPDATE person SET nickname = null WHERE lastname = 'Shady'" /*query written here*/ 
sql.execute(updateUser) 
// We are intentionally using the list all query from above 
sql.eachRow(listUsers) { 
println(it) 
} 
/* 
Exercise 4: Write a SQL query to remove ELEANOR RIGBY 
*/ 
println("\n") 
println("Exercise 4:\n") 
def deleteUser = "DELETE FROM person WHERE firstname = 'ELEANOR' and lastname = 'RIGBY'"  /*query went here*/
sql.execute(deleteUser) 
// We are intentionally using the list all query from above 
sql.eachRow(listUsers) { 
println(it) 
}
