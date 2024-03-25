from urllib import request
import sys, subprocess, ssl, zlib

def main():
    if len(sys.argv) != 3:
        print('参数错误')
        exit(-1)
    cid = int(sys.argv[1])
    path = sys.argv[2]
    response = request.urlopen(f'https://comment.bilibili.com/{cid}.xml', context=ssl.SSLContext(ssl.PROTOCOL_TLS))
    data = str(zlib.decompress(response.read(), -zlib.MAX_WBITS), "utf-8")
    response.close()
    open(f'{path}/danmu.xml', 'w', encoding='utf-8').write(str(data))
    subprocess.run([f'{path}/DanmakuFactory','-o',f'"{path}/danmu.ass"','-i','xml',f'"{path}/danmu.xml"','--ignore-warnings'])
    # DanmakuFactory -o “out.ass” -i xml “in.txt”
if __name__ == "__main__":
    main()