import Object_detect_OpenCV.main
import Object_detect_OpenCV.record

# 초기 변수

max_degree = 180
min_degree = 0

# 상시 녹화
Object_detect_OpenCV.record.record("stream",100)

while False : # 감지되면 
    mootr_data = Object_detect_OpenCV.main.function_detect()
    
    if moter_data == "left" :
        if max_degree < degree :
            print("끝")
        # 왼쪽으로 모터 조정
        else :
            print("왼쪽으로 조정중")
    elif motor_data == "right" :
        # 오른쪽으로 모터 조정
        if min_degree > degree :
            print("끝")
        else :
            print("오른쪽으로 조정중")