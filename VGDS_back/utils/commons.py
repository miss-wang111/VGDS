from flask import request
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
#import matplotlib.pyplot as plt
matplotlib.use('Agg') #
from matplotlib import pyplot as plt #
import base64
import json
import re
from lifelines import KaplanMeierFitter
from lifelines.statistics import logrank_test
from lifelines.plotting import add_at_risk_counts
from lifelines.statistics import logrank_test


# 定义分页包装，BQ为flask_sqlalchemy.BaseQuery类型
def PageCreate(BQ, page_limit):
    page = int(request.args.get('page', 1))
    result = BQ.paginate(page=page, per_page=page_limit)
    return result


def Volcano(data_path, fc, p):
    data = pd.read_csv(data_path)  # 读取数据作为dataframe的格式
    data['sig'] = 'normal'  # 给数据矩阵加一列‘sig’，且初始化为‘normal’
    data['log(pvalue)'] = -np.log10(data['pvalue'])  # 给数据矩阵加一列‘log(pvalue)’，其值等于-log10(pvalue)
    data.loc[(data.log2FoldChange > fc) & (data.pvalue < p), 'sig'] = 'up'  # 把满足条件的行的‘sig’项改为‘up’
    data.loc[(data.log2FoldChange < -fc) & (data.pvalue < p), 'sig'] = 'down'  # 把满足条件的行的‘sig’项改为‘down’

    sns.set_style("white")  # 增加该代码让背景变成白色

    ax = sns.scatterplot(x='log2FoldChange', y='log(pvalue)',  # 开始画图，X轴为foldchange，Y轴为pvalue
                         hue='sig',
                         hue_order=('down', 'normal', 'up'),  # 三个类
                         palette=('#012257', 'grey', '#970200'),  # 每个类别的颜色
                         data=data)  # 数据源为前面读取的data
    ax.set_ylabel('-log10(pvalue)', fontweight='bold')   # 设定y轴的名称
    ax.set_xlabel('logFoldchange', fontweight='bold')  # 设定x轴的名称
    scatter_fig = ax.get_figure()  # 画图
    volcano_path = './volcano.png'  # 图片保存的地址为当前文件夹下一个叫volcano的png文件
    scatter_fig.savefig(volcano_path, dpi=300, bbox_inches='tight')  # 保存图片
    up = ((data['log2FoldChange'] > fc) & (data['pvalue'] < p)).sum()  # 计算up类的数量
    down = ((data['log2FoldChange'] < -fc) & (data['pvalue'] < p)).sum()  # 计算down类的数量
    # if up == 0 and down == 0:
    #     return {'ERRO': 'logFC值过大，或P值过小'}
    with open(volcano_path, 'rb') as img:
        volcanoString = str(base64.b64encode(img.read()), encoding='utf-8')
    plt.close()
    res = data[data.sig != 'normal']  # 列表数据，选出data.sig不为Normal的行
    for col in res.columns:  # 格式转换 int -> float
        if res[col].dtype == 'int64':
            res[col] = res[col].astype(float)
    resList = []
    for i in res.index:  # 列表数据由dataframe转成[字典, 字典, ...]的形式
        tmp = res.loc[i, :].to_dict()
        resList.append(tmp)
    resList = json.dumps(resList)
    up_data = data[data.sig == 'up']  # 列表数据，选出data.sig为up的行
    up_list = up_data[['log2FoldChange', 'log(pvalue)', 'gene_name']].values.tolist()  # 将需要的数据转化成列表格式
    down_data = data[data.sig == 'down']
    down_list = down_data[['log2FoldChange', 'log(pvalue)', 'gene_name']].values.tolist()
    nor_data = data[data.sig == 'normal']
    nor_list = nor_data[['log2FoldChange', 'log(pvalue)', 'gene_name']].values.tolist()
    return up, down, volcanoString, resList,up_list, down_list, nor_list


