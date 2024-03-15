<template>
  <div class="ml-5 mr-5">
    <v-container>
      <div></div>
      <v-row>
        <v-col cols="8">
          <div class="d-flex justify-left">
            <h2 style="color:#6D819C " class="mt-n3 pt-3 pb-0 mb-0"> Differential Expression Analysis</h2>
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
      <p style="color:#6D819C " class="d-flex justify-left ">In this page, You can do differential expression analysis for {{GLOBAL.Dataset[0].Dataset_Num}} </p>
<!--      <v-row>
        <v-col cols="12">
          <v-card
            height="100">
            <div class="d-flex justify-space-between">
              <h3 style="color:#6D819C " class="d-flex mt-3 ml-3 mb-n2 textSmall">Choose Sampleset </h3>
              <v-btn
                icon
                justify-space-between
                color="#55967e"
                @click="table_out=!table_out">
                <v-icon
                large>mdi-menu-down</v-icon>
                </v-btn>
            </div>
            <v-radio-group
              row
              class="ml-5 "
              style="zoom:85%"
              v-model="dataset">
              <v-radio
                v-for="item in daatasets"
                :label="item"
                :key="item"
                :value="item"
                color="#55967e"
              ></v-radio>
            </v-radio-group>
          </v-card>
        </v-col>
      </v-row>
      <v-row v-if="table_out">
        <v-col cols="12">
          <datatable></datatable>
        </v-col>
      </v-row>-->
      <v-card
        class="mt-4"
        height="200">
        <v-row>
          <v-col cols="4">
            <div class="pr-2 ml-5">
              <p class="d-flex justify-left textSmall">Sample Data </p>
              <v-select
                style="transform: scale(0.9)"
                class="d-flex justify-left pb-0"
                :items="sampleType1"
                solo
                flat
                dense
                outlined
                color="#55967e"
                v-model="Sample"
              ></v-select>
            </div>
            <v-row>
              <v-col cols="6">
                <p class="textSmall">|Log2FC| Cutoff:</p>
                  <v-text-field
                    style="zoom:80%"
                    class="d-flex pl-6 ml-3"
                    dense
                    placeholder="1"
                    outlined
                    color="#55967e"
                    v-model="fc"
                  ></v-text-field>
              </v-col>
              <v-col cols="6">
                <p class="textSmall">p-value|Cutoff:</p>
                <v-text-field
                  style="zoom:80%"
                  class="d-flex pl-6 ml-3"
                  v-model="p"
                  outlined
                  dense
                  color="#55967e"
                ></v-text-field>
              </v-col>
            </v-row>
          </v-col>
          <v-col cols="4">
            <p class="d-flex textSmall">Differential Methods</p>
            <v-radio-group dense
                           style="zoom:80%"
                           v-model="methodp">
              <v-radio
                v-for="item in Method"
                :label="item"
                :key="item"
                :value="item"
                color="#55967e"
              ></v-radio>
            </v-radio-group>
            <p class="d-flex textExp">Choose a method to analyze the sample</p>
          </v-col>
          <v-col cols="4">
            <p class="d-flex justify-left textSmall">Clustering Method</p>
            <v-radio-group  dense
                            row
                            style="zoom:80%"
                           v-model="clustering_method ">
              <v-radio
                v-for="item in Clustering_method"
                :label="item"
                :key="item"
                :value="item"
                color="#55967e"
              ></v-radio>
            </v-radio-group>
            <p class="d-flex justify-left textExp">Choose a method to draw a heat map</p>
            <div class="d-flex ml-5">
              <v-btn color="#55967e"
                     dark
                     class="d-flex "
                     small
                     @click.stop=getData(),changeChoice>
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
               <p class="ml-8  mb-1">under-expressed genes:{{down}}</p>
              </div>
<!--              <div class="Echarts" id="preVol" style="width: 100%;height:100%;">
                <div id="volcono" style="width: 100%;height:100%;"></div>
              </div>-->
              <div class="Echarts" id="preVol">
                <div id="volcono" style="width: 100%;height:100%;"></div>
              </div>
