<template>
  <div class="ml-5 ml-5">
    <v-container>
      <v-row>
        <v-col cols="6">
          <div class="d-flex justify-left">
            <h2 style="color:#6D819C " class="pb-3 mt-n3 pt-3">list for  Targets </h2>
          </div>
        </v-col>
      </v-row>
      <template>
        <v-data-table
          :headers="headers"
          :items="datas"
          dense
          :items-per-page="10"
          class="elevation-1 "
          :sort-by.sync="sortBy"
        >
          <template v-slot:item.tag="{ item }">
            <v-chip small :color="getColor(item.tag)">{{ item.tag }}</v-chip>
          </template>
          <template v-slot:item.spencies="{  }">
            <p>Homo Spencies</p>
          </template>
          <template v-slot:item.details="{item}">
            <v-btn
              small
              color="#fbd14b"
              @click.stop=getDetail(item.target)
            >more</v-btn>
          </template>
        </v-data-table>
      </template>
      <v-dialog
        v-model="dialog"
        max-width="600"
      >
        <v-card >
          <div v-for="item in detail" :key=item.target>
            <v-card-title class="headline grey lighten-2 textGreen">
              {{item.target}}
            </v-card-title>
            <v-card-text >
              <p class="text-justify textBlue">Basic Information</p>
              <div class="d-flex">
                <p class="justify-start font-weight-black">Gene Name:</p>
                <p class="pl-5">{{item.target}}</p>
              </div>
              <p class="text-justify font-weight-black">Description:</p>
              <p class="text-justify pl-2">{{item.description}}</p>
              <p class="text-justify font-weight-black">Alias:</p>
              <p class="text-justify pl-2">{{item.alias}}</p>
              <!--            <p class="text-justify font-weight-black">Tag:</p>-->
              <div class="d-flex">
                <p class="justify-start font-weight-black">Tag:</p>
                <v-chip class="ml-5" small :color="getColor(item.tag)">{{item.tag}}</v-chip>
              </div>
              <p class="pl-2 text-justify" v-if="item.tag===1">{{explain1}}</p>
              <p class="pl-2 text-justify" v-else-if="item.tag===2">{{explain2}}</p>
              <p class="pl-2 text-justify" v-else-if="item.tag===3">{{explain3}}</p>
              <p class="pl-2 text-justify" v-else-if="item.tag===4">{{explain4}}</p>
              <!--              <p class="pl-5" :explain="getexplain(details.tag)">{{explain1}}</p>-->
              <!--            <v-chip small :color="getColor(details.tags)">{{details.tags}}</v-chip>-->
              <!--            <p class="text-justify pl-2">{{details.tags}}</p>-->
              <p class="text-justify font-weight-black">Summary:</p>
              <p class="text-justify pl-2">{{item.summary}}</p>
              <v-divider></v-divider>
              <p class="text-justify textBlue">Correlative Paper:</p>
              <div class="d-flex">
                <p class="text-justify pl-2">A total of {{item.article_num}} papers related to target {{item.target}} were published</p>
                <v-btn icon x-large color="#03A6FF"
                @click="toArticle(item.target)">
                  <v-icon>mdi-clipboard-text-multiple</v-icon>
                </v-btn>
              </div>
              <v-divider></v-divider>
              <p class="text-justify textBlue">Involved Drug:</p>
              <v-row v-if="item.drugs">
                <v-col cols="6">
                  <p class="text-justify pl-2">{{item.drugs}}</p>
                </v-col>
                <v-col cols="6">
                  <v-btn class="ml-5" icon x-large color="#03A6FF"
                         @click="toDrug(item.target)">
                    <v-icon>mdi-pill</v-icon>
                  </v-btn>
                </v-col>
              </v-row>
              <v-row v-else>
                <p class="text-justify pl-4">No Compound Related Data Available</p>
              </v-row>
              <v-divider></v-divider>
              <p class="text-justify textBlue">External Links</p>
              <div class="d-flex">
                <v-btn small color="primary "
                       class="mr-1"
                       @click="toGenecards(item.target)">GenCard</v-btn>
                <v-btn small color="#fbd14b "
                       class="mr-1"
                       @click="toNCBI(item.ncbi_id)">NCBI</v-btn>
                <v-btn small color="#3ac569 "
                       class="mr-1"
                       @click="toCOSMIC(item.target)">COSMIC</v-btn>
                <v-btn small color="#03A6FF "
                       class="mr-1"
                       @click="toGEPIA(item.target)">GEPIA</v-btn>
              </div>

            </v-card-text>
          </div>
          <v-divider></v-divider>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              color="primary"
              text
              @click="dialog = false"
            >
              close
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-container>
<!--    <h1 class="content">{{meg}}</h1>-->
  </div>
