from flask import Flask
from flask_restful import Api, Resource, reqparse
import config
import pymysql
import time
from exts import db
from models import Browse, Article, Detail, Genes
from marshmallow_sqlalchemy import ModelSchema
from flask_caching import Cache
from utils.commons import PageCreate, Volcano, Volcano2, Heatmap, Heatmap2, Correlation, survival_analyze1, \
    survival_analyze2, cor_deff, cor_deff2,cell_exp,cellCluster_tsne,cell_Meta
import os
import json
import pandas as pd

pymysql.install_as_MySQLdb()

app = Flask(__name__)
app.config.from_object(config)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

api = Api(app)
db.init_app(app)


@cache.cached(key_prefix = 'cell',timeout=6000)
def cell(data_path):
    data = pd.read_csv(data_path,sep=",")
    return data

@cache.cached(key_prefix = 'cell_mate',timeout=6000)
def cellMata(data_path):
    data = pd.read_csv(data_path,sep=",")
    return data

# @cache.cached(key_prefix = 'add')
# def add(a,b):
#     time.sleep(2)
#     return a+b

parser = reqparse.RequestParser()
parser.add_argument('id')
parser.add_argument('target')
parser.add_argument('gene') #基因总结查询
parser.add_argument('sampleType')  # 正常--癌症
parser.add_argument('FC')  # Fold change cutoff
parser.add_argument('PV')  # Pvalue cutoff
parser.add_argument('methods')  # Limma, edgR, deseq2
parser.add_argument('dataType')  # TCGA, TCGA-GTEx
parser.add_argument('dataset') #数据集
parser.add_argument('corr_sample') #相关性样本
parser.add_argument('nr')  # 正常的样本数目
parser.add_argument('tr')  # 肿瘤样本数目
parser.add_argument('mt')  # 热图里的聚类方法
parser.add_argument('gene_name')  # 用来画盒须图的基因名
parser.add_argument('data_path')  # 热图数据
parser.add_argument('gene_list')  # 用来话热图的基因名
parser.add_argument('data_path1')  # 生存分析数据
parser.add_argument('data_path2')  # 生存分析数据2
parser.add_argument('colorH')  # 生存分析颜色
parser.add_argument('colorL')  # 生存分析颜色
parser.add_argument('cut')  # 生存分析分组位置
parser.add_argument('confidence')  # 生存分析置信区间
parser.add_argument('risk')  # 生存分析风险表格
parser.add_argument('time')  # 生存分析时间单位
parser.add_argument('title1')  # 生存分析图标题1
parser.add_argument('title2')  # 生存分析图标题2


class ArticleSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Article


class TargetSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Browse


class DetailSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Detail


class GenesSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Genes


class ArticleList(Resource):
    def get(self, offset):
        offset = offset if offset else 1
        start = 10 * (int(offset) - 1)
        end = 10 * int(offset)
        get_art = Article.query.filter(Article.id >= start, Article.id <= end)
        art_schema = ArticleSchema(many=True)
        artics = art_schema.dump(get_art)
        return {"articles": artics}


class ArticleOne(Resource):
    def post(self):
        args = parser.parse_args()
        ident = args['id']
        get_art = Article.query.filter(Article.id == ident)
        art_schema = ArticleSchema(many=True)
        artic = art_schema.dump(get_art)
        return {"article": artic}


class Total(Resource):
    def get(self):
        tot = len(Article.query.all())
        return {"Total": tot}


class ArticleSome(Resource):
    def post(self):
        args = parser.parse_args()
        target = args['target']
        get_art = Article.query.filter(Article.target == target)
        total = len(get_art.all())
        art_page = PageCreate(get_art, 10)
        art_schema = ArticleSchema(many=True)
        artics = art_schema.dump(art_page.items)
        return {"articles": artics, "Total": total}

class Gene(Resource):
    def post(self):
        args = parser.parse_args()
        gene1 = args['gene']
        get_gene = Genes.query.filter(Genes.gene_name == gene1)
        gene_schema = GenesSchema(many=True)
        gene = gene_schema.dump(get_gene)
        return {"gene": gene}

