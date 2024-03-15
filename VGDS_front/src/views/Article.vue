<template>
  <div class="ml-5 mr-5">
   <v-container>
     <div>
       <v-row  v-if="total>500">
         <v-col cols="12">
           <div class="d-flex justify-left">
             <h2 style="color:#6D819C " class="pb-3 mt-n3 pt-3">This database contains {{total}} literatures related to liver cancer targets </h2>
           </div>
         </v-col>
       </v-row>
       <v-row v-else-if="total>0">
         <v-col cols="12">
           <div class="d-flex justify-left">
             <h2 style="color:#6D819C " class="pb-3 mt-n3 pt-3">A total of {{total}} literatures related to the target {{target}} </h2>
           </div>
         </v-col>
       </v-row>
       <v-row v-else>
         <v-col cols="12">
           <div class="d-flex justify-left">
             <h2 style="color:#6D819C " class="pb-3 mt-n3 pt-3">There is no literature on this gene in this database</h2>
           </div>
         </v-col>
       </v-row>
     </div>
<!--     <v-card-->
<!--       v-if="total===0"-->
<!--       class="overflow-y-auto" height="700">-->
<!--       <v-progress-linear-->
<!--         indeterminate-->
<!--         color="#55967e"-->
<!--       ></v-progress-linear>-->
<!--     </v-card>-->
     <v-card
       v-if="total>500"
       class="overflow-y-auto" height="700">
       <v-card v-for="item in datas" :key="item.title">
         <v-card-text>
           <div class="d-flex">
             <p class="mb-0 pt-2 pl-2 arText">Title:</p>
             <p class="col-11 text-truncate pt-2 text-justify mb-0 pb-0 titleText pl-15 ml-3"><a class=" text-truncate  text-justify  titleText " @click="getdialog(item)">{{item.title}}</a></p>
           </div>
           <div class="d-flex">
             <p class="mb-0 arText pl-2">PMID:</p>
             <p class="mb-0 arText pl-16">{{item.pmid}}</p>
           </div>
           <div class="d-flex">
             <p class="mb-0 arText pl-2">Rlated Gene:</p>
             <p class="mb-0 arText pl-5">{{item.target}}</p>
           </div>
           <div class="d-flex">
             <p class="mb-0 pb-2 arText pl-2">Abstract:</p>
             <p class=" text-truncate pt-0 mb-0 pb-2 arText pl-11" >{{item.abstract}}</p>
           </div>
         </v-card-text>
       </v-card>
     </v-card>
     <v-card
       v-else-if="total>0"
       class="overflow-y-auto" height="700">
       <v-card v-for="item in datas" :key="item.title">
         <v-card-text>
           <div class="d-flex">
             <p class="mb-0 pt-2 pl-2 arText">Title:</p>
             <p class="col-11 text-truncate pt-2 text-justify mb-0 pb-0 titleText pl-15 ml-3"><a class=" text-truncate  text-justify  titleText " @click="getdialog(item)">{{item.title}}</a></p>
           </div>
           <div class="d-flex">
             <p class="mb-0 arText pl-2">PMID:</p>
             <p class="mb-0 arText pl-16">{{item.pmid}}</p>
           </div>
           <div class="d-flex">
             <p class="mb-0 arText pl-2">Rlated Gene:</p>
             <p class="mb-0 arText pl-5">{{item.target}}</p>
           </div>
           <div class="d-flex">
             <p class="mb-0 pb-2 arText pl-2">Abstract:</p>
             <p class=" text-truncate pt-0 mb-0 pb-2 arText pl-11" >{{item.abstract}}</p>
           </div>
         </v-card-text>
       </v-card>
     </v-card>
     <div class="text-center">
       <v-pagination
         v-if="total>0"
         color="#55967e"
         style="zoom:80%"
         v-model="page"
         :length="Math.ceil(total/10)"
         :total-visible="7"
         @input="changePage(page)"
       ></v-pagination>
     </div>
     <v-dialog
       v-model="articl_dialog"
       max-width="1000px"
     >
       <v-card>
         <v-card-title class="headline grey lighten-2 textGreen">
           Details of Article
         </v-card-title>

         <v-card-text >
           <div class="d-flex">
             <p class="justify-start font-weight-black">Related Gene Name:</p>
             <p class="text-justify pl-4">{{total_detail.target}}</p>
           </div>
           <div class="d-flex">
             <p class="justify-start font-weight-black">PMID:</p>
             <p class="text-justify pl-5">{{total_detail.pmid}}</p>
           </div>
           <p class="text-justify font-weight-black">Title:</p>
           <p class="text-justify pl-2">{{total_detail.title}}</p>
           <p class="text-justify font-weight-black">Abstract:</p>
