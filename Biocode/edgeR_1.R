setwd("D:/差异分析")

if (!requireNamespace("BiocManager", quietly = TRUE))   
  install.packages("BiocManager")

BiocManager::install("edgeR")

library("limma")
library("edgeR")
setwd("D:/网站数据收集/肝癌复发数据/GSE101432/入库数据/火山图")


###############文件导入############
rt=read.table("复发VS原发.txt",sep="\t",header=T,check.names=F)  #改成自己的文件名
rt=as.matrix(rt)
rownames(rt)=rt[,1]#取第一列作为行名
exp=rt[,2:ncol(rt)]#第二列到最后一列是表达的数据#

dimnames=list(rownames(exp),colnames(exp))#取出行名和列名
data=matrix(as.numeric(as.matrix(exp)),nrow=nrow(exp),dimnames=dimnames)#将带引号的数据转换成数值
data=avereps(data)#有的基因出现过多行，把出现多行的gene取平均值#
data=data[rowMeans(data)>1,] #去除低表达的数据#
#write.csv(data,"D:/网站数据收集/肝癌复发数据/GSE56545/复发VS邻近/删除低表达.csv",quote = F)
data=round(data,0)


expr=data
group_list=factor(c(rep("experiment",5),rep("control group",17)))

colData <- data.frame(row.names = colnames(expr),condition = group_list)




condition = group_list
dge <- DGEList(counts=expr,group=group_list)
dge$samples$lib.size <- colSums(dge$counts)
dge <- calcNormFactors(dge)

#生成分组情况数据框
design <- model.matrix(~0+condition)
rownames(design)<-colnames(dge)
colnames(design)<- levels(condition)

dge <- estimateGLMCommonDisp(dge,design)
dge <- estimateGLMTagwiseDisp(dge, design)
dge <- estimateGLMTagwiseDisp(dge, design)

fit <- glmFit(dge, design)
fit2 <- glmLRT(fit, contrast = c(-1,1))

DEG=topTags(fit2, n=nrow(expr))
DEG=as.data.frame(DEG)
write.csv(DEG,"edgR.csv",quote = F)





                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          logFC_cutoff - with(DEG,mean(abs(logFC))+ 2*sd(abs(logFC)) )
logFC_cutoff = 1
DEG$change = as.factor(ifelse(DGE$PValue  0.05 & abs(DGE$logFC)  logFC_cutoff, ifelse(DEG$logFC  logFC_cutoff ,UP,DOWN), NOT))
head(DEG)
table(DEG$change)
edgeR_DEG - DEG
