setwd("D:\\单细胞分析\\单细胞\\GSE149614\\")
getwd()
sessionInfo()

memory.limit()
rm(list=ls()) 
gc()

a <- read.csv("count_转移.csv",sep=',')
a[1:4,1:4]
rownames(a)=a[,1]  #取出第一列
a=a[,-1]     #将第一列删除  
a=a[,-1]     #将第一列删除 
a[1:4,1:4]
summary(a[,1:4]) 
boxplot(a[,1:20])
head(rownames(a))
#write.csv(rownames(a),"基因名.csv",quote = F)
#pdf(file="测试.pdf")
#boxplot(a[,1:4])
#dev.off()

a_m1 <- apply(a, 2, sum)
a_m1
#读取注释文件
b <- read.csv("单细胞样本说明.csv",sep=',')
b[1:5,1:2]

library("Seurat")
#构建seurat对象
?CreateSeuratObject
#创建meta对象 #细胞名+病人/样本名
sce.meta <- data.frame(Patient_ID=b$name,
                       row.names = b$sample_name)
head(sce.meta)
table(sce.meta$Patient_ID)


scRNA = CreateSeuratObject(counts=a,
                           meta.data = sce.meta,
                           min.cells = 10, 
                           min.features = 50)
head(scRNA@meta.data)

summary(scRNA@meta.data)
scRNA@assays$RNA@counts[1:10,1:10]
dim(scRNA)


table(grepl("^MT-",rownames(scRNA)))#MT- 筛选MT开头的基因 这种基因只在线粒体中表达
scRNA[["percent.mt"]] <- PercentageFeatureSet(scRNA, pattern = "^MT-")#增加一行新的显示MT基因所占比例
head(scRNA@meta.data)
summary(scRNA@meta.data)
pctMT=5 #≥ 5% of mitochondria-expressed genes
scRNA <- subset(scRNA, subset = percent.mt < pctMT)#保留MT比例小于5的
dim(scRNA)

# Visualize QC metrics as a violin plot
VlnPlot(scRNA, features = c("nFeature_RNA", "nCount_RNA", "percent.mt"), ncol = 3)



plot1 <- FeatureScatter(scRNA, feature1 = "nCount_RNA", feature2 = "percent.mt")
plot2 <- FeatureScatter(scRNA, feature1 = "nCount_RNA", feature2 = "nFeature_RNA")
plot1 + plot2

#挑选高变基因
scRNA <- FindVariableFeatures(scRNA, selection.method = "vst", nfeatures = 2000)
top10 <- head(VariableFeatures(scRNA), 10)

# 高变基因散点图
plot1 <- VariableFeaturePlot(scRNA)
plot2 <- LabelPoints(plot = plot1, points = top10, repel = TRUE)
plot1 + plot2

#接下来，我们应用线性变换（“缩放”），这是在 PCA 等降维技术之前的标准预处理步骤。ScaleData()功能：

#移动每个基因的表达，使细胞间的平均表达为 0
#缩放每个基因的表达，使细胞间的方差为 1
#此步骤在下游分析中给予同等权重，因此高表达基因不会占主导地位
#结果存储在pbmc[["RNA"]]@scale.data
all.genes <- rownames(scRNA)
scRNA <- ScaleData(scRNA, features = all.genes)
#对比一下结果
GetAssayData(scRNA,slot = "scale.data",assay = "RNA")[1:8,1:4]
GetAssayData(scRNA,slot = "counts",assay = "RNA")[1:8,1:4]


#接下来，我们对缩放数据执行 PCA。默认情况下，仅将先前确定的变量特征用作输入，但features如果您希望选择不同的子集，可以使用参数定义。
?RunPCA
scRNA <- RunPCA(scRNA, features = VariableFeatures(object = scRNA))

DimPlot(scRNA,reduction = "pca",group.by = "Patient_ID")

# 输出前五个分类基因
print(scRNA[["pca"]], dims = 1:5, nfeatures = 5)

#可视化定义 PCA 的单元格和特征，包括VizDimReduction()、DimPlot()和DimHeatmap()
VizDimLoadings(scRNA, dims = 1:5, reduction = "pca")

DimPlot(scRNA, reduction = "pca")


DimHeatmap(scRNA, dims = 1, cells = 500, balanced = TRUE)
DimHeatmap(scRNA, dims = 1:20, cells = 500, balanced = TRUE)



scRNA <- JackStraw(scRNA, num.replicate = 100)
scRNA <- ScoreJackStraw(scRNA, dims = 1:20)

#该JackStrawPlot()函数提供了一个可视化工具，
#用于将每台 PC 的 p 值分布与均匀分布（虚线）进行比较。“显着”PC 将显示出具有低 p 值的特征的强烈丰富性（虚线上方的实线）。
#在这种情况下，在前 10-12 个 PC 之后，重要性似乎急剧下降。
JackStrawPlot(scRNA, dims = 1:20)
#画肘部图
ElbowPlot(scRNA)
?FindClusters
scRNA <- FindNeighbors(scRNA, dims = 1:20)
scRNA <- FindClusters(scRNA, resolution = 0.8)
#获得24个聚类

