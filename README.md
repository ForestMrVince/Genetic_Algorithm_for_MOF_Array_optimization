# Genetic_Algorithm_for_MOF_Array_optimization
[github repository](https://github.com/ForestMrVince/Genetic_Algorithm_for_MOF_Array_optimization)
## 内容说明
穆壮壮_1910294 的“复杂系统典型应用问题的建模与优化方法”课程作业。
## 文件目录说明
- `.\doc`：“复杂系统典型应用问题的建模与优化方法”课程作业的相关文档存放目录；
    - `.\doc\GA_for_MOF_Array_opt`：复现的“用于MOF阵列优化的遗传算法库”开发文档的存放目录；
    - `.\doc\HomeWorks`：作业文档存放目录。
- `.\src`：复现的“用于MOF阵列优化的遗传算法库”源文件的存放目录；
- `.\data`: 复现的“用于MOF阵列优化的遗传算法库”输出数据的存放目录。

## `src`代码使用及`data`目录使用的详细说明

### `src`代码使用说明：
- 文件`main.py`是使用本代码的入口文件，直接打开运行即可，同时可以根据其中的注释自行修改各项参数；
- 子目录`GA_for_MOF_Array_opt`中存放的是本作业遗传算法的代码源文件，如果没有修改遗传算法结构的需求，建议不要改动。

### `data`目录使用说明：
- 文件夹子目录命名为`mutation_rate = num1 to num2 step = num3`，其中num1、num2、num3分别为变异率参数化扫描的起始值、终止值、步长；
- 文件夹子目录的子目录命名为`crossover&mutation`或`mutation_only`，分别代表着产生子代的策略为交叉加变异，以及只使用变异。
- 文件夹子目录的子目录中名为`DataPlot.m`的文件，为matlab script，可以直接运行绘制出遗传算法适值-代数曲线，数据已经准备好不需要重新使用`csv`文件导入，数据文件为`matlab_data.mat`，另外的`fig`和`tif`文件是绘制好的遗传算法适值-代数曲线。

## 使用说明
1. 点击右上角的绿色`Clone or download`按钮；
2. 点击`Download ZIP`，即可以压缩包形式下载所有文件。

## 免责声明
1. 作业只允许在署名作者的前提下转载或使用！！！
2. 作业在课程中仅作交流之用，由抄袭作业引起的一切后果本人概不负责！！！