class TargetList(Resource):
    def get(self):
        get_tar = Browse.query.filter()
        tar_schema = TargetSchema(many=True)
        targets = tar_schema.dump(get_tar)
        return {"targets": targets}

    def post(self):
        args = parser.parse_args()
        tar = args['target']
        get_tar = Detail.query.filter(Detail.target == tar)
        tar_schema = DetailSchema(many=True)
        target = tar_schema.dump(get_tar)
        return {"target": target}



class Analyse(Resource):
    def post(self):
        args = parser.parse_args()
        dataset = args['dataset']
        sampleType = args['sampleType']
        FC = float(args['FC'])
        PV = float(args['PV'])
        methods = args['methods']
        dataType = args['dataType']
        nr = args['nr']
        tr = args['tr']
        mt = args['mt']
        # dataPath = 'analyzeData'+'/'+dataset+'volcano/' + methods + '/' + dataType + '_' + sampleType + '_' + methods + '.csv'
        # heatPath = 'analyzeData/heatmap/' + dataType + '_' + sampleType + '.csv'
        dataPath = 'analyzeData'+ '/' + dataset + '/volcano/' + methods + '/' + sampleType  + '.csv'
        heatPath = 'analyzeData' + '/' + dataset + '/heatmap/' + sampleType + '.csv'
        up, down, volcanoString, resList,up_list, down_list, nor_list= Volcano(dataPath, FC, PV)
        heatmapString = Heatmap(dataPath, heatPath, FC, PV, nr, tr, mt)
        return {'up': str(up), 'down': str(down), 'volcano': volcanoString, 'heatmap': heatmapString, 'matrix': resList,'up_list':up_list,'down_list':down_list,'nor_list':nor_list}

class Vocano2(Resource):
    def post(self):
        args = parser.parse_args()
        dataset = args['dataset']
        sampleType = args['sampleType']
        FC = float(args['FC'])
        PV = float(args['PV'])
        methods = args['methods']
        dataType = args['dataType']
        nr = args['nr']
        tr = args['tr']
        mt = args['mt']
        dataPath = 'analyzeData'+ '/' + dataset + '/volcano/' + methods + '/' + sampleType  + '.csv'
        up, down, resList, up_list, down_list, nor_list = Volcano2(dataPath, FC, PV)
        return {'up': str(up), 'down': str(down), 'matrix': resList,'up_list':up_list,'down_list':down_list,'nor_list':nor_list}


class Boxplot(Resource):
    def post(self):
        args = parser.parse_args()
        gene = args['gene_name']
        dir = 'analyzeData/boxplot'
        data_list = os.listdir(dir)
        print(data_list)
        res = []
        for file in data_list:
            data = pd.read_csv(dir + '/' + file, index_col='gene_name')
            if gene in data.index:
                tmp = list(data.loc[gene, :].astype(float).values)
                res.append(tmp)
            else:
                res.append([])
        return {'data': json.dumps(res)}

class Boxplot2(Resource):
    def post(self):
        args = parser.parse_args()
        gene = args['gene_name']
        dataset = args['dataset']
        dir = 'analyzeData/'+dataset +'/boxplot'
        data_list = os.listdir(dir)
        print(data_list)
        res = []
        for file in data_list:
            data = pd.read_csv(dir + '/' + file, index_col='gene_name')
            if gene in data.index:
                tmp = list(data.loc[gene, :].astype(float).values)
                res.append(tmp)
            else:
                res.append([])
        return {'data': json.dumps(res)}


class GeneHeatMap(Resource):
    def post(self):
        args = parser.parse_args()
        dataset = args['dataset']
        sampleType = args['sampleType']
        dir = 'analyzeData' + '/' + dataset + '/heatmap/' + sampleType + '.csv'
        gene_list = args['gene_list']
        nr = args['nr']
        tr = args['tr']
        res = Heatmap2(dir, gene_list, nr, tr)
        return {'res': res}


class Correlation2(Resource):
    def post(self):
        args = parser.parse_args()
        corr_sample = args['corr_sample']
        dataset = args['dataset']
        # data_path = args['data_path']
        path = 'analyzeData' + '/' + dataset + '/correlation/' + corr_sample + '.csv'
        # path = 'analyzeData/correlation/' + data_path
        gene_str = args['gene_list']
        method = args['methods']
        res = Correlation(path, gene_str, method)
        return res

