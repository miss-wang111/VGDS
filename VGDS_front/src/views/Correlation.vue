<template>
  <div class="ml-5 mr-5">
    <v-container>
      <v-row>
        <v-col cols="8">
          <div class="d-flex justify-left">
            <h2 style="color:#6D819C " class="mt-n3 pt-3 pb-0 mb-0"> Correlation Analysis</h2>
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
      <p style="color:#6D819C " class="d-flex justify-left">In this page, You can do correlation analysis for {{GLOBAL.Dataset[0].Dataset_Num}}</p>
      <v-card
        height="270">
        <v-row>
          <v-col cols="4">
            <div class="pr-2 ml-5">
              <p class="d-flex justify-left textSmall">Gene Symbol ID</p>
                <v-textarea
                  class="textSmall"
                  color="#55967e"
                  outlined
                  height="200"
                  v-model="geneChoose"
                  placeholder="Input Symbols split by ','or '\n'"
                ></v-textarea>
            </div>
          </v-col>
          <v-col cols="5">
            <p class="d-flex textSmall">Sample Data</p>
<!--                        <v-radio-group
                            dense
                            v-if="this.GLOBAL.Dataset[0].Dataset_Num === 'HCCMRDB10'"
                            v-model="corr_sample"
                            style="zoom:80%">
              <div class="d-flex textSmall">
                <v-radio    color="#55967e" class=" mt-0 " label="adjacent tissue from primary tumors"  value="TCGA_正常_TPM"></v-radio>
                <v-radio    color="#55967e" class=" mt-0 mx-16 mb-2 " label="primary tumors"  value="TCGA_肿瘤_TPM"></v-radio>
              </div>
              <div class="d-flex">
                <v-radio   color="#55967e" class=" mt-0 " label="normal liver tissue" value="TCGA-GTEx_正常_TPM"></v-radio>
&lt;!&ndash;                <v-radio   color="#55967e" class=" mt-0 mx-5 mb-2" label="TCGA-GETx_Tumor" value="TCGA-GTEx_肿瘤_TPM"></v-radio>&ndash;&gt;
              </div>
              <div class="d-flex">
                <v-radio  color="#55967e" class=" mt-0 " label="primary tumors：metastases" value="转移_TPM"></v-radio>
                <v-radio color="#55967e" class=" mt-0 mx-10 mb-2" label="primary tumors：metastases-free" value="非转移_TPM"></v-radio>
              </div>
              <div class="d-flex">
                <v-radio color="#55967e" class=" mt-0 " label="primary tumors：recurrent" value="复发_TPM"></v-radio>
                <v-radio color="#55967e" class=" mt-0 mx-9 mb-2" label="primary tumors：non-recurrent" value="未复发_TPM"></v-radio>
              </div>
&lt;!&ndash;              <v-radio color="#55967e" class=" mt-0 " label="TCGA_Normal & Tumor" value="TCGA_正常肿瘤_TPM"></v-radio>
              <v-radio color="#55967e" class=" mt-0 " label="TCGA-GETx_Normal & Tumor" value="TCGA-GTEx_正常肿瘤_TPM"></v-radio>
              <v-radio color="#55967e" class=" mt-0 " label="TCGA_Non-Metastasis & Metastasis " value="非转移转移_TPM"></v-radio>
              <v-radio color="#55967e" class=" mt-0 " label="TCGA_Non-Recurrence & Recurrence " value="TCGA_未复发复发_TPM"></v-radio>
              &ndash;&gt;
                          &lt;!&ndash;              <v-radio
                v-for="item in genSample"
                :label="item"
                :key="item"
                :value="item"
                color="#55967e"
              ></v-radio>&ndash;&gt;
            </v-radio-group>-->
            <v-radio-group dense
                           style="zoom:80%"
                           v-model="corr_sample">
              <v-radio
                v-for="item in corr_samples"
                :label="item"
                :key="item"
                :value="item"
                color="#55967e"
              ></v-radio>
            </v-radio-group>
          </v-col>
          <v-col cols="3">
            <p class="d-flex justify-left textSmall">Correlation Coefficient </p>
            <v-radio-group  dense
                            v-model="Coefficient_method ">
              <v-radio
                style="zoom:80%"
                v-for="item in Coefficient"
                :label="item"
                :key="item"
                :value="item"
                color="#55967e"
              ></v-radio>
            </v-radio-group>
            <p class="d-flex justify-left textExp">Choose a correlation coefficient for analysis</p>
            <div class="d-flex ml-5">
              <v-btn color="#55967e"
                     dark
                     small
                     @click.stop=Correlation >
                Analyze
              </v-btn>

            </div>
          </v-col>
        </v-row>
      </v-card>
      <v-progress-linear
        class ="d-flex mt-0 pt--0 "
        color="#55967e"
        v-if="this.linear === true"
      ></v-progress-linear>
        <v-alert
          v-if="alert === true"
          class="mt-5"
          outlined
          type="error">
          This sample did not contain the gene {{miss}}
        </v-alert>
      <div class="d-flex justify-center">
        <v-card class="mt-5"
                flat
                v-if="table===true">
          <div v-if="gen_list.length>10">
            <template>
              <!--创建一个echarts的容器-->
              <div id="plot1" style="width:100%; height:800px"></div>
            </template>
          </div>
          <div v-else>
            <template>
              <!--创建一个echarts的容器-->
              <div id="plot1" style="width:1000px; height:800px"></div>
            </template>
          </div>
          <template
          >
            <v-data-table
              dense
              flat
              :headers="headers"
              :items="gene_corr"
              disable-pagination
              hide-default-footer
              class="elevation-1 "
            >
            </v-data-table>
          </template>
        </v-card>
      </div>
    </v-container>
  </div>
