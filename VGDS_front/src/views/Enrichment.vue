<template>
  <div>
    <v-container>
      <v-row>
        <v-col cols="8">
          <div class="d-flex justify-left">
            <h2 style="color:#6D819C " class="mt-n3 pt-3 pb-0 mb-0"> KEGG enrichment Analysis</h2>
          </div>
        </v-col>
      </v-row>
      <v-row>
        <v-col cols="8">
          <div class="d-flex justify-left">
            <v-divider class="mt-n4 pt-0 pb-2 "></v-divider>
          </div>
        </v-col>
      </v-row>
      <p style="color:#6D819C " class="d-flex justify-left ">In this page, You can do differential expression analysis for liver cancer </p>
      <v-card
        class="mt-4"
        height="200">
        <v-row>
          <v-col cols="4">
            <div class="pr-2 ml-5">
              <p class="textSmall d-flex justify-left">|Log2FC| Cutoff:</p>
              <v-text-field
                style="zoom:80%"
                dense
                placeholder="1"
                outlined
                color="#55967e"
                v-model="fc"
              ></v-text-field>
            </div>
            <div class="pr-2 ml-5">
              <p class="textSmall d-flex justify-left">KEGG-p-value cutoff</p>
              <v-text-field
                style="zoom:80%"
                dense
                placeholder="1"
                outlined
                color="#55967e"
                v-model="fc"
              ></v-text-field>
            </div>
          </v-col>
          <v-col cols="4">
            <div class="pr-2 ml-5">
              <p class="textSmall d-flex justify-left">p-value Cutoff:</p>
              <v-text-field
                style="zoom:80%"
                dense
                placeholder="1"
                outlined
                color="#55967e"
                v-model="fc"
              ></v-text-field>
            </div>
            <div class="pr-2 ml-5">
              <p class="textSmall d-flex justify-left">KEGG-FDR Cutoff:</p>
              <v-text-field
                style="zoom:80%"
                dense
                placeholder="1"
                outlined
                color="#55967e"
                v-model="fc"
              ></v-text-field>
            </div>
          </v-col>
          <v-col cols="4">
            <div class="pr-2 ml-5">
              <p class="textSmall d-flex justify-left">Dysregulation type:</p>
              <v-text-field
                style="zoom:80%"
                dense
                placeholder="1"
                outlined
                color="#55967e"
                v-model="fc"
              ></v-text-field>
            </div>
            <div class="d-flex ml-5">
              <v-btn color="#55967e"
                     dark
                     class="d-flex "
                     small
                     @click.stop=Analyze()>
                Analyze
              </v-btn>
            </div>
          </v-col>

        </v-row>
      </v-card>
      <v-progress-linear
        v-if = "linear===true"
        class ="d-flex mt-0 pt--0 "
        indeterminate
        color="#55967e"
      ></v-progress-linear>
      <div v-if="list===true">
        <v-card class="mt-5">
          <div class="d-flex justify-space-between ">
            <h3 class="ml-8 mt-3">{{methodp}} Analysis Results</h3>
            <v-btn
              icon
              large
              color="#55967e"
              @click="handleDownloadQrIMg(volcano_base64) , handleDownloadQrIMg(heatmap_base64)"
            ><v-icon>mdi-download</v-icon></v-btn>
          </div>
          <v-row>
            <v-col cols="12" class="mt-5 ">
              <v-divider></v-divider>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="6">
              <div class="d-flex justify-start ">
                <p class="ml-8 " >over-expressed genes:{{up}}</p>
              </div>
              <div class="d-flex justify-start ">
                <p class="ml-8  mb-14">under-expressed genes:{{down}}</p>
              </div>
              <v-img :src="volcano" ></v-img>
            </v-col>
            <v-col cols="6" class="pt-1">
              <v-img :src="heatmap" ></v-img>
            </v-col>
          </v-row>
        </v-card>
        <v-card  class="mt-10" flat>
          <v-card-title>
            Differential Genes
            <v-spacer></v-spacer>
            <v-text-field
              v-model="search"
              append-icon="mdi-magnify"
              label="Search"
              single-line
              hide-details
            ></v-text-field>
          </v-card-title>
          <v-row>
            <v-col cols="2" class="pr-0 pl-3">
              <v-card
                class="overflow-y-auto"
                outlined
                height="380px"
              >
                <v-row
                  align="center"
                  justify="start"
                >
                  <v-col v-for="(selection, i) in AnalyzeArray" :key = "i"
                         class="shrink pl-5 mt-1"
                  >
                    <v-chip
                      close
                      small
                      color="#546E7A"
                      outlined
                      @click:close=" AnalyzeArray.splice(i, 1)"
                    >
                      {{ selection }}
                    </v-chip>
                  </v-col>
                </v-row>
              </v-card>
              <p class="d-flex ml-2">selected:{{AnalyzeArray.length}}</p>
              <v-btn-toggle
                color="#55967e"
                rounded
              >
                <v-tooltip bottom>
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn
                      small
                      color="#55967e"
                      v-bind="attrs"
                      v-on="on"
                      @click="geneHeatmap"
                    > <v-icon>mdi-tune-vertical</v-icon></v-btn>
                  </template>
                  <span>Let's draw a cluster heat map</span>
                </v-tooltip>
                <v-tooltip bottom>
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn
                      small
                      color="#55967e"
                      v-bind="attrs"
                      v-on="on"
                      @click="toCorrelation"
                    > <v-icon>mdi-transit-detour</v-icon></v-btn>
                  </template>
                  <span>Do a correlation analysis</span>
                </v-tooltip>
                <v-tooltip bottom>
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn
                      small
                      color="#55967e"
                      v-bind="attrs"
                      v-on="on"
                      @click="toSurvival"
                    ><v-icon>mdi-run</v-icon></v-btn>
                  </template>
                  <span>To do a survival analysis</span>
                </v-tooltip>
              </v-btn-toggle>
            </v-col>
            <v-col cols="10">
              <template
              >
                <v-data-table
                  dense
                  :headers="headers"
                  :items="datas"
                  :items-per-page="10"
                  :search="search"
                  class="elevation-1 "
                >
                  <template v-slot:item.sig="{ item }">
                    <v-chip small dark :color="getColor(item.sig)" ></v-chip>
                  </template>
                  <template v-slot:item.gene_name="{item}">
                    <v-btn
                      text
                      color="#55967e"
                      @click.stop=getBoxplotData(item.gene_name)
                    >{{item.gene_name}}</v-btn>
                  </template>
                  <template v-slot:item.add="{ item }">
                    <div v-if="!AnalyzeArray.includes(item.gene_name)">
                      <v-btn
                        small
                        icon
                        color="#55967e"
                        @click.stop="AddAnalyzeArray(item.gene_name,item.sig)"
                      ><v-icon>mdi-plus-circle</v-icon></v-btn>
                    </div>
                    <div v-else>
                      <v-btn
                        small
                        icon
                        color="blue-grey"
                      ><v-icon>mdi-plus-circle</v-icon></v-btn>
                    </div>
                  </template>
                </v-data-table>
              </template>
            </v-col>
          </v-row>
        </v-card>
      </div>
      <v-progress-linear
        v-if = "boxLinear===true"
        class ="d-flex mt-0 pt--0 "
        indeterminate
        color="#55967e"
      ></v-progress-linear>
      <v-card
        class = "mt-10"
        v-if="boxDate===true">
        <v-row>
          <v-col cols="3"
                 class="pr-0 pb-0 pt-0">
            <v-card
              flat
              @click="initChart1()">
              <template>
                <!--创建一个echarts的容器-->
                <div id="box1" style="width:100%; height:250px"></div>
              </template>
            </v-card>
          </v-col>
          <v-col cols="3"
                 class="pa-0">
            <v-card
              flat
              @click="initChart2()"
            >
              <template>
                <!--创建一个echarts的容器-->
                <div id="box2" style="width:100%; height:250px"></div>
              </template>
            </v-card>
          </v-col>
          <v-col cols="3"
                 class="pa-0">
            <v-card
              flat
              @click="initChart3()"
            >
              <template>
                <!--创建一个echarts的容器-->
                <div id="box3" style="width:100%; height:250px"></div>
              </template>
            </v-card>
          </v-col>
          <v-col cols="3"
                 class="pt-0 pb-0 pl-0">
            <v-card
              flat
              @click="initChart4()"
            >
              <template>
                <!--创建一个echarts的容器-->
                <div id="box4" style="width:100%; height:250px"></div>
              </template>
            </v-card>
          </v-col>
        </v-row>
      </v-card>
      <v-card>
        <div id="main" style="width: 800px;height:800px;"></div>
      </v-card>
    </v-container>
  </div>