def Volcano2(data_path, fc, p):
    data = pd.read_csv(data_path)  # 读取数据作为dataframe的格式
    data['sig'] = 'normal'  # 给数据矩阵加一列‘sig’，且初始化为‘normal’
    data['log(pvalue)'] = -np.log10(data['pvalue'])  # 给数据矩阵加一列‘log(pvalue)’，其值等于-log10(pvalue)
    data.loc[(data.log2FoldChange > fc) & (data.pvalue < p), 'sig'] = 'up'  # 把满足条件的行的‘sig’项改为‘up’
    data.loc[(data.log2FoldChange < -fc) & (data.pvalue < p), 'sig'] = 'down'  # 把满足条件的行的‘sig’项改为‘down’
    up = ((data['log2FoldChange'] > fc) & (data['pvalue'] < p)).sum()  # 计算up类的数量
    down = ((data['log2FoldChange'] < -fc) & (data['pvalue'] < p)).sum()  # 计算down类的数量

    res = data[data.sig != 'normal']  # 列表数据，选出data.sig不为Normal的行
    for col in res.columns:  # 格式转换 int -> float
        if res[col].dtype == 'int64':
            res[col] = res[col].astype(float)
    resList = []
    for i in res.index:  # 列表数据由dataframe转成[字典, 字典, ...]的形式
        tmp = res.loc[i, :].to_dict()
        resList.append(tmp)
    up_data = data[data.sig == 'up']  # 列表数据，选出data.sig为up的行
    up_list = up_data[['log2FoldChange', 'log(pvalue)', 'gene_name']].values.tolist()  # 将需要的数据转化成列表格式
    down_data = data[data.sig == 'down']
    down_list = down_data[['log2FoldChange', 'log(pvalue)', 'gene_name']].values.tolist()
    nor_data = data[data.sig == 'normal']
    nor_list = nor_data[['log2FoldChange', 'log(pvalue)', 'gene_name']].values.tolist()

    return up, down, resList, up_list, down_list, nor_list

def Heatmap(volcano_path, heatmap_path, fc, p, nr, tr, mt):
    """
    :param volcano_path: 火山图数据文件位置
    :param heatmap_path: 热图数据文件位置
    :param fc: Fold-change cutoff
    :param p:  P-value cutoff
    :param nr: 正常样本的数目
    :param tr: 肿瘤样本的数目
    :return:
    """
    data = pd.read_csv(volcano_path, index_col='gene_name')
    heat = pd.read_csv(heatmap_path, index_col='gene_name')
    numberOfGenes = len(data.index)
    filteredIds = []
    fold = data['log2FoldChange'].tolist()
    pvalue = data['pvalue'].tolist()
    for i in range(0, numberOfGenes):
        if abs(fold[i]) >= fc and pvalue[i] <= p:
            filteredIds.append(i)
    filtered = heat.iloc[filteredIds, :]
    #nr tr 调换位置
    col_ann = pd.DataFrame({'Sample Type':  (['#012257'] * int(nr)) + (['#970200'] * int(tr))}, index=filtered.columns)
    try:
        G = sns.clustermap(filtered, cmap='RdBu_r', standard_scale=0,
                           cbar_pos=(0.02, 0.15, 0.05, 0.54),
                           tree_kws={'linewidths': 0},
                           col_colors=col_ann,
                           xticklabels=False,
                           yticklabels=False,
                           method=mt)
    except:
        res = 'logFC值过大，或P值过小'
        return {'erro': res}
    # G = sns.clustermap(filtered, cmap='RdBu_r', standard_scale=0,
    #                    cbar_pos=(0.02, 0.15, 0.05, 0.54),
    #                    tree_kws={'linewidths': 0},
    #                    col_colors=col_ann,
    #                    xticklabels=False,
    #                    yticklabels=False,
    #                    method=mt)
    sns.set(font_scale=1.2)
    ss = G.ax_heatmap
    label_y = ss.get_yticklabels()
    plt.setp(label_y, rotation=360, horizontalalignment='left')
    heatmap_path = './heatmap.png'
    plt.savefig(heatmap_path, dpi=300, bbox_inches='tight')
    with open(heatmap_path, 'rb') as img:
        heatString = str(base64.b64encode(img.read()), encoding='utf-8')
    plt.close()
    return heatString


