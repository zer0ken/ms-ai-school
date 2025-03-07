function addSimulation() {
    const initial = parseInt(document.querySelector("input[name='now']").value);
    const finish = parseInt(document.querySelector("input[name='goal']").value);
    const delta = parseInt(document.querySelector("input[name='week']").value);

    let simulationHTML = "";
    if (finish < 0) {
        simulationHTML = "<li>목표 금액은 0원 이상이어야 합니다.</li>";
    } else if (delta <= 0 && initial < finish) {
        simulationHTML = "<li>매주 1원 이상의 금액을 저금해야 합니다.</li>";
    } else {
        let total = initial;
        let week = 0;
        while (total < finish) {
            week += 1;
            total += delta;
            simulationHTML += `
        <li>
            <div class="weeks">${week}주차 저금액:</div>
            <div class="now-saving">${total}원</div>
        </li>`;
        }
    }

    document.querySelector("#simulation").innerHTML = simulationHTML
        ? simulationHTML
        : "<li>이미 목표 금액을 달성했습니다!</li>";
}


document.querySelector("input[type='button']").onclick = addSimulation;
