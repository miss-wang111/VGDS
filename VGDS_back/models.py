from exts import db

"""
下面是数据库中表的定义 增加
"""


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True, unique=True)
    target = db.Column(db.String(20), comment='靶点基因')
    article_num = db.Column(db.Integer, comment='文献数量')
    pmid = db.Column(db.String(15), comment='pmid')
    title = db.Column(db.Text, comment='标题')
    abstract = db.Column(db.Text, comment='摘要')


class Browse(db.Model):
    __tablename__ = 'browse'
    ldb_id = db.Column(db.String(15), comment='LDB_id')
    target = db.Column(db.String(20), primary_key=True, unique=True, comment='靶点基因')
    description = db.Column(db.Text, comment='靶点描述')
    tag = db.Column(db.Integer, comment='靶点的标签')


class Detail(db.Model):
    __tablename__ = 'detail'
    target = db.Column(db.String(20), primary_key=True, unique=True, comment='靶点基因')
    description = db.Column(db.Text, comment='靶点描述')
    alias = db.Column(db.String(300), comment='别名')
    ncbi_id = db.Column(db.String(20))
    summary = db.Column(db.Text, comment='总结')
    tag = db.Column(db.Integer, comment='靶点的标签')
    drugs = db.Column(db.String(100), comment='针对靶点的相关药物')
    article_num = db.Column(db.Integer, comment='文献数量')


class Genes(db.Model):
    __tablename__ = 'genes'
    gene_name = db.Column(db.String(20), primary_key=True, unique=True, comment='基因')
    ncbi_id = db.Column(db.String(20))
    Description = db.Column(db.Text, comment='靶点描述')
    Alias = db.Column(db.String(300), comment='别名')
    Summary = db.Column(db.Text, comment='总结1')
    tag = db.Column(db.Integer, comment='靶点的标签')
    Drugs = db.Column(db.String(100), comment='针对靶点的相关药物')
    Log2FC1 = db.Column(db.String(20), comment='复发VS非复发')
    Log2FC2 = db.Column(db.String(20), comment='复发VS邻近')
    Log2FC3 = db.Column(db.String(20), comment='复发VS原发')
    Log2FC4 = db.Column(db.String(20), comment='非复发VS邻近')
    Log2FC5 = db.Column(db.String(20), comment='肿瘤VS邻近')
    Article_num = db.Column(db.Integer, comment='文献数量')