# 前5个细胞的cluster
head(Idents(scRNA), 5)
table(scRNA@meta.data$seurat_clusters)

# If you haven't installed UMAP, you can do so via reticulate::py_install(packages =
# 'umap-learn')
scRNA <- RunUMAP(scRNA, dims = 1:16)
# note that you can set `label = TRUE` or use the LabelClusters function to help label
# individual clusters
DimPlot(scRNA, reduction = "umap",label = TRUE)
?DimPlot
scRNA = RunTSNE(scRNA, dims = 1:16)
DimPlot(scRNA, reduction = "tsne")
scRNA@reductions$umap[1:2,1:2]
scRNA@reductions[["umap"]]@cell.embeddings
write.csv(scRNA@reductions[["tsne"]]@cell.embeddings,"tsne坐标.csv",quote = F)
write.csv(scRNA@reductions[["umap"]]@cell.embeddings,"umap坐标.csv",quote = F)
scRNA@active.ident
write.csv(scRNA@active.ident,"聚类结果4.csv",quote = F)

write.csv(scRNA.markers,"cluster基因.csv",quote = F)


#寻找差异表达的特征 marker基因
# find all markers of cluster 2
cluster2.markers <- FindMarkers(scRNA, ident.1 = 2, min.pct = 0.25)
head(cluster2.markers, n = 5)
# find markers for every cluster compared to all remaining cells, report only the positive
# ones
scRNA.markers <- FindAllMarkers(scRNA, only.pos = TRUE, min.pct = 0.25, logfc.threshold = 0.25)
?FindAllMarkers
scRNA.markers2 <- FindAllMarkers(scRNA, only.pos = TRUE,pct.1=0.5,min.pct = 0.25, logfc.threshold = 0.25)
library(dplyr)    # alternatively, this also loads %>%
scRNA.markers %>%
  group_by(cluster) %>%
  slice_max(n = 2, order_by = avg_log2FC)
#肝细胞cluster筛选
VlnPlot(scRNA, features = c("SLPI","DEFB1","ANXA13","CYP2C9"))
FeaturePlot(scRNA, features =c("SLPI","DEFB1","ANXA13","CYP2C9"))

#Endo细胞cluster筛选
VlnPlot(scRNA, features = c("PECAM1","CDH5","PLVAP","CCL14","TM4SF1","EMCN","ACKR1","ESM1"))
FeaturePlot(scRNA, features =c("PECAM1","CDH5","PLVAP","CCL14","TM4SF1","EMCN","ACKR1","ESM1"))

#HSC细胞筛选
VlnPlot(scRNA, features = c("ACTA2","PDGFRB"))
FeaturePlot(scRNA, features =c("ACTA2","PDGFRB"))

#NK细胞筛选
VlnPlot(scRNA, features = c("RPL18","RPS20","RPL28","RPL30","RPL32","RPL23A"))
FeaturePlot(scRNA, features = c("RPL18","RPS20"))

#T细胞筛选
VlnPlot(scRNA, features = c("CD3D","CD3G","CD3E"))
FeaturePlot(scRNA, features =c("ACTA2","PDGFRB"))

#mye细胞
VlnPlot(scRNA, features = c("LYZ","C1QB","PTPRC","CD14","AIF1","TYROBP","CD163"))
FeaturePlot(scRNA, features =c("LYZ","C1QB","PTPRC","CD14","AIF1","TYROBP","CD163"))

#B细胞
VlnPlot(scRNA, features = c("MS4A1","CD79A","CD19","MS4A1","BANK1","BLK","IRF8"))
FeaturePlot(scRNA, features = c("MS4A1","CD79A","CD19","MS4A1","BANK1","BLK","IRF8"))

#plasma细胞
VlnPlot(scRNA, features = c("MZB1","BRSK1","AC026202.3","AC026202.3","JSRP1","LINC00582","PARM1","TAS1R3"))
FeaturePlot(scRNA, features =c("ACTA2","PDGFRB"))

#Epi细胞
VlnPlot(scRNA, features = c("EPCAM","KRT19","CDH1","MYLK","ANKRD30A","ABCA13","ABCB10","ADGB","SFTPB","SFTPC"))
FeaturePlot(scRNA, features =c("ACTA2","PDGFRB"))


VlnPlot(scRNA, features = c("EPCAM","KRT8","KRT18","KRT19","EGFR"))
FeaturePlot(scRNA, features =c("EPCAM","KRT8","KRT18","KRT19","EGFR"))

# you can plot raw counts as well
VlnPlot(scRNA, features =  c("VWF", "PECAM1", "CDH5", "VEGFA","FLT1", "ECSCR"," ACYP1","ADGRL2","SELE","ICAM1"), slot = "counts", log = TRUE)

FeaturePlot(scRNA, features = c("IL7R", "CCR6", "CD3E", "CD14", "FCER1A", "FCGR3A", "LYZ", "PPBP",
                                "CD8A"))

