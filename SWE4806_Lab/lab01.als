//sig B{}
//sig A{
//	f: set B
//}	
//
//run {} for 10

abstract sig Person {
	children: set Person,
	siblings: set Person
} 

sig Man, Woman extends Person {} 

sig Married in Person {
	spouse: one Married
} 

fact {
	all p: Person | p not in p.children
	all p: Person | p not in p.siblings
	all p: Person | p not in p.spouse
	all disj p1, p2: Person | p2 in p1.children => p2 not in p1.spouse and 
									      p2 not in p1.siblings
}

run {} for 5
