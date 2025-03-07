const $input = document.querySelector("input[type='number']");
const $submitBtn = document.querySelector("input[type='button']");
const $message = document.querySelector(".message");
const $seatContainer = document.querySelector("#seat-container");


function renderSeat() {
    const num = $input.value ? parseInt($input.value) : 0;
    $input.value = num;

    if (num <= 0 || num > 100) {
        $message.textContent = "학생 수는 1명 ~ 100명이어야 합니다.";
        $seatContainer.innerHTML = "";
    } else {
        console.log(`학생 수: ${num}`);
        $message.textContent = "";
        let seatHTML = "";
        for (let i = 1; i <= num; i++) {
            seatHTML += `<div class="seat">${i}</div>`;
        }
        $seatContainer.innerHTML = seatHTML;
    }
}


$input.onkeyup = (e) => e.key == "Enter" ? renderSeat() : null;
$submitBtn.onclick = renderSeat;