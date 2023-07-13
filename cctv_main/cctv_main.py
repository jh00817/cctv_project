import sys
sys.path.append('C:\\Users\\Noel\\OneDrive - 고려대학교\\2023 KAsimov\\Python study\code\Object_detect-OpenCV')

import main
import record

def main_function() :
    # 초기 변수
    max_degree = 180
    min_degree = 0
    degree = 0

    MODE_DETECT : True


    # 상시 녹화
    record.record("stream",100)

    while MODE_DETECT == True : # 감지되면 
        
        count = 0
        
        while count < 4 :
            
            detect_data = main.function_detect()
            
            if detect_data == "left" :
                if max_degree < degree :
                    print("끝")
                # 왼쪽으로 모터 조정
                else :
                    print("왼쪽으로 조정중")
            elif detect_data == "right" :
                # 오른쪽으로 모터 조정
                if min_degree > degree :
                    print("끝")
                else :
                    print("오른쪽으로 조정중")

            if detect_data == "normal" :
                count = count + 1
            else :
                count = 0

if __name__ == "__main__" :
    main_function()
