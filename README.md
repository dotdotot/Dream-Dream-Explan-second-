# Dream-Dream-Explan-second-
🗓 프로젝트 소개 : Dream-Dream-Explan-second-</br>
🗓 기간 : 2022.8.13 ~ 2022.11.29  </br>
🗓 팀원:  [준석](https://github.com/dotdotot)</br>
🗓 리뷰어: [정준](https://github.com/oolle4043)</br>
🗓 리뷰어: [준석](https://github.com/dotdotot)</br></br>


#
# 도전학기제 신청 이유
![image](https://user-images.githubusercontent.com/77331459/204349578-82b485d3-a5d3-48ef-a9bb-82dc6aa8bf64.png)</br>
학교에 많은 강의를 들었지만, 대부분이 교수님이 알려주는 내용을 그대로 따라가서 학습하거나 앞, 부분의 진도를 예습하는 정도가 다였습니다.</br>
학교 수업도 물론 좋지만 내가 생각했던 아이디어를 간단한 프로젝트라도 진행해보는 경험이 중요하다고 생각하였고 배재대학교 도전 학기제라는 좋은 기회를 통해서 팀 프로젝트를 진행하기 위해서 신청하였습니다.</br>

#
# 주제 선정 이유
![image](https://user-images.githubusercontent.com/77331459/204350927-81843593-082c-4e72-a565-a9a7e9f87d17.png)

그동안 c, python, java, c++, andrioid 등 많은 언어들 듣고 실습을 진행해보았으나 실제로 해당 언어들로 내가 원하는 소프트웨어를 구현해본 적은 거의 없었습니다.

이번 팀 프로젝트로 내가 원하는 소프트웨어를 만들어 볼 기회가 생기게 되었고
하나의 주제를 선정하게 되었습니다.</br></br>


![image](https://user-images.githubusercontent.com/77331459/204360382-d3d37eba-701c-4534-81b1-17b1fdbdcc39.png)

소프트웨어만 구현하는 것이 아닌 Arduino를 활용하여 하드웨어와 소프트웨어가 동시에 동작하도록 만들고싶었고 다양한 자판기를 써보았으나
우산 자판기는 써본적이 없어서 해당 우산 자판기를 만들게되었습니다.

단순히 판매를 하는것이 아닌 우산을 대여하고 반납하는 형식으로 자판기를 만들게되었습니다.


#
# 하드웨어</br>

## Arduino
![image](https://user-images.githubusercontent.com/77331459/204361070-1402d197-bd57-41d3-8994-979d85cfdc05.png)

하드웨어는 아두이노 MEGA를 활용하고 무선 연결을 위해서 외부 배터리, DC모터, 습도를 연결하였습니다.
무선 연결을 위해서 사용한 외부 배터리는 리튬배터리이며 
DC모터는 도어를 열고 닫기위해 사용하였습니다.
또한, 제품 내부의 습도를 계속해서 계산하기 위해서 DHC-11 모듈을 사용하여 습도를 계산하였습니다.

![image](https://user-images.githubusercontent.com/77331459/204361770-889e38b1-03af-4fec-b2e8-f55416220fb4.png)

MEGA와 웹 서버가 통신를 하기위해서는 WeMos D1 WIFI모듈을 사용하여 통신의 중간 통로 역할을 도맡았으며 MAGA에서 발생하는 모든 데이터는 Server로 전송되었습니다.

## 부품 설계도

자판기 역할을 하는 실모델이 따로 존재해야하기 때문에 부품을 설계하고 해당 실모델을 배재대학교 레이저커팅기를 이용하여 제작하였습니다.

![image](https://user-images.githubusercontent.com/77331459/204362126-7420163d-b7aa-41ea-b6dc-d93c40ec09da.png)

![image](https://user-images.githubusercontent.com/77331459/204362158-075884a6-e1e8-4d2f-9eb2-6b82caf9bdab.png)

![image](https://user-images.githubusercontent.com/77331459/204362191-0021fb06-5f94-4961-9bb0-363283c8922a.png)

![image](https://user-images.githubusercontent.com/77331459/204362403-9ef398c5-385b-4a35-88b9-4dbe1220f761.png)

#
# 소프트웨어</br>

## 구조도
![image](https://user-images.githubusercontent.com/77331459/204364343-555c83b1-436f-486c-8a07-455a777bff90.png)
전체적인 구조는 안드로이드에서 클라이언트에서 우산을 대여했다는 Request가 서버로 전송되면 서버는 이미 대여중인 도어인지 문제가 없는지 메소드 내부 코드를 통해서 확인 절차를 진행하고</br>
문제가 없다는 것이 확인되면 MEGA에 클라이언트가 선택한 도어를 열라는 Response 요청을 발송합니다.</br>
MEGA는 해당 도어를 여는 도중에 문제가 없었다는 것을 Server에 Request 요청을 발송하고 서버는 내부 작업을 마친뒤 클라이언트에게 도어가 열렸다는 Response 메세지를 발송합니다.</br>

서버에서 데이터베이스를 관리하고 있기때문에 모든 기록은 DB에 저장됩니다.

## 안드로이드

#### 로그인화면 및 회원가입 화면
![image](https://user-images.githubusercontent.com/77331459/204364375-c4d55c62-3c5d-4eb1-bd7c-c56e04fb8b41.png)
#### 아이디 찾기 및 비밀번호 찾기 화면
![image](https://user-images.githubusercontent.com/77331459/204364392-000fbec5-c102-4583-b1c7-2680fa966d29.png)
#### 우산을 대여하는 메인 화면
![image](https://user-images.githubusercontent.com/77331459/204364429-ac7649c7-7b09-4152-aa47-9b7758cfd321.png)

## 데이터베이스
![image](https://user-images.githubusercontent.com/77331459/204364465-0f6c653f-b024-4977-9170-8507863824a1.png)
DB는 사용자가 회원가입할때마다 저장되는 회원 정보를 저장하는 테이블이 존재하며 기본키로 사용자의 아이디를 가지며 사용자 비밀번호, 사용자 이름, 사용자 성별, 이메일, 전하번호, 생일, 접근권한을 속성으로 가집니다.</br>
사용자 비밀번호는 모두 인코딩되어 저장되며 이후 클라이언트에서 로그인할때 비밀번호가 정확한지는 디코딩되어 확인하게됩니다.

도어를 관리하는 테이블이 존재하며 해당 테이블은 도어번호를 기본키로 가지며 
대여한 사용자의 ID, 도어 상태, 등록 날짜를 속성으로 가집니다.</br>
대여한 사용자가 없고 닫혀있는 상태라면 대여한 사용자의 아이디는 NULL값을 가집니다.

어떤 사용자가 대여했고 언제 반납을 하였는지 모든 기록은 로그 테이블에 저장되며 로그 테이블은 도어번호, 삭제이유, 삭제날짜, 등록날짜, 사용자 아이디를 속성으로 가집니다.
## 서버
### Flask
Flask는 Python의 마이크로 웹 프레임워크입니다.</br>
코드도 비교적 단순하고 가벼워서 API를 위한 서버를 만들기에 매우 편리합니다.(관련된 확장 기능이 많음)</br>
추후 Rest Api를 이용해 서버간 통신을 진행할 것이기 때문에 API를 위한 Server로 Flask를 선택했습니다.</br>

### Rest api
REST API는 다음의 구성으로 이루어져있습니다. 
- 자원(RESOURCE) - URI
- 행위(Verb) - HTTP METHOD
- 표현(Representations)

Rest api 특징
1) Uniform (유니폼 인터페이스)
Uniform Interface는 URI로 지정한 리소스에 대한 조작을 통일되고 한정적인 인터페이스로 수행하는 아키텍처 스타일을 말합니다.

2) Stateless (무상태성)
REST는 무상태성 성격을 갖습니다. 다시 말해 작업을 위한 상태정보를 따로 저장하고 관리하지 않습니다. 세션 정보나 쿠키정보를 별도로 저장하고 관리하지 않기 때문에 API 서버는 들어오는 요청만을 단순히 처리하면 됩니다. 때문에 서비스의 자유도가 높아지고 서버에서 불필요한 정보를 관리하지 않음으로써 구현이 단순해집니다.

3) Cacheable (캐시 가능)
REST의 가장 큰 특징 중 하나는 HTTP라는 기존 웹표준을 그대로 사용하기 때문에, 웹에서 사용하는 기존 인프라를 그대로 활용이 가능합니다. 따라서 HTTP가 가진 캐싱 기능이 적용 가능합니다. HTTP 프로토콜 표준에서 사용하는 Last-Modified태그나 E-Tag를 이용하면 캐싱 구현이 가능합니다.

4) Self-descriptiveness (자체 표현 구조)
REST의 또 다른 큰 특징 중 하나는 REST API 메시지만 보고도 이를 쉽게 이해 할 수 있는 자체 표현 구조로 되어 있다는 것입니다.

5) Client - Server 구조
REST 서버는 API 제공, 클라이언트는 사용자 인증이나 컨텍스트(세션, 로그인 정보)등을 직접 관리하는 구조로 각각의 역할이 확실히 구분되기 때문에 클라이언트와 서버에서 개발해야 할 내용이 명확해지고 서로간 의존성이 줄어들게 됩니다.

6) 계층형 구조
REST 서버는 다중 계층으로 구성될 수 있으며 보안, 로드 밸런싱, 암호화 계층을 추가해 구조상의 유연성을 둘 수 있고 PROXY, 게이트웨이 같은 네트워크 기반의 중간매체를 사용할 수 있게 합니다.


REST API 설계 시 가장 중요한 항목은 다음의 2가지로 요약할 수 있습니다.

첫 번째, URI는 정보의 자원을 표현해야 한다.</br>
두 번째, 자원에 대한 행위는 HTTP Method(GET, POST, PUT, DELETE)로 표현한다.</br>

POST - POST를 통해 해당 URI를 요청하면 리소스를 생성합니다.</br>
GET - GET를 통해 해당 리소스를 조회합니다. 리소스를 조회하고 해당 도큐먼트에 대한 자세한 정보를 가져온다.</br>
PUT - PUT를 통해 해당 리소스를 수정합니다.</br>
DELETE - DELETE를 통해 리소스를 삭제합니다.</br>

즉, Html 파일을 전송하는 것이 주된 목적이 아닌 데이터를 전송하는 것이 주된 목적이기 때문에 Http를 강화한 Rest api와 Flask를 사용하여 서버를 구상하였습니다.

#
# 결과물</br>

![image](https://user-images.githubusercontent.com/77331459/204364229-b5726349-e545-4673-aa47-4dd71fb79e6e.png)

#
# Commit 규칙
> 커밋 제목은 최대 50자 입력 </br>
본문은 한 줄 최대 72자 입력 </br>
Commit 메세지 </br>

🪛[chore]: 코드 수정, 내부 파일 수정. </br>
✨[feat]: 새로운 기능 구현. </br>
🎨[style]: 스타일 관련 기능.(코드의 구조/형태 개선) </br>
➕[add]: Feat 이외의 부수적인 코드 추가, 라이브러리 추가 </br>
🔧[file]: 새로운 파일 생성, 삭제 시 </br>
🐛[fix]: 버그, 오류 해결. </br>
🔥[del]: 쓸모없는 코드/파일 삭제. </br>
📝[docs]: README나 WIKI 등의 문서 개정. </br>
💄[mod]: storyboard 파일,UI 수정한 경우. </br>
✏️[correct]: 주로 문법의 오류나 타입의 변경, 이름 변경 등에 사용합니다. </br>
🚚[move]: 프로젝트 내 파일이나 코드(리소스)의 이동. </br>
⏪️[rename]: 파일 이름 변경이 있을 때 사용합니다. </br>
⚡️[improve]: 향상이 있을 때 사용합니다. </br>
♻️[refactor]: 전면 수정이 있을 때 사용합니다. </br>
🔀[merge]: 다른브렌치를 merge 할 때 사용합니다. </br>
✅ [test]: 테스트 코드를 작성할 때 사용합니다. </br>







