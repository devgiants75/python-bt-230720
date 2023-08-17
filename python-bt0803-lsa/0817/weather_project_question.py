# 도시 날씨 관리 시스템

#! 1. WeatherDataManager 클래스를 작성
# create_data: 사용자로부터 도시 이름, 날짜, 최고 기온, 최저 기온, 강수량을 입력받아 CSV 파일에 저장하는 기능을 구현
# read_data: 저장된 CSV 파일의 모든 데이터를 출력하는 기능을 구현
# update_data: 특정 도시와 날짜의 날씨 정보를 수정하는 기능을 구현
# delete_data: 특정 도시와 날짜의 날씨 정보를 삭제하는 기능을 구현

#! 2. WeatherVisualization 클래스를 작성
# matplotlib 라이브러리를 사용해 도시별 최고 및 최저 기온을 선 그래프로 시각화하는 visualize 메서드를 포함

#! 3. main 함수를 작성
#  사용자로부터 명령을 입력받아 해당 명령에 맞는 기능을 실행하도록 구현

# 데이터 생성 (create)
# 데이터 조회 (read)
# 데이터 수정 (update)
# 데이터 삭제 (delete)
# 데이터 시각화 (visualize)
# 프로그램 종료 (exit)

#! 4. validate_date 함수를 작성
# 사용자로부터 입력받은 날짜가 유효한 형식(YYYY-MM-DD)인지 검사하는 함수
# 유효한 날짜 형식일 경우 True를 반환하고, 그렇지 않을 경우 False를 반환

#! 5. filter_data 메서드를 WeatherDataManager 클래스에 추가
# 사용자가 특정 도시의 특정 날짜 범위의 데이터만 조회

#! 6. 예외 처리를 구현
# 파일 읽기/쓰기 오류, 데이터 형식 오류 등 다양한 예외 상황 코드 작성