</template>

<script>
import axios from 'axios'

var echarts = require('echarts')
export default {
  name: 'Correlation',
  data () {
    return {
      Coefficient: ['pearson', 'spearman', 'kendall'],
      corr_samples: [],
      corr_sample: '',
      corr_sample1: '',
      Coefficient_method: 'pearson',
      geneChoose: '',
      geneWrite: '',
      table: false,
      linear: false,
      gen_list: [],
      char_list: [],
      headers: [],
      gene_corr: [],
      miss: '',
      loading: false,
      alert: false
    }
  },
  methods: {
    Correlation () {
      this.linear = true
      this.table = false
      this.alert = false
      axios.post('/api/ldb/Correlation', { dataset: this.GLOBAL.Dataset[0].Dataset_Num, corr_sample: this.corr_sample, gene_list: this.geneChoose, methods: this.Coefficient_method })
        .then(res => {
          if ('char_list' in res.data) {
            // eslint-disable-next-line no-eval
            this.gene_corr = eval(res.data.cor_table_list)
            // eslint-disable-next-line no-eval
            this.headers = eval(res.data.header)
            this.gen_list = res.data.gene_list
            this.char_list = res.data.char_list
            this.miss = res.data.missing
            this.table = true
            this.linear = false
            this.$nextTick(() => {
              var myChartBig1 = echarts.init(document.getElementById('plot1'))
              var genes = this.gen_list
              // eslint-disable-next-line no-unused-vars
              var data = this.char_list
              myChartBig1.setOption({
                title: [
                  {
                    text: ' Correlation Coefficient',
                    textStyle: {
                      fontSize: 15,
                      color: '#6D819C'
                    },
                    left: 'center'
                  }
                ],
                toolbox: {
                  show: true,
                  feature: {
                    restore: { show: true },
                    saveAsImage: { show: true }
                  }
                },
                dataZoom: [
                  {
                    type: 'inside',
                    xAxisIndex: [0],
                    start: 1,
                    end: 100
                  },
                  {
                    type: 'inside',
                    yAxisIndex: [0],
                    start: 0,
                    end: 100
                  }
                ],
                tooltip: {
                  position: 'top',
                  // formatter: '{b0}:{c0[0]}<br/>{b1}: {c0}'
                  formatter: function (it) {
                    console.log(it)
                    return it.seriesName + '<br/>' + it.name + ':' + it.value[2]
                  }
                },
                backgroundColor: '#fff',
                grid: {
                  left: '10%',
                  height: '80%',
                  width: '80%',
                  top: '10%'
                },
                xAxis: {
                  type: 'category',
                  data: genes,
                  name: 'Gene Symbol',
                  splitLine: {
                    show: true,
                    lineStyle: {
                      color: ['#315070'],
                      width: 1,
                      type: 'solid'
                    }
                  },
                  splitArea: {
                    show: false
                  }
                },
                yAxis: {
                  type: 'category',
                  data: genes,
                  name: 'Gene Symbol',
                  splitLine: {
                    show: true,
                    lineStyle: {
                      color: ['#315070'],
                      width: 1,
                      type: 'solid'
                    }
                  },
                  splitArea: {
                    show: false
                  }
                },
                visualMap: {
                  min: -1,
                  max: 1,
                  calculable: true,
                  orient: 'horizontal',
                  left: 'center',
                  bottom: '2%',
                  inRange: {
                    color: ['#053061', '#e3dede', '#69011F']
                  }
                },
                series: [{
                  name: 'Correlation Coefficient',
                  type: 'scatter',
                  data: data,
                  // symbolSize: 35,
                  symbolSize: function (val) {
                    return Math.abs(val[2]) / 0.0224
                  },
                  label: {
                    show: false
                  },
                  emphasis: {
                    itemStyle: {
                      shadowBlur: 10,
                      shadowColor: 'rgba(0, 0, 0, 0.5)'
                      /* color: {
                        type: 'linear',
                        x: 0,
                        y: 0,
                        x2: 0,
                        y2: 1,
                        colorStops: [{
                          offset: 0,
                          color: 'red'
                        }, { offset: 1, color: 'blue' }]
                      } */
                    },
                    focus: 'self'
                  }
                }]
              })
            })
          } else {
            this.miss = res.data.missing
            this.linear = false
            this.alert = true
          }
          // console.log(this.sampleChoose, this.geneChoose, this.Coefficient_method)
          console.log(typeof (res.data))
          console.log('char_list' in res.data)
        })
        .catch(err => {
          console.log(err)
        })
      /* axios.post('/api/ldb/Correlation', { data_path: this.sampleChoose, gene_list: this.geneChoose, methods: this.Coefficient_method })
        .then(res => {
          if ('char_list' in res.data) {
            // eslint-disable-next-line no-eval
            this.gene_corr = eval(res.data.cor_table_list)
            // eslint-disable-next-line no-eval
            this.headers = eval(res.data.header)
            this.gen_list = res.data.gene_list
            this.char_list = res.data.char_list
            this.miss = res.data.missing
            this.table = true
            this.linear = false
            this.$nextTick(() => {
              var myChartBig1 = echarts.init(document.getElementById('plot1'))
              var genes = this.gen_list
              // eslint-disable-next-line no-unused-vars
              var data = this.char_list
              myChartBig1.setOption({
                title: [
                  {
                    text: ' Correlation Coefficient',
                    textStyle: {
                      fontSize: 15,
                      color: '#6D819C'
                    },
                    left: 'center'
                  }
                ],
                toolbox: {
                  show: true,
                  feature: {
                    restore: { show: true },
                    saveAsImage: { show: true }
                  }
                },
                dataZoom: [
                  {
                    type: 'inside',
                    xAxisIndex: [0],
                    start: 1,
                    end: 100
                  },
                  {
                    type: 'inside',
                    yAxisIndex: [0],
                    start: 0,
                    end: 100
                  }
                ],
                tooltip: {
                  position: 'top',
                  // formatter: '{b0}:{c0[0]}<br/>{b1}: {c0}'
                  formatter: function (it) {
                    console.log(it)
                    return it.seriesName + '<br/>' + it.name + ':' + it.value[2]
                  }
                },
                backgroundColor: '#fff',
                grid: {
                  left: '10%',
                  height: '80%',
                  width: '80%',
                  top: '10%'
                },
                xAxis: {
                  type: 'category',
                  data: genes,
                  name: 'Gene Symbol',
                  splitLine: {
                    show: true,
                    lineStyle: {
                      color: ['#315070'],
                      width: 1,
                      type: 'solid'
                    }
                  },
                  splitArea: {
                    show: false
                  }
                },
                yAxis: {
                  type: 'category',
                  data: genes,
                  name: 'Gene Symbol',
                  splitLine: {
                    show: true,
                    lineStyle: {
                      color: ['#315070'],
                      width: 1,
                      type: 'solid'
                    }
                  },
                  splitArea: {
                    show: false
                  }
                },
                visualMap: {
                  min: -1,
                  max: 1,
                  calculable: true,
                  orient: 'horizontal',
                  left: 'center',
                  bottom: '2%',
                  inRange: {
                    color: ['#053061', '#e3dede', '#69011F']
                  }
                },
                series: [{
                  name: 'Correlation Coefficient',
                  type: 'scatter',
                  data: data,
                  // symbolSize: 35,
                  symbolSize: function (val) {
                    return Math.abs(val[2]) / 0.0224
                  },
                  label: {
                    show: false
                  },
                  emphasis: {
                    itemStyle: {
                      shadowBlur: 10,
                      shadowColor: 'rgba(0, 0, 0, 0.5)'
                      /!* color: {
                        type: 'linear',
                        x: 0,
                        y: 0,
                        x2: 0,
                        y2: 1,
                        colorStops: [{
                          offset: 0,
                          color: 'red'
                        }, { offset: 1, color: 'blue' }]
                      } *!/
                    },
                    focus: 'self'
                  }
                }]
              })
            })
          } else {
            this.miss = res.data.missing
            this.linear = false
            this.alert = true
          }
          // console.log(this.sampleChoose, this.geneChoose, this.Coefficient_method)
          console.log(typeof (res.data))
          console.log('char_list' in res.data)
        })
        .catch(err => {
          console.log(err)
        }) */
    },
    changeChoice1 () {
      if (this.GLOBAL.Dataset[0].Dataset_Num === 'HCCMRDB1') {
        this.corr_samples = ['tumor：Bone metastasis', 'tumor：Metastases-free', 'adjacent：Bone metastasis', 'adjacent：Metastases-free']
        // this.corr_samples = ['瘤内骨转移', '瘤内非转移', '瘤周骨转移', '瘤周非转移']
      } else if (this.GLOBAL.Dataset[0].Dataset_Num === 'HCCMRDB2') {
        this.corr_samples = ['tumor：lymph node Metastasis', 'tumor：Metastases-free', 'adjacent：lymph node Metastasis', 'adjacent：Metastases-free']
        // this.corr_samples = ['瘤内淋巴转移', '瘤内非转移', '瘤周淋巴转移', '瘤周非转移']
      } else if (this.GLOBAL.Dataset[0].Dataset_Num === 'HCCMRDB3') {
        this.corr_samples = ['primary tumors：metastases', 'metastasis tumor', 'primary tumors：metastases-free']
      } else if (this.GLOBAL.Dataset[0].Dataset_Num === 'HCCMRDB4') {
        this.corr_samples = ['primary tumors', 'metastasis tumor', 'primary tumors：metastases-free']
      } else if (this.GLOBAL.Dataset[0].Dataset_Num === 'HCCMRDB6') {
        this.corr_samples = ['primary tumors', 'recurrent tumors']
      } else if (this.GLOBAL.Dataset[0].Dataset_Num === 'HCCMRDB5') {
        this.corr_samples = ['primary tumors：non-recurrent', 'adjacent tissue from non-recurrent tumors', 'recurrent tumors', 'adjacent tissue from recurrent tumors']
      } else if (this.GLOBAL.Dataset[0].Dataset_Num === 'HCCMRDB7' || this.GLOBAL.Dataset[0].Dataset_Num === 'HCCMRDB8') {
        this.corr_samples = ['primary tumors：recurrent', 'primary tumors：non-recurrent', 'adjacent tissue']
      } else if (this.GLOBAL.Dataset[0].Dataset_Num === 'HCCMRDB9') {
        this.corr_samples = ['primary tumors：recurrent', 'primary tumors：non-recurrent', 'adjacent tissue from recurrent tumors', 'adjacent tissue from non-recurrent tumors']
      } else if (this.GLOBAL.Dataset[0].Dataset_Num === 'HCCMRDB10') {
        this.corr_samples = ['normal liver tissue', 'primary tumors', 'primary tumors：recurrent', 'primary tumors：non-recurrent', 'primary tumors：metastases', 'primary tumors：metastases-free', 'adjacent tissue from primary tumors']
      }
    }
  },
  watch: {
    loading (val) {
      if (!val) return

      setTimeout(() => (this.loading = false), 3000)
    }

  },
  mounted () {
    this.$nextTick(function () {
      this.changeChoice1()
    })
  },
  created () {
    // 若用 function () 则this指向有问题，不能更改target的值
    this.bus.$on('gene_translate', (data) => {
      this.geneChoose = data
      console.log(this.geneChoose)
    })
  },
  beforeDestroy () {
    this.bus.$off('gene_translate')
    // console.log('关闭时的值', this.geneChoose)
  }
}
</script>

<style lang="scss" scoped>
.textSmall{
  font-size: 14px;
}
.textBig{
  font-size: 20px;
}
.textExp{
  font-size: 12px;
  color: dimgrey;
}

</style>
