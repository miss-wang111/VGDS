<template>
  <div class="ml-5 mr-5">
    <p class="titleText mb-2" style="text-align:left">Introduction</p>
    <p class="parText pt-2 mb-2 " style="text-align:left">Provide target-based studies and analysis of the clinical prognosis of HCC(VGDS), which focus on recurrence and metastasis of HCC.</p>
    <p class="parText pt-2 mb-2 " style="text-align:left">VGDS has integrated 1605 RNA sequencing expression samples from 10 datasets, which includes almost all HCC metastasis and recurrence-related RNA-seq samples from The Cancer Genome Atlas (TCGA) and Gene Expression Omnibus (GEO). In addition, we collected public Single-cell RNA sequencing (scRNA-seq) datasets involving 18,801 high-quality single cells from 24 samples across different liver tissue.</p>
    <v-divider></v-divider>
    <p class="titleText mb-2" style="text-align:left">Target & Article</p>
    <p class="parText pt-2 mb-2 " style="text-align:left">We obtained 2768 liver cancer-related targets from >8000 liver cancer-related papers and collected information on these targets </p>
    <v-row>
      <v-col cols="2"></v-col>
      <v-col cols="8">
        <v-img :src=img1  class="grey darken-4 align-end " ></v-img>
      </v-col>
      <v-col cols="2"></v-col>
    </v-row>
    <v-divider></v-divider>
    <p class="titleText mb-2" style="text-align:left">System function</p>
    <p class="parText pt-2 mb-2 " style="text-align:left">We designed and implemented an interactive web interface
      and a complete analysis pipeline. First, the dataset
      details page provides the source of the dataset and its details.
      Users can select data sets of interest for subsequent analysis on
      this page. The analysis page provides multiple data interfaces
      allowing users the flexibility to analyze and visualize the results
      to suit their needs. Analysis functions include differential analysis, correlation analysis, survival analysis, and multidimensional differential expression of genes. Finally, we provide a
      target ranking based on the number of associated literature.</p>
    <v-row>
      <v-col cols="2"></v-col>
      <v-col cols="8">
        <v-img :src=img6  class="grey darken-4 align-end " ></v-img>
      </v-col>
      <v-col cols="2"></v-col>
    </v-row>
    <p class="titleText mb-2" style="text-align:left">Differential analysis.</p>
    <p class="parText pt-2 mb-2 " style="text-align:left">VGDS provides analysis for a specified dataset and allows users to select statistical methods and thresholds for a specified dataset to dynamically obtain differentially expressed genes and plot heat and volcano maps against the obtained differential genes. When the mouse is positioned at the point of the graph of the volcano the corresponding gene symbol, Log2FC, P-value, change status and other details are displayed. Three analysis methods were used including limma, DESeq2 and edgeR related R packages, respectively. Users can select genes of interest from the screened differential genes for further heat mapping or the next step of the analysis.</p>
    <v-row>
      <v-col cols="2"></v-col>
      <v-col cols="8">
        <v-img :src=img2  class="grey darken-4 align-end " ></v-img>
      </v-col>
      <v-col cols="2"></v-col>
    </v-row>
    <v-divider></v-divider>
    <p class="titleText mb-2" style="text-align:left">Correlation analysis.</p>
    <p class="parText pt-2 mb-2 " style="text-align:left">This section accepts genes selected by the user from the variance analysis section, as well as genes of interest entered by the user. This function uses methods such as Pearson, Spearman and Kendall correlation statistics to perform a two-by-two gene correlation analysis on a given expression dataset obtains correlation coefficients, and returns a heat map and table of correlation coefficients.</p>
    <v-row>
      <v-col cols="2"></v-col>
      <v-col cols="8">
        <v-img :src=img3  class="grey darken-4 align-end " ></v-img>
      </v-col>
      <v-col cols="2"></v-col>
    </v-row>
    <v-divider></v-divider>
    <p class="titleText mb-2" style="text-align:left">Survival analysis.</p>
    <p class="parText pt-2 mb-2 " style="text-align:left">This function is based on gene expression level survival analysis, a function that allows the user to select the dataset of interest and the corresponding classification for overall survival analysis. Only three datasets, HCCMRDB4, HCCMRDB6 and HCCMRDB10, containing clinical information, are available. This function uses log-rank tests (sometimes called Mantel-Cox tests) for hypothesis evaluation. The Cox proportional risk ratio and 95% confidence interval information can also be included in the survival plot. Users can also adjust the thresholds and time units for high and low expressions.</p>
    <v-row>
      <v-col cols="2"></v-col>
      <v-col cols="8">
        <v-img :src=img4  class="grey darken-4 align-end " ></v-img>
      </v-col>
      <v-col cols="2"></v-col>
    </v-row>
    <v-divider></v-divider>
    <p class="titleText mb-2" style="text-align:left">Single gene search page</p>
    <p class="parText pt-2 mb-2 " style="text-align:left">The single-gene search results page contains four main
      parts: (1) basic information; (2) gene expression pattern 5D
      metrics; (3) expression distribution; (4) single-cell level expression. Taking HAMP as an example, we will introduce the design
      of the gene page in detail.</p>
    <v-row>
      <v-col cols="2"></v-col>
      <v-col cols="8">
        <v-img :src=img5  class="grey darken-4 align-end " ></v-img>
      </v-col>
      <v-col cols="2"></v-col>
    </v-row>
  </div>
</template>

<script>

