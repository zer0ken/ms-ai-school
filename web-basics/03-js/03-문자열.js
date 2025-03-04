console.log(typeof "hello");
console.log(typeof `hello`);

console.log("newline\nwow");

let a = 12;
let b = "what?!";

console.log(`a is ${a} and ${b}`);

let name_ = "이현령";
let age = 24
console.log(`이제는 프로그래밍 고수가 되고 싶은 ${age}세 ${name_}... 그러다 그는 문득`);

const message = 'Hello, world!';
console.log(message);
console.log("length:", message.length);
console.log("at 0:", message[0]);
console.log("at -1:", message[-1]);
console.log("at 100:", message[100]);

console.log("index of 'w':", message.indexOf("w"));
console.log("index of 'wor':", message.indexOf("wor"));
console.log("index of 'X':", message.indexOf("X"));

console.log("includes \"Hello\"?", message.includes("Hello"));
console.log("includes \"xxx\"?", message.includes("xxx"));

console.log(message.toUpperCase());
console.log(message.toLowerCase());

console.log(message.substring(0, 5));
console.log(message.substring(-6, -1)); // 안됨

console.log(message.slice(0, 5));
console.log(message.slice(-6, -1));

console.log(message.startsWith('Hell'));
