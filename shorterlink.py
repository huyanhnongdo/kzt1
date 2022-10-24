import json,requests,time
from time import strftime

ngay=int(strftime('%d'))
key= "huykazuto_"+str(ngay*192892982+19282)

key_vip="huykazutosuper"
url=f'https://tranthuongtv.name.vn/key.php?key={key}'
# mình hd code thì nó khá lâu nên mình đã code sẵn cho các bạn
# link code mình để dưới mô tả
#thay token link1s

token_link1s="1580058dee70fe85a4daccb984fea8f364151d26"
post_url=requests.get(f'https://octolink.io/api?api={token_link1s}&url={url}').json()
if post_url['status']=="error":
	print(post_url['message'])
	quit()
else:
	link_key=post_url['shortenedUrl']

nhap_key=input(f'''\033[1;32m Link lấy key: \033[1;33m{link_key}
\033[1;32m Nhạp key ngày hôm nay: \033[1;33m''')
if nhap_key==key or nhap_key == key_vip:
	print('\033[1;32m Key chính xác')
else:
	print('\033[1;31m Key không hợp lệ')
	quit()