def Heatmap2(data_path, gene_list, nr, tr):
    gene_list = eval(gene_list)
    nr = int(nr)
    tr = int(tr)
    gen_data = pd.read_csv(data_path, index_col='gene_name')
    gen_dataT = pd.DataFrame(gen_data.values.T, index=gen_data.columns, columns=gen_data.index)
    gene_choose = gen_dataT[gene_list]
    gene_chooseT = pd.DataFrame(gene_choose.values.T, index=gene_choose.columns, columns=gene_choose.index)
    col_ann = pd.DataFrame({'Sample Type': (['#970200'] * nr) + (['#012257'] * tr)}, index=gene_chooseT.columns)
    G = sns.clustermap(gene_chooseT, cmap='RdBu_r',
                       standard_scale=0,
                       method='average',
                       cbar_pos=(0.02, 0.15, 0.05, 0.54),  # (left, bottom, width, height)
                       tree_kws={'linewidths': 0},  # 线宽
                       col_colors=col_ann,
                       xticklabels=False)
    sns.set(font_scale=1.2)

    ss = G.ax_heatmap
    label_y = ss.get_yticklabels()
    plt.setp(label_y, rotation=360, horizontalalignment='left')
    heatmap_path = './heatmap.png'
    plt.savefig(heatmap_path, dpi=300, bbox_inches='tight')
    with open(heatmap_path, 'rb') as img:
        heatString = str(base64.b64encode(img.read()), encoding='utf-8')
    plt.close()
    return heatString


def Correlation(data_path, gene_str, method):
    gen_data = pd.read_csv(data_path, index_col='gene_name')
    gen_dataT = pd.DataFrame(gen_data.values.T, index=gen_data.columns, columns=gen_data.index)
    # 将gen_str 转化成 gene_list
    gene_str = gene_str.upper()
    gene_str = gene_str.replace("'", "")
    gene_list3 = re.split(r'[;,/()?\n !"\s]\s*', gene_str)
    gene_list2 = [x for x in gene_list3 if x != '']
    gene_list1 = [x for x in gene_list2 if x != ' ']
    gene_list = list(set(gene_list1))
    # print(gene_list)

    # 计算相关系数矩阵
    try:
        gene_choose = gen_dataT[gene_list]
    except Exception as e:
        info = str(e.args)
        res = info.split('[')[-1].split(']')[0]
        return {'missing': res}
    if method == 'pearson':
        cor_matrix2 = gene_choose.corr()
    else:
        cor_matrix2 = gene_choose.corr(method)
    cor_matrix = cor_matrix2.fillna(0)

    # 计算相关系数矩阵
    # gene_choose = gen_dataT[gene_list]
    # if (method == 'pearson'):
    #     cor_matrix = gene_choose.corr()
    # else:
    #     cor_matrix = gene_choose.corr(method)

    # 输出关系热图需要的数据
    m = len(gene_list)
    char_list = [[i, j, cor_matrix.iloc[i, j]] for i in range(m) for j in range(m)]

    # 生成表格需要的数据
    cor_table = cor_matrix.round(2)
    gene_col = pd.DataFrame(gene_list, columns=['Gene Symbol'], index=gene_list)
    cor_table1 = pd.concat([cor_table, gene_col], axis=1)
    cor_table_list = []
    for i in cor_table1.index:  # 列表数据由dataframe转成[字典, 字典, ...]的形式
        tmp = cor_table1.loc[i, :].to_dict()
        cor_table_list.append(tmp)
    cor_table_list = json.dumps(cor_table_list)
    cor_table_list = json.loads(cor_table_list)  # 将 JSON 字符串转回列表
    cor_table_list = list(reversed(cor_table_list))

    # 生成表格的表头
    gene_list.insert(0, 'Gene Symbol')
    gene_header = []
    for i in range(len(gene_list)):
        key_list = ['text', 'value']
        gene = [gene_list[i], gene_list[i]]
        gene_h = dict(zip(key_list, gene))
        gene_header.append(gene_h)
    gene_header1 = str(gene_header)
    header = gene_header1.replace("{'", "{").replace("':", ":").replace(", '", ", ")

    del (gene_list[0])

    return {'char_list': char_list, 'header': header, 'cor_table_list': cor_table_list, 'gene_list': gene_list}


