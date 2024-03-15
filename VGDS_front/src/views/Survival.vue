<template>
  <div class="ml-5 mr-5">
    <v-container>
      <v-row>
        <v-col cols="6">
          <div class="d-flex justify-left">
            <h2 style="color:#6D819C " class="mt-n3 pt-3 pb-0 mb-0"> Survival Analysis</h2>
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
      <p style="color:#6D819C " class="d-flex justify-left">In this page, You can do survival analysis for HCCMRDB8,HCCMRDB9,HCCMRDB10</p>
      <v-card
        height="290">
        <v-row>
          <v-col cols="4">
            <div class="pr-2 ml-5">
              <p class="d-flex justify-left textSmall">Gene Symbol ID</p>
              <v-text-field
                dense
                single-line
                outlined
                color="#55967e"
                v-model = 'gen_name'
              ></v-text-field>
            </div>
            <v-card
              v-if="names.length !== 0"
              flat
              outlined
              class="mr-2 ml-5 mb-2"
              max-width="800"
            >
              <v-virtual-scroll
                :items="items"
                :item-height="30"
                height="70"
              >
                <template v-slot="{ item }">
                  <v-list-item>
                    <v-list-item-avatar>
                      <v-avatar
                        :color="item.color"
                        size="20"
                        class="white--text"
                      >
                      </v-avatar>
                    </v-list-item-avatar>

                    <v-list-item-content>
                      <v-list-item-title>{{ item.geneName }}</v-list-item-title>
                    </v-list-item-content>

                    <v-list-item-action>
                      <v-btn
                        depressed
                        small
                        icon
                        @click="addGene(item.geneName)"
                      >
                        <v-icon
                          color="#55967e"
                          right
                        >
                          mdi-plus-circle
                        </v-icon>
                      </v-btn>
                    </v-list-item-action>
                  </v-list-item>
                </template>
              </v-virtual-scroll>
            </v-card>
            <div>
              <div class="pr-2 ml-5">
                <v-row>
                  <v-col cols="1">
                  </v-col>
                  <v-col cols="4">
                    <p class="textSmall">High Group</p>
                    <v-menu
                      offset-x
                      transition="slide-x-transition"
                    >
                      <template v-slot:activator="{ on, attrs }">
                        <v-text-field
                          outlined
                          v-on="on"
                          v-bind="attrs"
                          dense
                          dark
                          :background-color= highColor
                          v-model="highColor"
                        ></v-text-field>
                      </template>
                      <v-card
                        width="320"
                        height="230"
                      >
                        <div class="d-flex justify-center">
                          <v-color-picker
                            class="mt-3"
                            link
                            v-model = highColor
                            :value = highColor
                            hide-inputs
                          ></v-color-picker>
                        </div>
                      </v-card>
                    </v-menu>
                  </v-col>
                  <v-col cols="2"></v-col>
                  <v-col cols="4">
                    <p class="textSmall">Low Group</p>
                    <v-menu
                      offset-x
                      transition="slide-x-transition"
                    >
                      <template v-slot:activator="{ on, attrs }">
                        <v-text-field
                          outlined
                          v-on="on"
                          v-bind="attrs"
                          dense
                          dark
                          :background-color= lowColor
                          v-model="lowColor"
                        ></v-text-field>
                      </template>
                      <v-card
                        width="320"
                        height="230"
                      >
                        <div class="d-flex justify-center">
                          <v-color-picker
                            class="mt-3"
                            link
                            v-model = lowColor
                            :value = lowColor
                            hide-inputs
                          ></v-color-picker>
                        </div>
                      </v-card>
                    </v-menu>
                  </v-col>
                </v-row>
              </div>
            </div>
          </v-col>
          <v-col cols="4">
            <p class="d-flex justify-left textSmall">Axis Units</p>
            <v-radio-group  dense
                            row
                            v-model="time1">
              <v-radio
                style="zoom:80%"
                v-for="item in Time"
                :label="item"
                :key="item"
                :value="item"
                color="#55967e"
              ></v-radio>
            </v-radio-group>
            <p class="d-flex textSmall">Group Cutoff</p>
            <v-radio-group  dense
                            row
                            v-model="cutoff">
              <v-radio
                style="zoom:80%"
                v-for="item in Cutoff"
                :label="item"
                :key="item"
                :value="item"
                color="#55967e"
              ></v-radio>
            </v-radio-group>
            <v-row>
              <v-col cols="4">
                <p class="textSmall">Cutoff-High(%)</p>
                <v-text-field
                  style="zoom:80%"
                  dense
                  placeholder="1"
                  outlined
                  color="#55967e"
                  v-model="high"
                ></v-text-field>
              </v-col>
              <v-col cols="4">
                <p class="textSmall">Cutoff-Low(%)</p>
                <v-text-field
                  style="zoom:80%"
                  v-model="low"
                  outlined
                  dense
                  color="#55967e"
                ></v-text-field>
              </v-col>
            </v-row>
          </v-col>
          <v-col cols="4">
            <p class="d-flex justify-left textSmall">Choose Dataset</p>
            <v-select
              style="zoom:90%"
              class="mr-16"
              :items="Datasets"
              solo
              flat
              dense
              outlined
              color="#55967e"
              v-model="Dataset"
            ></v-select>
            <p class="d-flex justify-left textSmall"> Confidence Interval  & Risk Form </p>
            <v-radio-group  dense
                            row
                            v-model="confidence ">
              <v-radio
                style="zoom:80%"
                v-for="item in  Confidence"
                :label="item"
                :key="item"
                :value="item"
                color="#55967e"
              ></v-radio>
            </v-radio-group>
            <p class="d-flex justify-left textExp">Whether to display confidence intervals and risk tables</p>
            <div class="d-flex ml-16 pl-16">
              <v-btn color="#55967e"
                     dark
                     small
                     @click.stop= Survival >
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
        <v-card class="mt-8">
          <div class="d-flex justify-space-between ">
            <p class="ml-8 mt-3">Log-rank test P</p>
            <v-btn
              icon
              large
              color="#55967e"
              @click="handleDownloadQrIMg(pic1_base64), handleDownloadQrIMg(pic2_base64)"
            ><v-icon>mdi-download</v-icon></v-btn>
          </div>
          <div class="d-flex justify-start ">
            <p class="ml-8 ">{{title2}}:{{p2}}</p>
          </div>
          <div class="d-flex justify-start ">
            <p class="ml-8">{{title1}}:{{p1}}</p>
          </div>
          <v-row>
            <v-col cols="12">
              <v-divider></v-divider>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="1" v-if="risk === 'No'">
            </v-col>
            <v-col cols="5">
              <v-img :src="pic2" ></v-img>
            </v-col>
            <v-col cols="5" class="pt-1">
              <v-img :src="pic1" ></v-img>
            </v-col>
            <v-col cols="1">
            </v-col>
          </v-row>
        </v-card>
      </div>
    </v-container>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Survival',
  data () {
    return {
      Datasets: ['HCCMRDB8', 'HCCMRDB9', 'HCCMRDB10'],
      Dataset: 'HCCMRDB10',
      Time: ['Years', 'Months', 'Days'],
      time1: 'Days',
      Cutoff: ['Median', 'Quartile', 'Custom'],
      cutoff: 'Median',
      high: 50,
      low: 50,
      Confidence: ['Yes', 'No'],
      confidence: 'No',
      Risk: ['Yes', 'No'],
      risk: 'Yes',
      highColor: '#970200',
      lowColor: '#012257',
      data_path1: '',
      data_path2: '',
      nr: 0,
      tr: 0,
      gen_name: '',
      linear: false,
      pic1_base64: '',
      pic1: '',
      pic2_base64: '',
      pic2: '',
      list: false,
      title1: '',
      title2: '',
      p1: 0,
      p2: 0,
      colors: [],
      names: [],
      x: -1
    }
  },
  methods: {
    Survival () {
      this.data_path1 = 'Adjacent.csv'
      this.data_path2 = 'Tumor.csv'
      this.title1 = 'Adjacent'
      this.title2 = 'Tumor'
      if (this.Dataset === 'HCCMRDB8') {
        this.nr = 212
        this.tr = 221
      } else if (this.Dataset === 'HCCMRDB9') {
        this.nr = 52
        this.tr = 115
      } else {
        this.nr = 40
        this.tr = 321
      }
      if (this.confidence === 'Yes') {
        this.risk = 'Yes'
      } else {
        this.risk = 'No'
      }
      this.linear = true
      this.list = false
      axios.post('/api/ldb/Survival', {
        dataset: this.Dataset,
        data_path1: this.data_path1,
        data_path2: this.data_path2,
        gene_name: this.gen_name,
        nr: this.nr,
        tr: this.tr,
        colorH: this.highColor,
        colorL: this.lowColor,
        cut: this.high,
        confidence: this.confidence,
        risk: this.risk,
        time: this.time1,
        title1: this.title1,
        title2: this.title2
      })
        .then(res => {
          this.pic1_base64 = res.data.pic1
          this.pic1 = 'data:;base64,' + res.data.pic1
          this.pic2_base64 = res.data.pic2
          this.pic2 = 'data:;base64,' + res.data.pic2
          this.p1 = res.data.p1
          this.p2 = res.data.p2
          console.log(res.data)
          this.linear = false
          this.list = true
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
    genIndex () {
      this.x = this.x + 1
      return this.x
    },
    addGene (gen) {
      this.gen_name = gen
    }
  },
  computed: {
    items () {
      return Array.from({ length: this.colors.length }, (k, v) => {
        var i = this.genIndex()

        return {
          color: this.colors[i],
          geneName: this.names[i]
        }
      })
    }
  },
  watch: {
    cutoff (newName, oldName) {
      if (newName === 'Median') {
        this.high = 50
        this.low = 50
      } else if (newName === 'Quartile') {
        this.high = 75
        this.low = 25
      }
    }

  },
  created () {
    // 若用 function () 则this指向有问题，不能更改target的值
    this.bus.$on('gene_translate1', (data) => {
      this.names = data
      console.log(this.names)
    })
    this.bus.$on('gene_color', (data) => {
      this.colors = data
      console.log(this.colors)
    })
  },
  beforeDestroy () {
    this.bus.$off('gene_translate1')
    this.bus.$off('gene_color')
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
.textGreen{
  color:#55967e;
  font-size: 20px;
  font-weight: bold;
}

</style>
