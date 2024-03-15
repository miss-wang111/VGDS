#获取工作目录
getwd()
# 更改工作目录
setwd("D:/差异分析")
setwd("D:/网站数据收集/肝癌复发数据/GSE101432/入库数据/火山图")

### 清理内存
memory.limit()
rm(list=ls()) 
gc()
###############文件导入############
rt=read.table("复发VS原发.txt",sep="\t",header=T,check.names=F)  #改成自己的文件名
rt=as.matrix(rt)
rownames(rt)=rt[,1]#取第一列作为行名
exp=rt[,2:ncol(rt)]#第二列到最后一列是表达的数据#

library(DESeq2)
library(limma)
dimnames=list(rownames(exp),colnames(exp))#取出行名和列名
data=matrix(as.numeric(as.matrix(exp)),nrow=nrow(exp),dimnames=dimnames)#将带引号的数据转换成数值
data=avereps(data)#有的基因出现过多行，把出现多行的gene取平均值#
data=data[rowMeans(data)>1,] #去除低表达的数据#
write.csv(data,"删除低表达.csv",quote = F)
data=round(data,0)
#write.csv(data,"333.csv",quote = F)

#将TXT格式的文件改为表达矩阵，行名是样本列名是基因

###################DESeq2包进行差异分析#################
#生成样本信息的factor
group=c(rep("experiment",5),rep("control group",17))   #按照癌症和正常样品数目修改 样本中正常样本写在前面所以这样写
condition = factor(group)
#定义表达矩阵的信息：将样本标好类别
colData <- data.frame(row.names = colnames(data),condition)


#生成DESeq2差异分析输入文件
dds <- DESeqDataSetFromMatrix(countData = data, colData = colData, design = ~ condition)
#过滤低表达的gene
dds <- dds[rowSums(counts(dds)) > 1,]
#进行差异分析
dds <- DESeq(dds)
#对基因表达count数据处理
vsd <- vst(dds, blind = FALSE)
write.csv(as.data.frame(assay(vsd)),
          file="555.csv")
#获取DESeq2差异分析结果
res <- results(dds)
write.csv(res,"deseq2.csv",quote = F)




