import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from '@/plugins/vuetify'
// import echarts from 'echarts'
import * as echarts from 'echarts'
// import highcharts from 'highcharts'
// import VueHighcharts from 'vue-highcharts'
import datatable from '@/components/datatable'
import global_ from './components/Global'
import '@mdi/font/css/materialdesignicons.css'
Vue.component('datatable', datatable)
Vue.config.productionTip = false
Vue.prototype.$echarts = echarts// 引用文件
Vue.prototype.GLOBAL = global_// 挂载到Vue实例上面
// Vue.use(VueHighcharts)
Vue.prototype.bus = new Vue()// 在 Vue 的prototype挂载了一个bus属性
new Vue({
  vuetify,
  router,
  store,
  render: h => h(App)
}).$mount('#app')