<!--           <p class="text-justify content pl-2" v-html="abstract" ></p>-->
           <p class="text-justify content pl-2" >{{abstract}}</p>
         </v-card-text>
         <v-divider></v-divider>
         <v-card-actions>
           <v-spacer></v-spacer>
           <v-btn
             color="primary"
             text
             @click="toPubMed(total_detail.pmid)"
           >
             View ON pubmed
           </v-btn>
         </v-card-actions>
       </v-card>
     </v-dialog>
   </v-container>
  </div>
</template>
<script>

import axios from 'axios'
export default {
  name: 'Article',
  data () {
    return {
      articl_dialog: false,
      articles: [],
      total_detail: {},
      abstract: '',
      datas: [],
      target: '',
      total: 7250,
      maxTotal: 7250,
      page: 1

    }
  },
  methods: {
    getdialog: function (item) {
      this.articl_dialog = true
      this.total_detail = item
      // eslint-disable-next-line no-eval
      this.abstract = item.abstract
      console.log(this.abstract)
      this.abstract = this.abstract.replace(/\\n/g, '\n')
      console.log(this.abstract)
    },
    getAllArticle () {
      axios.get('/api/ldb/Articles/1')
        .then(res => {
          this.datas = res.data.articles
          console.log(this.datas)
        })
        .catch(err => {
          console.log(err)
        })
    },
    getTargetArticle () {
      axios.post('/api/ldb/TarArt', { target: this.target })
        .then(res => {
          this.datas = res.data.articles
          this.total = res.data.Total
          console.log(res.data)
        })
    },
    changePage (p) {
      if (this.total === this.maxTotal) {
        axios.get('/api/ldb/Articles/' + p)
          .then((res) => {
            this.datas = res.data.articles
            console.log(res.data)
          })
          .catch(err => {
            console.log('错误' + err)
          })
      } else {
        axios.post('/api/ldb/TarArt?page=' + p, {
          target: this.target
        })
          .then((res) => {
            this.datas = res.data.articles
            console.log(res.data)
          })
          .catch(err => {
            console.log('错误' + err)
          })
      }
    },

    toPubMed: function (pmid) {
      this.url = 'https://pubmed.ncbi.nlm.nih.gov/' + pmid
      window.open(this.url, '_blank')
    }
  },
  props: ['search'],
  mounted: function () {
    /* this.articles = this.searchArticle
    this.total = this.totalnum */
    console.log('target的值m', this.target)
    console.log('total的值m', this.total)
    if (this.target) {
      this.getTargetArticle()
    } else if (this.search) {
      this.target = this.search.toUpperCase()
      this.getTargetArticle()
    } else {
      this.getAllArticle()
    }
  },
  created () {
    // 若用 function () 则this指向有问题，不能更改target的值
    this.bus.$on('change', (data) => {
      // console.log('收到了', data)
      this.target = data
      // console.log('$on传的值', this.target)
    })
    // console.log('target的值c', this.target)
    // console.log('total的值c', this.total)
  },
/*  watch: {
    // 监听相同路由下参数变化的时候，从而实现异步刷新
    '$route' (to, from) {
      this.target = this.search.toUpperCase()
      // this.getCellExp()
      this.getTargetArticle()
    }
  },*/
  beforeDestroy () {
    this.bus.$off('change')
    this.target = ''
    this.total = 0
    console.log('关闭时的值', this.target)
  }
}
</script>
<style lang="scss" scoped>
.arText{
  font-size: 14px;
}
.titleText{
  font-size: 14px;
  color: #42b983;
}
.geneText{
  font-size: 14px;
  color: #42b983;
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