def survival_analyze1(survival_path1, genname, Num1, colorH, colorL, cut, confidence, risk, time, title1):
    data = pd.read_csv(survival_path1, index_col='ID')
    genname = genname.upper()

    # 提取对应基因的生存数据
    data1 = data[[genname, 'state', 'time']]

    # 按照基因表达量排序
    data2 = data1.sort_values(by=genname, ascending=False)

    ## 对基因按百分比分组
    num1 = round(int(Num1) * int(cut) * 0.01)
    num2 = int(Num1) - num1
    group_list = []
    group_list = ['high'] * num1 + ['low'] * num2

    # 生存数据增加分组列
    data2['group'] = group_list

    # 对分组后的生存数据进行生存分析

    f = data2
    km = KaplanMeierFitter()
    if time == 'Months':
        T = f['time'] / 30
    elif time == 'Years':
        T = f['time'] / 365
    else:
        T = f['time']
    E = f['state']

    gender = (f['group'] == 'high')
    ax = plt.subplot(111)

    km_high = KaplanMeierFitter()
    km_high.fit(T[gender], event_observed=E[gender], label=genname + ' high expression')
    if confidence == 'Yes':
        km_high.plot_survival_function(color=colorH)
    else:
        km_high.plot_survival_function(ci_show=False, color=colorH)

    km_low = KaplanMeierFitter()
    km_low.fit(T[~gender], event_observed=E[~gender], label=genname + ' low expression')
    if confidence == 'Yes':
        km_low.plot_survival_function(color=colorL)
    else:
        km_low.plot_survival_function(ci_show=False, color=colorL)

    if risk == 'Yes':
        add_at_risk_counts(km_high, km_low, rows_to_show=['At risk'])

    plt.title(title1, fontsize=20, pad=25, fontweight='bold')  # 图片标题
    ax.set_xlabel(time, fontsize=15)
    ax.set_ylabel('Percent survival', fontsize=15)
    ax.legend(loc='upper right')  # 标签位置
    sns.set_style("white")  # 增加该代码让背景变成白色
    scatter_fig = ax.get_figure()
    pic_path1 = './pic1.png'
    scatter_fig.savefig(pic_path1, dpi=300, bbox_inches='tight')
    with open(pic_path1, 'rb') as img:
        pic1String = str(base64.b64encode(img.read()), encoding='utf-8')
    plt.close()
    results = logrank_test(T[gender], T[~gender], E[gender], E[~gender], alpha=.99)
    p1 = results.p_value
    return p1, pic1String


def survival_analyze2(survival_path2, genname, Num2, colorH, colorL, cut, confidence, risk, time, title2):
    data = pd.read_csv(survival_path2, index_col='ID')
    genname = genname.upper()

    # 提取对应基因的生存数据
    data1 = data[[genname, 'state', 'time']]

    # 按照基因表达量排序
    data2 = data1.sort_values(by=genname, ascending=False)

    ## 对基因按百分比分组
    num1 = round(int(Num2) * int(cut) * 0.01)
    num2 = int(Num2) - num1
    group_list = []
    group_list = ['high'] * num1 + ['low'] * num2

    # 生存数据增加分组列
    data2['group'] = group_list

    # 对分组后的生存数据进行生存分析

    f = data2
    km = KaplanMeierFitter()
    if time == 'Months':
        T = f['time'] / 30
    elif time == 'Years':
        T = f['time'] / 365
    else:
        T = f['time']
    E = f['state']

    gender = (f['group'] == 'high')

    plt.figure()
    ax = plt.subplot(111)

    km_high = KaplanMeierFitter()
    km_high.fit(T[gender], event_observed=E[gender], label=genname + ' high expression')
    if confidence == 'Yes':
        km_high.plot_survival_function(color=colorH)
    else:
        km_high.plot_survival_function(ci_show=False, color=colorH)

    km_low = KaplanMeierFitter()
    km_low.fit(T[~gender], event_observed=E[~gender], label=genname + ' low expression')
    if confidence == 'Yes':
        km_low.plot_survival_function(color=colorL)
    else:
        km_low.plot_survival_function(ci_show=False, color=colorL)

    if risk == 'Yes':
        add_at_risk_counts(km_high, km_low, rows_to_show=['At risk'])

    plt.title(title2, fontsize=20, pad=25, fontweight='bold')  # 图片标题
    ax.set_xlabel(time, fontsize=15)
    ax.set_ylabel('Percent survival', fontsize=15)
    ax.legend(loc='upper right')  # 标签位置

    scatter_fig = ax.get_figure()
    pic_path2 = './pic2.png'
    scatter_fig.savefig(pic_path2, dpi=300, bbox_inches='tight')
    with open(pic_path2, 'rb') as img:
        pic2String = str(base64.b64encode(img.read()), encoding='utf-8')
    plt.close()
    results = logrank_test(T[gender], T[~gender], E[gender], E[~gender], alpha=.99)
    p2 = results.p_value
    print(p2)
    return p2, pic2String

