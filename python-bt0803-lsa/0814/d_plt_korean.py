### matplotlib 라이브러리 한글 처리 ###

# font-manager & rc 을 이용하여 사용하고자 하는
# 한글 폰트를 등록
from matplotlib import font_manager, rc
import matplotlib.pyplot as plt
import matplotlib

# 폰트 경로 직접 지정
font_path = 'c:\Windows\Fonts\HMKMRHD.TTF'

font_name = font_manager.FontProperties(fname=font_path).get_name()
matplotlib.rc('font', family=font_name)
# plt('font', family=font_name)

plt.plot(['봄', '여름', '가을', '겨울'], [20, 30, 15, 10])
plt.title('한글 깨짐 방지')

plt.show()
