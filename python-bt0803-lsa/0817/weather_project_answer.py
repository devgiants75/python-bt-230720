import csv

class WeatherDataManager:
    def __init__(self, filename):
        self.filename = filename  # 파일 이름을 인스턴스 변수로 저장
    
    def create_data(self, city_name, date, max_temp, min_temp, rainfall):
        # CSV 파일에 새로운 날씨 데이터를 추가하는 메서드
        with open(self.filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([city_name, date, max_temp, min_temp, rainfall])
            # 주어진 데이터를 CSV 파일에 한 행으로 추가
    
    def read_data(self):
        # CSV 파일의 모든 날씨 데이터를 출력하는 메서드
        with open(self.filename, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
                # 파일의 각 행을 출력
    
    def update_data(self, city_name, date, new_data):
        # 특정 도시와 날짜의 날씨 데이터를 수정하는 메서드
        data = self._load_data()  # 파일에서 데이터를 로드
        for row in data:
            if row[0] == city_name and row[1] == date:
                row[2:] = new_data  # 조건에 맞는 행의 데이터를 업데이트
        self._save_data(data)  # 수정된 데이터를 파일에 다시 저장
    
    def delete_data(self, city_name, date):
        # 특정 도시와 날짜의 날씨 데이터를 삭제하는 메서드
        data = self._load_data()  # 파일에서 데이터를 로드
        # 조건에 맞지 않는 행만 새로운 데이터 목록을 생성
        data = [row for row in data if not (row[0] == city_name and row[1] == date)]
        self._save_data(data)  # 수정된 데이터를 파일에 다시 저장
        
    def _load_data(self):
        # CSV 파일에서 날씨 데이터를 로드하는 내부 메서드
        with open(self.filename, mode='r') as file:
            reader = csv.reader(file)
            return [row for row in reader]  # 파일의 각 행을 리스트로 반환
    
    def _save_data(self, data):
        # 날씨 데이터를 CSV 파일에 저장하는 내부 메서드
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)  # 주어진 데이터를 파일에 쓰기

import matplotlib.pyplot as plt

class WeatherVisualization:
    @staticmethod
    def visualize(data):
        # 정적 메서드로, 날씨 데이터를 선 그래프로 시각화
        # data 파라미터는 날씨 정보가 담긴 2차원 리스트

        city_names = set(row[0] for row in data)
        # 데이터에서 유일한 도시 이름들을 추출하여 집합으로 저장
        
        for city in city_names:
            # 각 도시에 대한 데이터를 순회

            city_data = [row for row in data if row[0] == city]
            # 해당 도시의 날씨 데이터만 추출
            
            dates = [row[1] for row in city_data]
            # 해당 도시의 날씨 데이터에서 날짜 정보를 추출
            
            max_temps = [float(row[2]) for row in city_data]
            # 해당 도시의 날씨 데이터에서 최고 기온 정보를 추출하고, 숫자로 변환
            
            min_temps = [float(row[3]) for row in city_data]
            # 해당 도시의 날씨 데이터에서 최저 기온 정보를 추출하고, 숫자로 변환
            
            plt.plot(dates, max_temps, label=f'{city} Max Temp')
            # 해당 도시의 날짜와 최고 기온을 사용하여 선 그래프를 그립니다. 범례에는 도시 이름과 'Max Temp'가 표시
            
            plt.plot(dates, min_temps, label=f'{city} Min Temp')
            # 해당 도시의 날짜와 최저 기온을 사용하여 선 그래프를 그립니다. 범례에는 도시 이름과 'Min Temp'가 표시
        
        plt.xlabel('Date')
        # x축에 'Date' 라는 레이블을 추가
        
        plt.ylabel('Temperature')
        # y축에 'Temperature' 라는 레이블을 추가
        
        plt.legend()
        # 그래프에 범례를 추가
        
        plt.show()
        # 그래프를 화면에 표시

# 이 클래스는 WeatherVisualization이며, 도시별로 최고 및 최저 기온을 선 그래프로 시각화하는 기능을 제공

def main():
    filename = 'weather_data.csv' 
    # 날씨 데이터를 저장할 CSV 파일의 이름을 설정
    
    weather_manager = WeatherDataManager(filename)
    # WeatherDataManager 클래스의 인스턴스를 생성하고, 파일 이름을 매개변수로 전달
    
    while True:
        # 무한 루프를 통해 사용자로부터 계속해서 명령을 받기
        
        command = input('Enter command (create, read, update, delete, visualize, exit): ')
        # 사용자로부터 명령어를 입력받기
        
        if command == 'create':
            # 'create' 명령을 받으면, 새로운 날씨 데이터를 생성
            
            # 사용자로부터 필요한 정보를 입력받기
            city_name = input('Enter City Name: ')
            date = input('Enter Date (YYYY-MM-DD): ')
            max_temp = input('Enter Max Temperature: ')
            min_temp = input('Enter Min Temperature: ')
            rainfall = input('Enter Rainfall: ')
            
            # 입력받은 정보를 이용해 새로운 날씨 데이터를 CSV 파일에 저장
            weather_manager.create_data(city_name, date, max_temp, min_temp, rainfall)
            
        elif command == 'read':
            # 'read' 명령을 받으면, 저장된 날씨 데이터를 읽어와 화면에 출력
            weather_manager.read_data()
            
        elif command == 'update':
            # 'update' 명령을 받으면, 기존의 날씨 데이터를 수정
            
            # 수정할 데이터의 도시 이름과 날짜를 입력받기
            city_name = input('Enter City Name: ')
            date = input('Enter Date (YYYY-MM-DD): ')
            # 수정할 데이터를 입력받습니다. 쉼표로 구분된 문자열로 받아오기
            new_data = input('Enter New Data (Max Temp, Min Temp, Rainfall): ').split(',')
            
            # 입력받은 정보를 이용해 해당 날씨 데이터를 수정
            weather_manager.update_data(city_name, date, new_data)
            
        elif command == 'delete':
            # 'delete' 명령을 받으면, 날씨 데이터를 삭제
            
            # 삭제할 데이터의 도시 이름과 날짜를 입력받기
            city_name = input('Enter City Name: ')
            date = input('Enter Date (YYYY-MM-DD): ')
            
            # 입력받은 정보를 이용해 해당 날씨 데이터를 삭제
            weather_manager.delete_data(city_name, date)
            
        elif command == 'visualize':
            # 'visualize' 명령을 받으면, 날씨 데이터를 선 그래프로 시각화
            
            # 저장된 날씨 데이터를 불러오기
            data = weather_manager._load_data()
            
            # 불러온 날씨 데이터를 시각화
            WeatherVisualization.visualize(data)
            
        elif command == 'exit':
            # 'exit' 명령을 받으면, 프로그램을 종료
            break
            
        else:
            # 그 외의 명령어를 입력받으면, 오류 메시지를 출력하고 다시 명령을 입력
            print('Invalid command. Please try again.')

if __name__ == '__main__':
    # 이 스크립트를 직접 실행할 때, main() 함수를 호출하여 프로그램을 시작
    main()

# 사용자로부터 명령을 입력받아 해당 명령에 따라 날씨 데이터를 관리하는 프로그램
# WeatherDataManager 클래스를 이용해 데이터를 생성, 조회, 수정, 삭제하며, WeatherVisualization 클래스를 이용해 데이터를 시각화