</template>

<script>

import axios from 'axios'
export default {
  name: 'Target',
  data () {
    return {
      target: '',
      ncbi_id: '',
      drug_url: '',
      dialog: false,
      datas: [],
      detail: [],
      article: [],
      total: 0,
      sortBy: 'ldb_id',
      explain1: 'This target has been approved as an anticancer drug target or as a drug candidate in preclinical development',
      explain2: 'There are currently no drugs in clinical development for these targets, but there is evidence to support their operability',
      explain3: 'There is currently no information or lack of information to support the operability of this target',
      explain4: 'This target is not a priority target',
      headers: [
        {
          text: 'LDB ID',
          align: 'start',
          value: 'ldb_id'
        },
        {
          text: 'Target',
          value: 'target'
        },
        {
          text: 'Description',
          value: 'description',
          width: 400,
          sortable: false
        },
        {
          text: 'Spencies',
          value: 'spencies',
          sortable: false
        },
        {
          text: 'Tag',
          value: 'tag'
        },
        {
          text: 'Details',
          value: 'details',
          sortable: false
        }
      ]
    }
  },
  methods: {
    getColor (tag) {
      // eslint-disable-next-line eqeqeq
      if (tag === 1) return '#3ac569'
      // eslint-disable-next-line eqeqeq
      else if (tag === 2) return '#88dba3'
      // eslint-disable-next-line eqeqeq
      else if (tag === 3) return '#cff0da'
      else return '#e4e7ec'
    },
    getData () {
      axios.get('/api/ldb/Targets')
        .then(res => {
          this.datas = res.data.targets
          // console.log(this.datas)
        })
        .catch(err => {
          console.log(err)
        })
    },
    getDetail (ta) {
      this.dialog = true
      axios.post('/api/ldb/Targets', { target: ta })
        .then(res => {
          this.detail = res.data.target
          // console.log(res.data.target)
        })
        .catch(err => {
          console.log(err)
        })
      console.log(this.$route.params)
    },
    toArticle: function (target) {
      this.target = target
      this.$router.push({ name: 'Article' })
    },
    toGenecards: function (target) {
      this.url = 'https://www.genecards.org/cgi-bin/carddisp.pl?gene=' + target
      window.open(this.url, '_blank')
    },
    toNCBI: function (ncbiId) {
      this.url = 'https://www.ncbi.nlm.nih.gov/gene/?term=' + ncbiId
      window.open(this.url, '_blank')
    },
    toCOSMIC: function (target) {
      this.url = 'https://cancer.sanger.ac.uk/cosmic/gene/analysis?ln=' + target
      window.open(this.url, '_blank')
    },
    toGEPIA: function (target) {
      this.url = 'http://gepia.cancer-pku.cn/detail.php?gene=' + target
      window.open(this.url, '_blank')// 打开新的窗口，跳转
    },
    toDrug: function (target) {
      this.url = 'https://www.genecards.org/cgi-bin/carddisp.pl?gene=' + target + '#drugs_compounds'
      window.open(this.url, '_blank')
    }

  },
  created () {
    this.getData()
  },
  // $emit 放在其它位置的话 $on 监听不到 因为在该组件销毁前下一个组件才开始创建，写在其它位置下一个组件还没监听，该组件便开始传值
  beforeDestroy () {
    this.bus.$emit('change', this.target)// 通过$emit向外层触发事件并传递参数；第一个参数是事件名字随便起但需跟$on中的事件名字一样
    console.log('change传值了', this.target)
  }
}
</script>

<style scoped lang="scss">
.textBlue{
  color:#03A6FF;
  font-size: 17px;
  font-weight: bold;
}
.textGreen{
  color:#55967e;
  font-size: 20px;
  font-weight: bold;
}
.content {
  white-space: pre-line;
}
</style>
