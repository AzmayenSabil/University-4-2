abstract sig Person {
  father: lone Man,
  mother: lone Woman
}

sig Man extends Person {
  wife: lone Woman
}

sig Woman extends Person {
  husband: lone Man
}

fact {
	no p: Person | p in p.^(mother + father)
}

fact {
	no m: Man | m.wife in m.^(mother + father)
	no w: Woman | w.husband in w.^(mother + father)
}

fact {
	wife = ~husband
}

//TASK-1

// Assertions
assert NoSelfFather {
  no m: Man | m in m.^father
}
check NoSelfFather

assert NoSelfMother {
  no w: Woman | w in w.^mother
}
check NoSelfMother

assert NoSelfParent {
  no p: Person | p in (p.father + p.mother)
}
check NoSelfParent


//TASK-2
fun grandpas[p: Person] : set Person {
	p.(mother + father).father
}

//TASK-3
pred ownGrandpa[p: Person] {
	p in grandpas[p]
}

run {
    some p: Person | grandpas[p] in Person
} for 6 Person, 3 Man, 3 Woman
run ownGrandpa for 10 Person
run {} for 6 Person, 3 Man, 3 Woman


















