var name = "Marco";// var variables are just function based. They can't be accessed outside of a function, but can be accessed outsofe of a block ( like an if block)



console.log(name);//This is the same as the ptint function in python, but in the browser console. 

name = "luos";

console.log(name);

if (name == "lous") {
     let fullName = "lous Pineda";//Let variables are "block" based. They can be accessed outside this if statement. 

}
console.log(fullName);

// let should be used over var 

var nombre = "Proal"; //Var can have its value updated. It's function scoped, which means it can't be accessed outside a function, but can be accessed outside a block (like if)
let apeido = "Cotras";// let can have its value updated. It's blocked scoped, which means it can'e be accessed from any block, including "if" or "function"
const age = 23;// Const is a constant and it can't have it's value changed. It's blocked scoped (just like "let"), which means it can't be access inside of a block (like an if block)



const person = { // This is a const value, with two properties, name and gender. NOTE THAT THE const person CAN'T BE UPDATED, HOWEVER, IT'S PROPERTIES CAN, AS DECLARED BELOW:
    name: "Bill";
    gender: "male";
}

person.name = "jane";//This is how you update properties of const values 
person.gender = "female";


// To change values inside of an array, we can use the map function. 
//The following example is done with ES5 syntax. ES6 has an arrow function built-in to simplify the syntax:
//ES% Syntax:
const integers = [1,2,3];

function plus_one(x) {
    return x += 1;
}

const newintegers = integers.map(plus_one);

//ES6 has a new so called "Arrow functions":
//The same function above can be written in ES6:

const newintegers = integers.map((number) => numbers += 1);

// Going through and array, can also be used with the option "filter", to simplify out filtering out elements in the array in one single line of code:

//ES5 Sytax:

const ages = [23,42,6,19];

function Filtering_adults(x) {

    return x > 20;
}

const adults = ages.filter(Filtering_adults);

//ES6 Syntax:

const adults = ages.filter((x) => x > 20);


// Template strings (string formatting):

const name = "Bill";
const age = 25;

const sentence = `My name is ${name}, and I am ${age} years old.`;


// Classes and constructors:

class Person {

    constructor(name, age) {//This constructor creates a new object of the Person class. 
        this.name = name;
        this.age = age;
    }

    speak(){//This is to create a Method of the Class object.
        console.log(`Hi my name is ${this.name}, and I am ${this.age} years old`);
    }
}

const Bill = new Person('bill', 50); // We just created an object "Bill"

Bill.speak(); // This is how a method is called from that object. This will print "Hi my name is bill, and I am 50 years old"



// Adding a new method, and adding elements to it:

class Person {

    constructor(name, age, children) {//This constructor creates a new object of the Person class. 
        this.name = name;
        this.age = age;
        this.children = children
    }

    speak(){//This is to create a Method of the Class object.
        console.log(`Hi my name is ${this.name}, and I am ${this.age} years old`);
    }
    birth(){
        this.children.push(child);//This appends to the children array/list
    }
}

const Bill = new Person('bill', 50, ['sean', 'paul']); // We just created an object "Bill"

Bill.speak(); // This is how a method is called from that object. This will print "Hi my name is bill, and I am 50 years old"
Bill.birth('Jess');//This appends "Jess" to the list through the method of birth
console.log(Bill.children); //This will print/log ['sean', 'paul', 'Jess']

// Spread operator (...) - The Spread operator will "sread" or indivualize elements in an array/list. They will be treated as independent elements, no longer a s a list of elements:

const names = ['John', 'Bill', 'Sam'];
const new_names = ['William', 'Paul']

//What if we want to output: ['John', 'Bill', 'Sam', 'Gio', 'William', 'Paul']?

const allNames = [...names, 'Gio', ...new_names];

console.log(allNames); //This will print ['John', 'Bill', 'Sam', 'Gio', 'William', 'Paul']. With ES5, and no Spread operator, each list would have been concatenated to the new array. 



