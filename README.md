# AzurLanePaintingExtract-v1.0
a easy tool to transform AzurLane's painting

### 工具：
---------------------
| 工具 | 介绍
|:--:|:--|
| [asset studio](https://github.com/Perfare/AssetStudio) | 居家使用的解包工具 |
| [UABE](https://github.com/DerPopo/UABE) | 可以获取Path_ID |
------------------
### 功能介绍
------------------
|功能|适用范围|效果|需求|
|:--:|:-----:|:---:|:--:|
| 基本立绘处理功能 | 针对[碧蓝航线](https://game.bilibili.com/blhx/)角色立绘，是本脚本的核心功能 | 将破碎的原始解包立绘恢复原样 | 至少一张Texure2D（.png），至少一个Mesh(.obj) |
| 立绘附加表情功能 | 针对[碧蓝航线](https://game.bilibili.com/blhx/)角色差分表情，和部分立绘没有头而开发的功能 | 能为立绘附加面部表情（正在考虑用Path_ID进行匹配） | 可以为一个角色单个或组合进行附加表情 | 符合基本立绘处理功能的要求即可 |
| Q版（[Spine](http://zh.esotericsoftware.com/)）小人切割 | 适用所有的atlas切割（[Spine](http://zh.esotericsoftware.com/)） | 将单张的贴图切割成图片组 | 至少一张Texuture2D（.png）和一个Atlas（.atlas|.atlas.txt）|
| Sprite切割 | 针对[Unity](http://www.unity3d.com/)的Sprite的切割功能，理论上适用所有Unity Sprite对象 | 参考被切割图片PathID和Sprite的Dump文件，切割原始图片，获得图片组 | 至少一个Texture2D（.png）,一个Dump(.txt) |
------------
### 历次更新介绍
#### 1.X版本
* [【碧蓝航线】立绘辅助处理工具-1.4](https://www.bilibili.com/read/cv5048786)
* [【碧蓝航线】立绘处理辅助工具v1.2更新](https://www.bilibili.com/read/cv3983757)
* [【碧蓝航线】立绘导出工具-1.0重制版](https://www.bilibili.com/read/cv2801922)
--------------------------
#### 0.X版本
* [【碧蓝航线】AzurLane-PaintingExtract v 0.7.0更新内容](https://www.bilibili.com/read/cv1786736)
* [【碧蓝航线】立绘，spine小人，Live2D](https://www.bilibili.com/read/cv1566510)
* [【碧蓝航线】立绘还原程序 v-0.6.0更新](https://www.bilibili.com/read/preview/1439259)
* [碧蓝航线立绘还原更新-v-0.2.0](https://www.bilibili.com/read/cv1316278)
* [碧蓝航线立绘还原程序更新](https://www.bilibili.com/read/cv1127720)
* [碧蓝航线立绘还原程序（GUI版本）更新](https://www.bilibili.com/read/cv1019910)
* [碧蓝航线立绘还原程序（GUI版本）](https://www.bilibili.com/read/cv1013553)
* [碧蓝航线立绘还原更新（批处理）](https://www.bilibili.com/read/cv941333)
* [碧蓝航线立绘还原程序更新（1）](https://www.bilibili.com/read/cv936784)
* [碧蓝航线立绘还原程序更新](https://www.bilibili.com/read/cv933308)
* [AzurLanePaintingRestore更新](https://www.bilibili.com/read/cv911094)
* [ AzurLinePaintingRestore更新](https://www.bilibili.com/read/cv893994)
* [【碧蓝航线】立绘还原程序更新](https://www.bilibili.com/read/cv886956)
---------------------
#### 教程
* [【碧蓝航线】如何手动挖出舰娘的立绘](https://www.bilibili.com/read/cv1330829)
* [ 如何挖出碧蓝航线的立绘教程（简单版）](https://www.bilibili.com/read/cv894737)
* [ 如何手动挖出碧蓝航线的立绘](https://www.bilibili.com/read/cv565639)
