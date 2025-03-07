const answer = Math.floor(Math.random() * 100) + 1;

const $inputNumber = document.querySelector('#input-number');

const $btnSubmit = document.querySelector('button');
$btnSubmit.onclick = guess;

const $result = document.querySelector('#result');

let trial = 0;
let is_finished = false;

function guess() {
    if (is_finished) {
        return;
    }

    const input = $inputNumber.value.trim();
    if (!input) {
        return;
    }
    
    const guess = parseInt(input);
    let message = '';

    if (guess < 1 || guess > 100) {
        message = '1 이상 100 이하의 수만 입력하세요.';
    }
    else {
        trial++;
        if (guess == answer) {
            message = `🎊 <b>정답입니다!</b> ${trial}회 만에 맞췄습니다. 🎊`
        } else if (guess < answer) {
            message = `정답은 ${guess} 보다 <b>큰</b> 숫자입니다.`
        } else {
            message = `정답은 ${guess} 보다 <b>작은</b> 숫자입니다.`
        }
    }

    $result.innerHTML = message;
}