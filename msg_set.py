# =====================================
# Taekyung Kim 2018
from kakaoplusfriend import MessageBox,Pic,PicButton,MessageButton,Message
# == Message Tree ==================================

all_msgs=[]
msg_1_1=Message("몇 층인가요?","5층입니다.")
msg_1_2=Message("미래혁신관?","수원대 대운동장 주변에 있는 검은색의 큰 건물입니다.",Ext=MessageButton("지도","http://naver.me/xm5y7SvY"))
msg_1_3=Message("수원대?","화성에 위치한 4년제 대학입니다.",Ext=MessageButton("홈페이지","http://www.suwon.ac.kr"))
msg_1_4=Message("학생에게 좋은 점?","여러분! 미래혁신관 5층에 학생들이 자유롭게 토론할 수 있는 공간이 많이 마련되어 있습니다. 특히 충전이 가능한 장소가 여럿 있으니 반드시 참고하시어 많은 이용바랍니다.")
## 2
msg_2_1=Message("데이터 과학이란?","빅데이터를 분석하여 비즈니스 가치를 발견하는 방법과 이론을 연구하는 학문입니다.",Ext=MessageButton("알아보기","http://www.bloter.net/archives/244855"))
msg_2_2=Message("이를 위해 갖추고 있는 것은?","DS랩, ML랩, 그리고 Content Creation Studio입니다.",Ext=MessageButton("알아보기","http://wow.suwon.ac.kr/wow/dsml/"))
msg_2_3=Message("DSML의 자랑은?","IBM S822LC Minsky!",Ext=PicButton("http://www.datacenterdynamics.com/pictures/280xany/6/5/9/17659_IBM-2.png","SuperDSML","http://superdsml.suwon.ac.kr"))
## 3
msg_3_1=Message("연락처는 뭐죠?","2017년부터 지금까지 경영학부 김태경 교수가 센터장을 맡고 있습니다. 연락처는 kimtk@suwon.ac.kr입니다. 궁금하신 점은 언제든지 상담 바랍니다.")
msg_3_2=Message("사무실은 어떻게 찾아가죠?","미래혁신관 5층 서편, 창업지원단 사무실에 있습니다. 미리 1:1 채팅 등으로 약속을 잡고 찾아오시면 편리합니다.")
## 4
msg_4_1=Message("2018년 사업에 대해?","4월 중순 Jupyter Notebook 워크샵을 실시합니다. 오는 6월 초에 AI Day!를 개최하여 DS&ML을 응원하는 인공지능 개발사들과 수원대 교수, 학생, 직원 간의 네트워크를 강화하는 행사가 있습니다. 2018년 하반기에는 Cintiq Day!와 딥러닝 워크샵 등이 예정되어 있고 파이썬 데이터 전문가 비교과도 개설될 예정입니다. 많은 응원 부탁드립니다.")
msg_4_2=Message("2018년의 목표는?","DS&ML센터는 2017년 한 해 동안 시스템을 설치하고 학내 네트워크 강화에 힘을 썼습니다. 이를 바탕으로 2018년은 학생과 교수 및 직원과의 스킨십을 강화시키도록 노력하겠습니다. 수원대 내에 4차 산업에 관한 관심을 높이며 각종 인공지능 관련 사업과 교육 콘텐츠를 개발하는데 힘쓸 것입니다. 2018년의 목표는 200명 이상의 학생들이 DS&ML의 친구가 되고 20명 이상의 교수님들을 상임 운영위원으로 참여하시도록 돕는 일입니다.")
msg_4_3=Message("DS&ML? 창업?","DS&ML센터는 학내 창업 팀 중 고등콘텐츠를 개발하거나 인공지능 알고리즘을 활용한 서비스를 개발하고자 할 때 필요한 장비를 대여하고 멘토링을 실시하는 등의 도움을 드립니다. 창업지원단과 특별히 연대하여 수원대학생의 꿈과 비전을 밀어들이겠습니다.")
## 5
msg_5_1=Message("C2S 체크인/아웃","링크를 누르세요.",Ext=MessageButton("Form","https://goo.gl/forms/akwagp6ilRzWgAp52"))
msg_5_2=Message("ML 랩 사용허가","링크를 누르세요.",Ext=MessageButton("Form","https://goo.gl/forms/1Fr66NGXvxDzGMhn2"))
## main
msg_1=Message("센터는 어디에 있나요?","수원대학교 미래혁신관에 있습니다. 미래혁신관은 수원대 대운동장을 바라보며 솟아 있는 지상 8층의 첨단 건물입니다. 수원대에서 가장 큰 건물이니 쉽게 알아볼 수 있습니다. *^.^*",toMessages=[msg_1_1,msg_1_2,msg_1_3])
msg_2=Message("무엇을 하는 곳인가요?","DS&ML 센터는 Data Science & Machine Learning 센터입니다. 이곳은 데이터 과학 및  디지털 콘텐츠 관련 연구, 교육, 창업을 지원을 합니다. 각종 연구와 강의 그리고 산학협력 및 창업지도 등이 다양하게 이루어지는 공간입니다.",toMessages=[msg_2_1,msg_2_2,msg_2_3])
msg_3=Message("누가 일하시나요?","DS&ML은 수원대 데이터 과학부 교수님들과 경영학부, 경제학부 교수님들, IT대학의 컴퓨터 관련 교수님들을 비롯하여 창업지원단 소속의 여러 교수님들께서 함께 하십니다.",toMessages=[msg_3_1,msg_3_2])
msg_4=Message("어떤 성과가 있나요?","DS&ML센터는 데이터 과학에 대한 학내 구성원들의\
     관심을 높이기 위해 노력합니다. 또한 고성능의 컴퓨팅 인프라를 제공하여 교육과 연구에 딥러닝이\
      적극 활용되도록 지원하고 있습니다. 또한 산학협력 과제를 통해 4차산업 시대의 수원대가 적극 기여하도록 합니다.\
      2017년부터 지금까지 DS&ML센터는 총 1억 4천만원의 연구프로젝트를 수주하였고 2018년에 누계\
      2억 5천만원을 목표로 노력하고 있습니다. 아울러 비즈니스 코딩 능력을 향상시켜 보다\
      많은 사람들이 데이터 과학의 혜택을 누릴 수 있도록 사회적 책무를 다하기 위한 사업을 추진 중에 있습니다.",toMessages=[msg_4_1,msg_4_2,msg_4_3])
