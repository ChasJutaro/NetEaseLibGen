Last Update: May.31 2020

# NetEaseLibGen - Contact: zhao.lu@mail.utoronto.ca OR zhaolu1t9@gmail.com
Generate a unified view of your local NetEase Cloud Music library

***English:***
This repo's python script shall merge all your NetEase local music library into one uniform library with a few steps.
The project is developed on OS X 10.15.2 Catalina using Python 3.7.

**Feature of the project:**

 - Automatically copy .mp3 and .flac file to a new directory
 - Automatically convert .ncm file to its original state and copy the converted file to the new directory
 - remove the artist name and the following " - " to format all songs with only songname + filetype
 
**Dependency**
 - ncmdump by anonymous5l : [repo of original ncmdump](https://github.com/anonymous5l/ncmdump)
 - Huge shoutout to anonymous5l who made the most important feature of this project possible

**Usage**

 - Put all your music files inside a directory called "music-test"
 - clone the repo so that the final structure shall look like: 
	 `$ ls`
	 `$ ... sortlib.py music-test`
 - By using `python3 sortlib.py` just lean back and cross your fingers :), and hopefully shortly you shall get all your songs in the "final-lib" directory

**Test Environment**

 - OS X ( **Tested** )
    

 - Windows 10 ( X )

 - Linux - Arch Linux based on the release version around Oct 2019. ( **Tested** )


**Possible Bugs**
 -  ~~The final library of my "test" library is missing 1 song. This will be fixed in the next commit.~~
 - ~~Bugs arising due to multiple songs performed by different artists. i.e, a song by the original, and 2 other cover versions.~~
 - cornercases of the above 2 categories that are not exposed with my library

**TODO list**

 - Test on Windows and Linux platform
 - Make sure all songs are converted/processed
 - generate library according to artist/album/genre/production year(if all are present in the file)

最后更新于：2019.1.13

***中文：***
该 python 脚本会自动将网易云音乐的所有文件移动到新目录中，同时自动转换其中格式为 ncm 的文件并将转换后的文件移动至新目录中，以求达到自动整理你的音乐库的目的。
该项目在 OS X 10.15.2 Catalina 上用 python 3.7 开发完成。

**功能**：

 - 自动将 mp3 与 flac文件拷贝至新目录中
 - 自动将 ncm 文件转换为原文件并将原文件拷贝至新目录中
 - 将表演者以及 “ - ” 删除以保证所有文件名为：歌名 + 扩展名

**依赖关系**？
 - ncmdump by anonymous5l : [repo of original ncmdump](https://github.com/anonymous5l/ncmdump)
 - 感谢 anonymous5l 使得实现该项目最重要的功能变为可能
 
 **使用方法**
- 将所有的音乐文件放入 "music-test" 中
 - 使文件夹结构达到如下效果: 
	 `$ ls`
	 `$ ... sortlib.py music-test`
 - 使用 `python3 sortlib.py` 运行程序，祝你好运 :) ，在没有bug的情况下你可以很快在 “final-lib” 看到你的最终音乐库

**测试平台**

 - OS X（已测试）
 - Windows 10（未测试）
 - Linux - arch linux 基于 2020 年 5 月的版本（已测试）

**可能存在的Bug**

 - ~~在使用我自己的曲库进行测试时，最终生成的曲库缺少了一首歌~~
 - ~~由于有多首同名的歌曲所导致的bug，例如当有原唱与2首翻唱歌曲时~~
 - 由于我的曲库的局限性所无法暴露的属于上述2类的特殊情况

**未来计划**

 - 于 Windows 平台上进行测试
 - 确保所有的歌曲都经过处理
 - 根据演唱者/专辑/流派/创作年份（ 在源文件提供所有信息的情况下）分类成曲库