#不同维度差异基因表达散点图
def cor_deff(data_path):
    data = pd.read_csv(data_path)
    co1_list= data[['log2FC1','log2FC2','gene_name']].values.tolist()
    co2_list= data[['log2FC2','log2FC4','gene_name']].values.tolist()
    co3_list= data[['log2FC1','log2FC3','gene_name']].values.tolist()
    co4_list= data[['log2FC2','log2FC3','gene_name']].values.tolist()
    return co1_list,co2_list,co3_list,co4_list

#输出全部差异表达
def cor_deff2(data_path):
    data = pd.read_csv(data_path)
    # co_list= data[['gene_name','log2FC1','log2FC2','log2FC3','log2FC4','log2FC5']].values.tolist()
    gene = data['gene_name'].values.tolist()
    log2FC1 = data['log2FC1'].tolist()
    log2FC2 = data['log2FC2'].tolist()
    log2FC3 = data['log2FC3'].tolist()
    log2FC4 = data['log2FC4'].tolist()
    log2FC5 = data['log2FC5'].tolist()
    return gene,log2FC1,log2FC2,log2FC3,log2FC4,log2FC5

# 单细胞的聚类结果输出
def cellCluster_tsne(data,gene_name):
    Tumor = data[data.cell == 'Tumor']
    tumor_list = Tumor[['tSNE_1', 'tSNE_2', gene_name]].values.tolist()

    NK = data[data.cell == 'NK cell']
    nk_list = NK[['tSNE_1', 'tSNE_2', gene_name]].values.tolist()

    Endo = data[data.cell == 'Endothelial cells']
    endo_list = Endo[['tSNE_1', 'tSNE_2', gene_name]].values.tolist()

    Mye = data[data.cell == 'Myeloid cell']
    mye_list = Mye[['tSNE_1', 'tSNE_2', gene_name]].values.tolist()

    Tcell = data[data.cell == 'T cell']
    tcell_list = Tcell[['tSNE_1', 'tSNE_2', gene_name]].values.tolist()

    HSC = data[data.cell == 'Hepatic stellate cells']
    hsc_list = HSC[['tSNE_1', 'tSNE_2', gene_name]].values.tolist()

    Bcell = data[data.cell == 'B cell']
    bcell_list = Bcell[['tSNE_1', 'tSNE_2', gene_name]].values.tolist()

    Hep = data[data.cell == ' Hepatocytes']
    hep_list = Hep[['tSNE_1', 'tSNE_2', gene_name]].values.tolist()

    Und = data[data.cell == 'undifine']
    und_list = Und[['tSNE_1', 'tSNE_2', gene_name]].values.tolist()

    return {"tumor_list": tumor_list,"nk_list":nk_list,"endo_list":endo_list,"mye_list":mye_list,"tcell_list":tcell_list,"hsc_list":hsc_list,"bcell_list":bcell_list,"hep_list":hep_list,"und_list":und_list}