msg_5=Message("DSML-양식 보기","원하는 양식을 고르십시오.",toMessages=[msg_5_1,msg_5_2])
#home
msg_home=Message("HOME","보다 자세한 점이 궁금하시면 1:1 채팅으로 물어봐 주시면 곧 연락드리겠습니다. 감사합니다. DSML 센터 일동 올림.",toMessages=[msg_1,msg_2,msg_3,msg_4,msg_5]) #HOME
#hook
# level 2
msg_1_1.hook([msg_1,msg_home])
msg_1_2.hook([msg_1,msg_home])
msg_1_3.hook([msg_1,msg_home])
msg_1_4.hook([msg_1,msg_home])
msg_2_1.hook([msg_2,msg_home])
msg_2_2.hook([msg_2,msg_home])
msg_2_3.hook([msg_2,msg_home])
msg_3_1.hook([msg_3,msg_home])
msg_3_2.hook([msg_3,msg_home])
msg_4_1.hook([msg_4,msg_home])
msg_4_2.hook([msg_4,msg_home])
msg_4_3.hook([msg_4,msg_home])
msg_5_1.hook([msg_5,msg_home])
msg_5_2.hook([msg_5,msg_home])
#level 1
msg_1.hook([msg_home])
msg_2.hook([msg_home])
msg_3.hook([msg_home])
msg_4.hook([msg_home])
msg_5.hook([msg_home])
#register
all_msgs.append(msg_home)
all_msgs.append(msg_1)
all_msgs.append(msg_1_1)
all_msgs.append(msg_1_2)
all_msgs.append(msg_1_3)
all_msgs.append(msg_1_4)
all_msgs.append(msg_2)
all_msgs.append(msg_2_1)
all_msgs.append(msg_2_2)
all_msgs.append(msg_2_3)
all_msgs.append(msg_3)
all_msgs.append(msg_3_1)
all_msgs.append(msg_3_2)
all_msgs.append(msg_4)
all_msgs.append(msg_4_1)
all_msgs.append(msg_4_2)
all_msgs.append(msg_4_3)
all_msgs.append(msg_5)
all_msgs.append(msg_5_1)
all_msgs.append(msg_5_2)