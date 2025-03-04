let x;
x = String(1);
console.log(x, typeof x);

x = (false).toString();
console.log(x, typeof x);

x = (1.5).toString();
console.log(x, typeof x);

x = Number(4.5);
console.log(x, typeof x);

x = parseFloat("5.1245")
console.log(x, typeof x);

// 사사오입(round half-up)
x = (4.5).toFixed(0);
console.log(x, typeof x);

x = Boolean(4.5);
console.log(x, typeof x);