var v1;
v1 = 1;
console.log("v1:", v1);

console.log("v2:", v2);
console.log("v3:", v3);

var v2 = 2;
var v3 = 3;

console.log("v2:", v2);
console.log("v3:", v3);


/** console.log("l1:", l1);
 * ReferenceError: Cannot access 'l1' before initialization
 */

let l1;
console.log("l1:", l1);
l1 = 11;
console.log("l1:", l1);

/** const c1;
 * SyntaxError: Missing initializer in const declaration
 */
const c1 = 21;
console.log("c1:", c1);