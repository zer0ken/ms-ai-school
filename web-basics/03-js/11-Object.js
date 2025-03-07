// Object 생성
a = new Object();
b = {};
console.log(a, b);

// Object 생성과 초기화
c = { 1: 591, 2: "오", "감자튀김": "먹고싶다", "abc": "def" };
console.log(c);

// Object의 속성 읽기
console.log(c[1], c[2], c["감자튀김"], c.abc);

// Object 속성 변경
c[1] = 1;
console.log(c);

// Object 속성 삭제
delete c[2];
console.log(c);

// 이건 삭제되는게 아니라 값이 undefined로 바뀌는 것일 뿐입니다.
c.abc = undefined;
console.log(c);

// 복잡한 object 사용 예시
const user = {
    name: '이현령',
    age: '25',
    addAge: function () {
        this.age++;
        return this.age;
    }
};

console.log('user', user);
console.log('user.addAge()', user.addAge());
console.log('user', user);

// 속성 추가
user.height = 166;
console.log('user', user);