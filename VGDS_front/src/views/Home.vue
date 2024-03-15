<template>
  <div class="ml-5 mr-5">
<!--    <v-card color="#fffadd" height="250" class="pa-0">
      <v-row>
        <v-col cols="8">
        </v-col>
        <v-col cols="4">
          <v-img :src=src3  width="100%" height="250" ></v-img>
        </v-col>
      </v-row>

    </v-card>-->
    <v-img :src=src4  class="grey darken-4 align-end " >
     <v-row>
       <v-col cols="1">
       </v-col>
       <v-col cols="6">
<!--         <v-btn
           color="#192d47"
           dark
           class="mt-16 mb-2 ml-16">How To Use</v-btn>-->
       </v-col>
     </v-row>
    </v-img>
      <div class="d-flex justify-start pt-5  ">
        <p class="titleText mb-2">Welcome to the VGDS! </p>
      </div>
    <v-divider></v-divider>
      <div class="d-flex justify-start ">
        <p class="pt-2 mb-2 " style="text-align:left">VGDS:The first multi-dimensional data analysis platform that integrates bulk RNA-seq, scRNA-seq and literature data with a focus on HCC prognosis.In the current version, we have: </p>
      </div>
    <v-row class="mt-10 mb-5">
      <v-col cols="6">
       <v-card
         flat
         height="300">
         <v-row  >
           <v-col cols="6">
             <v-card
               :class="`rounded-xl`"
             height="113">

               <v-card height="84" width="84" color="#192d47" :class="`rounded-xl`"
                       style="position: absolute;top:-20px;left:20px"
                       elevation="13">
                 <v-icon color="white" class="mt-5" large>mdi-crosshairs-gps</v-icon>
               </v-card>
               <div class="d-flex flex-row-reverse pr-3 ">
                 <h5 class="mt-5" style="color: lightslategrey" >Including Targets</h5>
               </div>
               <div class="d-flex flex-row-reverse pr-10 ">
                 <h2 class="mt-3" style="color:#192d47">2678</h2>
               </div>
             </v-card>
           </v-col>
           <v-col cols="6">
             <v-card
               :class="`rounded-xl`"
               height="113">

               <v-card height="84" width="84" color="#192d47" :class="`rounded-xl`"
                       style="position: absolute;top:-20px;left:20px"
                       elevation="13">
                 <v-icon color="white" class="mt-5" large>mdi-clipboard-text</v-icon>
               </v-card>
               <div class="d-flex flex-row-reverse pr-3">
                 <h5 class="mt-5" style="color: lightslategrey" >Including Articles</h5>
               </div>
               <div class="d-flex flex-row-reverse pr-10 ">
                 <h2 class="mt-3" style="color:#192d47 ">7250</h2>
               </div>
             </v-card>
           </v-col>
         </v-row>
         <v-row class="mt-11">
           <v-col cols="6">
             <v-card
               :class="`rounded-xl`"
               height="113">

               <v-card height="84" width="84" color="#192d47" :class="`rounded-xl`"
                       style="position: absolute;top:-20px;left:20px"
                       elevation="13">
                 <v-icon color="white" class="mt-5" large>mdi-view-list-outline</v-icon>
               </v-card>
               <div class="d-flex flex-row-reverse pr-3 ">
                 <h5 class="mt-5" style="color: lightslategrey" >Including Samples</h5>
               </div>
               <div class="d-flex flex-row-reverse pr-10 ">
                 <h2 class="mt-3" style="color:#192d47">1605</h2>
               </div>
             </v-card>
           </v-col>
           <v-col cols="6">
             <v-card
               :class="`rounded-xl`"
               height="113">

               <v-card height="84" width="84" color="#192d47" :class="`rounded-xl`"
                       style="position: absolute;top:-20px;left:20px"
                       elevation="13">
                 <v-icon color="white" class="mt-5" large>mdi-google-circles-communities</v-icon>
               </v-card>
               <div class="d-flex flex-row-reverse pr-3">
                 <h5 class="mt-5" style="color: lightslategrey" >Including Cells</h5>
               </div>
               <div class="d-flex flex-row-reverse pr-10 ">
                 <h2 class="mt-3" style="color:#192d47 ">18，801</h2>
               </div>
             </v-card>
           </v-col>
         </v-row>

       </v-card>
      </v-col>
      <v-col cols="6">
        <v-card
          :class="`rounded-xl`"
          height="300px">
          <v-row>
              <v-card height=260  color="#192d47" :class="`rounded-xl`"
                      style="position: absolute;top:-20px;right:20px;left:20px;"
                      elevation="13">
                <div class="Echarts">
                  <div id="diff" style="width: 100%;height:280px;"></div>
                </div>
              </v-card>
          </v-row>
            <v-row  style="position: absolute;bottom:-15px" >
              <v-col cols="1">

              </v-col>
              <v-col cols="4">
                <div class="d-flex">
                  <p class="pr-3 mt-3" >X</p>
                  <v-select
                    style="transform: scale(0.8)"
                    class="d-flex justify-left pb-0"
                    :items="logFC"
                    solo
                    flat
                    dense
                    outlined
                    color="#55967e"
                    v-model="x_log"
                  ></v-select>
                </div>
              </v-col>
              <v-col cols="4">
                <div class="d-flex">
                  <p class="pr-3 mt-3" >Y</p>
                  <v-select
                    style="transform: scale(0.8)"
                    class="d-flex justify-left pb-0"
                    :items="logFC"
                    solo
                    flat
                    dense
                    outlined
                    color="#55967e"
                    v-model="y_log"
                  ></v-select>
                </div>
              </v-col>
              <v-col cols="2">
                <v-btn
                  class="mt-2"
                  small
                  @click="changeChart">Print</v-btn>
              </v-col>
              <v-col cols="1">

              </v-col>
            </v-row>

        </v-card>

      </v-col>
    </v-row>

