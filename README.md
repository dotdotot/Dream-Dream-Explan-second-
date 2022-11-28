# # Dream-Dream-Explan-second-
🗓 프로젝트 소개 : Dream-Dream-Explan-second-</br>
🗓 기간 : 2022.8.13 ~ 2022.11.29  </br>
🗓 팀원:  [준석](https://github.com/dotdotot)</br>
🗓 리뷰어: [정준](https://github.com/oolle4043)</br></br>
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

#
# 결과물</br>


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







