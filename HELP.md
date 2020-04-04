
# 【碧蓝航线】立绘辅助处理工具（AZPT）教程

## Author: 凊弦凝绝Official

------------

### 需求程序

* 本教程需要除了AZPT外的Unity解包工具(二选一，都用也可以)：

   1. [UABE(Unity Assets Bundle Extractor)](https://github.com/DerPopo/UABE)

   2. [Assets Studio(原Unity Studio)](https://github.com/Perfare/AssetStudio)

* 工具本体：[碧蓝航线立绘辅助处理工具(AzurLanePaintingTool)](https://github.com/azurlane-doujin/AzurLanePaintingExtract-v1.0)

### 工具下载

![image](https://i0.hdslb.com/bfs/bigfun/febdbde6ba1a03d918fc28e43452da9f33d42fc0.png@760w_1o_1g)

<font color = ff000>下载对应工具请到release页面下载（图中箭头指向），不要使用“clone or download”这个是下载源代码的。</font>

ALPT[下载页面](https://ci.appveyor.com/project/Perfare/assetstudio/branch/master/artifacts)

Assets Studio[下载界面](https://ci.appveyor.com/project/Perfare/assetstudio/branch/master/artifacts)


------------

### 素材准备（只使用Unity解包工具即可，这部分推荐Assets Studio）

#### 资源位置

* 碧蓝航线的游戏资源，分为2个部分。其中，一部分位于游戏的安装包中；另一部分位于热更新游戏资源包中

#### 如何获取

##### 对于位于安装包中的资源文件

1. 可以通过碧蓝航线的官网直接下载安装包（*.apk）随后使用压缩软件（如果电脑自带的压缩软件没法解压，可以试着将扩展名改成*.zip）解压文件，获取解压文件夹。

2. 在解压后获得的文件夹内，找到“assets”文件夹，进入；再找到“AssetBundles”文件夹，这个文件夹就是碧蓝航线的游戏内素材所在的文件夹，可以将这个文件夹拷贝到别处待用。

##### 对于热更游戏资源包，以下操作仅支持安卓手机或安卓模拟器。

> <font color=#ff0000 >注意，碧蓝航线热更资源包位于手机内部储存，而不是在外部储存（SD卡）</font>

1. 在手机资源管理器找到以下路径”/storage/emulated/0/Android/data/com.biliblili.azurlane/files/AssetBundles“,可以将该文件夹整个或部分打包，通过如QQ我的设备等方式发送到电脑备用。

#### 资源分布

---

* activity_painting 活动立绘
* activitybanner 活动横幅
* aircrafticon 飞机图标
* battlescore 战斗得分
* bg 背景
* box 框
* boxprefab 框
* chapter 章节地图纹理图
* > pic 图
* char Q版小人结构图
* chargeicon 氪金图标
* chargo 大飞机图标
* clouds 云贴图
* clutter 活动宣传图
* commanderhrz 指挥喵放技能横图
* commandericon 指挥喵头像
* commanderrarity 指挥喵稀有度
* commanderskillicon 指挥喵技能图标
* commandertalenticon 指挥喵天赋
* commonbg 常用背景
* cue 语音
* dailylevelicon 每日副本图标
* dormbase 宿舍基地
* dutyicon 职位图标
* effect 效果
* > img 效果图
* >mat_anim
* emblem 军衔
* emoji 表情
* enemies 敌舰
* equips 装备
* event type 事件结果
* extra 附加
* font 字体图片
* furniture 家具
* furnitureicon 家具图标
* helpbg 帮助
* herohrzicon 放技能横图
* item 外观装备
* levelmap 地图
* live2d live2d
* loadingbg 过场图
* lotterybg 奖池背景
* map 贴图
* mapres 贴图资源
* >sea_single 海
* >sky_single 天
* memoryicon 回忆 剧情
* numbericon 数字图标
* painting 立绘
* paintingface 表情差分
* prints 阵营
* props 道具
* puzzla 拼图
* qicon Q版头像
* sfurniture 家具贴图
* shipdesignicon 科研图标
* shipmodels 小人
* shiprarity 舰船稀有度
* shipyardicon 船坞图标
* skillicon 技能图标
* squareicon 方形图标
* strategyicon 阵型图标
* ui 用户界面

---

* by Crayonkun

> <font color = ffoxe0>（如果只要应用于本工具，只需要保留“char”,"painting","paintingface"）</font>

---

#### 开始解包

* 运行AssetsStudio，效果如图：

![image](https://i0.hdslb.com/bfs/bigfun/902cc4c7245d984a7e584008d5d114ff1f1c7f42.png@760w_1o_1g)

##### 【导入】

* 使用“file”->"load file"(加载文件)/"load folder"（加载文件夹）进行文件加载；导入painting中文件可能会发现，文件夹中有同一舰娘立绘的2个文件（图中以塔什干原始皮肤为例）

![inage](https://i0.hdslb.com/bfs/bigfun/41ac888697026754cc8fe9b5820b31e305480600.png@760w_1o_1g)
> 在实际操作中，有的立绘的原始立绘和还原参数文件会分布在这2个文件中，所以，通常情况下是同时导入

* 导入完成后，点击“Asset List”显示文件列表，效果如图：

![mage](https://i0.hdslb.com/bfs/bigfun/5b5d577e615c2685d58cc6b834f203c0d94028af.png@760w_1o_1g)

* 图中选中的元素即为还原立绘的需求文件

![image](https://i0.hdslb.com/bfs/bigfun/6ad4039d7b83ca641610a317cbb945e9d9f4b604.png@760w_1o_1g)

##### 【导出】

* 点击“Export”->"Select assets"，选择导出文件夹后，等待导出完成，在未改变默认设置，导出完成后会自动打开导出目标文件夹，如图

![image](https://i0.hdslb.com/bfs/bigfun/b69228fd15ebdde1d273a59b9c630e26c6bb9d29.png@760w_1o_1g)

> 导出目录中出现了2个文件夹，Texture2D中为贴图（.png）；Mesh中为切割信息文件（.obj）。资源准备完成！

----

### 工具介绍

> <font color=ff234d>如果想直接上手使用，可跳过该部分</font>

* 解压下载的7Z文件，找到其中的exe文件，双击运行（请先解压！）

![image](https://i0.hdslb.com/bfs/bigfun/ca2dc12cbfeb0afde48b81e31bba24dd595427b6.png@760w_1o_1g)

* 界面如图：

![image](https://i0.hdslb.com/bfs/bigfun/c987ec964dabb177ddb1f1e7ecf94df881660c44.png@760w_1o_1g)
##### 区域介绍
| 标号 | 信息 |
|:----:|:---|
| ① | 为素材导入、数据显示区。在该区域内，可以进行素材拖动导入（支持含有多级文件夹和文件文件夹混合导入），和导入完成后的元素显示|
| ② | 为图像预览区。在该区域内，可以显示导入素材的原始文件预览和还原效果预览。 |
 | ③ | 为进度条。在导入，导出时显示导入和导出进度 |
 | ④ | 为信息框。会显示导入元素的数量，预览类型，导出状态等信息 |

##### 其他部分：
| 标号 | 信息 |
|:----:|:---|
| ① |①区上方左侧为筛选器，会筛选并显示符合条件的对象 |
| ② |①区上方右侧为搜索框，输入字符会马上进行搜索，并显搜索结果 |
| ③ |“导出”按键。进行导出点击会弹出导出类型窗口 |
| ④ |“选择对应文件”按键。用于给对象修改用于还原的Texture2D文件和Mesh文件 |
| ⑤ |“设置”按键。进入设置界面 |

>为了显示完整功能，我先将素材导入
 
![image](https://i0.hdslb.com/bfs/bigfun/8e1df4b50404e924183318abbb8eb46061a48be4.png@760w_1o_1g) 

* 如图，导入完成。

---

> 我将塔什干元素内的信息完全展开，如图

![image](https://i0.hdslb.com/bfs/bigfun/6cc592f06132fd9f362b7bffdf26443e0e115e1f.png@760w_1o_1g)

>从上至下，进行编号

| 标号 | 名称 | 功能介绍 |
|:----:|:---|:---|
| ① | 元素根标签 | 点击将会进行还原预览，如不可预览，就显示原始文件 |
| ② | 元素本地化名称 | 如果该标签的字体颜色为粉红色（图中），表面该元素为可还原对象 |
| ③ | 元素索引名称 | 即导入元素的文件名 |
| ④ | 当前使用的Texture2D文件路径（优先级：Texture2D中文件>Sprite中文件>含有 #\d+同名文件标识戳文件） | 点击可进行元素文件预览 |
| ⑤⑥⑦ | 可供选择的Texture2D | 实际使用时可能会有更长的列表，选中其中元素后，可进行元素文件预览（如果可以预览），还可以点击“选择对应文件”将当前选中的文件设置为当前使用的Texture2D。如果修改为“Empty”则会禁用Texture2D(将会使本元素变为“不可还原”) |
| ⑧ | 当前使用的Mesh文件路径（优先级：Mesh中文件>含有 #\d+同名文件标识戳文件） | 无 |
| ⑨⑩⑾ | 可供选择的Mesh | 实际使用时可能会有更长的列表，还可以点击“选择对应文件”将当前选中的文件设置为当前使用的Mesh。如果修改为“Empty”则会禁用Mesh(将会使本元素变为“不可还原”) |
| ⑿~⒆ | 为附加功能区 | 这里不做重点介绍 |

---

* 点击“导出”，弹出导出窗口，如图

![image](https://i0.hdslb.com/bfs/bigfun/7790d67205998f5e74b62246f066e983c82c7340.png@760w_1o_1g)

###### 导出类型：

| 标号 | 名称 | 功能介绍 |
|:----:|:---|:---|
| ① | “导出全部可还原” | 将会将所有的可还原的导入元素全部导出到目标文件夹（至少有一个可还原对象时可用） |
| ② | “拷贝全部不可还原” | 将会将不可还原的对象直接拷贝到目标文件夹（至少有一个不可还原对象可用） |
| ③ | “导出选择项” | 将会把当前选中的元素（选择每个元素内的子元素也可）导出到指定路径 |
| ④ | “导出当前列表项” | 将当前列表中元素导出到目标文件夹（在使用了搜索功能或筛选器功能后可用） |

---

* 点击“设置”，打开设置界面，如图

![image](https://i0.hdslb.com/bfs/bigfun/cbc556ba89b3802b00029811c987f25f264d7814.png@760w_1o_1g)

> 从上到下，从左到右，依次编号

| 标号 | 名称 | 功能介绍 |
|:----:|:---|:---|
| ① | “使用中文名作为导出文件名（如果可用）” | 勾选后，将会以立绘的本地化名称作为导出的文件名（使用“导出选择项”不受影响） |
| ② | “在导出目标目录下新建导出文件夹” | 勾选后，将会在导出目标文件夹内新建“碧蓝航线-导出”文件夹，再将导出文件放在上述文件夹中 |
| ③ | “完成后打开目标文件夹” | 该功能已弃用，请勿勾选 |
| ④ | “跳过目标目录中已经存在同名文件” | 勾选后，将会跳过目标文件夹内已有的文件（不勾选将会覆盖） |
| ⑤ | “导入时清空原有文件” | 勾选后，每次导入会清空原有列表，不勾选，导入效果为附加 |
| ⑥ | “完成任务后退出” | 当完成导出任务后，会自动退出 |
| ⑦ | “导出同时拷贝不可还原” | 相当于导出时同时选择了”导出全部可还原“和”拷贝全部不可还原“ |
| ⑧ | “导入文件筛选” | 与主界面筛选器类似，但是是在导入的时候过滤不符合条件的文件 |
| ⑨ | “导出文件分类” | 将会按选择的方式，将导出的文件按“类型”或按“舰娘”进行分类 |
| ⑩ | “更新本地化资源”，“编辑本地化资源” | 用于在线更新和手动编辑、添加本地化资源 |

---

* 点击“更新本地化资源”，进入“更新本地化资源界面”，如图

![image](https://i0.hdslb.com/bfs/bigfun/596c7eb238117f2fd5b3c8fdba89233d9da87fd5.png@760w_1o_1g)

①区域是选择区，使用上部的“+”和“-”可以添加和删除本地化资源源；双击中部的本地化资源源，会进行本地化资源加载（可能会造成卡顿），加载完成后，在②中会显示结果，也可以选择直接使用“加载文件”选择目标json文件

②是本地化加载结果，可以展开，查看具体信息

③是更新应用类型。“应用-全部”将会使用新的本地化资源文件直接覆盖原有文件；“应用-新增”将只把新增的资源添加到原有本地化文件中；“应用-覆盖”将只把加载的资源中与原始本地化资源不同的部分使用加载的资源替换

点击“编辑本地化资源”，进入“编辑本地化资源”界面，如图

![image](https://i0.hdslb.com/bfs/bigfun/883ebde1f5bf19b09b7c1e4fed128ee5f5e1c262.png@760w_1o_1g)

| 标号 | 信息 |
|:----:|:---|
| ① | 是已有的本地化资源列表，单击选中可以将选中的本地化内容添加到②中，双击选中会以弹窗形式显示选中的本地化资源 |
| ② | 可以编辑键(导入元素的索引名称)、值（导入元素的本地化名称），键可以存在于已有的本地化资源列表中，也可以是新的，值可以与本地化资源列表中值相同（但是不推荐这么做） |
| “清空” | 会将当前“键”与“值”中对应的内容清空 |
| “添加“ | 会将当前”键“与”值“添加到已有的本地化资源中，如果键已经存在，将会弹窗进行询问 |
| ”+“ | 功能同”更新本地化资源“中的”加载文件“，不过效果是直接应用全部 |

#### 介绍完成！

---

### 附加功能区介绍
> 敬请期待

---

### 工具使用

1. 【导入】选择使用Assets Studio导出的文件或文件夹，拖动到图中红框中。（不用担心是否有其他干扰文件，本工具含有完善的入口检测，会自动过滤不符合条件的文件的，是的，你甚至可以把整个磁盘的文件全部拖动进去，但是可能会卡很久）

![image](https://i0.hdslb.com/bfs/bigfun/f0ac35077a2db8ef7b515683284d437319d98028.png@760w_1o_1g)

2. 等导入完成后，可以先随便点击几个元素，进行预览。

![image](https://i0.hdslb.com/bfs/bigfun/8d1aae843fdf6be5d848f13c3aec08dc81f85fd7.png@760w_1o_1g)

3. 点击“导出”->“导出全部可还原”，选择导出文件夹后，等待完成

![image](https://i0.hdslb.com/bfs/bigfun/c29ef1c6bda34f726baa415187acc5c53c748ec6.png@760w_1o_1g)

4.等待完成

> 就可以在导出目录下看到导出的立绘了！

![image](https://i0.hdslb.com/bfs/bigfun/c6d1c042a3786f0fdc5a82a26d383d6943db3db3.png@760w_1o_1g)