def cellCluster_umap(data,gene_name):
    Tumor = data[data.cell == 'Tumor']
    tumor_list = Tumor[['UMAP_1', 'UMAP_2', gene_name]].values.tolist()

    NK = data[data.cell == 'NK cell']
    nk_list = NK[['UMAP_1', 'UMAP_2', gene_name]].values.tolist()

    Endo = data[data.cell == 'Endothelial cells']
    endo_list = Endo[['UMAP_1', 'UMAP_2', gene_name]].values.tolist()

    Mye = data[data.cell == 'Myeloid cell']
    mye_list = Mye[['UMAP_1', 'UMAP_2', gene_name]].values.tolist()

    Tcell = data[data.cell == 'T cell']
    tcell_list = Tcell[['UMAP_1', 'UMAP_2', gene_name]].values.tolist()

    HSC = data[data.cell == 'Hepatic stellate cells']
    hsc_list = HSC[['UMAP_1', 'UMAP_2', gene_name]].values.tolist()

    Bcell = data[data.cell == 'B cell']
    bcell_list = Bcell[['UMAP_1', 'UMAP_2', gene_name]].values.tolist()

    Hep = data[data.cell == ' Hepatocytes']
    hep_list = Hep[['UMAP_1', 'UMAP_2', gene_name]].values.tolist()

    Und = data[data.cell == 'undifine']
    und_list = Und[['UMAP_1', 'UMAP_2', gene_name]].values.tolist()

    return {"tumor_list": tumor_list,"nk_list":nk_list,"endo_list":endo_list,"mye_list":mye_list,"tcell_list":tcell_list,"hsc_list":hsc_list,"bcell_list":bcell_list,"hep_list":hep_list,"und_list":und_list}

def cell_exp(data,gene_name):
    #data = pd.read_csv(data_path,sep=",")
    data1=data[['source','HCC_type','tSNE_1','tSNE_2','UMAP_1','UMAP_2','cell',gene_name]]#挑选出需要用的列
    normal =data1[data1.source=='Adjacent liver']#提取正常组织表达
    primary = data1[(data1.source=='Tumor') & (data1.HCC_type=='Primary')]#提取原发肿瘤表达
    relapsed = data1[(data1.source=='Tumor') & (data1.HCC_type=='Relapsed')]#提取复发肿瘤表达
    # normal_list = cellCluster_tsne(normal,gene_name)
    # primary_list = cellCluster_tsne(primary,gene_name)
    # replased_list = cellCluster_tsne(relapsed,gene_name)
    normal_list = cellCluster_umap(normal, gene_name)
    primary_list = cellCluster_umap(primary, gene_name)
    replased_list = cellCluster_umap(relapsed, gene_name)
    return normal_list,primary_list,replased_list

def cell_Meta(data,gene_name):
    #data = pd.read_csv(data_path,sep=",")
    Meta =data[['tSNE_1','tSNE_2','UMAP_1','UMAP_2','cell',gene_name]]#挑选出需要用的列
    Meta_list = cellCluster_tsne(Meta,gene_name)
    return Meta_list


# def cellCluster(data_path):
#     data = pd.read_csv(data_path, sep=";")
#
#     Tumor = data[data.cell == 'Tumor']
#     tumor_list = Tumor[['UMAP_1', 'UMAP_2']].values.tolist()
#
#     NK = data[data.cell == 'NK']
#     nk_list = NK[['UMAP_1', 'UMAP_2']].values.tolist()
#
#     Endo = data[data.cell == 'Endo.']
#     endo_list = Endo[['UMAP_1', 'UMAP_2']].values.tolist()
#
#     Mye = data[data.cell == 'Mye.']
#     mye_list = Mye[['UMAP_1', 'UMAP_2']].values.tolist()
#
#     Tcell = data[data.cell == 'Tcell']
#     tcell_list = Tcell[['UMAP_1', 'UMAP_2']].values.tolist()
#
#     HSC = data[data.cell == 'HSC']
#     hsc_list = HSC[['UMAP_1', 'UMAP_2']].values.tolist()
#
#     Bcell = data[data.cell == 'Bcell']
#     bcell_list = Bcell[['UMAP_1', 'UMAP_2']].values.tolist()
#
#     pDC = data[data.cell == 'pDC']
#     pdc_list = pDC[['UMAP_1', 'UMAP_2']].values.tolist()
#
#     Plasma = data[data.cell == 'Plasma']
#     Plasma_list = Plasma[['UMAP_1', 'UMAP_2']].values.tolist()
#
#     Epi = data[data.cell == 'Epi.']
#     Epi_list = Epi[['UMAP_1', 'UMAP_2']].values.tolist()
#
#     return tumor_list, nk_list, endo_list, mye_list, tcell_list, hsc_list, bcell_list, pdc_list, Plasma_list, Epi_list

