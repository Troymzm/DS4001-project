### 实验介绍

本实验为深度学习入门与生成模型入门，以MNIST数据集和VAE为核心，目标实现通过深度学习网络来完成VAE的实现与条件生成的任务。整体分为三部分：第一部分主要为VAE数学原理推导，需要补充部分证明步骤等。第二部分为VAE的代码实现与深度学习代码框架的实现，需要补充部分代码，在submission.py中。第三部分为独立设计网络架构，完成更复杂的条件生成任务。前两部分指导性质为主，评分标准主要在于完成度以及报告规范。第三部分会要求有好的效果和设计的独特性。

### 环境配置

本实验涉及PyTorch使用，这里不过多赘述，直接贴一个帖子[【超详细教程】2024最新Pytorch安装教程（同时讲解安装CPU和GPU版本）][https://blog.csdn.net/Little_Carter/article/details/135934842?sharetype=blog&shareId=135934842&sharerefer=APP&sharesource=m0_74214690&sharefrom=link]，之后再安装必要的库即可

### Deadline

截止日期为：北京时间6月27日晚12点。迟交1/2/4/7天扣除10/30/80/200分。

### 提交要求

提交一个这样的压缩文件夹

+ `G组号-FINAL.zip` (e.g. `G0-FINAL.zip`)
  + VAEwolabel
    + epoch.pth
    + hyperparameters.json
  + Genwithlabel
    + epoch.pth
    + hyperparameters.json
  + submission.py
  + report.pdf
  + [If needed] Other .py file (Not Recommended)

### 报告要求

为了培养大家一定的学术规范性，我们希望大家提交一份**论文格式**的，**符合学术写作规范**的报告，具体包括如下内容：

+ Title/标题
+ Author list/作者名单: 所有小组成员的姓名学号
+ Abstract/摘要：整体介绍你们设计架构的动机，基本介绍你们做的各种实验取得的效果
+ Preliminary/预备知识：这里我们当作需要完成的理论部分
  + 四个证明问题
+ Methodology/方法论：提出你在条件生成任务中的提出的方法，设计的架构
+ Experiment/实验：
  + Setting/设置：模型的超参数设置等基本设置
  + Results/结果：展示下你们实验的整体结果，包括整体的指标以及实验效果图
  + Indepth analysis/深入分析：通过实验验证你们各种设计的意义，在实验上有什么直接的效果。提示：推荐进行设计技巧的消融实验，以及一定的超参数分析实验等
+ Conclusion/总结：总结一下你的实验体会吧，以及考虑下对于其他任务，你们可能需要什么更多的改进，你们的模型效果如何？
+ Appendix/补充信息：课程反馈，以及你想补充的相对不那么重要的信息

我们将不提供标准的报告模板，这里推荐大家使用overleaf上的[arxiv模板](https://www.overleaf.com/latex/templates/arxiv-and-prime-ai-style-template/qdnhqytdqzsc)，语言不设限制（中文/英文均可）

**********************************

**注：我们只想强调报告的规范性，让大家了解一个AI相关的论文是大致什么样的格式，绝非想要大家在报告上内卷！！！只要你的报告符合标准的格式，每一个必须完成的地方都完成了，一定会拿到应该有的分数！！！！不要卷字数卷美观程度！！！能够两页写完所有必须内容一样能拿到所有的分数！！！**

---

### 成绩评定

**一共满分200分**

+ **第一部分(40pt)** （写在报告中）
+ **第二部分(30pt完成度+10pt效果 = 40pt)**
+ **第三部分(20pt完成度+30pt效果 = 50pt)**
+ **回答问题(20pt)** （写在报告中）
  + 1. 你是怎么调整超参数的，比如学习率，隐藏变量$\textbf{z}$的维度等，你发现这些超参数与实际的效果有哪些影响区别？(10pt)
  + 2. 你尝试了哪些不同的模型架构（比如卷积层？比如全连接层？比如attention机制？）他们有什么特点，哪个更适合本任务呢？(10pt)
+ **实验报告(40pt)** （重点体现第三部分自己的设计）
  + 阐述你的模型的设计思路（主要是条件生成任务中模型的架构，如何控制条件生成）(10pt)
  + 说明你的设计思路的理论支持，如果是模型的小技巧请简述你觉得这样设计的意义，为什么会有效果，**最好有理论推导，或者有实验证明你的设计的效果！！！**(10pt)
  + 报告完整性，规范性 (20pt)
+ **课程反馈(10pt)**：完成本任务花费时长（必须），是否有收获对于本课程，实验有关任何建议问题都可以提
