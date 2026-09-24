# 视频下载器

这是一个基于 yt-dlp 的简单 Python 视频下载工具。

## 1. 安装 Python

建议使用 Python 3.10 或更高版本。

## 2. 安装依赖

在本文件夹打开 PowerShell：

```powershell
py -m pip install -r requirements.txt
```

## 3. 运行

```powershell
py video_downloader.py
```

然后输入视频网站的视频网址。

也可以直接：

```powershell
py video_downloader.py "视频网址"
```

下载的视频会保存到当前文件夹下的 `downloads` 文件夹。

## 4. 关于画质

程序会尝试下载网站提供的较高质量视频和音频，并自动合并为 MP4。

部分网站需要 FFmpeg 才能完成音视频合并。如果出现合并相关错误，请安装 FFmpeg 并把它加入 Windows PATH。

## 5. 使用说明

请只下载你有权保存、复制或离线观看的内容，并遵守目标网站的服务条款和版权规定。

某些网站可能要求登录、Cookie、DRM 或其他授权方式；本程序不会绕过 DRM 或访问控制。