<!--              <v-img :src="volcano" ></v-img>-->
            </v-col>
            <v-col cols="6" class="pt-1">
              <div>
                <v-img :src="heatmap"></v-img>
              </div>
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
      <v-dialog
        v-model="dialog1"
        width="600"
      >
        <v-card class="pt-10" >
          <template>
            <!--创建一个echarts的容器-->
            <div id="bigbox1" style="width:500px; height:500px"></div>
          </template>
            <v-btn
              color="primary"
              text
              @click="dialog1=false"
            >
              close
            </v-btn>
        </v-card>
      </v-dialog>
      <v-dialog
        v-model="dialog2"
        width="600"
      >
        <v-card class="pt-10" >
          <template>
            <!--创建一个echarts的容器-->
            <div id="bigbox2" style="width:500px; height:500px"></div>
          </template>
          <v-btn
            color="primary"
            text
            @click="dialog2=false"
          >
            close
          </v-btn>
        </v-card>
      </v-dialog>
      <v-dialog
        v-model="dialog3"
        width="600"
      >
        <v-card class="pt-10" >
          <template>
            <!--创建一个echarts的容器-->
            <div id="bigbox3" style="width:500px; height:500px"></div>
          </template>
          <v-btn
            color="primary"
            text
            @click="dialog3=false"
          >
            close
          </v-btn>
        </v-card>
      </v-dialog>
      <v-dialog
        v-model="dialog4"
        width="600"
      >
        <v-card class="pt-10" >
          <template>
            <!--创建一个echarts的容器-->
            <div id="bigbox4" style="width:500px; height:500px"></div>
          </template>
          <v-btn
            color="primary"
            text
            @click="dialog4=false"
          >
            close
          </v-btn>
        </v-card>
      </v-dialog>
      <v-dialog
        v-model="dialog5"
        max-width="600"
        height="650"
      >
        <v-card class="pt-0"
                max-width="600"
                height="650"
                v-if = "boxLinear1===true">
          <v-progress-linear
            class ="d-flex mt-0 pt--0 "
            indeterminate
            color="#55967e"
          ></v-progress-linear>
        </v-card>
        <v-card class="pt-2 overflow-y-auto"
                max-width="600"
                height="650"
                v-else>
          <div class="d-flex">
            <div>
              <v-btn
                icon
                color="#55967e"
                @click="handleDownloadQrIMg(heatmap_base64)"
              ><v-icon>mdi-download</v-icon></v-btn>
            </div>
            <div class="ml-auto">
              <v-btn
                icon
                color="#55967e"
                @click="dialog5=false"
              ><v-icon>mdi-close</v-icon></v-btn>
            </div>
          </div>
          <v-img :src="heatmap1" ></v-img>
        </v-card>
      </v-dialog>
    </v-container>
  </div>
</template>
<script>
import axios from 'axios'
var echarts = require('echarts')