export default {
  name: 'Echarts',
  data () {
    return {
      img1: require('@/assets/target.png'),
      img2: require('@/assets/img2.jpg'),
      img3: require('@/assets/img3.jpg'),
      img4: require('@/assets/img4.jpg'),
      img5: require('@/assets/img5.jpg'),
      img6: require('@/assets/img6.jpg')
    /*  co1_list: [],
      co2_list: [],
      co3_list: [],
      co4_list: [],
      newdata: [] */
    }
  },
  methods: {
  /*  myEcharts1 () {
      // 基于准备好的dom，初始化echarts实例
      var myChart = this.$echarts.init(document.getElementById('main1'))
      var co1_list = this.co1_list
      // eslint-disable-next-line no-unused-vars
      var data = this.char_list
      // 指定图表的配置项和数据
      var option = {
        grid: {
          show: true,
          left: '3%',
          right: '7%',
          top: '0%',
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
             '<br />P-value:' +
             params.data[0] +
             '<br />Log2Foldchange:' +
             params.data[1]
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
        series: [
          {
            name: 'normal',
            type: 'scatter',
            emphasis: {
              focus: 'series'
            },
            data: co1_list
          }
        ]
      }

      // 使用刚指定的配置项和数据显示图表。
      myChart.setOption(option)
    }, */
    /* Correlation () {
      axios.get(this.ROOT_PATH + '/data/asset/data/nutrients.json')
        .then(res => {
          this.data = normalizeData(res.data).slice(0, 1000)
          myChart.setOption((option = getOption(data)))
         /!* this.co1_list = res.data.co1_list
          this.co2_list = res.data.co2_list
          this.co3_list = res.data.co3_list
          this.co4_list = res.data.co4_list*!/
          console.log(this.co1_list)
          this.$nextTick(() => {
            this.myEcharts1()
          })
          // console.log(res.data.heatmap)
        })
        .catch(err => {
          console.log(err)
        })
    }, */
    /* myEcharts1 () {
      var app = {}
      var chartDom = document.getElementById('main')
      var myChart = echarts.init(chartDom)
      var option

      const indices = {
        name: 0,
        group: 1,
        id: 16
      }
      const schema = [
        { name: 'name', index: 0 },
        { name: 'group', index: 1 },
        { name: 'protein', index: 2 },
        { name: 'calcium', index: 3 },
        { name: 'sodium', index: 4 },
        { name: 'fiber', index: 5 },
        { name: 'vitaminc', index: 6 },
        { name: 'potassium', index: 7 },
        { name: 'carbohydrate', index: 8 },
        { name: 'sugars', index: 9 },
        { name: 'fat', index: 10 },
        { name: 'water', index: 11 },
        { name: 'calories', index: 12 },
        { name: 'saturated', index: 13 },
        { name: 'monounsat', index: 14 },
        { name: 'polyunsat', index: 15 },
        { name: 'id', index: 16 }
      ]
      const axisColors = {
        xAxisLeft: '#2A8339',
        xAxisRight: '#367DA6',
        yAxisTop: '#A68B36',
        yAxisBottom: '#BD5692'
      }
      const colorBySchema = {}
      const fieldIndices = schema.reduce(function (obj, item) {
        obj[item.name] = item.index
        return obj
      }, {})
      const groupCategories = []
      const groupColors = []
      var data = this.data
      // zlevel 为 1 的层开启尾迹特效
      myChart.getZr().configLayer(1, {
        motionBlur: true
      })
      function normalizeData (originData) {
        const groupMap = {}
        originData.forEach(function (row) {
          const groupName = row[indices.group]
          if (!groupMap.hasOwnProperty(groupName)) {
            groupMap[groupName] = 1
          }
        })
        originData.forEach(function (row) {
          row.forEach(function (item, index) {
            if (
              index !== indices.name &&
              index !== indices.group &&
              index !== indices.id
            ) {
              // Convert null to zero, as all of them under unit "g".
              row[index] = parseFloat(item) || 0
            }
          })
        })
        for (const groupName in groupMap) {
          if (groupMap.hasOwnProperty(groupName)) {
            groupCategories.push(groupName)
          }
        }
        const hStep = Math.round(300 / (groupCategories.length - 1))
        for (let i = 0; i < groupCategories.length; i++) {
          groupColors.push(echarts.color.modifyHSL('#5A94DF', hStep * i))
        }
        return originData
      }
      function makeAxis (dimIndex, id, name, nameLocation) {
        const axisColor = axisColors[id.split('-')[dimIndex]]
        colorBySchema[name] = axisColor
        return {
          id: id,
          name: name,
          nameLocation: nameLocation,
          nameGap: nameLocation === 'middle' ? 30 : 10,
          gridId: id,
          splitLine: { show: false },
          axisLine: {
            lineStyle: {
              color: axisColor
            }
          },
          axisLabel: {
            color: axisColor
          },
          axisTick: {
            lineStyle: {
              color: axisColor
            }
          }
        }
      }
      function makeSeriesData (xLeftOrRight, yTopOrBottom) {
        return data.map(function (item, idx) {
          const schemaX = app.config[xLeftOrRight]
          const schemaY = app.config[yTopOrBottom]
          return [
            item[fieldIndices[schemaX]],
            item[fieldIndices[schemaY]],
            item[1],
            item[0],
            schemaX,
            schemaY,
            idx // 6
          ]
        })
      }
      function makeSeries (xLeftOrRight, yTopOrBottom) {
        const id = xLeftOrRight + '-' + yTopOrBottom
        return {
          zlevel: 1,
          type: 'scatter',
          name: 'nutrients',
          xAxisId: id,
          yAxisId: id,
          symbolSize: 8,
          emphasis: {
            itemStyle: {
              color: '#fff'
            }
          },
          data: makeSeriesData(xLeftOrRight, yTopOrBottom)
        }
      }
      function makeDataZoom (opt) {
        return Object.assign(
          {
            type: 'slider',
            filterMode: 'empty',
            realtime: false
          },
          opt
        )
      }
      function tooltipFormatter (params) {
        // Remove duplicate by data name.
        const mapByDataName = {}
        const mapOnDim = {
          x: {},
          y: {},
          xy: {}
        }
        params.forEach(function (item) {
          const data = item.data
          const dataName = data[3]
          const mapItem = mapByDataName[dataName] || (mapByDataName[dataName] = {})
          mapItem[data[4]] = data[0]
          mapItem[data[5]] = data[1]
          mapOnDim[item.axisDim][dataName] = mapItem
        })
        Object.keys(mapByDataName).forEach(function (dataName) {
          if (mapOnDim.x[dataName] && mapOnDim.y[dataName]) {
            mapOnDim.xy[dataName] = mapByDataName[dataName]
            delete mapOnDim.x[dataName]
            delete mapOnDim.y[dataName]
          }
        })
        const resultHTML = [];
        [
          ['xy', 'CROSS'],
          ['x', 'V LINE'],
          ['y', 'H LINE']
        ].forEach(function (dimDefine) {
          const html = []
          Object.keys(mapOnDim[dimDefine[0]]).forEach(function (dataName) {
            const mapItem = mapOnDim[dimDefine[0]][dataName]
            const valuesHTML = []
            Object.keys(mapItem).forEach(function (dataName) {
              valuesHTML.push(
                '<span style="color:' +
                colorBySchema[dataName] +
                '">' +
                dataName +
                '</span>: ' +
                mapItem[dataName]
              )
            })
            html.push(
              '<div style="margin: 10px 0">' +
              dataName +
              '<br/>' +
              valuesHTML.join('<br/>') +
              '</div>'
            )
          })
          html.length &&
          resultHTML.push(
            '<div style="margin: 10px 0">' +
            '<div style="font-size: 16px; color: #aaa">POINTS ON ' +
            dimDefine[1] +
            '</div>' +
            html.join('') +
            '</div>'
          )
        })
        return resultHTML.join('')
      }
      function getOption (data) {
        const gridWidth = '35%'
        const gridHeight = '35%'
        const gridLeft = 80
        const gridRight = 50
        const gridTop = 50
        const gridBottom = 80
        return {
          tooltip: {
            trigger: 'none',
            padding: [10, 20, 10, 20],
            backgroundColor: '#42b983',
            transitionDuration: 0,
            extraCssText: 'width: 300px; white-space: normal',
            textStyle: {
              color: '#fff',
              fontSize: 12
            },
            position: function (pos, params, el, elRect, size) {
              const obj = {}
              obj[['left', 'right'][+(pos[0] < size.viewSize[0] / 2)]] = 60
              obj[['top', 'bottom'][+(pos[1] < size.viewSize[1] / 2)]] = 20
              return obj
            },
            formatter: tooltipFormatter
          },
          axisPointer: {
            show: true,
            snap: true,
            lineStyle: {
              type: 'dashed'
            },
            label: {
              show: true,
              margin: 6,
              backgroundColor: '#42b983',
              color: '#fff'
            },
            link: [
              {
                xAxisId: ['xAxisLeft-yAxisTop', 'xAxisLeft-yAxisBottom']
              },
              {
                xAxisId: ['xAxisRight-yAxisTop', 'xAxisRight-yAxisBottom']
              },
              {
                yAxisId: ['xAxisLeft-yAxisTop', 'xAxisRight-yAxisTop']
              },
              {
                yAxisId: ['xAxisLeft-yAxisBottom', 'xAxisRight-yAxisBottom']
              }
            ]
          },
          xAxis: [
            makeAxis(0, 'xAxisLeft-yAxisTop', 'carbohydrate', 'middle'),
            makeAxis(0, 'xAxisLeft-yAxisBottom', 'carbohydrate', 'middle'),
            makeAxis(0, 'xAxisRight-yAxisTop', 'potassium', 'middle'),
            makeAxis(0, 'xAxisRight-yAxisBottom', 'potassium', 'middle')
          ],
          yAxis: [
            makeAxis(1, 'xAxisLeft-yAxisTop', 'calcium', 'end'),
            makeAxis(1, 'xAxisLeft-yAxisBottom', 'fiber', 'end'),
            makeAxis(1, 'xAxisRight-yAxisTop', 'calcium', 'end'),
            makeAxis(1, 'xAxisRight-yAxisBottom', 'fiber', 'end')
          ],
          grid: [
            {
              id: 'xAxisLeft-yAxisTop',
              left: gridLeft,
              top: gridTop,
              width: gridWidth,
              height: gridHeight
            },
            {
              id: 'xAxisLeft-yAxisBottom',
              left: gridLeft,
              bottom: gridBottom,
              width: gridWidth,
              height: gridHeight
            },
            {
              id: 'xAxisRight-yAxisTop',
              right: gridRight,
              top: gridTop,
              width: gridWidth,
              height: gridHeight
            },
            {
              id: 'xAxisRight-yAxisBottom',
              right: gridRight,
              bottom: gridBottom,
              width: gridWidth,
              height: gridHeight
            }
          ],
          dataZoom: [
            makeDataZoom({
              width: gridWidth,
              height: 20,
              left: gridLeft,
              bottom: 10,
              xAxisIndex: [0, 1]
            }),
            makeDataZoom({
              width: gridWidth,
              height: 20,
              right: gridRight,
              bottom: 10,
              xAxisIndex: [2, 3]
            }),
            makeDataZoom({
              orient: 'vertical',
              width: 20,
              height: gridHeight,
              left: 10,
              top: gridTop,
              yAxisIndex: [0, 2]
            }),
            makeDataZoom({
              orient: 'vertical',
              width: 20,
              height: gridHeight,
              left: 10,
              bottom: gridBottom,
              yAxisIndex: [1, 3]
            })
          ],
          visualMap: [
            {
              show: false,
              type: 'piecewise',
              categories: groupCategories,
              dimension: 2,
              inRange: {
                color: groupColors // ['#d94e5d','#eac736','#50a3ba']
              },
              outOfRange: {
                color: ['#ccc'] // ['#d94e5d','#eac736','#50a3ba']
              },
              top: 20,
              textStyle: {
                color: '#fff'
              },
              realtime: false
            }
          ],
          series: [
            makeSeries('xAxisLeft', 'yAxisTop'),
            makeSeries('xAxisLeft', 'yAxisBottom'),
            makeSeries('xAxisRight', 'yAxisTop'),
            makeSeries('xAxisRight', 'yAxisBottom')
          ],
          animationThreshold: 5000,
          progressiveThreshold: 5000,
          animationEasingUpdate: 'cubicInOut',
          animationDurationUpdate: 2000
        }
      }
      const fieldNames = schema
        .map(function (item) {
          return item.name
        })
        .slice(2)
      app.config = {
        xAxisLeft: 'carbohydrate',
        yAxisTop: 'calcium',
        xAxisRight: 'potassium',
        yAxisBottom: 'fiber',
        onChange: function () {
          if (data) {
            colorBySchema[app.config.xAxisLeft] = axisColors.xAxisLeft
            colorBySchema[app.config.xAxisRight] = axisColors.xAxisRight
            colorBySchema[app.config.yAxisTop] = axisColors.yAxisTop
            colorBySchema[app.config.yAxisBottom] = axisColors.yAxisBottom
            myChart.setOption({
              xAxis: [
                {
                  name: app.config.xAxisLeft
                },
                {
                  name: app.config.xAxisLeft
                },
                {
                  name: app.config.xAxisRight
                },
                {
                  name: app.config.xAxisRight
                }
              ],
              yAxis: [
                {
                  name: app.config.yAxisTop
                },
                {
                  name: app.config.yAxisBottom
                },
                {
                  name: app.config.yAxisTop
                },
                {
                  name: app.config.yAxisBottom
                }
              ],
              series: [
                {
                  data: makeSeriesData('xAxisLeft', 'yAxisTop')
                },
                {
                  data: makeSeriesData('xAxisLeft', 'yAxisBottom')
                },
                {
                  data: makeSeriesData('xAxisRight', 'yAxisTop')
                },
                {
                  data: makeSeriesData('xAxisRight', 'yAxisBottom')
                }
              ]
            })
          }
        }
      }
      app.configParameters = {
        xAxisLeft: {
          options: fieldNames
        },
        xAxisRight: {
          options: fieldNames
        },
        yAxisTop: {
          options: fieldNames
        },
        yAxisBottom: {
          options: fieldNames
        }
      }
      console.log('在执行')
      axios.get('https://cdn.jsdelivr.net/gh/apache/echarts-website@asf-site/examples/data/asset/data/nutrients.json')
        .then(res => {
          this.newdata = res.data
          data = normalizeData(this.newdata).slice(0, 1000)
          myChart.setOption((option = getOption(data)))
          console.log('完成')
        })

      option && myChart.setOption(option)
    }, */
    /* myEcharts2 () {
     /!* axios.get('/api/ldb/CorDeff2')
        .then(res => {
          console.log('开始')
          this.newdata = res.data
          console.log('完成')
        })*!/
      var app = {}
      var chartDom = document.getElementById('main')
      var myChart = echarts.init(chartDom)
      var option

      const indices = {
        name: 0,
        group: 1,
        id: 16
      }
      const schema = [
        { name: 'gene_name', index: 0 },
        { name: 'log2FC1', index: 1 },
        { name: 'log2FC2', index: 2 },
        { name: 'log2FC3', index: 3 },
        { name: 'log2FC4', index: 4 },
      ]
      const axisColors = {
        xAxisLeft: '#2A8339',
        xAxisRight: '#367DA6',
        yAxisTop: '#A68B36',
        yAxisBottom: '#BD5692'
      }
      const colorBySchema = {}
      const fieldIndices = schema.reduce(function (obj, item) {
        obj[item.name] = item.index
        return obj
      }, {})
      const groupCategories = []
      const groupColors = []
      var data = this.data
      // zlevel 为 1 的层开启尾迹特效
      myChart.getZr().configLayer(1, {
        motionBlur: true
      })
      function normalizeData (originData) {
        const groupMap = {}
        originData.forEach(function (row) {
          const groupName = row[indices.group]
          if (!groupMap.hasOwnProperty(groupName)) {
            groupMap[groupName] = 1
          }
        })
        originData.forEach(function (row) {
          row.forEach(function (item, index) {
            if (
              index !== indices.name &&
              index !== indices.group &&
              index !== indices.id
            ) {
              // Convert null to zero, as all of them under unit "g".
              row[index] = parseFloat(item) || 0
            }
          })
        })
        for (const groupName in groupMap) {
          if (groupMap.hasOwnProperty(groupName)) {
            groupCategories.push(groupName)
          }
        }
        const hStep = Math.round(300 / (groupCategories.length - 1))
        for (let i = 0; i < groupCategories.length; i++) {
          groupColors.push(echarts.color.modifyHSL('#5A94DF', hStep * i))
        }
        return originData
      }
      function makeAxis (dimIndex, id, name, nameLocation) {
        const axisColor = axisColors[id.split('-')[dimIndex]]
        colorBySchema[name] = axisColor
        return {
          id: id,
          name: name,
          nameLocation: nameLocation,
          nameGap: nameLocation === 'middle' ? 30 : 10,
          gridId: id,
          splitLine: { show: false },
          axisLine: {
            lineStyle: {
              color: axisColor
            }
          },
          axisLabel: {
            color: axisColor
          },
          axisTick: {
            lineStyle: {
              color: axisColor
            }
          }
        }
      }
      function makeSeriesData (xLeftOrRight, yTopOrBottom) {
        return data.map(function (item, idx) {
          const schemaX = app.config[xLeftOrRight]
          const schemaY = app.config[yTopOrBottom]
          return [
            item[fieldIndices[schemaX]],
            item[fieldIndices[schemaY]],
            item[1],
            item[0],
            schemaX,
            schemaY,
            idx // 6
          ]
        })
      }
      function makeSeries (xLeftOrRight, yTopOrBottom) {
        const id = xLeftOrRight + '-' + yTopOrBottom
        return {
          zlevel: 1,
          type: 'scatter',
          name: 'nutrients',
          xAxisId: id,
          yAxisId: id,
          symbolSize: 8,
          emphasis: {
            itemStyle: {
              color: '#fff'
            }
          },
          data: makeSeriesData(xLeftOrRight, yTopOrBottom)
        }
      }
      function makeDataZoom (opt) {
        return Object.assign(
          {
            type: 'slider',
            filterMode: 'empty',
            realtime: false
          },
          opt
        )
      }
      function tooltipFormatter (params) {
        // Remove duplicate by data name.
        const mapByDataName = {}
        const mapOnDim = {
          x: {},
          y: {},
          xy: {}
        }
        params.forEach(function (item) {
          const data = item.data
          const dataName = data[3]
          const mapItem = mapByDataName[dataName] || (mapByDataName[dataName] = {})
          mapItem[data[4]] = data[0]
          mapItem[data[5]] = data[1]
          mapOnDim[item.axisDim][dataName] = mapItem
        })
        Object.keys(mapByDataName).forEach(function (dataName) {
          if (mapOnDim.x[dataName] && mapOnDim.y[dataName]) {
            mapOnDim.xy[dataName] = mapByDataName[dataName]
            delete mapOnDim.x[dataName]
            delete mapOnDim.y[dataName]
          }
        })
        const resultHTML = [];
        [
          ['xy', 'CROSS'],
          ['x', 'V LINE'],
          ['y', 'H LINE']
        ].forEach(function (dimDefine) {
          const html = []
          Object.keys(mapOnDim[dimDefine[0]]).forEach(function (dataName) {
            const mapItem = mapOnDim[dimDefine[0]][dataName]
            const valuesHTML = []
            Object.keys(mapItem).forEach(function (dataName) {
              valuesHTML.push(
                '<span style="color:' +
                colorBySchema[dataName] +
                '">' +
                dataName +
                '</span>: ' +
                mapItem[dataName]
              )
            })
            html.push(
              '<div style="margin: 10px 0">' +
              dataName +
              '<br/>' +
              valuesHTML.join('<br/>') +
              '</div>'
            )
          })
          html.length &&
          resultHTML.push(
            '<div style="margin: 10px 0">' +
            '<div style="font-size: 16px; color: #aaa">POINTS ON ' +
            dimDefine[1] +
            '</div>' +
            html.join('') +
            '</div>'
          )
        })
        return resultHTML.join('')
      }
      function getOption (data) {
        const gridWidth = '35%'
        const gridHeight = '35%'
        const gridLeft = 80
        const gridRight = 50
        const gridTop = 50
        const gridBottom = 80
        return {
          tooltip: {
            trigger: 'none',
            padding: [10, 20, 10, 20],
            backgroundColor: 'rgba(0,0,0,0.7)',
            transitionDuration: 0,
            extraCssText: 'width: 300px; white-space: normal',
            textStyle: {
              color: '#fff',
              fontSize: 12
            },
            position: function (pos, params, el, elRect, size) {
              const obj = {}
              obj[['left', 'right'][+(pos[0] < size.viewSize[0] / 2)]] = 60
              obj[['top', 'bottom'][+(pos[1] < size.viewSize[1] / 2)]] = 20
              return obj
            },
            formatter: tooltipFormatter
          },
          axisPointer: {
            show: true,
            snap: true,
            lineStyle: {
              type: 'dashed'
            },
            label: {
              show: true,
              margin: 6,
              backgroundColor: '#556',
              color: '#fff'
            },
            link: [
              {
                xAxisId: ['xAxisLeft-yAxisTop', 'xAxisLeft-yAxisBottom']
              },
              {
                xAxisId: ['xAxisRight-yAxisTop', 'xAxisRight-yAxisBottom']
              },
              {
                yAxisId: ['xAxisLeft-yAxisTop', 'xAxisRight-yAxisTop']
              },
              {
                yAxisId: ['xAxisLeft-yAxisBottom', 'xAxisRight-yAxisBottom']
              }
            ]
          },
          xAxis: [
            makeAxis(0, 'xAxisLeft-yAxisTop', 'log2FC1', 'middle'),
            makeAxis(0, 'xAxisLeft-yAxisBottom', 'log2FC1', 'middle'),
            makeAxis(0, 'xAxisRight-yAxisTop', 'log2FC2', 'middle'),
            makeAxis(0, 'xAxisRight-yAxisBottom', 'log2FC2', 'middle')
          ],
          yAxis: [
            makeAxis(1, 'xAxisLeft-yAxisTop', 'log2FC3', 'end'),
            makeAxis(1, 'xAxisLeft-yAxisBottom', 'log2FC3', 'end'),
            makeAxis(1, 'xAxisRight-yAxisTop', 'log2FC4', 'end'),
            makeAxis(1, 'xAxisRight-yAxisBottom', 'log2FC4', 'end')
          ],
          grid: [
            {
              id: 'xAxisLeft-yAxisTop',
              left: gridLeft,
              top: gridTop,
              width: gridWidth,
              height: gridHeight
            },
            {
              id: 'xAxisLeft-yAxisBottom',
              left: gridLeft,
              bottom: gridBottom,
              width: gridWidth,
              height: gridHeight
            },
            {
              id: 'xAxisRight-yAxisTop',
              right: gridRight,
              top: gridTop,
              width: gridWidth,
              height: gridHeight
            },
            {
              id: 'xAxisRight-yAxisBottom',
              right: gridRight,
              bottom: gridBottom,
              width: gridWidth,
              height: gridHeight
            }
          ],
          dataZoom: [
            makeDataZoom({
              width: gridWidth,
              height: 20,
              left: gridLeft,
              bottom: 10,
              xAxisIndex: [0, 1]
            }),
            makeDataZoom({
              width: gridWidth,
              height: 20,
              right: gridRight,
              bottom: 10,
              xAxisIndex: [2, 3]
            }),
            makeDataZoom({
              orient: 'vertical',
              width: 20,
              height: gridHeight,
              left: 10,
              top: gridTop,
              yAxisIndex: [0, 2]
            }),
            makeDataZoom({
              orient: 'vertical',
              width: 20,
              height: gridHeight,
              left: 10,
              bottom: gridBottom,
              yAxisIndex: [1, 3]
            })
          ],
          visualMap: [
            {
              show: false,
              type: 'piecewise',
              categories: groupCategories,
              dimension: 2,
              inRange: {
                color: groupColors // ['#d94e5d','#eac736','#50a3ba']
              },
              outOfRange: {
                color: ['#ccc'] // ['#d94e5d','#eac736','#50a3ba']
              },
              top: 20,
              textStyle: {
                color: '#fff'
              },
              realtime: false
            }
          ],
          series: [
            makeSeries('xAxisLeft', 'yAxisTop'),
            makeSeries('xAxisLeft', 'yAxisBottom'),
            makeSeries('xAxisRight', 'yAxisTop'),
            makeSeries('xAxisRight', 'yAxisBottom')
          ],
          animationThreshold: 5000,
          progressiveThreshold: 5000,
          animationEasingUpdate: 'cubicInOut',
          animationDurationUpdate: 2000
        }
      }
      const fieldNames = schema
        .map(function (item) {
          return item.name
        })
        .slice(2)
      app.config = {
        xAxisLeft: 'log2FC1',
        yAxisTop: 'log2FC2',
        xAxisRight: 'log2FC3',
        yAxisBottom: 'log2FC4',
        onChange: function () {
          if (data) {
            colorBySchema[app.config.xAxisLeft] = axisColors.xAxisLeft
            colorBySchema[app.config.xAxisRight] = axisColors.xAxisRight
            colorBySchema[app.config.yAxisTop] = axisColors.yAxisTop
            colorBySchema[app.config.yAxisBottom] = axisColors.yAxisBottom
            myChart.setOption({
              xAxis: [
                {
                  name: app.config.xAxisLeft
                },
                {
                  name: app.config.xAxisLeft
                },
                {
                  name: app.config.xAxisRight
                },
                {
                  name: app.config.xAxisRight
                }
              ],
              yAxis: [
                {
                  name: app.config.yAxisTop
                },
                {
                  name: app.config.yAxisBottom
                },
                {
                  name: app.config.yAxisTop
                },
                {
                  name: app.config.yAxisBottom
                }
              ],
              series: [
                {
                  data: makeSeriesData('xAxisLeft', 'yAxisTop')
                },
                {
                  data: makeSeriesData('xAxisLeft', 'yAxisBottom')
                },
                {
                  data: makeSeriesData('xAxisRight', 'yAxisTop')
                },
                {
                  data: makeSeriesData('xAxisRight', 'yAxisBottom')
                }
              ]
            })
          }
        }
      }
      app.configParameters = {
        xAxisLeft: {
          options: fieldNames
        },
        xAxisRight: {
          options: fieldNames
        },
        yAxisTop: {
          options: fieldNames
        },
        yAxisBottom: {
          options: fieldNames
        }
      }
      axios.get('/api/ldb/CorDeff2')
        .then(res => {
          this.newdata = res.data
          data = normalizeData(this.newdata).slice(0, 1000)
          myChart.setOption((option = getOption(data)))
          console.log('完成')
        })

      option && myChart.setOption(option)
    } */
    /* cor_deff () {
      axios.get('/api/ldb/CorDeff2')
        .then(res => {
          this.newdata = res.data
          console.log(this.newdata)
          this.$nextTick(() => {
            this.myEcharts2()
          })
        })
    },
    myEcharts2 () {
      var app = {}
      var chartDom = document.getElementById('main')
      var myChart = echarts.init(chartDom)
      var option
      var Xleft = this.x_left
      var Xright = this.x_right
      var Yleft = this.y_left
      var Yright = this.y_right
      // eslint-disable-next-line camelcase

      const indices = {
        name: 0,
        group: 1,
        id: 16
      }
      const schema = [
        { name: 'gene_name', index: 0 },
        { name: 'log2FC1', index: 1 },
        { name: 'log2FC2', index: 2 },
        { name: 'log2FC3', index: 3 },
        { name: 'log2FC4', index: 4 },
        { name: 'log2FC5', index: 5 }
      ]
      const axisColors = {
        xAxisLeft: '#2A8339',
        xAxisRight: '#367DA6',
        yAxisTop: '#A68B36',
        yAxisBottom: '#BD5692'
      }
      const colorBySchema = {}
      const fieldIndices = schema.reduce(function (obj, item) {
        obj[item.name] = item.index
        return obj
      }, {})
      const groupCategories = []
      const groupColors = []
      var data = this.data
      var x_left = this.x_left
      // zlevel 为 1 的层开启尾迹特效
      myChart.getZr().configLayer(1, {
        motionBlur: true
      })
      function normalizeData (originData) {
        const groupMap = {}
        originData.forEach(function (row) {
          const groupName = row[indices.group]
          if (!groupMap.hasOwnProperty(groupName)) {
            groupMap[groupName] = 1
          }
        })
        originData.forEach(function (row) {
          row.forEach(function (item, index) {
            if (
              index !== indices.name &&
              index !== indices.group &&
              index !== indices.id
            ) {
              // Convert null to zero, as all of them under unit "g".
              row[index] = parseFloat(item) || 0
            }
          })
        })
        for (const groupName in groupMap) {
          if (groupMap.hasOwnProperty(groupName)) {
            groupCategories.push(groupName)
          }
        }
        const hStep = Math.round(300 / (groupCategories.length - 1))
        for (let i = 0; i < groupCategories.length; i++) {
          groupColors.push(echarts.color.modifyHSL('#5A94DF', hStep * i))
        }
        return originData
      }
      function makeAxis (dimIndex, id, name, nameLocation) {
        const axisColor = axisColors[id.split('-')[dimIndex]]
        colorBySchema[name] = axisColor
        return {
          id: id,
          name: name,
          nameLocation: nameLocation,
          nameGap: nameLocation === 'middle' ? 30 : 10,
          gridId: id,
          splitLine: { show: false },
          axisLine: {
            lineStyle: {
              color: axisColor
            }
          },
          axisLabel: {
            color: axisColor
          },
          axisTick: {
            lineStyle: {
              color: axisColor
            }
          }
        }
      }
      function makeSeriesData (xLeftOrRight, yTopOrBottom) {
        return data.map(function (item, idx) {
          const schemaX = app.config[xLeftOrRight]
          const schemaY = app.config[yTopOrBottom]
          return [
            item[fieldIndices[schemaX]],
            item[fieldIndices[schemaY]],
            item[1],
            item[0],
            schemaX,
            schemaY,
            idx // 6
          ]
        })
      }
      function makeSeries (xLeftOrRight, yTopOrBottom) {
        const id = xLeftOrRight + '-' + yTopOrBottom
        return {
          zlevel: 1,
          type: 'scatter',
          name: 'nutrients',
          xAxisId: id,
          yAxisId: id,
          symbolSize: 8,
          emphasis: {
            itemStyle: {
              color: '#fff'
            }
          },
          data: makeSeriesData(xLeftOrRight, yTopOrBottom)
        }
      }
      function makeDataZoom (opt) {
        return Object.assign(
          {
            type: 'slider',
            filterMode: 'empty',
            realtime: false
          },
          opt
        )
      }
      function tooltipFormatter (params) {
        // Remove duplicate by data name.
        const mapByDataName = {}
        const mapOnDim = {
          x: {},
          y: {},
          xy: {}
        }
        params.forEach(function (item) {
          const data = item.data
          const dataName = data[3]
          const mapItem = mapByDataName[dataName] || (mapByDataName[dataName] = {})
          mapItem[data[4]] = data[0]
          mapItem[data[5]] = data[1]
          mapOnDim[item.axisDim][dataName] = mapItem
        })
        Object.keys(mapByDataName).forEach(function (dataName) {
          if (mapOnDim.x[dataName] && mapOnDim.y[dataName]) {
            mapOnDim.xy[dataName] = mapByDataName[dataName]
            delete mapOnDim.x[dataName]
            delete mapOnDim.y[dataName]
          }
        })
        const resultHTML = [];
        [
          ['xy', 'CROSS'],
          ['x', 'X LINE'],
          ['y', 'Y LINE']
        ].forEach(function (dimDefine) {
          const html = []
          Object.keys(mapOnDim[dimDefine[0]]).forEach(function (dataName) {
            const mapItem = mapOnDim[dimDefine[0]][dataName]
            const valuesHTML = []
            Object.keys(mapItem).forEach(function (dataName) {
              valuesHTML.push(
                '<span style="color:' +
                colorBySchema[dataName] +
                '">' +
                dataName +
                '</span>: ' +
                mapItem[dataName]
              )
            })
            html.push(
              '<div style="margin: 10px 0">' +
              dataName +
              '<br/>' +
              valuesHTML.join('<br/>') +
              '</div>'
            )
          })
          html.length &&
          resultHTML.push(
            '<div style="margin: 10px 0">' +
            '<div style="font-size: 16px; color: #aaa">POINTS ON ' +
            dimDefine[1] +
            '</div>' +
            html.join('') +
            '</div>'
          )
        })
        return resultHTML.join('')
      }
      function getOption (data) {
        const gridWidth = '35%'
        const gridHeight = '35%'
        const gridLeft = 80
        const gridRight = 50
        const gridTop = 50
        const gridBottom = 80
        return {
          tooltip: {
            trigger: 'none',
            padding: [10, 20, 10, 20],
            backgroundColor: 'rgba(0,0,0,0.7)',
            transitionDuration: 0,
            extraCssText: 'width: 300px; white-space: normal',
            textStyle: {
              color: '#fff',
              fontSize: 12
            },
            position: function (pos, params, el, elRect, size) {
              const obj = {}
              obj[['left', 'right'][+(pos[0] < size.viewSize[0] / 2)]] = 60
              obj[['top', 'bottom'][+(pos[1] < size.viewSize[1] / 2)]] = 20
              return obj
            },
            formatter: tooltipFormatter
          },
          axisPointer: {
            show: true,
            snap: true,
            lineStyle: {
              type: 'dashed'
            },
            label: {
              show: true,
              margin: 6,
              backgroundColor: '#556',
              color: '#fff'
            },
            link: [
              {
                xAxisId: ['xAxisLeft-yAxisTop', 'xAxisLeft-yAxisBottom']
              },
              {
                xAxisId: ['xAxisRight-yAxisTop', 'xAxisRight-yAxisBottom']
              },
              {
                yAxisId: ['xAxisLeft-yAxisTop', 'xAxisRight-yAxisTop']
              },
              {
                yAxisId: ['xAxisLeft-yAxisBottom', 'xAxisRight-yAxisBottom']
              }
            ]
          },
          xAxis: [
            {
              id: 'xAxisLeft-yAxisTop',
              name: Xleft,
              nameLocation: 'middle',
              nameGap: 30,
              gridId: 'xAxisLeft-yAxisTop',
              splitLine: { show: false },
              axisLine: {
                lineStyle: {
                  color: '#012257'
                }
              },
              axisLabel: {
                color: '#012257'
              },
              axisTick: {
                lineStyle: {
                  color: '#012257'
                }
              }
            },
            {
              id: 'xAxisLeft-yAxisBottom',
              name: Xleft,
              nameLocation: 'middle',
              nameGap: 30,
              gridId: 'xAxisLeft-yAxisBottom',
              splitLine: { show: false },
              axisLine: {
                lineStyle: {
                  color: '#012257'
                }
              },
              axisLabel: {
                color: '#012257'
              },
              axisTick: {
                lineStyle: {
                  color: '#012257'
                }
              }
            },
            {
              id: 'xAxisRight-yAxisTop',
              name: Xright,
              nameLocation: 'middle',
              nameGap: 30,
              gridId: 'xAxisRight-yAxisTop',
              splitLine: { show: false },
              axisLine: {
                lineStyle: {
                  color: '#012257'
                }
              },
              axisLabel: {
                color: '#012257'
              },
              axisTick: {
                lineStyle: {
                  color: '#012257'
                }
              }
            },
            {
              id: 'xAxisRight-yAxisBottom',
              name: Xright,
              nameLocation: 'middle',
              nameGap: 30,
              gridId: 'xAxisRight-yAxisBottom',
              splitLine: { show: false },
              axisLine: {
                lineStyle: {
                  color: '#012257'
                }
              },
              axisLabel: {
                color: '#012257'
              },
              axisTick: {
                lineStyle: {
                  color: '#012257'
                }
              }
            }
            // makeAxis(0, 'xAxisLeft-yAxisTop', 'log2FC1', 'middle'),
            /!*      makeAxis(0, 'xAxisLeft-yAxisBottom', 'log2FC1', 'middle'),
                  makeAxis(0, 'xAxisRight-yAxisTop', 'log2FC3', 'middle'),
                  makeAxis(0, 'xAxisRight-yAxisBottom', 'log2FC3', 'middle') *!/
          ],
          yAxis: [
            {
              id: 'xAxisLeft-yAxisTop',
              name: Yleft,
              nameLocation: 'middle',
              nameGap: 30,
              gridId: 'xAxisLeft-yAxisTop',
              splitLine: { show: false },
              axisLine: {
                lineStyle: {
                  color: '#012257'
                }
              },
              axisLabel: {
                color: '#012257'
              },
              axisTick: {
                lineStyle: {
                  color: '#012257'
                }
              }
            },
            {
              id: 'xAxisLeft-yAxisBottom',
              name: Yleft,
              nameLocation: 'middle',
              nameGap: 30,
              gridId: 'xAxisLeft-yAxisBottom',
              splitLine: { show: false },
              axisLine: {
                lineStyle: {
                  color: '#012257'
                }
              },
              axisLabel: {
                color: '#012257'
              },
              axisTick: {
                lineStyle: {
                  color: '#012257'
                }
              }
            },
            {
              id: 'xAxisRight-yAxisTop',
              name: Yright,
              nameLocation: 'middle',
              nameGap: 30,
              gridId: 'xAxisRight-yAxisTop',
              splitLine: { show: false },
              axisLine: {
                lineStyle: {
                  color: '#012257'
                }
              },
              axisLabel: {
                color: '#012257'
              },
              axisTick: {
                lineStyle: {
                  color: '#012257'
                }
              }
            },
            {
              id: 'xAxisRight-yAxisBottom',
              name: Yright,
              nameLocation: 'middle',
              nameGap: 30,
              gridId: 'xAxisRight-yAxisBottom',
              splitLine: { show: false },
              axisLine: {
                lineStyle: {
                  color: '#012257'
                }
              },
              axisLabel: {
                color: '#012257'
              },
              axisTick: {
                lineStyle: {
                  color: '#012257'
                }
              }
            }
            /!*    makeAxis(1, 'xAxisLeft-yAxisTop', 'log2FC2', 'end'),
                makeAxis(1, 'xAxisLeft-yAxisBottom', 'log2FC2', 'end'),
                makeAxis(1, 'xAxisRight-yAxisTop', 'log2FC4', 'end'),
                makeAxis(1, 'xAxisRight-yAxisBottom', 'log2FC4', 'end') *!/
          ],
          grid: [
            {
              id: 'xAxisLeft-yAxisTop',
              left: gridLeft,
              top: gridTop,
              width: gridWidth,
              height: gridHeight
            },
            {
              id: 'xAxisLeft-yAxisBottom',
              left: gridLeft,
              bottom: gridBottom,
              width: gridWidth,
              height: gridHeight
            },
            {
              id: 'xAxisRight-yAxisTop',
              right: gridRight,
              top: gridTop,
              width: gridWidth,
              height: gridHeight
            },
            {
              id: 'xAxisRight-yAxisBottom',
              right: gridRight,
              bottom: gridBottom,
              width: gridWidth,
              height: gridHeight
            }
          ],
          dataZoom: [
            makeDataZoom({
              width: gridWidth,
              height: 20,
              left: gridLeft,
              bottom: 10,
              xAxisIndex: [0, 1]
            }),
            makeDataZoom({
              width: gridWidth,
              height: 20,
              right: gridRight,
              bottom: 10,
              xAxisIndex: [2, 3]
            }),
            makeDataZoom({
              orient: 'vertical',
              width: 20,
              height: gridHeight,
              left: 10,
              top: gridTop,
              yAxisIndex: [0, 2]
            }),
            makeDataZoom({
              orient: 'vertical',
              width: 20,
              height: gridHeight,
              left: 10,
              bottom: gridBottom,
              yAxisIndex: [1, 3]
            })
          ],
          visualMap: [
            {
              show: false,
              type: 'piecewise',
              categories: groupCategories,
              dimension: 2,
              inRange: {
                color: groupColors // ['#d94e5d','#eac736','#50a3ba']
              },
              outOfRange: {
                color: ['#ccc'] // ['#d94e5d','#eac736','#50a3ba']
              },
              top: 20,
              textStyle: {
                color: '#fff'
              },
              realtime: false
            }
          ],
          series: [
            makeSeries('xAxisLeft', 'yAxisTop'),
            makeSeries('xAxisLeft', 'yAxisBottom'),
            makeSeries('xAxisRight', 'yAxisTop'),
            makeSeries('xAxisRight', 'yAxisBottom')
          ],
          animationThreshold: 5000,
          progressiveThreshold: 5000,
          animationEasingUpdate: 'cubicInOut',
          animationDurationUpdate: 2000
        }
      }
      const fieldNames = schema
        .map(function (item) {
          return item.name
        })
        .slice(2)
      app.config = {
        xAxisLeft: Xleft,
        yAxisTop: Xright,
        xAxisRight: Yleft,
        yAxisBottom: Yright,
        onChange: function () {
          if (data) {
            colorBySchema[app.config.xAxisLeft] = axisColors.xAxisLeft
            colorBySchema[app.config.xAxisRight] = axisColors.xAxisRight
            colorBySchema[app.config.yAxisTop] = axisColors.yAxisTop
            colorBySchema[app.config.yAxisBottom] = axisColors.yAxisBottom
            myChart.setOption({
              xAxis: [
                {
                  name: app.config.xAxisLeft
                },
                {
                  name: app.config.xAxisLeft
                },
                {
                  name: app.config.xAxisRight
                },
                {
                  name: app.config.xAxisRight
                }
              ],
              yAxis: [
                {
                  name: app.config.yAxisTop
                },
                {
                  name: app.config.yAxisBottom
                },
                {
                  name: app.config.yAxisTop
                },
                {
                  name: app.config.yAxisBottom
                }
              ],
              series: [
                {
                  data: makeSeriesData('xAxisLeft', 'yAxisTop')
                },
                {
                  data: makeSeriesData('xAxisLeft', 'yAxisBottom')
                },
                {
                  data: makeSeriesData('xAxisRight', 'yAxisTop')
                },
                {
                  data: makeSeriesData('xAxisRight', 'yAxisBottom')
                }
              ]
            })
          }
        }
      }
      app.configParameters = {
        xAxisLeft: {
          options: fieldNames
        },
        xAxisRight: {
          options: fieldNames
        },
        yAxisTop: {
          options: fieldNames
        },
        yAxisBottom: {
          options: fieldNames
        }
      }
      data = normalizeData(this.newdata).slice(0, 1000)
      myChart.setOption((option = getOption(data)))
      option && myChart.setOption(option)
    } */
  }
  /* mounted () {
    this.myEcharts()
  } */
}

</script>

<style lang="scss" scoped>
.titleText{
  font-size: large;
  color: black;
  font-weight: bold;
}
.parText{
  font-size: small;
  color: black;
  font-size: 0.95em;
}
.widget-left{
  display: inline-block;
  vertical-align: center;
  text-align: center;
  width: 40%;
}
.widget-right{
  display: inline-block;

}

</style>