FeaturePlot(scRNA, features = c("VWF", "PECAM1", "CDH5", "VEGFA","FLT1", "ECSCR"," ACYP1","ADGRL2","SELE","ICAM1" ))

#NK细胞
VlnPlot(scRNA, features =  c("FCGR3A", "KLRB1", "KLRD1", "NKG7", "XCL1", "XCL2", "NCR3", "NCR1", "CD247", "GZMB", "KLRC1", "KLRK1"), slot = "counts", log = TRUE)

FeaturePlot(scRNA, features = c("IL7R", "CCR6", "CD3E", "CD14", "FCER1A", "FCGR3A", "LYZ", "PPBP",
                                "CD8A"))
library(dplyr)
scRNA.markers %>%
  group_by(cluster) %>%
  top_n(n = 10, wt = avg_log2FC) -> top10
scRNA.markers2 %>%
  group_by(cluster) %>%
  top_n(n = 20, wt = avg_log2FC) -> top202
scRNA.markers %>%
  group_by(cluster) %>%
  top_n(n = 20, wt = avg_log2FC) -> top20
scRNA.markers %>%
  group_by(cluster) %>%
  top_n(n = 5, wt = avg_log2FC) -> top5
write.csv(top10,"4top10.csv",quote = F)
write.csv(top20,"top20.csv",quote = F)
DoHeatmap(scRNA, features = top5$gene) + NoLegend()


gene <- read.csv("E:/单细胞分析/genemap.csv",sep=',')

DoHeatmap(scRNA, features = gene$gene) + NoLegend()



#免疫细胞有注释









#恶性细胞注释
#install.packages("devtools")
library(devtools)
install_github("navinlabcode/copykat")

library(copykat)
?copykat

a#识别恶性细胞
scRNA@assays$RNA@counts
exp.rawdata <- as.matrix(scRNA@assays$RNA@counts)

cnv <- copykat(rawmat=exp.rawdata, ngene.chr=5, sam.name="SCLC", plot.genes="FALSE", n.cores=1)
# ngene.chr参数是过滤细胞的一个标准，它要求被用来做CNV预测的细胞，一个染色体上至少有5个基因。
# sam.name定义样本名称 (sample name)，会给出来的文件加前缀
pred <- data.frame(cnv$prediction)

saveRDS(cnv, "cnv.rds")


copykat.test <- copykat(rawmat=exp.rawdata, id.type="S", ngene.chr=5, win.size=25, KS.cut=0.1, sam.name="test", distance="euclidean", norm.cell.names="",output.seg="FLASE", plot.genes="FALSE", genome="hg20",n.cores=1)

pred.test <- data.frame(copykat.test$prediction)
CNA.test <- data.frame(copykat.test$CNAmat)

write.csv(pred.test,"识别肿瘤细胞total.csv",quote = F)



head(pred.test)
head(CNA.test[ , 1:5])

my_palette <- colorRampPalette(rev(RColorBrewer::brewer.pal(n = 3, name = "RdBu")))(n = 999)

chr <- as.numeric(CNA.test$chrom) %% 2+1
rbPal1 <- colorRampPalette(c('black','grey'))
CHR <- rbPal1(2)[as.numeric(chr)]
chr1 <- cbind(CHR,CHR)

rbPal5 <- colorRampPalette(RColorBrewer::brewer.pal(n = 8, name = "Dark2")[2:1])
com.preN <- pred.test$copykat.pred
pred <- rbPal5(2)[as.numeric(factor(com.preN))]

cells <- rbind(pred,pred)
col_breaks = c(seq(-1,-0.4,length=50),seq(-0.4,-0.2,length=150),seq(-0.2,0.2,length=600),seq(0.2,0.4,length=150),seq(0.4, 1,length=50))

heatmap.3(t(CNA.test[,4:ncol(CNA.test)]),dendrogram="r", distfun = function(x) parallelDist::parDist(x,threads =4, method = "euclidean"), hclustfun = function(x) hclust(x, method="ward.D2"),
          ColSideColors=chr1,RowSideColors=cells,Colv=NA, Rowv=TRUE,
          notecol="black",col=my_palette,breaks=col_breaks, key=TRUE,
          keysize=1, density.info="none", trace="none",
          cexRow=0.1,cexCol=0.1,cex.main=1,cex.lab=0.1,
          symm=F,symkey=F,symbreaks=T,cex=1, cex.main=4, margins=c(10,10))

legend("topright", paste("pred.",names(table(com.preN)),sep=""), pch=15,col=RColorBrewer::brewer.pal(n = 8, name = "Dark2")[2:1], cex=0.6, bty="n")


















cnv <- copykat(rawmat=counts, ngene.chr=5, sam.name="SCLC", n.cores=8)
# ngene.chr参数是过滤细胞的一个标准，它要求被用来做CNV预测的细胞，一个染色体上至少有5个基因。
# sam.name定义样本名称 (sample name)，会给出来的文件加前缀
saveRDS(cnv, "cnv.rds")