# def cellCluster2(data,gene_name):
#     #data = pd.read_csv( data_path, sep=",")
#     data1 = data[['cluster', 'tSNE_1', 'tSNE_2', gene_name]]
#
#     cluster0 = data1[data.cluster == 0]
#     cluster0_list = cluster0[['tSNE_1', 'tSNE_2', gene_name]].values.tolist()
#
#     cluster1 = data1[data.cluster == 1]
#     cluster1_list = cluster1[['tSNE_1', 'tSNE_2', gene_name]].values.tolist()
#
#     cluster2 = data1[data.cluster == 2]
#     cluster2_list = cluster2[['tSNE_1', 'tSNE_2', gene_name]].values.tolist()
#
#     cluster3 = data1[data.cluster == 3]
#     cluster3_list = cluster3[['tSNE_1', 'tSNE_2', gene_name]].values.tolist()
#
#     cluster4 = data1[data.cluster == 4]
#     cluster4_list = cluster4[['tSNE_1', 'tSNE_2', gene_name]].values.tolist()
#
#     cluster5 = data1[data.cluster == 5]
#     cluster5_list = cluster5[['tSNE_1', 'tSNE_2', gene_name]].values.tolist()
#
#     cluster6 = data1[data.cluster == 6]
#     cluster6_list = cluster6[['tSNE_1', 'tSNE_2', gene_name]].values.tolist()
#
#     cluster7 = data1[data.cluster == 7]
#     cluster7_list = cluster7[['tSNE_1', 'tSNE_2', gene_name]].values.tolist()
#
#     cluster8 = data1[data.cluster == 8]
#     cluster8_list = cluster8[['tSNE_1', 'tSNE_2', gene_name]].values.tolist()
#
#     cluster9 = data1[data.cluster == 9]
#     cluster9_list = cluster9[['tSNE_1', 'tSNE_2', gene_name]].values.tolist()
#
#     cluster10 = data1[data.cluster == 10]
#     cluster10_list = cluster10[['tSNE_1', 'tSNE_2', gene_name]].values.tolist()
#
#     cluster11 = data1[data.cluster == 11]
#     cluster11_list = cluster11[['tSNE_1', 'tSNE_2', gene_name]].values.tolist()
#
#     cluster12 = data1[data.cluster == 12]
#     cluster12_list = cluster12[['tSNE_1', 'tSNE_2', gene_name]].values.tolist()
#
#     cluster13 = data1[data.cluster == 13]
#     cluster13_list = cluster13[['tSNE_1', 'tSNE_2', gene_name]].values.tolist()
#
#     cluster14 = data1[data.cluster == 14]
#     cluster14_list = cluster14[['tSNE_1', 'tSNE_2', gene_name]].values.tolist()
#
#     cluster15 = data1[data.cluster == 15]
#     cluster15_list = cluster15[['tSNE_1', 'tSNE_2', gene_name]].values.tolist()
#
#     return cluster0_list ,cluster1_list, cluster2_list ,cluster3_list,cluster4_list,cluster5_list,cluster6_list,\
#            cluster7_list,cluster8_list,cluster9_list,cluster10_list,cluster11_list,cluster12_list,\
#            cluster13_list,cluster14_list,cluster15_list

