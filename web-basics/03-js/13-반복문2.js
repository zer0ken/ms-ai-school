arr = [1, 2, 3]
arr["오?"] = "오오 ㅋㅋ"
arr["와"] = "이거 진짜에요?"

console.log("# for-in");
for (const key in arr) {
    console.log(`${key}: ${arr[key]}`);
}

console.log("\n# for-of");
for (const element of arr) {
    console.log(element);
}

console.log("\n# for-each");
arr.forEach((item, index, array) => {
    console.log(`[${array}][${index}]: ${item}`);
});