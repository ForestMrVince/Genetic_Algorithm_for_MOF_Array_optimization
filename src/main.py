from GA_for_MOF_Array_opt.Genetic_Algorithm import GA_Handle_typedef
import numpy

population_size = 20                    # 种群大小
array_size = 5                          # MOF阵列大小
parent_top = population_size // 5       # 在竞争中胜出的顶部染色体个数
parent_lucky = population_size // 5     # 在竞争中胜出的幸运染色体个数
# mutation_rate = list(numpy.linspace(0.1,0.9,num = 5))   # 变异率
mutation_rate = list(numpy.linspace(0.01,0.1,num = 10)) # 变异率
mof_list = range(1, 51)                 # MOF列表
# 单独的MOF对应值，详情参见：开发文档.docx中2.2.3.小结
mof_SimResults = numpy.genfromtxt('Current_mof_SimResults.csv', delimiter=',')
mof_SimResults = mof_SimResults.tolist()
# mof_SimResults = list(numpy.random.\
#                       rand(len(mof_list)))
max_NumOfIterations = 50                # 最大迭代次数

# 计算理论最大值
mof_SimResults_temp = mof_SimResults.copy()
mof_SimResults_temp.sort(reverse = True)
result = 1
for i in range(array_size):
    result = result * mof_SimResults_temp[i]
print(result)

for j in range(len(mutation_rate)):
    GA_Handle = GA_Handle_typedef(population_size, array_size, parent_top,\
                                  parent_lucky, mutation_rate[j], mof_list,\
                                  mof_SimResults, max_NumOfIterations)
    GA_Handle()
GA_Handle.DataFile_output('Theoretical maximum.csv',['Theoretical maximum: ', result])
# GA_Handle.DataFile_output('Current_mof_SimResults.csv',mof_SimResults)
GA_Handle.DataFile_output('mutation_rate.csv',mutation_rate)
