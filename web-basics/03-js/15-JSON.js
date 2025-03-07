const user = {
    name: "이현령",
    age: 25
};

console.log('user', typeof user, user);

const data = JSON.stringify(user);
console.log('data', typeof data, data);

const user2 = JSON.parse(data);
console.log('user2', typeof user2, user2);

const data2 = JSON.stringify(user2);
console.log('data2', typeof data2, data2);

console.log('user == user2', user == user2);
console.log('user === user2', user === user2);
console.log('data == data2', data == data2);