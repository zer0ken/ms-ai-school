function add(x, y) {
    return x + y;
}

console.log(add(3, 5));

const add2 = function (x, y) {
    return x + y;
};

console.log(add2(3, 5));

const add3 = (x, y) => {
    return x + y;
}
console.log(add3(3, 5));

const add4 = (x, y) => x + y;
console.log(add4(5, 5));
