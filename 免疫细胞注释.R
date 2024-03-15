setwd("D:\\单细胞分析\\单细胞\\GSE149614\\")
getwd()
sessionInfo()

memory.limit()
rm(list=ls()) 
gc()

a <- read.csv("免疫细胞_count.csv",sep=',')
a[1:4,1:4]
rownames(a)=a[,1]  #取出第一列
a=a[,-1]     #将第一列删除  
a[1:4,1:4]
summary(a[,1:4]) 
boxplot(a[,1:20])
head(rownames(a))

head(colnames(a))
#sample_name = colnames(a)
#write.csv(sample_name,"免疫细胞样本说明.csv",quote = F)

a_m1 <- apply(a, 2, sum)
a_m1
#读取注释文件
b <- read.csv("免疫细胞样本说明.csv",sep=',')
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
#获得6个聚类

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

#singleR注释免疫亚型
library(SingleR)
#if (!requireNamespace("BiocManager", quietly = TRUE))#    install.packages("BiocManager")

BiocManager::install("celldex")
BiocManager::install("Seurat")

library(celldex)
library(Seurat)
library(pheatmap)
##下载注释数据库
hpca.se <- HumanPrimaryCellAtlasData()
hpca.se

#直接load下载好的数据库
load("HumanPrimaryCellAtlas_hpca.se_human.RData")
load("BlueprintEncode_bpe.se_human.RData")

#进行singleR注释
pbmc_for_SingleR <- GetAssayData(scRNA, slot="data") ##获取标准化矩阵
pbmc.hesc <- SingleR(test = pbmc_for_SingleR, ref = hpca.se, labels = hpca.se$label.main) #
pbmc.hesc

#seurat 和 singleR的table表
table(pbmc.hesc$labels,scRNA@meta.data$seurat_clusters)

scRNA@meta.data$labels <-pbmc.hesc$labels
print(DimPlot(scRNA, group.by = c("seurat_clusters", "labels"),reduction = "umap"))
