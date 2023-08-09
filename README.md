# 오토 홀덤 게임 ( Auto Card Game )

## 목차
*  📝 [개요](#-개요)
*  🛠 [기술 및 도구](#-기술-및-도구)
*  ✨ [기능 구현](#-기능-구현)
*  ⏰ [일정](#-일정)

## **📝 개요**
> **프로젝트** : 카드 자동 분배기
>
> **인원** : 5인
> 
> **주제** : 서보모터 제어를 통한 세븐 포커 규칙을 활용한 게임
> 
> **제작 기간** : 6.30 ~ 7.24
> 
> **주요 기능**   
> > * 인원수에 따른 해당 게임의 시작   
> > * 각 인원 위치에 게임 룰에 따른 카드 분배 동작
> > * MG995 서브 모터를 활용한 카드 출력 부분 제어
>
> [**NOTION 링크**](https://www.notion.so/db9bc874b60b441797a1a5883396fe31?pvs=4)



## **🛠 기술 및 도구**   
> **언어** : <img alt="python" src ="https://img.shields.io/badge/python-3776AB.svg?&style=flat-square&logo=python&logoColor=white"/>   
> **환경** : <img alt="raspberrypi" src ="https://img.shields.io/badge/raspberrypi-A22846.svg?&style=flat-square&logo=raspberrypi&logoColor=white"/>
> - Raspberry Pi OS (32-bit) | release : 2023-05-03
>
> **도구** : <img alt="github" src ="https://img.shields.io/badge/github-181717.svg?&style=flat-square&logo=github&logoColor=white"/>, <img alt="notion" src ="https://img.shields.io/badge/notion-000000.svg?&style=flat-square&logo=notion&logoColor=white"/> 


## **✨ 기능 구현**
### 작업
#### 서보 모터와 라즈베리 파이(Pyhon)을 활용한 프로젝트
* 전체적인 모형의 도면 제작 후 아크릴판과 하드보드지를 이용하여 외형 제작
* 라즈베리파이에서 Python 코들르 활용하여 구현
* MG995 서보모터(360도 회전 가능)을 두 개를 사용해서 주축 부분과 카드 출력 부분을 제어
* 인원수를 따로 입력 받아 두 개의 모터 제어(GPIO핀과 PWM 제어)
* 세븐 포커 규칙을 활용하여 코드 작성 후 모터와 결합하여 구동 확인

### [세븐포커 규칙](Seven_Rule.md)

## **⏰ 일정**

|일정|내용|
|:---|:---|
|1일차|프로젝트 주제 선정 및 작품 외형 기본 구성 빌드|
|2일차|프로젝트 물품 선정 및 구매|
|3일차|프로젝트 개요 및 구성 정리 Notion 기본 틀 작성, Notion 관리 및 github관리|
|4일차|프로젝트 역할 분담 및 게임 룰 선정|
|5일차|하드웨어 제어 파트 및 외형 제작|
|6일차|상단,하단부 모터제어 및 하단부 외형 제작|
|7일차|세븐 포커 규칙 정리 및 해당 동작 모터제어, 상단부 외형 제작|
|8일차|하단부 외형과 모터 결합 및 테스트|