export default {
  data () {
    return {
      // table_out: false,
      // daatasets: ['HCCMRDB1', 'HCCMRDB2', 'HCCMRDB3', 'HCCMRDB4', 'HCCMRDB5', 'HCCMRDB6', 'HCCMRDB7', 'HCCMRDB8', 'HCCMRDB9', 'HCCMRDB10'],
      sampleType1: ['TCGA_Normal——Tumour', 'TCGA_GTEx_Normal——Tumour', 'Metastasis--Non-metastatic', 'Recurrence--Non-recurrence'],
      Method: ['LIMMA', 'edgR', 'DESeq2'],
      dataType: ['TCGA', 'TCGA-GTEx'],
      Clustering_method: ['average', 'median', 'complete'],
      // dataset: 'HCCMRDB1',
      methodp: 'LIMMA',
      clustering_method: 'average',
      dataT: '',
      Sample: '',
      Sample1: 'NT',
      Sample0: '',
      Sample3: '',
      fc: 1,
      p: 0.1,
      up: '',
      down: '',
      volcano: '',
      volcano_base64: '',
      heatmap: '',
      heatmap_base64: '',
      heatmap1: '',
      sig: '',
      dialog1: false,
      dialog2: false,
      dialog3: false,
      dialog4: false,
      dialog5: false,
      list: false,
      linear: false,
      boxLinear: false,
      boxLinear1: false,
      boxDate: false,
      datas: [],
      AnalyzeArray: [],
      AnalyzeColor: [],
      search: '',
      gen: '',
      gen_name: '',
      gen_sig: '',
      up_list: [],
      down_list: [],
      nor_list: [],
      headers: [
        {
          text: 'Sig',
          value: 'sig'
        },
        {
          text: 'Gene Symbol',
          value: 'gene_name'
        },
        // {
        //   text: 'Median(Normal)',
        //   value: 'median1'
        // },
        // {
        //   text: 'Median(Tumor)',
        //   value: 'median2'
        // },
        {
          text: 'log2FoldChange',
          value: 'log2FoldChange'
        },
        {
          text: 'pvalue',
          value: 'pvalue'
        },
        {
          text: 'Add',
          value: 'add',
          sortable: false
        }
      ],
      nr: 58,
      tr: 407,
      box: [],
      box1: [],
      box2: [],
      box3: [],
      box4: [],
      AnalyzeStr: '',
      screenWidth: null
    }
  },
  methods: {
    getColor (tag) {
      if (tag === 'up') return '#970200'
      else return '#012257'
    },
    // eslint-disable-next-line camelcase
    AddAnalyzeArray: function (gen_name, gen_sig) {
      this.AnalyzeArray.push(gen_name)
      // eslint-disable-next-line camelcase
      if (gen_sig === 'up') {
        this.AnalyzeColor.push('#970200')
      } else {
        this.AnalyzeColor.push('#012257')
      }
      // console.log(this.AnalyzeArray)
    },
    myEcharts () {
      // 基于准备好的dom，初始化echarts实例
      var myChart = this.$echarts.init(document.getElementById('volcono'))
      var up = this.up_list
      var down = this.down_list
      var nor = this.nor_list
      // var temp = myChart.getWidth()
      // console.log(temp)
      const el = document.getElementById('preVol')
      var preWidth = window.getComputedStyle(el).width
      myChart.resize({ width: preWidth, height: preWidth })
      // const el = document.getElementById('preVol')
      // var preWidth = window.getComputedStyle(el).width
      // var preHeight = window.getComputedStyle(el).height
      // console.log(preWidth, preHeight)
      // chart_preHist.resize({width:mWidth, height:mHeight});
      // eslint-disable-next-line no-unused-vars
      var data = this.char_list
      // 指定图表的配置项和数据
      var option = {
        grid: {
          show: true,
          borderWidth: 1,
          borderColor: 'black',
          left: '10%',
          right: '7%',
          bottom: '7%',
          containLabel: true
        },
        tooltip: {
          position: 'top',
          formatter: function (params) {
            var str =
              '类别:' +
              params.seriesName +
              '<br />Gene:' +
              params.data[2] +
              '<br />Log2Foldchange:' +
              params.data[0] +
              '<br />P-value:' +
              Math.pow(10, params.data[1] * -1)
            return str
          }
        },
        xAxis: [
          {
            type: 'value',
            scale: true,
            axisLabel: {
              formatter: '{value}'
            },
            splitLine: {
              show: false
            },
            name: 'LogFoldchange',
            nameLocation: 'middle',
            nameTextStyle: {
              color: 'black',
              fontWeight: 'bolder',
              fontSize: 16,
              padding: 10
            }
          }
        ],
        yAxis: [
          {
            type: 'value',
            scale: false,
            axisLine: { show: false },
            axisTick: { show: false },
            splitLine: {
              show: false
            },
            name: '-log10(pvalue)',
            nameLocation: 'middle',
            nameTextStyle: {
              color: 'black',
              fontWeight: 'bolder',
              fontSize: 16,
              padding: 10
            }
          }
        ],
        color: ['#970200', '#012257', 'grey'],
        dataZoom: [
          {
            type: 'inside',
            xAxisIndex: [0],
            start: 1,
            end: 100
          }],
        legend: {
          data: ['up', 'down', 'normal'],
          top: 20
        },
        series: [
          {
            name: 'up',
            type: 'scatter',
            emphasis: {
              focus: 'series'
            },
            data: up
          },
          {
            name: 'down',
            type: 'scatter',
            emphasis: {
              focus: 'series'
            },
            data: down
          },
          {
            name: 'normal',
            type: 'scatter',
            emphasis: {
              focus: 'series'
            },
            data: nor
          }
        ]
      }

      // 使用刚指定的配置项和数据显示图表。
      myChart.setOption(option)
    },
    getBoxplot2 () {
      axios.post('/api/ldb/BoxplotDB', { gene_name: this.target })
        .then(res => {
          // this.boxplot_num = res.data.data
          // eslint-disable-next-line no-eval
          this.boxplot_num.push(eval(res.data.data))
          this.expr0 = this.boxplot_num[0][0]
          this.expr1 = this.boxplot_num[0][1]
          this.expr2 = this.boxplot_num[0][2]
          this.expr3 = this.boxplot_num[0][3]
          this.expr4 = this.boxplot_num[0][4]
          console.log(this.expr0)
          this.$nextTick(() => {
            this.myEcharts2()
          })
        })
    },
    myEchartsBOX () {
      var myChart = this.$echarts.init(document.getElementById('main'))
      // 指定图表的配置项和数据
      var option
      var data = echarts.dataTool.prepareBoxplotData(this.boxplot_num[0])
      option = {
        title: [{
          text: 'Gene Expression Levels in TCGA HCC Tumor Projects(RNA-Seq)',
          left: 'center',
          textStyle: {
            fontSize: 20,
            color: 'black'
          }
        },
        {
          text: 'upper: Q3 + 1.5 * IRQ \nlower: Q1 - 1.5 * IRQ',
          borderColor: '#999',
          borderWidth: 1,
          textStyle: {
            fontSize: 14
          },
          left: '10%',
          top: '90%'
        }
        ],
        tooltip: {
          trigger: 'item', // 触发类型,数据项图形触发，主要在散点图，饼图等无类目轴的图表中使用。
          axisPointer: { // 指示器类型。
            type: 'shadow'
          }
        },
        grid: { // 直角坐标系网格。
          // show: true,//default: false
          left: '10%',
          right: '10%',
          bottom: '15%'
          // borderWidth: 1,
          // borderColor: '#000',
        },
        xAxis: { // X轴
          type: 'category', // 'category' 类目轴，适用于离散的类目数据，为该类型时必须通过 data 设置类目数据。
          // data: data.axisData,
          data: ['复发', '未复发', '正常', '肿瘤', '转移', '非转移'],
          boundaryGap: true, // 类目轴中 boundaryGap 可以配置为 true 和 false。默认为 true，这时候刻度只是作为分隔线，标签和数据点都会在两个刻度之间的带(band)中间。
          nameGap: 30, // 坐标轴名称与轴线之间的距离。
          splitArea: { // 坐标轴在 grid 区域中的分隔区域，默认不显示。
            // show: true, //是否显示分隔区域
            // interval: 'auto', //坐标轴分隔区域的显示间隔，在类目轴中有效
          },
          axisLabel: { // 坐标轴刻度标签的相关设置。
            // formatter: 'expr {value}',  // 使用字符串模板，模板变量为刻度默认标签 {value}
            show: true, // 是否显示刻度标签。
            // interval: 'auto', //坐标轴刻度标签的显示间隔，在类目轴中有效。
            color: 'black'

          },
          splitLine: { // 坐标轴在 grid 区域中的分隔线。
            show: true, // 是否显示分隔线。默认数值轴显示，类目轴不显示。
            lineStyle: { // 分隔线样式
              type: 'dashed' // 分隔线线的类型。
            }
          },
          axisLine: { // 坐标轴轴线相关设置。
            show: true, // 是否显示坐标轴轴线。
            // onZero:false,//X 轴或者 Y 轴的轴线是否在另一个轴的 0 刻度上，只有在另一个轴为数值轴且包含 0 刻度时有效。
            // symbol:'arrow', //轴线两边的箭头, 默认不显示箭头，即 'none'
            lineStyle: { // 轴线样式
              width: 2,
              color: 'black'
              // opacity: 1, //图形透明度。支持从 0 到 1 的数字，为 0 时不绘制该图形。
            }
          },
          axisTick: { // 坐标轴刻度相关设置。
            show: true // 是否显示坐标轴刻度。
            // alignWithLabel: true,//类目轴中在 boundaryGap 为 true 的时候有效，可以保证刻度线和标签对齐,default: false

          }
        },
        yAxis: { // y轴
          type: 'value',
          name: 'Log2(FPKM+1)',
          splitArea: { // 坐标轴在 grid 区域中的分隔区域，默认不显示。
            // show: true
          },
          axisLabel: { // 坐标轴刻度标签的相关设置。
            // formatter: 'expr {value}',  // 使用字符串模板，模板变量为刻度默认标签 {value}
            show: true, // 是否显示刻度标签。
            // interval: 'auto', //坐标轴刻度标签的显示间隔，在类目轴中有效。
            color: 'black'
          },
          splitLine: {
            show: true,
            lineStyle: {
              type: 'dashed'
            }
          },
          axisLine: {
            show: true, // 是否显示坐标轴轴线。
            // onZero:false,//X 轴或者 Y 轴的轴线是否在另一个轴的 0 刻度上，只有在另一个轴为数值轴且包含 0 刻度时有效。
            // symbol:'arrow', //轴线两边的箭头
            lineStyle: {
              width: 2,
              color: 'black'
            }
          }
        },
        dataZoom: [
          {
            type: 'slider',
            yAxisIndex: 0,
            start: 0,
            end: 100
          }
        ],
        series: [
          {
            name: '复发', // 箱形图
            type: 'boxplot',
            data: data.boxData,
            colorBy: 'data',
            legendHoverLink: true, // 是否启用图例 hover 时的联动高亮。
            // hoverAnimation: false, //是否开启 hover 在 box 上的动画效果。
            itemStyle: { // 盒须图样式。
              // color: '#fff', //boxplot图形的颜色。 默认从全局调色盘 option.color 获取颜色
              // boxplot图形的描边颜色。支持的颜色格式同 color，不支持回调函数。
            },
            // data: data.boxData,
            tooltip: { // 注意：series.tooltip 仅在 tooltip.trigger 为 'item' 时有效。
              formatter: function (param) {
                return [
                  '类目名 ' + param.name + ': ',
                  'upper: ' + param.data[5],
                  'Q3: ' + param.data[4],
                  'median: ' + param.data[3],
                  'Q1: ' + param.data[2],
                  'lower: ' + param.data[1]
                ].join('<br/>')
              }
            }
          },
          {
            name: '异常值', // 异常值
            type: 'scatter', // 分散
            data: data.outliers
          }
        ]
      }
      // 使用刚指定的配置项和数据显示图表。
      myChart.setOption(option)
    },
    getData () {
      if (this.GLOBAL.Dataset[0].Dataset_Num === 'HCCMRDB1') {
        this.nr = 24
        this.tr = 24
      } else if (this.GLOBAL.Dataset[0].Dataset_Num === 'HCCMRDB2') {
        this.nr = 20
        this.tr = 20
      } else if (this.GLOBAL.Dataset[0].Dataset_Num === 'HCCMRDB3') {
        if (this.Sample === 'primary tumors：metastases vs metastases-free') {
          this.tr = 10
          this.nr = 10
        } else {
          this.tr = 20
          this.nr = 10
        }
      } else if (this.GLOBAL.Dataset[0].Dataset_Num === 'HCCMRDB4') {
        this.tr = 28
        if (this.Sample === 'primary tumors：metastases vs metastases-free') {
          this.nr = 27
        } else { this.nr = 30 }
      } else if (this.GLOBAL.Dataset[0].Dataset_Num === 'HCCMRDB5') {
        if (this.Sample === 'recurrent tumors vs adjacent tissue') {
          this.nr = 9
          this.tr = 9
        } else {
          this.nr = 12
          this.tr = 12
        }
      } else if (this.GLOBAL.Dataset[0].Dataset_Num === 'HCCMRDB6') {
        this.tr = 5
        this.nr = 17
      } else if (this.GLOBAL.Dataset[0].Dataset_Num === 'HCCMRDB7') {
        if (this.Sample === 'primary tumors：recurrent vs adjacent tissue') {
          this.nr = 19
          this.tr = 15
        } else if (this.Sample === 'primary tumors：recurrent vs non-recurrent') {
          this.nr = 6
          this.tr = 15
        } else {
          this.nr = 19
          this.tr = 6
        }
      } else if (this.GLOBAL.Dataset[0].Dataset_Num === 'HCCMRDB8') {
        if (this.Sample === 'primary tumors：recurrent vs adjacent tissue') {
          this.nr = 220
          this.tr = 121
        } else {
          this.nr = 100
          this.tr = 121
        }
      } else if (this.GLOBAL.Dataset[0].Dataset_Num === 'HCCMRDB9') {
        if (this.Sample === 'primary tumors：recurrent vs adjacent tissue') {
          this.nr = 20
          this.tr = 48
        } else if (this.Sample === 'primary tumors：recurrent vs non-recurrent') {
          this.nr = 60
          this.tr = 48
        } else {
          this.nr = 30
          this.tr = 60
        }
      } else if (this.GLOBAL.Dataset[0].Dataset_Num === 'HCCMRDB10') {
        if (this.Sample === 'primary tumors vs adjacent tissue') {
          this.nr = 58
          this.tr = 407
        } else if (this.Sample === 'primary tumors vs normal liver tissue') {
          this.nr = 160
          this.tr = 371
        } else if (this.Sample === 'primary tumors：metastases vs metastases-free') {
          this.nr = 15
          this.tr = 154
        } else {
          this.nr = 158
          this.tr = 148
        }
      }
      this.linear = true
      this.list = false
      this.boxDate = false
      console.log(this.Sample, this.Sample1)
      console.log(this.Sample1, this.fc, this.p, this.methodp, this.dataT, this.nr, this.tr, this.clustering_method)
      axios.post('/api/ldb/Analyse', { dataset: this.GLOBAL.Dataset[0].Dataset_Num, sampleType: this.Sample, FC: this.fc, PV: this.p, methods: this.methodp, nr: this.nr, tr: this.tr, mt: this.clustering_method })
        .then(res => {
          // eslint-disable-next-line no-eval
          this.datas = eval(res.data.matrix)
          console.log(this.datas)
          this.up = res.data.up
          this.down = res.data.down
          this.volcano_base64 = res.data.volcano
          this.volcano = 'data:;base64,' + res.data.volcano
          this.heatmap = 'data:;base64,' + res.data.heatmap
          this.heatmap_base64 = res.data.heatmap
          this.list = true
          this.linear = false
          this.up_list = res.data.up_list
          this.down_list = res.data.down_list
          this.nor_list = res.data.nor_list
          this.$nextTick(() => {
            /* const el = document.getElementById('preVol')
            var preWidth = window.getComputedStyle(el).width
            var preHeight = window.getComputedStyle(el).height
            console.log(preWidth, preHeight) */
            this.myEcharts()
          })
          console.log(res)
        })
        .catch(err => {
          console.log(err)
        })
    },
    handleDownloadQrIMg (qrBase64) {
      // 这里是获取到的图片base64编码,这里只是个例子哈，要自行编码图片替换这里才能测试看到效果
      const imgUrl = `data:image/png;base64,${qrBase64}`
      // 如果浏览器支持msSaveOrOpenBlob方法（也就是使用IE浏览器的时候），那么调用该方法去下载图片
      if (window.navigator.msSaveOrOpenBlob) {
        const bstr = atob(imgUrl.split(',')[1])
        let n = bstr.length
        const u8arr = new Uint8Array(n)
        while (n--) {
          u8arr[n] = bstr.charCodeAt(n)
        }
        const blob = new Blob([u8arr])
        window.navigator.msSaveOrOpenBlob(blob, 'chart-download' + '.' + 'png')
      } else {
        // 这里就按照chrome等新版浏览器来处理
        const a = document.createElement('a')
        a.href = imgUrl
        a.setAttribute('download', 'chart-download')
        a.click()
      }
    },
    getBoxplotData (gen) {
      this.gen = gen
      this.box = []
      this.boxDate = false
      this.boxLinear = true
      axios.post('/api/ldb/Boxplot', { gene_name: gen })
        .then(res => {
          // eslint-disable-next-line no-eval
          this.box = eval(res.data.data)
          this.box1 = [this.box[2], this.box[3]]
          this.box2 = [this.box[0], this.box[1]]
          this.box3 = [this.box[4], this.box[5]]
          this.box4 = [this.box[6], this.box[7]]
          this.boxLinear = false
          this.boxDate = true
          this.$nextTick(() => {
            var myChart1 = echarts.init(document.getElementById('box1'))
            // 绘制图表
            myChart1.setOption({
              title: [
                {
                  text: 'TCGA_Normal——Tumour',
                  textStyle: {
                    fontSize: 15,
                    color: '#6D819C'
                  },
                  left: 'center'
                }
              ],
              dataset: [{
                source: this.box1
              },
              {
                transform: {
                  type: 'boxplot',
                  config: { itemNameFormatter: 'expr {value}' }
                }
              }, {
                fromDatasetIndex: 1,
                fromTransformResult: 1
              }],
              tooltip: {
                trigger: 'item',
                axisPointer: {
                  type: 'shadow'
                }
              },
              grid: {
                left: '27%',
                right: '5%',
                bottom: '15%'
              },
              xAxis: {
                name: 'Sample Type',
                type: 'category',
                nameLocation: 'middle',
                boundaryGap: true,
                nameGap: 20,
                splitArea: {
                  show: false
                },
                splitLine: {
                  show: false
                }
              },
              yAxis: {
                type: 'value',
                name: this.gen + '--count',
                splitArea: {
                  show: true
                }
              },
              series: [
                {
                  name: 'boxplot',
                  type: 'boxplot',
                  datasetIndex: 1
                },
                {
                  name: 'outlier',
                  type: 'scatter',
                  datasetIndex: 2
                }
              ]
            })
            var myChart2 = echarts.init(document.getElementById('box2'))
            // 绘制图表
            myChart2.setOption({
              title: [
                {
                  text: 'TCGA_GTEx_Normal——Tumour',
                  textStyle: {
                    fontSize: 15,
                    color: '#6D819C'
                  },
                  left: 'center'
                }
              ],
              dataset: [{
                source: this.box2
              },
              {
                transform: {
                  type: 'boxplot',
                  config: { itemNameFormatter: 'expr {value}' }
                }
              }, {
                fromDatasetIndex: 1,
                fromTransformResult: 1
              }],
              tooltip: {
                trigger: 'item',
                axisPointer: {
                  type: 'shadow'
                }
              },
              grid: {
                left: '27%',
                right: '5%',
                bottom: '15%'
              },
              xAxis: {
                name: 'Sample Type',
                type: 'category',
                nameLocation: 'middle',
                boundaryGap: true,
                nameGap: 20,
                splitArea: {
                  show: false
                },
                splitLine: {
                  show: false
                }
              },
              yAxis: {
                type: 'value',
                name: this.gen + '--count',
                splitArea: {
                  show: true
                }
              },
              series: [
                {
                  name: 'boxplot',
                  type: 'boxplot',
                  datasetIndex: 1
                },
                {
                  name: 'outlier',
                  type: 'scatter',
                  datasetIndex: 2
                }
              ]
            })
            var myChart3 = echarts.init(document.getElementById('box3'))
            // 绘制图表
            myChart3.setOption({
              title: [
                {
                  text: 'Non-metastatic--Metastasis',
                  textStyle: {
                    fontSize: 15,
                    color: '#6D819C'
                  },
                  left: 'center'
                }
              ],
              dataset: [{
                source: this.box3
              },
              {
                transform: {
                  type: 'boxplot',
                  config: { itemNameFormatter: 'expr {value}' }
                }
              }, {
                fromDatasetIndex: 1,
                fromTransformResult: 1
              }],
              tooltip: {
                trigger: 'item',
                axisPointer: {
                  type: 'shadow'
                }
              },
              grid: {
                left: '27%',
                right: '5%',
                bottom: '15%'
              },
              xAxis: {
                name: 'Sample Type',
                type: 'category',
                nameLocation: 'middle',
                boundaryGap: true,
                nameGap: 20,
                splitArea: {
                  show: false
                },
                splitLine: {
                  show: false
                }
              },
              yAxis: {
                type: 'value',
                name: this.gen + '--count',
                splitArea: {
                  show: true
                }
              },
              series: [
                {
                  name: 'boxplot',
                  type: 'boxplot',
                  datasetIndex: 1
                },
                {
                  name: 'outlier',
                  type: 'scatter',
                  datasetIndex: 2
                }
              ]
            })
            var myChart4 = echarts.init(document.getElementById('box4'))
            // 绘制图表
            myChart4.setOption({
              title: [
                {
                  text: 'Non-recurrence--Recurrence',
                  textStyle: {
                    fontSize: 15,
                    color: '#6D819C'
                  },
                  left: 'center'
                }
              ],
              dataset: [{
                source: this.box4
              },
              {
                transform: {
                  type: 'boxplot',
                  config: { itemNameFormatter: 'expr {value}' }
                }
              }, {
                fromDatasetIndex: 1,
                fromTransformResult: 1
              }],
              tooltip: {
                trigger: 'item',
                axisPointer: {
                  type: 'shadow'
                }
              },
              grid: {
                left: '27%',
                right: '5%',
                bottom: '15%'
              },
              xAxis: {
                name: 'Sample Type',
                type: 'category',
                nameLocation: 'middle',
                boundaryGap: true,
                nameGap: 20,
                splitArea: {
                  show: false
                },
                splitLine: {
                  show: false
                }
              },
              yAxis: {
                type: 'value',
                name: this.gen + '--count',
                splitArea: {
                  show: true
                }
              },
              series: [
                {
                  name: 'boxplot',
                  type: 'boxplot',
                  datasetIndex: 1
                },
                {
                  name: 'outlier',
                  type: 'scatter',
                  datasetIndex: 2
                }
              ]
            })
          })
          console.log(this.box1)
        })
        .catch(err => {
          console.log(err)
        })
    },
    geneHeatmap () {
      this.dialog5 = true
      this.boxLinear1 = true
      this.AnalyzeStr = JSON.stringify(this.AnalyzeArray)
      console.log(this.AnalyzeStr)
      axios.post('/api/ldb/Heatmap', { dataset: this.GLOBAL.Dataset[0].Dataset_Num, sampleType: this.Sample, gene_list: this.AnalyzeStr, nr: this.nr, tr: this.tr })
        .then(res => {
          this.heatmap1 = 'data:;base64,' + res.data.res
          this.boxLinear1 = false
          console.log(typeof (this.AnalyzeStr))
        })
        .catch(err => {
          console.log(err)
        })
    },
    toCorrelation: function () {
      this.$router.push({ name: 'Correlation' })
    },
    toSurvival: function () {
      this.$router.push({ name: 'Survival' })
    },
    initChart1 () {
      this.dialog1 = true
      this.$nextTick(() => {
        var myChartBig1 = echarts.init(document.getElementById('bigbox1'))
        // 绘制图表
        myChartBig1.setOption({
          title: [
            {
              text: 'TCGA_Normal——Tumour',
              subtext: this.gen + 'Gene Expression',
              textStyle: {
                fontSize: 15,
                color: '#6D819C'
              },
              subtextStyle: { fontSize: 10 },
              left: 'center'
            }
          ],
          dataset: [{
            source: this.box1
          },
          {
            transform: {
              type: 'boxplot',
              config: { itemNameFormatter: 'expr {value}' }
            }
          }, {
            fromDatasetIndex: 1,
            fromTransformResult: 1
          }],
          tooltip: {
            trigger: 'item',
            axisPointer: {
              type: 'shadow'
            }
          },
          dataZoom: [
            {
              type: 'slider',
              yAxisIndex: 0,
              start: 0,
              end: 80
            }
          ],
          grid: {
            left: '20%',
            right: '10%',
            bottom: '15%'
          },
          toolbox: {
            show: true,
            feature: {
              restore: {},
              saveAsImage: {}
            }
          },
          xAxis: {
            name: 'Sample Type',
            type: 'category',
            nameLocation: 'middle',
            boundaryGap: true,
            nameGap: 30,
            splitArea: {
              show: false
            },
            splitLine: {
              show: false
            }
          },
          yAxis: {
            type: 'value',
            name: this.gen + '--count',
            splitArea: {
              show: true
            }
          },
          series: [
            {
              name: 'boxplot',
              type: 'boxplot',
              datasetIndex: 1
            },
            {
              name: 'outlier',
              type: 'scatter',
              datasetIndex: 2
            }
          ]
        })
      })
    },
    initChart2 () {
      this.dialog2 = true
      this.$nextTick(() => {
        var myChartBig2 = echarts.init(document.getElementById('bigbox2'))
        // 绘制图表
        myChartBig2.setOption({
          title: [
            {
              text: 'TCGA_GTEx_Normal——Tumour',
              subtext: this.gen + 'Gene Expression',
              textStyle: {
                fontSize: 15,
                color: '#6D819C'
              },
              subtextStyle: { fontSize: 10 },
              left: 'center'
            }
          ],
          dataset: [{
            source: this.box2
          },
          {
            transform: {
              type: 'boxplot',
              config: { itemNameFormatter: 'expr {value}' }
            }
          }, {
            fromDatasetIndex: 1,
            fromTransformResult: 1
          }],
          tooltip: {
            trigger: 'item',
            axisPointer: {
              type: 'shadow'
            }
          },
          dataZoom: [
            {
              type: 'slider',
              yAxisIndex: 0,
              start: 0,
              end: 80
            }
          ],
          grid: {
            left: '20%',
            right: '10%',
            bottom: '15%'
          },
          toolbox: {
            show: true,
            feature: {
              restore: {},
              saveAsImage: {}
            }
          },
          xAxis: {
            name: 'Sample Type',
            type: 'category',
            nameLocation: 'middle',
            boundaryGap: true,
            nameGap: 30,
            splitArea: {
              show: false
            },
            splitLine: {
              show: false
            }
          },
          yAxis: {
            type: 'value',
            name: this.gen + '--count',
            splitArea: {
              show: true
            }
          },
          series: [
            {
              name: 'boxplot',
              type: 'boxplot',
              datasetIndex: 1
            },
            {
              name: 'outlier',
              type: 'scatter',
              datasetIndex: 2
            }
          ]
        })
      })
    },
    initChart3 () {
      this.dialog3 = true
      this.$nextTick(() => {
        var myChartBig3 = echarts.init(document.getElementById('bigbox3'))
        // 绘制图表
        myChartBig3.setOption({
          title: [
            {
              text: 'Non-metastatic--Metastasis',
              subtext: this.gen + 'Gene Expression',
              textStyle: {
                fontSize: 15,
                color: '#6D819C'
              },
              subtextStyle: { fontSize: 10 },
              left: 'center'
            }
          ],
          dataset: [{
            source: this.box3
          },
          {
            transform: {
              type: 'boxplot',
              config: { itemNameFormatter: 'expr {value}' }
            }
          }, {
            fromDatasetIndex: 1,
            fromTransformResult: 1
          }],
          tooltip: {
            trigger: 'item',
            axisPointer: {
              type: 'shadow'
            }
          },
          dataZoom: [
            {
              type: 'slider',
              yAxisIndex: 0,
              start: 0,
              end: 80
            }
          ],
          grid: {
            left: '20%',
            right: '10%',
            bottom: '15%'
          },
          toolbox: {
            show: true,
            feature: {
              restore: {},
              saveAsImage: {}
            }
          },
          xAxis: {
            name: 'Sample Type',
            type: 'category',
            nameLocation: 'middle',
            boundaryGap: true,
            nameGap: 30,
            splitArea: {
              show: false
            },
            splitLine: {
              show: false
            }
          },
          yAxis: {
            type: 'value',
            name: this.gen + '--count',
            splitArea: {
              show: true
            }
          },
          series: [
            {
              name: 'boxplot',
              type: 'boxplot',
              datasetIndex: 1
            },
            {
              name: 'outlier',
              type: 'scatter',
              datasetIndex: 2
            }
          ]
        })
      })
    },
    initChart4 () {
      this.dialog4 = true
      this.$nextTick(() => {
        var myChartBig4 = echarts.init(document.getElementById('bigbox4'))
        // 绘制图表
        myChartBig4.setOption({
          title: [
            {
              text: 'Non-recurrence--Recurrence',
              subtext: this.gen + 'Gene Expression',
              textStyle: {
                fontSize: 15,
                color: '#6D819C'
              },
              subtextStyle: { fontSize: 10 },
              left: 'center'
            }
          ],
          dataset: [{
            source: this.box4
          },
          {
            transform: {
              type: 'boxplot',
              config: { itemNameFormatter: 'expr {value}' }
            }
          }, {
            fromDatasetIndex: 1,
            fromTransformResult: 1
          }],
          tooltip: {
            trigger: 'item',
            axisPointer: {
              type: 'shadow'
            }
          },
          dataZoom: [
            {
              type: 'slider',
              yAxisIndex: 0,
              start: 0,
              end: 80
            }
          ],
          grid: {
            left: '20%',
            right: '10%',
            bottom: '15%'
          },
          toolbox: {
            show: true,
            feature: {
              restore: {},
              saveAsImage: {}
            }
          },
          xAxis: {
            name: 'Sample Type',
            type: 'category',
            nameLocation: 'middle',
            boundaryGap: true,
            nameGap: 30,
            splitArea: {
              show: false
            },
            splitLine: {
              show: false
            }
          },
          yAxis: {
            type: 'value',
            name: this.gen + '--count',
            splitArea: {
              show: true
            }
          },
          series: [
            {
              name: 'boxplot',
              type: 'boxplot',
              datasetIndex: 1
            },
            {
              name: 'outlier',
              type: 'scatter',
              datasetIndex: 2
            }
          ]
        })
      })
    },
    changeChoice () {
      if (this.GLOBAL.Dataset[0].Dataset_Num === 'HCCMRDB1') {
        this.sampleType1 = ['tumor：Bone metastasis vs Metastases-free', 'adjacent：Bone metastasis vs Metastases-free']
        this.Method = ['LIMMA']
      } else if (this.GLOBAL.Dataset[0].Dataset_Num === 'HCCMRDB2') {
        this.sampleType1 = ['tumor：lymph node Metastasis vs Metastases-free', 'adjacent：lymph node Metastasis vs Metastases-free']
        this.Method = ['LIMMA']
      } else if (this.GLOBAL.Dataset[0].Dataset_Num === 'HCCMRDB3' || this.GLOBAL.Dataset[0].Dataset_Num === 'HCCMRDB4') {
        this.sampleType1 = ['metastasis tumor vs primary tumors', 'primary tumors：metastases vs metastases-free']
        this.Method = ['LIMMA']
      } else if (this.GLOBAL.Dataset[0].Dataset_Num === 'HCCMRDB5') {
        this.sampleType1 = ['recurrent tumors vs adjacent tissue', 'primary tumors：non-recurrent vs adjacent tissue']
        this.Method = ['LIMMA', 'edgR', 'DESeq2']
      } else if (this.GLOBAL.Dataset[0].Dataset_Num === 'HCCMRDB6') {
        this.sampleType1 = ['recurrent tumors vs primary tumors']
        this.Method = ['LIMMA', 'edgR', 'DESeq2']
      } else if (this.GLOBAL.Dataset[0].Dataset_Num === 'HCCMRDB7' || this.GLOBAL.Dataset[0].Dataset_Num === 'HCCMRDB9') {
        this.sampleType1 = ['primary tumors：recurrent vs non-recurrent', 'primary tumors：non-recurrent vs adjacent tissue', 'primary tumors：recurrent vs adjacent tissue']
        this.Method = ['LIMMA']
      } else if (this.GLOBAL.Dataset[0].Dataset_Num === 'HCCMRDB8') {
        this.sampleType1 = ['primary tumors：recurrent vs non-recurrent', 'primary tumors：recurrent vs adjacent tissue']
        this.Method = ['LIMMA']
      } else if (this.GLOBAL.Dataset[0].Dataset_Num === 'HCCMRDB10') {
        this.sampleType1 = ['primary tumors vs adjacent tissue', 'primary tumors vs normal liver tissue', 'primary tumors：metastases vs metastases-free', 'primary tumors：recurrent vs non-recurrent']
        this.Method = ['LIMMA', 'edgR', 'DESeq2']
      }
    }
    /* chartssize (preVol, volcono) {
      function getStyle (el, name) {
        if (window.getComputedStyle) {
          return window.getComputedStyle(el, null)
        } else {
          return el.currentStyle
        }
      }
      var wi = getStyle(preVol, 'width').width
      var hi = getStyle(preVol, 'height').height
      volcono.style.width = wi
      volcono.style.height = hi
    } */
  },
  mounted () {
    this.$nextTick(function () {
      this.changeChoice()
    })
  },
  beforeDestroy () {
    var Analyze = this.AnalyzeArray.toString()
    this.bus.$emit('gene_translate', Analyze)
    this.bus.$emit('gene_translate1', this.AnalyzeArray)
    this.bus.$emit('gene_color', this.AnalyzeColor)
  }
}
</script>
<style lang="scss" scoped>
.textSmall{
  font-size: 14px;
}
.textExp{
  font-size: 12px;
  color: dimgrey;
}
</style>
