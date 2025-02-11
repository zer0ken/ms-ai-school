# 👁️‍🗨️ Custom-Vision

Azure Custom Vision을 사용해 이미지 분류와 객체 검출을 수행하는 실습입니다.

<table>
    <tr>
        <th>🐇 Object Detection</th>
        <th>🪨 Classification</th>
    </tr>
    <tr>
        <td>이미지 내에서 객체의 위치를 찾는 객체 검출 실습입니다.</th>
        <td>이미지의 유형을 분류하는 실습입니다.</th>
    </tr>
    <tr>
        <td><img src="/resources/custom-vision2.png"></th>
        <td><img src="/resources/custom-vision3.png"></th>
    </tr>
</table>

> [!NOTE]
> 학습과 테스트에 사용한 데이터셋은 저장소에 포함되어있지 않습니다. 코드를 직접 실행하려면 `dataset/` 디렉토리에 강의자료로 배포된 [데이터셋](https://elixirrkc.sharepoint.com/:u:/r/sites/Microsoft6/Shared%20Documents/%EC%9D%BC%EB%B0%98/%EA%B0%95%EC%9D%98%EC%9E%90%EB%A3%8C/25.02%EC%9B%94%20%EA%B0%95%EC%9D%98%EC%9E%90%EB%A3%8C/0203%2009-18%EC%8B%9C%20%EA%B0%95%EC%9D%98%EC%9E%90%EB%A3%8C(%EA%B6%8C%EC%A7%84%EC%9A%B1)/CV_%E1%84%89%E1%85%B5%E1%86%AF%E1%84%89%E1%85%B3%E1%86%B8%E1%84%83%E1%85%A6%E1%84%8B%E1%85%B5%E1%84%90%E1%85%A5(%E1%84%89%E1%85%A1%E1%86%BC%E1%84%80%E1%85%A9%E1%86%BC).zip?csf=1&web=1&e=jK2JnR)의 내용물을 붙여넣어야 합니다.

> [!NOTE]
> 코드 실행에 사용될 인터프리터에 `requirements.txt`에서 명시하는 라이브러리들을 미리 설치하세요. `pip` 버전을 업그레이드해야 할 수도 있습니다. 다음 예시 코드를 참고하세요.
> ```
> python -m pip -U pip
> pip install -r requirements.txt
> ```
> 사용 가능한 라이브러리 버전은 인터프리터 버전에 따라 다를 수 있습니다. 이 저장소에서는 python 3.12.7 인터프리터와 그에 맞는 라이브러리들을 사용하고 있으니 참고하세요.

---
[`나가기`](../)