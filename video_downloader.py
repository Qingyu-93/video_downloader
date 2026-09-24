import os
import sys
import subprocess

def install_yt_dlp():
    try:
        import yt_dlp  # noqa: F401
    except ImportError:
        print("未检测到 yt-dlp，正在安装……")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-U", "yt-dlp"])

def download_video(url, output_dir="downloads"):
    import yt_dlp

    os.makedirs(output_dir, exist_ok=True)

    options = {
        # 优先下载最高画质的视频+音频并自动合并
        "format": "bv*+ba/b",
        "merge_output_format": "mp4",
        "outtmpl": os.path.join(output_dir, "%(title)s.%(ext)s"),
        "noplaylist": True,
        "continuedl": True,
        "retries": 5,
        "fragment_retries": 5,
        "progress": True,
    }

    print(f"\n开始下载：{url}\n")
    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            info = ydl.extract_info(url, download=True)
            print("\n下载完成！")
            print("标题：", info.get("title", "未知"))
            print("保存目录：", os.path.abspath(output_dir))
    except Exception as e:
        print("\n下载失败：")
        print(e)
        print("\n提示：")
        print("1. 检查网址是否正确")
        print("2. 某些网站需要登录、Cookie 或特殊授权")
        print("3. 仅下载你有权保存或网站允许下载的内容")

if __name__ == "__main__":
    install_yt_dlp()

    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("请输入视频网址：").strip()

    if not url:
        print("没有输入网址，程序结束。")
        input("按回车退出……")
        sys.exit(1)

    download_video(url)
    input("\n按回车退出……")
