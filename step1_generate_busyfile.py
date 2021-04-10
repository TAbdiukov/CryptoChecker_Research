
fp = open("busy.dat", 'wb+')
page_len = 1024*1024*8 # 8 MB
page = b'\x00'*page_len
cnt = 600/8
cnt = int(cnt)
for i in range(cnt):
	fp.write(page)
fp.close