</template>

<script>
const echarts = require('echarts')
export default {
  name: 'Echarts',
  data () {
    return {
      token: ''
    }
  },
  methods: {
    myEcharts () {
      var myChart = echarts.init(
        document.getElementById('main')
      )
      var links = [
        { target: 'ALDOC', source: 'Glycolysis / Gluconeogenesis' },
        { target: 'ENO2', source: 'Glycolysis / Gluconeogenesis' },
        { target: 'HK2', source: 'Glycolysis / Gluconeogenesis' },
        { target: 'PFKL', source: 'Glycolysis / Gluconeogenesis' },
        { target: 'ALDOC', source: 'Fructose and mannose metabolism' },
        { target: 'HK2', source: 'Fructose and mannose metabolism' },
        { target: 'MPI', source: 'Fructose and mannose metabolism' },
        { target: 'PFKFB3', source: 'Fructose and mannose metabolism' },
        { target: 'PFKFB4', source: 'Fructose and mannose metabolism' },
        { target: 'PFKL', source: 'Fructose and mannose metabolism' },
        { target: 'GBE1', source: 'Starch and sucrose metabolism' },
        { target: 'GYS1', source: 'Starch and sucrose metabolism' },
        { target: 'HK2', source: 'Starch and sucrose metabolism' },
        { target: 'AK4', source: 'Metabolic pathways' },
        { target: 'ALDOC', source: 'Metabolic pathways' },
        { target: 'BCKDHA', source: 'Metabolic pathways' },
        { target: 'ENO2', source: 'Metabolic pathways' },
        { target: 'GBE1', source: 'Metabolic pathways' },
        { target: 'HK2', source: 'Metabolic pathways' },
        { target: 'IPMK', source: 'Metabolic pathways' },
        { target: 'KYNU', source: 'Metabolic pathways' },
        { target: 'MPI', source: 'Metabolic pathways' },
        { target: 'P4HA1', source: 'Metabolic pathways' },
        { target: 'PFKL', source: 'Metabolic pathways' },
        { target: 'PTGES', source: 'Metabolic pathways' },
        { target: 'RDH10', source: 'Metabolic pathways' },
        { target: 'RIMKLA', source: 'Metabolic pathways' },
        { target: 'AK4', source: 'Biosynthesis of antibiotics' },
        { target: 'ALDOC', source: 'Biosynthesis of antibiotics' },
        { target: 'BCKDHA', source: 'Biosynthesis of antibiotics' },
        { target: 'ENO2', source: 'Biosynthesis of antibiotics' },
        { target: 'PFKL', source: 'Biosynthesis of antibiotics' },
        { target: 'HK2', source: 'Biosynthesis of antibiotics' },
        { target: 'ALDOC', source: 'Carbon metabolism' },
        { target: 'ENO2', source: 'Carbon metabolism' },
        { target: 'HK2', source: 'Carbon metabolism' },
        { target: 'PFKL', source: 'Carbon metabolism' }

      ]
      //  数据
      var datas = [
        { category: '基因', name: 'AK4', logFC: 2.553953833 },
        { category: '基因', name: 'ALDOC', logFC: 4.706364833 },
        { category: '基因', name: 'BCKDHA', logFC: 1.011662778 },
        { category: '基因', name: 'EGLN1', logFC: 1.736573611 },
        { category: '基因', name: 'EGLN3', logFC: 2.217054278 },
        { category: '基因', name: 'ENO2', logFC: 2.121238333 },
        { category: '基因', name: 'GBE1', logFC: 1.253053 },
        { category: '基因', name: 'GYS1', logFC: 1.612489556 },
        { category: '基因', name: 'HIF1A', logFC: -1.297995944 },
        { category: '基因', name: 'HK2', logFC: 2.396326222 },
        { category: '基因', name: 'IPMK', logFC: 1.065951 },
        { category: '基因', name: 'KYNU', logFC: -1.076542611 },
        { category: '基因', name: 'MPI', logFC: 1.072411556 },
        { category: '基因', name: 'P4HA1', logFC: 2.371185167 },
        { category: '基因', name: 'PDK1', logFC: 2.777550611 },
        { category: '基因', name: 'PFKFB3', logFC: 2.203315389 },
        { category: '基因', name: 'PFKFB4', logFC: 4.298310278 },
        { category: '基因', name: 'PFKL', logFC: 1.086148611 },
        { category: '基因', name: 'PPP1R3B', logFC: 1.409372056 },
        { category: '基因', name: 'PPP1R3C', logFC: 1.171660889 },
        { category: '基因', name: 'PTGES', logFC: -1.374651556 },
        { category: '基因', name: 'RDH10', logFC: -1.104499889 },
        { category: '基因', name: 'RIMKLA', logFC: 1.292232667 },
        { category: '基因', name: 'SLC2A1', logFC: 1.445802389 },
        { category: '基因', name: 'TFRC', logFC: -1.109742222 },
        { category: 'Glycolysis / Gluconeogenesis', name: 'Glycolysis / Gluconeogenesis' },
        { category: 'Fructose and mannose metabolism', name: 'Fructose and mannose metabolism' },
        { category: 'Starch and sucrose metabolism', name: 'Starch and sucrose metabolism' },
        { category: 'Metabolic pathways', name: 'Metabolic pathways' },
        { category: 'Biosynthesis of antibiotics', name: 'Biosynthesis of antibiotics' },
        { category: 'Carbon metabolism', name: 'Carbon metabolism' }
      ]
      // 分类集合
      var categories = [
        { name: '基因' },
        { name: 'Glycolysis / Gluconeogenesis' },
        { name: 'Fructose and mannose metabolism' },
        { name: 'Starch and sucrose metabolism' },
        { name: 'Metabolic pathways' },
        { name: 'Biosynthesis of antibiotics' },
        { name: 'Carbon metabolism' }
      ]

      // 增加value和symbolSize属性，且设置通路不做渐变
      datas.forEach((value, index) => {
        if (value.category !== '基因') {
          value.symbolSize = 20
          // 通路不做渐变
          value.visualMap = false
        } else {
          value.value = value.logFC
          value.symbolSize = 10
        }
      })

      // 按照value值排序，并展示有value值的名字
      datas.sort(function (a, b) {
        return a.value - b.value
      }).forEach(function (node) {
        node.label = {
          show: node.value != null
        }
      })

      // 配置项
      var option = {
        animationDurationUpdate: 1500,
        animationEasingUpdate: 'quinticInOut',
        tooltip: {
          show: true
        },
        title: {
          text: 'GO Terms',
          left: 'left',
          bottom: '10px',
          textStyle: {
            fontSize: 14
          }
        },

        // 图例设置
        legend: [{
          orient: 'horizontal',
          // 这个是下面种类的形状；正方形
          icon: 'square',
          // 位置
          left: '10%',
          top: 'bottom',

          width: '80%',
          textStyle: {
            fontSize: 10
          },
          // 图例内容，由上面的分类集合决定，舍去基因
          data: categories.map(function (a) {
            if (a.name !== '基因') {
              return a.name
            }
          })
        }],

        // 让基因按照它们的logFC来进行颜色渐变
        visualMap: { // visualMap 是视觉映射组件，用于进行『视觉编码』，也就是将数据映射到视觉元素（视觉通道）。
          show: true, // 是否显示组件
          type: 'continuous',
          max: 4, // 指定 visualMapContinuous 组件的允许的最大值
          min: -3,
          reeltime: true,
          itemHeight: 140,
          itemWidth: 20,
          right: 'right',
          top: 'bottom',
          width: '20%',
          orient: 'horizontal',
          text: ['4', '-3'], // 两端的文本，如 ['High', 'Low']
          inRange: { // 定义 在选中范围中 的视觉元素。
            color: ['#3b84f4', '#96b8eb', '#b6cef1', 'white', '#ea5348', '#fc230f']// 图元的颜色。
          }
        },

        // 数据设置
        series: [{
          // 类型
          type: 'graph',

          layout: 'circular',
          focusNodeAdjacency: true,
          // 开启平移与缩放
          roam: true,
          // 让每个节点的标签居于上方且不会遮挡住图标
          circular: {
            rotateLabel: true
          },
          draggable: true,
          data: datas,
          categories: categories,
          // 连线
          edges: links.map(function (edge) {
            return {
              source: edge.source,
              target: edge.target
            }
          }),
          // 改变结点形状
          symbol: 'pin',
          emphasis: {
            focus: 'adjacency',
            label: {
              position: 'left,top',
              show: true
            }
          },

          // 标签设置
          label: {
            show: true,
            position: 'left',
            formatter: '{b}',
            fontSize: '10px'

          },

          // 线条颜色和大小设置
          lineStyle: {
            width: 3,
            curveness: 0.3,
            opacity: 1,
            color: 'source'
          },

          // 给节点加边框
          itemStyle: {
            borderColor: '#666',
            borderWidth: 0.1
          }
        }]
      }
      myChart.setOption(option)
    },
    Analyze () {
      this.token = this.GLOBAL.Dataset[0].Dataset_Num
      alert(this.token)
    }
  },
  mounted () {
    this.myEcharts()
  }
}
</script>

<style>

</style>
