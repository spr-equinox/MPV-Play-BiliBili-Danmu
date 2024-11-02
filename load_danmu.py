from urllib import request
import sys, subprocess, ssl, zlib

def main():
    if len(sys.argv) != 3:
        print('参数错误')
        exit(-1)
    cid = int(sys.argv[1])
    path = sys.argv[2]
    response = request.urlopen(request.Request(
        url = f'https://comment.bilibili.com/{cid}.xml',
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36 Edg/124.0.0.0'
        }
    ))
    data = str(zlib.decompress(response.read(), -zlib.MAX_WBITS), "utf-8")
    response.close()
    open(f'{path}/danmu.xml', 'w', encoding='utf-8').write(str(data))
    subprocess.run([f'{path}/DanmakuFactory','-o',f'"{path}/danmu.ass"','-i','xml',f'"{path}/danmu.xml"','--ignore-warnings'])
    # DanmakuFactory -o “out.ass” -i xml “in.txt”
if __name__ == "__main__":
    main()