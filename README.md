# Labelme-auto-seg

### 1.介绍

Labelme，众所周知是一款开源的图像标注工具。[Github地址](https://github.com/wkentaro/labelme)

FastDeploy是一款基于PaddlePaddle的**全场景**、**易用灵活**、**极致高效**的AI推理部署工具提供开箱即用的云边端部署体验, 支持超过 150+ Text, Vision, Speech和跨模态模型，并实现端到端的推理性能优化。包括图像分类、物体检测、图像分割、人脸检测、人脸识别、关键点检测、抠图、OCR、NLP、TTS等任务。[Github地址](https://github.com/PaddlePaddle/FastDeploy)

Labelme-auto-seg 是一款 Labelme与FastDeploy相结合的辅助语义分割标注的工具。

### 2.快速安装

`1. 克隆仓库。 git clone https://github.com/richarddddd198/Labelme-auto-seg.git`

`2. 安装依赖。 pip install labelme fastdeploy-python -f https://www.paddlepaddle.org.cn/whl/fastdeploy.html`

`3. 卸载labelme。  pip uninstall labelme`

`4. 进入目录。 cd Labelme-auto-seg`

`5. 构建labelme。python setup.py install`

`6. 输入命令打开即可。 labelme`



### 3.使用教程

视频教程：[B站：Labelme与FastDeploy相结合，辅助分割标注，减少生命消耗](https://www.bilibili.com/video/BV1vv4y1R7YB/?share_source=copy_web&vd_source=3fc869b3c9caaee3695f6232d3e3d32c)