###############文件导入############
setwd("D:/网站数据收集/肝癌复发数据/GSE101432/入库数据/")
setwd("D:\\单细胞分析\\单细胞\\GSE149614\\")

getwd()

filepath<-file.choose()
filepath
rt=read.table(filepath,sep="\t",header=T,check.names=F) 
rt=read.table("GSE149614_HCC.scRNAseq.txt",sep="\t",header=T,check.names=F)  #改成自己的文件名
df = rt[51149:53991]
write.csv(df,"count_转移.csv",quote = F)



rt=as.matrix(rt)
rownames(rt)=rt[,1]#取第一列作为行名
exp=rt[,2:ncol(rt)]#第二列到最后一列是表达的数据#

dimnames=list(rownames(exp),colnames(exp))#取出行名和列名
data=matrix(as.numeric(as.matrix(exp)),nrow=nrow(exp),dimnames=dimnames)#将带引号的数据转换成数值
data=avereps(data)#有的基因出现过多行，把出现多行的gene取平均值#
data=data[rowMeans(data)>1,] #去除低表达的数据#
data=round(data,0)


expr=data
group_list=factor(c(rep("treat",5),rep("con",17)))



# Limma-voomI library(limma)
library(limma)


design <- model.matrix(~0+group_list)
colnames(design)=levels(group_list)
rownames(design)=colnames(expr)


dge <- DGEList(counts=expr) 
dge<-calcNormFactors(dge)
logCPM<-cpm(dge,log=TRUE, prior.count=3)
v <- voom(dge,design,normalize="quantile")
fit <- lmFit(v,design)
constrasts=paste(rev(levels(group_list)),collapse="-")
cont.matrix<-makeContrasts(contrasts=constrasts,levels=design)
fit2=contrasts.fit(fit,cont.matrix)
fit2=eBayes(fit2)
DEG=topTable(fit2,coef=constrasts,n=Inf)
DEG=na.omit(DEG)

write.csv(DEG,"limma.csv",quote = F)


#logFC_cutoff-with(EG,mean(abs(1ogFC))+2*sd(abs(logFC)))
logFC_cutoff - 1
DEG$change=as.factor(
  ifelse(DEG$P.Value 0.05 & abs(DEG$logFC)  logFC_cutoff, 
         ifelse(DEG$logFClogFC_cutoff,UP,DOWN),NOT)
)