class Cor_deff_List(Resource):
    def get(self):
        data_path = 'analyzeData/genes_deff8.csv'
        co1_list, co2_list, co3_list, co4_list = cor_deff(data_path)
        return {"co1_list": co1_list,"co2_list": co2_list,"co3_list": co3_list,"co4_list": co4_list}

class Cor_deff_List2(Resource):
    def get(self):
        data_path = 'analyzeData/genes_deff8.csv'
        gene,log2FC1,log2FC2,log2FC3,log2FC4,log2FC5 = cor_deff2(data_path)
        return {"gene":gene,"log2FC1":log2FC1,"log2FC2":log2FC2,"log2FC3":log2FC3,"log2FC4":log2FC4,"log2FC5":log2FC5}
# 增加单细胞
class cell_cluster(Resource):
    def get(self):
        data_path = 'analyzeData/cell.csv'
        tumor_list,nk_list,endo_list,mye_list,tcell_list, hsc_list,bcell_list, pdc_list,Plasma_list,Epi_list = cellCluster(data_path)
        return {"tumor_list":tumor_list,"nk_list":nk_list,"mye_list":mye_list,"tcell_list":tcell_list,"hsc_list":hsc_list,"bcell_list":bcell_list,
                "pdc_list":pdc_list,"Plasma_list":Plasma_list,"Epi_list":Epi_list}

class cell_cluster2(Resource):
    def post(self):
        args = parser.parse_args()
        gene_name = args['gene_name']
        #cluster_type = args['cluster_type']
        data_path = 'analyzeData/cellExp.csv'
        data = cell(data_path)
        normal_list, primary_list, replased_list = cell_exp(data,gene_name)

        return {"normal_list":normal_list,"primary_list":primary_list,"replased_list":replased_list,}
class cell_cluster_Meta(Resource):
    def post(self):
        args = parser.parse_args()
        gene_name = args['gene_name']
        #cluster_type = args['cluster_type']
        data_path = 'analyzeData/cell_Meta.csv'
        data = cellMata(data_path)
        meta_list = cell_Meta(data,gene_name)

        return {"meta_list":meta_list}
class Survival(Resource):
    def post(self):
        args = parser.parse_args()
        dataset = args['dataset']
        path1 = args['data_path1']
        survival_path1 = 'analyzeData/Survival/'+dataset+'/'+path1
        path2 = args['data_path2']
        survival_path2 = 'analyzeData/Survival/'+dataset+'/'+path2
        genname = args['gene_name']
        Num1 = args['nr']
        Num2 = args['tr']
        colorH = args['colorH']
        colorL = args['colorL']
        cut = args['cut']
        confidence = args['confidence']
        risk = args['risk']
        time = args['time']
        title1 = args['title1']
        title2 = args['title2']
        p1, pic1String = survival_analyze1(survival_path1, genname, Num1, colorH, colorL, cut, confidence, risk, time,
                                           title1)
        p2, pic2String = survival_analyze2(survival_path2, genname, Num2, colorH, colorL, cut, confidence, risk, time,
                                           title2)
        return {'p1': p1, 'p2': p2, 'pic1': pic1String, 'pic2': pic2String}


api.add_resource(Total, '/api/ldb/Total')
api.add_resource(ArticleList, '/api/ldb/Articles/<offset>')
api.add_resource(ArticleOne, '/api/ldb/Article')
api.add_resource(ArticleSome, '/api/ldb/TarArt')
api.add_resource(TargetList, '/api/ldb/Targets')
api.add_resource(Analyse, '/api/ldb/Analyse')
api.add_resource(Boxplot, '/api/ldb/Boxplot')
api.add_resource(GeneHeatMap, '/api/ldb/Heatmap')
api.add_resource(Correlation2, '/api/ldb/Correlation')
api.add_resource(Survival, '/api/ldb/Survival')
api.add_resource(Gene, '/api/ldb/Gene')
api.add_resource(Vocano2, '/api/ldb/Vocano2')
# api.add_resource(Cor_deff_List, '/api/ldb/CorDeff')
api.add_resource(Cor_deff_List2, '/api/ldb/CorDeff2')
# api.add_resource(cell_cluster, '/api/ldb/cellCluster')
api.add_resource(cell_cluster2, '/api/ldb/cellCluster2')
api.add_resource(cell_cluster_Meta, '/api/ldb/cell_cluster_Meta')
if __name__ == '__main__':
    app.run()