<!--      <v-row class="mt-2" >
        <v-col cols="4">
          <v-card height="100" class="d-flex justify-start" >
            <div class="widget-left d-flex justify-center ">
              <v-icon  color="red" class="align-center display-3" x-large>mdi-chart-donut-variant</v-icon>
            </div>
            <div class="widget-right ">
              <h3 class="mt-3">Target</h3><br/>
              <h3>2678</h3>
            </div>
          </v-card>
        </v-col>
        <v-col cols="4">
          <v-card height="100" class="d-flex justify-start" >
            <div class="widget-left d-flex justify-center ">
              <v-icon  color="#192d47" class="align-center display-3" x-large>mdi-file-document-multiple-outline</v-icon>
            </div>
            <div class="widget-right ">
              <h3 class="mt-3">Article</h3><br/>
              <h3>10289</h3>
            </div>
          </v-card>
        </v-col>
        <v-col cols="4">
          <v-card height="100" class="d-flex justify-start" >
            <div class="widget-left d-flex justify-center ">
              <v-icon  color="#55967e" class="align-center display-3" x-large>mdi-chart-box-outline</v-icon>
            </div>
            <div class="widget-right ">
              <h3 class="mt-3">Analyze</h3><br/>
              <h3>10098</h3>
            </div>
          </v-card>
        </v-col>
      </v-row>-->
<!--    <v-card class="mt-5">
      <v-row>
        <v-col cols="3">
          <div class="d-flex pl-3">
            <p >x_left</p>
            <v-select
              style="zoom:90%"
              class="d-flex justify-left pb-0"
              :items="logFC"
              solo
              flat
              dense
              outlined
              color="#55967e"
              v-model="x_left"
            ></v-select>
          </div>
        </v-col>
        <v-col cols="3">
          <div class="d-flex pl-3">
            <p >x_right</p>
            <v-select
              style="zoom:90%"
              class="d-flex justify-left pb-0"
              :items="logFC"
              solo
              flat
              dense
              outlined
              color="#55967e"
              v-model="x_right"
            ></v-select>
          </div>
        </v-col>
        <v-col cols="3">
          <div class="d-flex pl-3">
            <p >y_left</p>
            <v-select
              style="zoom:90%"
              class="d-flex justify-left pb-0"
              :items="logFC"
              solo
              flat
              dense
              outlined
              color="#55967e"
              v-model="y_left"
            ></v-select>
          </div>
        </v-col>
        <v-col cols="3">
          <div class="d-flex pl-3">
            <p >y_right</p>
            <v-select
              style="zoom:90%"
              class="d-flex justify-left pb-0"
              :items="logFC"
              solo
              flat
              dense
              outlined
              color="#55967e"
              v-model="y_right"
            ></v-select>
            <v-btn
            @click="myEcharts2">分析</v-btn>
          </div>
        </v-col>
      </v-row>
      <div class="Echarts">
        <div id="main" style="width: 100%;height:650px;"></div>
      </div>
    </v-card>-->
    <v-card
      elevation="4"
      :class="`rounded-xl`"
     >
      <v-carousel
        cycle
        hide-delimiters
        height="auto">
        <v-carousel-item
          v-for="item in pics1"
          :key="item.url"
        ><v-img  :src="item.url"></v-img>
        </v-carousel-item>
      </v-carousel>

    </v-card>
  </div>
</template>

<script>
import axios from 'axios'
// import * as echarts from 'echarts'

