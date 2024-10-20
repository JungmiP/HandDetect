# 수화 알파벳 탐지 프로젝트
  OpenCV, Mediapipe을 활용하여 알파벳 수화 탐지 Lstm 모델을 학습시킨 후 웹 서비스로 구현한 프로젝트

## Configure
- hand_detect : 데이터 생성, Lstm 모델 학습
- lstm_rest_server : 이미지 데이터를 받아 이미지 판별 후 리턴하는 rest 서버
- spring_boot_lstm : 실시간 웹캠 이미지 전송하고 화면에 보여주기 위한 웹 서버

## 프로젝트 개요
![handdetectarchitect](https://github.com/user-attachments/assets/7e166820-cbd8-4eae-a84b-3229b1a2b427)

## 사용 기술 및 개발 환경 
- 사용 언어: Python, Java, javascript
- Framework: Flask, SpringBoot
- 영상인식 기술: OpenCV, Mediapipe
- AI: keras 

## 데이터 수집
- 웹 캠을 이용하여 한 파일당 600 frame 수집
- mediapipe의 손 landmark 위치를 구한 후 각 관절 간의 거리와 각도를 구하여 전처리
- numpy 2차원 배열 형태로 저장 -> .npy 파일

## 사용 모델
- LSTM
- J와 Z의 경우 알파벳을 그리는 모션을 취하기때문에 단순 이미지 정보로는 판별이 어려움
- 이전 시점의 정보를 학습에 반영하는 LSTM 사용
- 데이터를 5초 간격으로 잘라 학습하고 5초 간격의 데이터를 입력으로 사용
