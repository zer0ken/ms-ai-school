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


// 홀짝

function isOdd(x) {
    return Boolean(x % 2);
}

const isOdd2 = function (x) {
    return Boolean(x % 2);
};

const isOdd3 = (x) => Boolean(x % 2);


for (let i = 1; i <= 5; i++) {
    console.log(isOdd(i), isOdd2(i), isOdd3(i));
    console.log(`${i} -> ${isOdd3(i) ? "홀수" : "짝수"}`);
}