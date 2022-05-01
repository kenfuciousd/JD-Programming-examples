// List of identities in CSV format 
// Firstname, Middlename, Lastname, Nickname 
def identities = [ 
["John", "Jacob", "Schmidt", "Jingleheimer"], 
["Billie", "", "Jean", ""], 
["ELEANOR", "", "RIGBY", ""], 
["Slim", "", "Shady", "Marshal"], 
["Eleanor", "", "Rigby", ""] 
] 
// adding a new line to start on a clean foot, for troubleshooting
print "\n" 
// Complete the functions by returning an array of usernames. Use sequences 
// to prevent duplicates, but only when a duplicate occurs. 
//// A ////
// in the following format <first_initial_of_first_name><lastname><numeric_sequence> 
def formatA(List list) { 
// // beginning edits here, fourth iteration
// loop through the list, get ahold of each entry, manipulate as needed.
// iterate the list, with indexes, to build map.
def outList = []
list.eachWithIndex{row, i ->
//	print "i is: $i and row is: $row \n"
// make an empty string to use to reconstruct each element
	def inString = ""
	row.eachWithIndex{column, j ->
//		print "-- within each row, item $j is $column\n"
		// hard coding the formatting till I get more clever
		if(j == 0){ 
//		print "Adding substring: " + inString + "\n"
		inString = column.substring(0,1)
		}
		if(j == 2){ 
//		print "adding lastname:" + inString + "\n"
		inString += column
		}
	}
	// and close with the iteration, for the row
	inString += i
//	print "Now reconstructed, it looks like $inString - \n"
	outList.add(inString)
}
//print "outList looks like: $outList\n"
// def usernames = list
def usernames = outList
return usernames 
} 
print "Format A, usernames: "+ formatA(identities) + "\n" 

// B 
// in the following format 
//<first_name><nickname_if_present><lastname><numeric_sequence> 
def formatB(List list) { 
def outList = []
list.eachWithIndex{row, i ->
//	print "i is: $i and row is: $row \n"
// make an empty string to use to reconstruct each element
	def inString = ""
	def firstName
	def middleName
	def lastName
	def nickName
	row.eachWithIndex{column, j ->
// instantiating empty variables for each row, to avoid a later test error.
//		print "-- within each row, item $j is $column\n"
		if(j == 0){ firstName = column}
		if(j == 1 && column != "") { 
//			print "Double checking: found a middle name $column\n"
			middleName = column
		}
		if(j == 2){ lastName = column }
		if(j == 3 && column != ""){
//			print "Double checking: found a nickname $column\n"
			nickName = column
		}
	}
		// then construct the string
	if(nickName != null){
		inString = firstName + nickName + lastName + i
	}
	else{
		inString = firstName + lastName + i
	}
	// and close with the iteration, for the row
//	print "Now reconstructed, it looks like $inString - \n"
	outList.add(inString)
}
def usernames = outList
return usernames 
} 
print "Format B: " + formatB(identities) + "\n" 

// C 
// in the following format 
//<first_initial_of_nickname_if_present_otherwise_use_fi_of_firstname><lastname><numeric_sequence> 
def formatC(List list) { 
def outList = []
list.eachWithIndex{row, i ->
// make an empty string to use to reconstruct each element
	def inString = ""
	def firstName
	def middleName
	def lastName
	def nickName
	row.eachWithIndex{column, j ->
// instantiating empty variables for each row, to avoid a later test error.
		if(j == 0){ firstName = column.substring(0,1)}
		if(j == 1 && (column != null && column != "")){middleName = column}
		if(j == 2){ lastName = column }
		if(j == 3 && (column != null && column != "")){nickName = column.substring(0,1)}
	} //end columns .each
		// then construct the string
	if(nickName != null){
		inString = nickName + lastName + i
	}
	else{
		inString = firstName + lastName + i
	}
	// and close with the iteration, for the row
//	print "Now reconstructed, it looks like $inString - \n"
	outList.add(inString)
} // end rows .each
def usernames = outList 
return usernames 
} 
print "Format C: " + formatC(identities) + "\n" 

// D 
// in the following format 
//<Lastname><comma><Firstname><comma_if_middlename><Middlename><comma_if_nickname><Nickname><numeric_sequence> 
def formatD(List list) { 
def outList = []
list.eachWithIndex{row, i ->
//	print "i is: $i and row is: $row \n"
// make an empty string to use to reconstruct each element
	def inString = ""
	def firstName
	def middleName
	def lastName
	def nickName
	row.eachWithIndex{column, j ->
//		print "-- within each row, item $j is $column\n"
		if(j == 0){ firstName = column}
		if(j == 1 && (column != null && column != "")){middleName = column}
		if(j == 2){ lastName = column }
		if(j == 3 && (column != null && column != "")){nickName = column}
	}
	// then construct the string
	inString = lastName + ", " + firstName + ", "
	if(middleName != null){ inString += middleName + ", "}
	if(nickName != null){inString += nickName + ", "}
	inString += i
	outList.add(inString)
}
def usernames = outList 
return usernames 
} 
print "Format D: " + formatD(identities) + "\n"