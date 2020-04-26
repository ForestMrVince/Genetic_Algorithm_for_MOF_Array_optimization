import random
import operator
import csv
import copy
# test
import numpy

class GA_Handle_typedef:
    
    population = [] # 种群列表
    fitness = []    # 适值列表
    generations_file = './generations.csv'        # 保存每一代的种群和适值的文件
    generations_file_head = []
    big_file = './Fitness_in_generations.csv'     # 每一代的最好适值和平均适值数据保存文件
    big_file_head = ["Generation", "BestFitness", "AverageFitness"]
    generation_number = 0 # 当前代数

    def DataFile_output(self, filename, Data): # 文件输出函数
        with open(filename, 'a', newline='') as DataFile:
            DataFile_csv_handle = csv.writer(DataFile)
            DataFile_csv_handle.writerow(Data)

    def creat_first_generation(self): # 创建初始种群
        for i in range(self.population_size):
            array_temp = random.sample(self.mof_list, self.array_size)
            array_temp.sort()
            self.population.append(array_temp)

    def fix_duplicate_in_arrays(self): # 修复种群中重复的染色体和染色体上重复的基因
        # 先修复每个染色体上的重复基因
        for m in range(self.population_size):
            self.population[m] = list(set(self.population[m]))
            while len(self.population[m]) < self.array_size:
                Unique_elements = [mof for mof in self.mof_list\
                                   if mof not in self.population[m]]# 选择出当前染色体于MOF列表的补集
                self.population[m].append(random.sample(Unique_elements,\
                                                        self.array_size\
                                                        - len(self.population[m])))
                self.population[m] = list(set(self.population[m]))
            self.population[m].sort()
        # 再修复种群中重复的染色体
        self.population = self.remove_duplicate_in_arrays(self.population)
        size_temp = len(self.population)
        while size_temp < self.population_size:
            for i in range(self.population_size - size_temp):
                array_temp = random.sample(self.mof_list, self.array_size)
                array_temp.sort()
                self.population.append(array_temp)
            self.population = self.remove_duplicate_in_arrays(self.population)
            size_temp = len(self.population)

    def remove_duplicate_in_arrays(self, arrays): # 删除输入种群中重复的染色体
        size_temp2 = len(arrays)
        duplicate_list = []
        for i in range(size_temp2):
            array = arrays[i]
            for j in range(i+1, size_temp2):
                if operator.eq(array, arrays[j]):
                    duplicate_list.append(i)
        duplicate_list = list(set(duplicate_list))
        duplicate_list.sort(reverse = True)
        for n in range(len(duplicate_list)):
            del arrays[duplicate_list[n]]
        return(arrays)

    def fitness_calculation(self): # 计算适值，详情参见：开发文档.docx中2.2.3.小结
        self.fitness = list(numpy.random.rand(self.population_size))
        for i in range(self.population_size):
            result = 1
            for j in range(self.array_size):
                result = result * self.mof_SimResults[(self.population[i])[j]-1]
            self.fitness[i] = result

    def generation_sort(self):
        self.population = [x for _,x in sorted(zip(self.fitness, self.population),reverse = True)]
        self.fitness.sort(reverse = True)

    def save_generations(self): # 保存当前种群和适值至文件“generations.csv”
                                # 保存每一代最大适值和平均适值至文件'Fitness_in_generations.csv' 
        self.DataFile_output(self.generations_file,\
                             ["Generation: ", self.generation_number] + self.generations_file_head)
        Data_temp = copy.deepcopy(self.population)
        for i in range(len(Data_temp)):
            Data_temp[i].append(self.fitness[i])
            self.DataFile_output(self.generations_file, Data_temp[i])
        self.DataFile_output(self.big_file, [self.generation_number, self.fitness[0],\
                                             sum(self.fitness)/self.population_size])

    def choose_parents(self): # 选择父代
        result = []
        result.extend(self.population[0:self.parent_best])
        result.extend(random.sample(self.population[self.parent_best:], self.parent_lucky))
        self.population = result

    def multiplication_by_crossover(self): # 使用交叉方法
        size_parents = len(self.population)
        parents = copy.deepcopy(self.population)
        for i in range(size_parents, self.population_size):
            parent1, parent2 = random.sample(parents,2)
            Children = random.sample(list(set(parent1 + parent2)), self.array_size)
            Children = self.mutation_aftrt_crossover(Children)
            Children.sort()
            self.population.append(Children)

    def mutation_aftrt_crossover(self, children): # 交叉方法中的变异方法
        mof_list_Withoutchildren = [mof for mof in self.mof_list if mof not in children]
        mof_list_Withoutchildren_new = mof_list_Withoutchildren # 不需要浅拷贝
        for i in range(self.array_size):
            if random.random() < self.mutation_rate:
                children[i] = random.choice(mof_list_Withoutchildren_new)
                mof_list_Withoutchildren_new = [mof for mof in mof_list_Withoutchildren\
                                              if mof not in children]
                mof_list_Withoutchildren = mof_list_Withoutchildren_new
                # 该↑语句，是猜测原程序的意图是为了删除用过的基因，以保证染色体中基因不重复，但必须有该句才有效
                if not mof_list_Withoutchildren_new: # 判断列表是否为空
                    mof_list_Withoutchildren_new = [mof for mof in self.mof_list if\
                                                  mof not in children]
        return(children)

    def multiplication_by_mutation(self): # 使用变异方法
        size_parents = len(self.population)
        parents = copy.deepcopy(self.population)
        for i in range(size_parents, self.population_size):
            parent = random.choice(parents)
            children = parent.copy()
            mof_list_WithoutParent = [mof for mof in self.mof_list if mof not in parent]
            mof_list_WithoutParent_new = mof_list_WithoutParent # 不需要浅拷贝
            for j in range(self.array_size):
                if random.random() < self.mutation_rate:
                    children[j] = random.choice(mof_list_WithoutParent_new)
                    mof_list_WithoutParent_new = [mof for mof in mof_list_WithoutParent\
                                                  if mof not in children]
                    mof_list_WithoutParent = mof_list_WithoutParent_new
                    # 该↑语句，是猜测原程序的意图是为了删除用过的基因，以保证染色体中基因不重复，但必须有该句才有效
                    if not mof_list_WithoutParent_new: # 判断列表是否为空
                        mof_list_WithoutParent_new = [mof for mof in self.mof_list if\
                                                      mof not in children]
            children.sort()
            self.population.append(children)

    def multiplication(self): # 产生子代形成新的种群
        self.multiplication_by_crossover() # 使用交叉方法
        # self.multiplication_by_mutation() # 使用变异方法

    def __init__(self, population_size, array_size, parent_best, parent_lucky,\
                 mutation_rate, mof_list, mof_SimResults, max_NumOfIterations):
        # 设置遗传算法关键参数
        self.population_size = population_size         # 种群大小
        self.array_size = array_size                   # MOF阵列大小
        self.parent_best = parent_best                 # 在竞争中胜出的顶部染色体个数
        self.parent_lucky = parent_lucky               # 在竞争中胜出的幸运染色体个数
        self.mutation_rate = mutation_rate             # 变异率
        self.mof_list = mof_list                       # MOF列表
        self.mof_SimResults = mof_SimResults           # 单独的MOF对应值，详情参见：开发文档.docx中2.2.3.小结
        self.max_NumOfIterations = max_NumOfIterations # 最大迭代次数
        # 初始化输出文件
        #  初始化 generations.csv 文件
        for i in range(2, self.array_size):
            self.generations_file_head.append('#')
        self.generations_file_head.append('fitness')
        # 初始化 BestFitness_in_generations.csv 文件
        self.DataFile_output(self.big_file, self.big_file_head)
        self.generation_number = 0             # 初始化当前代数

    def __call__(self): # 运算
        self.creat_first_generation()   # 第一步：创建初始种群
        self.fix_duplicate_in_arrays()  # 第二步：修复种群中重复的染色体和染色体上重复的基因
        # 开始遗传运算的循环
        while self.generation_number < self.max_NumOfIterations:
            print(self.generation_number)
            self.fitness_calculation()      # 循环第一步：计算适值
            self.generation_sort()          # 循环第二步：按照适值大小将适值和种群列表对应排序
            self.save_generations()         # 循环第三步：保存当前种群和适值至文件“generations.csv”
            ################################# 保存每一代最大适值和平均适值至文件'Fitness_in_generations.csv' 
            self.choose_parents()           # 循环第四步：选择父代
            self.multiplication()           # 循环第五步：产生子代形成新的种群
            self.fix_duplicate_in_arrays()  # 循环第六步：修复种群中重复的染色体和染色体上重复的基因
            self.generation_number = self.generation_number + 1 # 当前代数+1
        print('end')
