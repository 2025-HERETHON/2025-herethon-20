# TOOK
2025 여기톤 : HER+ETHON 20팀

### 여성들의 고민을 있는 그대로, "툭"
<img width="830" height="467" alt="image" src="https://github.com/user-attachments/assets/0140e2ab-007c-4f0e-b708-6c50cd8f6a53" />


## 목차
[1. 프로젝트 소개](#1-프로젝트-소개)

[2. 기능](#2-기능)

[3. 기술 스택](#3-기술-스택)

[4. 설치 및 실행](#4-설치-및-실행)

[5. 팀원](#5-팀원)

## 1. 프로젝트 소개
**서비스 개요**
- 10, 20대를 위한 **여성 건강 상담 웹 서비스**로 사용자에게 정서적 지원과 올바른 성 지식을 동시에 지원하고자 한다.
병원 갈 일은 아닌 것 같고, 친구나 가족에게 묻기엔 민망한 여성 건강 관련 질문들을 익명으로 편하게 물을 수 있는 안전한 온라인 공간을 제공한다.

**서비스 기획 의도**
- 10대와 20대는 여성 건강에 대한 관심과 필요가 급격히 증가하는 시기임에도 불구하고, 관련 정보를 정확하고 안전하게 얻을 수 있는 창구가 매우 제한적이다. 
  또한, 산부인과는 진입 장벽이 높은 공간으로 인식된다. 그래서 ‘이 정도로 병원에 가야 할까?’ 싶은 애매한 고민들은 쉽게 외부로 드러내기 어려워 마음속에 묻히게 된다.
  기존의 여성 건강 관련 앱과 웹 서비스는 일방적인 정보를 제공하거나 병원 방문을 유도하는 형식으로 이루어져 있다.
  "툭"은 가볍지만 중요한 질문에 대해 사용자는 익명으로 질문하고 전문의는 실명으로 신뢰도 높은 답변을 제공함으로써 10, 20대 여성들이 정확하고 건강한 성 지식을 편안하게 습득할 수 있는 환경을 만들고자 한다.



## 2. 기능

### 1. 홈 화면
  - **일반 회원의 경우**
    - 성 지식 큐레이션

    - 이번주 HOT 질문: 3일 이내 작성 글 중 답변 수가 가장 많은 질문글 4개 표시

    - 방금 답변된 질문: 가장 최근에 답변이 달린 글 4개 표시

    - 방금 등록된 리뷰: 가장 최근에 작성된 리뷰 4개 표시

    - 내가 쓴 글에 새로운 답변이 달렸을 때 온 알림 확인
  
 -  **전문의 회원의 경우**
    - 방금 등록된 질문: 가장 최근에 작성된 글 4개 표시

    - 전문의 답변을 기다리고 있는 질문: 전문의 답변이 하나도 없는 가장 최근 글 4개 표시

    - 이번주 HOT 질문: 3일 이내 작성 글 중 답변 수가 가장 많은 질문글 4개 표시


### 2. Q&A 게시판
  - **일반 회원의 경우**
    - 게시판:카테고리에 해당하는 글 찾기
    - 게시글: 구제적인 글 확인 및 댓글
    - 검색: 제목 및 내용 키워드로 글 찾기
    - 내 답변: 자신이 작성한 글/ 한 눈에 확인

 -  **전문의 회원의 경우**
    - 게시판:카테고리에 해당하는 글 찾기
    - 게시글: 구제적인 글 확인 및 댓글
    - 검색: 제목 및 내용 키워드로 글 찾기
    - 내 답변/게시물 : 자신이 작성한 글/ 게시물 한 눈에 확인

 
  
### 3. 안심 병원 추천
   - **안심 병원 리스트**
     - 지역을 선택하면 해당 지역의 산부인과 병원을 공공 API로 불러옴
     - 사용자 리뷰를 기반으로 별점, 10대 친화, 여성 전문의 여부 기준으로 병원을 정렬
     
   - **병원 리뷰**
     - 리뷰 작성 및 내가 작성한 리뷰를 확인 & 삭제 가능
     - 병원 상세 페이지 -> 카카오 지도를 통해 병원의 정보와 위치를 직관적으로 확인
     - 병원 리뷰 페이지 -> 전체 사용자가 남긴 리뷰를 최신순, 별점순, 10대 친화순 등으로 정렬하여 볼 수 있으며 리뷰 검색 가능


### 4. 간편상담예약
   - **전문의 리스트**
     - 질문글에 답변을 가장 많이 단 순서로 전문의가 정렬
     - 사용자들은 원하는 전문의를 선택해 해당 전문의가 소속된 병원의 전화번호를 바로 확인할 수 있어 간편하게 상담 예약이 가능

### 5. 마이페이지
  - **일반 회원의 경우**
    - 스크랩한 게시물, 알림 설정, 고객센터, 사용자 가이드
    - 로그아웃, 회원 탈퇴

 -  **전문의 회원의 경우**
    - 본인이 답변한 게시물, 스크랩 게시물, 알림 설정, 고객센터, 사용자 가이드
    - 로그아웃, 회원 탈퇴



## 3. 기술 스택

**백엔드:**
- Python
- Django

**프론트엔드:**
- HTML5
- CSS3
- JavaScript


## 4. 설치 및 실행
### 🚀 2025-HERETHON-20 프로젝트 시작하기

### 1\. 프로젝트 클론 📥

GitHub 저장소에서 프로젝트를 로컬 컴퓨터로 \*\*복제(클론)\*\*합니다.

```bash
git clone https://github.com/2025-HERETHON/2025-herethon-20
```

### 2\. 프로젝트 디렉토리로 이동 📂

프로젝트의 루트 디렉토리로 **이동**합니다.

```bash
cd 2025-herethon-20
```

-----

### 3\. 가상 환경 설정 및 의존성 설치 🛠️

**파이썬 가상 환경**을 설정하고, Django를 설치합니다.

#### 3.1. 가상 환경 생성 (최초 1회)

```bash
python -m venv .venv
```

#### 3.2. 가상 환경 활성화

운영체제에 맞는 명령어를 사용하여 가상 환경을 **활성화**합니다.

  * **Windows 사용자:**
    ```bash
    .venv\Scripts\activate
    ```
  * **macOS/Linux 사용자:**
    ```bash
    source .venv/bin/activate
    ```

#### 3.3. Django 설치

가상 환경이 활성화된 상태에서 **Django**를 설치합니다.

```bash
pip install django
```

-----

### 4\. 데이터베이스 초기화 및 마이그레이션 📊

데이터베이스를 설정하고, Django 모델 변경 사항을 데이터베이스에 **반영**합니다.

#### 4.1. 데이터베이스 오류 발생 시 초기화 (선택 사항)

🚨 **경고**: **데이터베이스 관련 오류**가 발생했을 때만 다음 단계를 수행하세요. 명령어가 제대로 실행되지 않는 경우 해당 파일들을 찾아 수동으로 삭제해주세요.

  * **`db.sqlite3` 파일 삭제:**

      * Windows: `del db.sqlite3`
      * macOS/Linux: `rm db.sqlite3`

  * **각 앱(`hospital`, `posts`, `review`, `users`)의 `migrations` 폴더 내 `.py` 파일 삭제:**
    (`__init__.py` 파일은 삭제하지 마세요\!)

    ```bash
    rm hospital/migrations/*.py
    rm posts/migrations/*.py
    rm review/migrations/*.py
    rm users/migrations/*.py
    ```

#### 4.2. 마이그레이션 파일 생성

데이터베이스에 적용할 마이그레이션 파일을 **생성**합니다.

```bash
python manage.py makemigrations
```

#### 4.3. 데이터베이스에 마이그레이션 적용

생성된 마이그레이션 파일을 데이터베이스에 **적용**하여 테이블을 구축합니다. 이 과정에서 새로운 `db.sqlite3` 파일이 생성됩니다.

```bash
python manage.py migrate
```

-----

### 5\. 초기 데이터 로드

미리 정의된 **초기 데이터**(`fixtures/test_fixture_final.json`)를 데이터베이스에 로드합니다.

```bash
python manage.py loaddata fixtures/test_fixture_final.json
```

-----
### 5.1 테스트 데이터 세팅 

강남구 산부인과 병원 불러오기
공공 API를 통해 실제 병원 데이터를 수집합니다:

```bash
python manage.py fetch_hospitals --sidoCd=110000 --sgguCd=110001
```
👩‍⚕️ 전문의 → 병원 연결 (1:1 매칭)
```bash
python manage.py shell
from users.models import User
from hospital.models import Hospital
```

### 강남구 병원 리스트
```python
gangnam_hospitals = list(Hospital.objects.filter(sgguCd='110001'))
doctor_users = list(User.objects.filter(is_doctor=True))

for i, doctor in enumerate(doctor_users):
    if i < len(gangnam_hospitals):
        doctor.hospital = gangnam_hospitals[i]
        doctor.save()
        print(f"👨‍⚕️ {doctor.username} → 🏥 {gangnam_hospitals[i].name}")
    else:
        print(f"❗ 남은 병원이 없습니다 (총 병원 수: {len(gangnam_hospitals)})")
```
### 6\. Django 개발 서버 실행 🚀

모든 설정이 완료되었다면, **Django 개발 서버**를 시작하여 프로젝트를 실행합니다.

```bash
python manage.py runserver
```

서버가 성공적으로 실행되면, 웹 브라우저에서 `http://127.0.0.1:8000/` (또는 콘솔에 표시되는 주소)로 접속하여 프로젝트를 확인할 수 있습니다.

## 5. 팀원
<table
  style="
    table-layout: fixed;      /* 너비 고정 */
    width: 100%;               /* 테이블 전체 폭 채우기 */
    text-align: center;        /* 가로 중앙정렬 */
    vertical-align: middle;    /* 세로 중앙정렬 */
  "
>
  <colgroup>
    <col width="15%" />
    <col width="25%" />
    <col width="20%" />
    <col width="20%" />
    <col width="20%" />
  </colgroup>

  <thead>
    <tr>
      <th>김지후</th>
      <th>박소연</th>
      <th>이민아</th>
      <th>김가윤</th>
      <th>우예빈</th>
    </tr>
  </thead>

  <tbody>
    <!-- 1. 역할(row) -->
    <tr>
      <th>PM</th>
      <th>FE</th>
      <th>FE</th>
      <th>BE</th>
      <th>BE</th>
    </tr>
    <!-- 2. 기능/업무(row) -->
    <tr>
      <td>기획/디자인</td>
      <td>
        - 안심병원 추천<br>
        - 홈화면<br>
        - 간편상담예약<br>
        - 마이페이지
      </td>
      <td>
        - Q&A 게시판
      </td>
      <td>
        - 안심병원 추천<br>
          (공공api, 카카오맵api)<br>
        - 간편상담예약
      </td>
      <td>
        - 로딩<br>
        - 홈<br>
        - Q&A 게시판<br>
        - 마이페이지
      </td>
    </tr>
    <!-- 3. 소속 학교(row) -->
    <tr>
      <td>이화여자대학교 융합콘텐츠학과</td>
      <td>숙명여자대학교 컴퓨터과학전공</td>
      <td>덕성여자대학교 가상현실융합학과</td>
      <td>성신여자대학교 컴퓨터공학과</td>
      <td>서울여자대학교 소프트웨어융합학과</td>
    </tr>
  </tbody>
</table>