export default {
  name: 'Home',
  data () {
    return {
      /* src1: require('@/assets/background.png'),
      src2: require('@/assets/14.jpg'),
      src3: require('@/assets/15.png'), */
      src4: require('@/assets/17.jpg'),
      /*  pics: [
        { url: require('../assets/slider1.png') },
        { url: require('../assets/slider2.png') }
      ], */
      pics1: [
        { url: require('../assets/process.jpg') },
        { url: require('../assets/diff.jpg') },
        { url: require('../assets/cor.jpg') },
        { url: require('../assets/gene.jpg') }
      ],
      logFC: ['log2FC1', 'log2FC2', 'log2FC3', 'log2FC4', 'log2FC5'],
      co1_list: [],
      co2_list: [],
      co3_list: [],
      co4_list: [],
      newdata: [],
      gene: ['A', 'B', 'C'],
      x_log: 'log2FC5',
      x: [],
      y_log: 'log2FC1',
      y: [],
      log2FC1: [],
      log2FC2: [],
      log2FC3: [],
      log2FC4: [],
      log2FC5: []
    }
  },
  methods: {
    cor_deff () {
      axios.get('/api/ldb/CorDeff2')
        .then(res => {
          this.newdata = res.data
          this.gene = res.data.gene
          this.log2FC1 = res.data.log2FC1
          this.log2FC2 = res.data.log2FC2
          this.log2FC3 = res.data.log2FC3
          this.log2FC4 = res.data.log2FC4
          this.log2FC5 = res.data.log2FC5
          this.x = this.log2FC5
          this.y = this.log2FC1
          console.log(res.data)
          this.$nextTick(() => {
            // this.myEcharts2()
            this.myDeffcharts()
          })
        })
    },
    changeChart () {
      if (this.x_log === 'log2FC1') {
        this.x = this.log2FC1
      } else if (this.x_log === 'log2FC2') {
        this.x = this.log2FC2
      } else if (this.x_log === 'log2FC3') {
        this.x = this.log2FC3
      } else if (this.x_log === 'log2FC4') {
        this.x = this.log2FC4
      } else if (this.x_log === 'log2FC5') {
        this.x = this.log2FC5
      }
      if (this.y_log === 'log2FC1') {
        this.y = this.log2FC1
      } else if (this.y_log === 'log2FC2') {
        this.y = this.log2FC2
      } else if (this.y_log === 'log2FC3') {
        this.y = this.log2FC3
      } else if (this.y_log === 'log2FC4') {
        this.y = this.log2FC4
      } else if (this.y_log === 'log2FC5') {
        this.y = this.log2FC5
      }
      this.myDeffcharts()
    },
    myDeffcharts () {
      // 基于准备好的dom，初始化echarts实例
      var myChart = this.$echarts.init(document.getElementById('diff'))
      var X = this.x
      var Y = this.y
      var gene = this.gene
      // 指定图表的配置项和数据
      var option = {
        grid: {
          show: false,
          // borderWidth: 1,
          // borderColor: 'black',
          left: '7%',
          right: '7%',
          top: '10%',
          bottom: '10%',
          containLabel: true
        },
        tooltip: {
          position: 'top',
          formatter: function (params) {
            var str =
              'Gene:' +
              params.data[2]
            return str
          }
        },
        xAxis: [
          {
            type: 'value',
            scale: false,
            axisLabel: {
              formatter: '{value}'
            },
            axisLine: { show: false },
            axisTick: { show: false },
            splitLine: {
              show: false
            },
            name: 'X',
            nameLocation: 'middle',
            nameTextStyle: {
              color: 'black',
              fontSize: 10,
              padding: 2
            }
          }
        ],
        yAxis: [
          {
            type: 'value',
            scale: false,
            axisLabel: {
              formatter: '{value}'
            },
            axisLine: { show: false },
            axisTick: { show: false },
            splitLine: {
              show: false
            },
            name: 'Y',
            nameLocation: 'middle',
            nameTextStyle: {
              color: 'black',
              fontSize: 10,
              padding: 2
            }
          }
        ],
        /* xAxis: [
          {
            type: 'value',
            scale: true,
            axisLabel: {
              formatter: '{value}'
            },
            splitLine: {
              show: false
            },
            // name: 'LogFoldchange',
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
            // name: '-log10(pvalue)',
            nameLocation: 'middle',
            nameTextStyle: {
              color: 'black',
              fontWeight: 'bolder',
              fontSize: 16,
              padding: 10
            }
          }
        ], */
        color: ['white'],
        dataZoom: [
          {
            type: 'inside',
            xAxisIndex: [0],
            start: 1,
            end: 100
          }],
        series: [
          {
            type: 'scatter',
            symbolSize: 5,
            // data.map(function (item, idx) {
            //   return [item[2], item[3], item[1], idx];
            // }),
            // data: newdata.map(function (item) {
            //   return [item[0], item[1], item[2]];
            // }),
            data: gene.map(function (key, value) {
              return [X[value], Y[value], key]
            })
            // data: gene.map(key,value) => [X[value],Y[value],key]
          }
        ]
      }

      // 使用刚指定的配置项和数据显示图表。
      myChart.setOption(option)
    }
  },
  created () {
    this.cor_deff()
  }
}
</script>
<style lang="scss" scoped>
.titleText{
  font-size: large;
  color: black;
  font-weight: bold;
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
