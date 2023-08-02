### 파이썬 파일 입출력 ###

# 1. 파일 복사
# 원본 파일(source)의 복사본 파일(copy)을 만드는 것

# 2. 파일 복사의 절차
# 2-1. 원본 파일 열기
# 2-2. 복사본 파일 생성
# 2-3. 원본 파일의 내용 읽기 & 복사본에 쓰기
# : 원본 파일에서 한 번에 읽어들이는 데이터 크기를 1KB(1024Byte)로 설정해 복사 프로그램을 구현
# 2-4. 파일 닫기(with문 사용 시 생략 가능)

video_size = 1024 # 1024Byte로 1KB를 의미

with open('pexels_videos_1093662 (1080p).mp4', 'rb') as source:
    with open('copy_video.mp4', 'wb') as copy:
        while True:
            # read(파일의 용량을 지정)
            buffer = source.read(video_size)
            if not buffer:
                break
            copy.write(buffer)
print('copy_video.mp4 파일이 복사되었습니다.')