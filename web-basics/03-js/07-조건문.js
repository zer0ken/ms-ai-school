let temperature = 25;

if (temperature >= 30) {
    console.log("집에 있기");
} else if (temperature >= 20) {
    console.log("공원");
} else if (temperature >= 10) {
    console.log("카페");
} else {
    console.log("영화관");
}

let score = 40;

if (score >= 60) {
    console.log("합격입니다.");
} else {
    console.log("불합격입니다.");
}


let year = 2024;
let month = 2;
let days, cond1, cond2, cond3;

switch (month) {
    case 1:
    case 3:
    case 5:
    case 7:
    case 8:
    case 10:
    case 12:
        days = 31;
        break;
    case 4:
    case 6:
    case 9:
    case 11:
        days = 30;
        break;
    case 2:
        cond1 = year % 4 == 0;
        cond2 = year % 100 == 0;
        cond3 = year % 400 == 0;
        days = cond1 && (!cond2 || cond3) ? 29 : 28;
        break;
    default:
        days = `${ month } is Invalid Month`;
}

console.log(`year: ${year}\nmonth: ${month}\ndays: ${days}`);
