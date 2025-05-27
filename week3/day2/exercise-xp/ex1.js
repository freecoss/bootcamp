const people = ["Greg", "Mary", "Devon", "James"];

people.shift();

people[people.indexOf("James")] = "Jason";

people.push("YourName");

console.log(people.indexOf("Mary"));

const newPeople = people.slice(1, 3);
console.log(newPeople);

console.log(people.indexOf("Foo"));

const last = people[people.length - 1];
console.log(last);

for (let person of people) {
  console.log(person);
}

for (let person of people) {
  console.log(person);
  if (person === "Devon") break;
}

