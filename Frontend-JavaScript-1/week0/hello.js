"use strict";

// variables
var a = 5;
var b = 6;

console.log(a + b);
console.log("\nData types");
// data types
var n = 7;
var str = "JS is deceptive";


// array/list
var list = [5, 6, 7];
console.log(list);

// functions
var f = function(x) {
    return x * x;
};
console.log("\nFunctions");
console.log(f(5));

// objects
var courses = {
    "Frontend JS": "javascript.com",
    "Core Java": "java.com",
};

console.log("\nObjects");
console.log(courses);

// func scope
var arr = [1, 2, 3];
for (var i = 0; i < arr.length; i++) {
    console.log(arr[i]);
}

console.log("\nFunc scope");
console.log(i);


// iterating arrays
var
    iterArr = [1, 2, 3],
    i = 0,
    n = iterArr.length;


for (var course in courses) {
    console.log("A link for " + course + " can be found here " + courses[course]);
}

console.log(Object.keys(courses));


// forEach
Object.keys(courses).forEach(function(value) {
    console.log("A link for " + value + " can be found here - " + courses[value]);
});

// Array sort
var numbers = [4, 2, 5, 1, 3];
console.log(numbers);
numbers.sort(function(a, b) {
    return b - a;
});
console.log(numbers);
