# 2025-herethon-20 (!서비스 이름, 제목)
2025 여기톤 : HER+ETHON 20팀(!한줄 소개)

## 목차
[1. 프로젝트 소개](#1-프로젝트-소개) v

[2. 기능](#2-기능) v

[3. 기술 스택](#3-기술-스택)

[4. 설치 및 실행](#4-설치-및-실행)

[5. 팀원](#5-팀원) v (각자 담당기능 쓰기)

## 1. 프로젝트 소개
ㄴㅇㄴㄹㄹㄴ

## 2. 기능

- **안심병원 추천**:  
지역을 선택하면 해당 지역의 산부인과 병원을 공공 API로 불러오고,  
사용자 리뷰를 기반으로 별점, 10대 친화, 여성 전문의 여부 기준으로 정렬하여 안심하고 방문할 수 있는 병원을 추천합니다.  
사용자들은 리뷰를 작성하고, 내가 작성한 리뷰를 모아보고, 수정/삭제할 수 있습니다.  
병원 상세 페이지에서는 카카오 지도를 통해 병원의 위치를 직관적으로 확인할 수 있고,  
전화번호도 바로 확인할 수 있어 예약 및 문의가 용이합니다.

- **간편상담예약**:  
  질문글에 답변을 가장 많이 단 순서로 전문의가 정렬되며,  
  사용자들은 원하는 전문의를 선택해 해당 전문의가 소속된 병원의 전화번호를 바로 확인할 수 있어  
  간편하게 상담 예약이 가능합니다.

## 3. 기술 스택

**백엔드:**
- Python
- Django

**프론트엔드:**
- HTML5
- CSS3
- JavaScript


## 4. 설치 및 실행
## 🚀 2025-HERETHON-20 프로젝트 시작하기

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
* **김지후**: 멋쟁이사자처럼 13기 아기사자 | **기획/디자인** (담당 기능) | 이화여자대학교 융합콘텐츠학과
* **김가윤**: 멋쟁이사자처럼 13기 아기사자 | **백엔드** (담당 기능) | 성신여자대학교 컴퓨터공학과
* **우예빈**: 멋쟁이사자처럼 13기 아기사자 | **백엔드** (로딩, 홈, Q&A 게시판, 마이페이지) | 서울여자대학교 소프트웨어융합학과
* **박소연**: 멋쟁이사자처럼 13기 아기사자 | **프론트엔드** (담당 기능) | 숙명여자대학교 컴퓨터과학전공
* **이민아**: 멋쟁이사자처럼 13기 아기사자 | **프론트엔드** (담당 기능) | 덕성여자대학교 가상현실융합학과
