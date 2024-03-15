<template>
  <div>
    <div id="container"></div>
  </div>
</template>

<!--
<script>
import Highcharts from 'highcharts/highstock'
import HighchartsMore from 'highcharts/highcharts-more'
import HighchartsDrilldown from 'highcharts/modules/drilldown'
import Highcharts3D from 'highcharts/highcharts-3d'
//import dependencywheel from 'highcharts/modules/dependency-wheel'

HighchartsMore(Highcharts)
HighchartsDrilldown(Highcharts)
Highcharts3D(Highcharts)
//dependencywheel(Highcharts)
/*import HighCharts from 'highcharts'
// 和弦图的引入依赖
import HC_sankey from 'highcharts/modules/sankey'
import dependencywheel from 'highcharts/modules/dependency-wheel'
// HC_sankey(HighCharts)
dependencywheel(Highcharts)*/

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  mounted () {
    this.moreChart()
  },
  methods: {
    moreChart () {
      if (this.chart) {
        this.chart.destroy()
      }
      // 初始化 Highcharts 图表
      this.chart = new Highcharts.Chart('container', {
        title: {
          text: 'Highcharts 和弦图'
        },
        subtitle: {
          text: '数据来源：thesolarfoundation.com'
        },
        yAxis: {
          title: {
            text: '就业人数'
          }
        },
        legend: {
          layout: 'vertical',
          align: 'right',
          verticalAlign: 'middle'
        },
        plotOptions: {
          series: {
            label: {
              connectorAllowed: false
            },
            pointStart: 2010
          }
        },
        series: [
          {
            name: '安装，实施人员',
            data: [43934, 52503, 57177, 69658, 97031, 119931, 137133, 154175]
          },
          {
            name: '工人',
            data: [24916, 24064, 29742, 29851, 32490, 30282, 38121, 40434]
          },
          {
            name: '销售',
            data: [11744, 17722, 16005, 19771, 20185, 24377, 32147, 39387]
          },
          {
            name: '项目开发',
            data: [null, null, 7988, 12169, 15112, 22452, 34400, 34227]
          },
          {
            name: '其他',
            data: [12908, 5948, 8105, 11248, 8989, 11816, 18274, 18111]
          }
        ],
        responsive: {
          rules: [
            {
              condition: {
                maxWidth: 500
              },
              chartOptions: {
                legend: {
                  layout: 'horizontal',
                  align: 'center',
                  verticalAlign: 'bottom'
                }
              }
            }
          ]
        }
       /* title: {
          text: 'Highcharts 和弦图'
        },
        series: [{
          keys: ['from', 'to', 'weight'],
          data: [
            ['Brazil', 'Portugal', 5],
            ['Brazil', 'France', 1],
            ['Brazil', 'Spain', 1],
            ['Brazil', 'England', 1],
            ['Canada', 'Portugal', 1],
            ['Canada', 'France', 5],
            ['Canada', 'England', 1],
            ['Mexico', 'Portugal', 1],
            ['Mexico', 'France', 1],
            ['Mexico', 'Spain', 5],
            ['Mexico', 'England', 1],
            ['USA', 'Portugal', 1],
            ['USA', 'France', 1],
            ['USA', 'Spain', 1],
            ['USA', 'England', 5],
            ['Portugal', 'Angola', 2],
            ['Portugal', 'Senegal', 1],
            ['Portugal', 'Morocco', 1],
            ['Portugal', 'South Africa', 3],
            ['France', 'Angola', 1],
            ['France', 'Senegal', 3],
            ['France', 'Mali', 3],
            ['France', 'Morocco', 3],
            ['France', 'South Africa', 1],
            ['Spain', 'Senegal', 1],
            ['Spain', 'Morocco', 3],
            ['Spain', 'South Africa', 1],
            ['England', 'Angola', 1],
            ['England', 'Senegal', 1],
            ['England', 'Morocco', 2],
            ['England', 'South Africa', 7],
            ['South Africa', 'China', 5],
            ['South Africa', 'India', 1],
            ['South Africa', 'Japan', 3],
            ['Angola', 'China', 5],
            ['Angola', 'India', 1],
            ['Angola', 'Japan', 3],
            ['Senegal', 'China', 5],
            ['Senegal', 'India', 1],
            ['Senegal', 'Japan', 3],
            ['Mali', 'China', 5],
            ['Mali', 'India', 1],
            ['Mali', 'Japan', 3],
            ['Morocco', 'China', 5],
            ['Morocco', 'India', 1],
            ['Morocco', 'Japan', 3],
            ['Japan', 'Brazil', 1]
          ],
          type: 'dependencywheel',
          name: 'Dependency wheel series',
          dataLabels: {
            color: '#333',
            textPath: {
              enabled: true,
              attributes: {
                dy: 5
              }
            },
            distance: 10
          },
          size: '95%'
        }]*/
      })
    }
  }
}
</script>

&lt;!&ndash; Add "scoped" attribute to limit css to this component only &ndash;&gt;
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
-->
<!--<script>
import Highcharts from 'highcharts/highstock'
import HighchartsExporting from 'highcharts/modules/exporting'
import HighchartsOfflineExporting from 'highcharts/modules/offline-exporting'
import HighchartsSankey from 'highcharts/modules/sankey'
import HighchartsOldie from 'highcharts/modules/oldie'
import HighchartsDependencyWheel from 'highcharts/modules/dependency-wheel'
HighchartsExporting(Highcharts)
HighchartsOfflineExporting(Highcharts)
HighchartsSankey(Highcharts)
HighchartsOldie(Highcharts)
HighchartsDependencyWheel(Highcharts)

export default {
  name: 'Search',
  props: {
    msg: String
  },
  mounted () {
    this.initEchart()
  },
  methods: {
    initEchart () {
      if (this.chart) {
        this.chart.destroy()
      }
      this.chart = Highcharts.chart('container', {
        colors: this.colors,
        title: {
          text: ''
        },
        chart: {
          backgroundColor: 'transparent'
        },
        credits: {
          enabled: false // 右下角版权信息
        },
        navigation: {
          // 右上角导出按钮组
          buttonOptions: {
            enabled: false
          }
        },
        series: [
          {
            keys: ['from', 'to', 'weight'],
            data: [
              ['Brazil', 'Portugal', 5],
              ['Brazil', 'France', 1],
              ['Brazil', 'Spain', 1],
              ['Brazil', 'England', 1],
              ['Canada', 'Portugal', 1],
              ['Canada', 'France', 5],
              ['Canada', 'England', 1],
              ['Mexico', 'Portugal', 1],
              ['Mexico', 'France', 1],
              ['Mexico', 'Spain', 5],
              ['Mexico', 'England', 1],
              ['USA', 'Portugal', 1],
              ['USA', 'France', 1],
              ['USA', 'Spain', 1],
              ['USA', 'England', 5],
              ['Portugal', 'Angola', 2],
              ['Portugal', 'Senegal', 1],
              ['Portugal', 'Morocco', 1],
              ['Portugal', 'South Africa', 3],
              ['France', 'Angola', 1],
              ['France', 'Senegal', 3],
              ['France', 'Mali', 3],
              ['France', 'Morocco', 3],
              ['France', 'South Africa', 1],
              ['Spain', 'Senegal', 1],
              ['Spain', 'Morocco', 3],
              ['Spain', 'South Africa', 1],
              ['England', 'Angola', 1],
              ['England', 'Senegal', 1],
              ['England', 'Morocco', 2],
              ['England', 'South Africa', 7],
              ['South Africa', 'China', 5],
              ['South Africa', 'India', 1],
              ['South Africa', 'Japan', 3],
              ['Angola', 'China', 5],
              ['Angola', 'India', 1],
              ['Angola', 'Japan', 3],
              ['Senegal', 'China', 5],
              ['Senegal', 'India', 1],
              ['Senegal', 'Japan', 3],
              ['Mali', 'China', 5],
              ['Mali', 'India', 1],
              ['Mali', 'Japan', 3],
              ['Morocco', 'China', 5],
              ['Morocco', 'India', 1],
              ['Morocco', 'Japan', 3],
              ['Japan', 'Brazil', 1]
            ],
            type: 'dependencywheel',
            name: '',
            dataLabels: {
              color: '#defeff',
              textPath: {
                enabled: true,
                attributes: {
                  dy: 5
                }
              },
              distance: 10
            },
            size: '95%'
          }
        ]
      })
    }
  }
}
</script>-->
<!--<script>
import Highcharts from 'highcharts/highstock'
import HighchartsExporting from 'highcharts/modules/exporting'
import HighchartsOfflineExporting from 'highcharts/modules/offline-exporting'
import HighchartsSankey from 'highcharts/modules/sankey'
import HighchartsOldie from 'highcharts/modules/oldie'
import HighchartsDependencyWheel from 'highcharts/modules/dependency-wheel'
HighchartsExporting(Highcharts)
HighchartsOfflineExporting(Highcharts)
HighchartsSankey(Highcharts)
HighchartsOldie(Highcharts)
HighchartsDependencyWheel(Highcharts)

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  mounted () {
    this.moreChart()
  },
  methods: {
    moreChart () {
      if (this.chart) {
        this.chart.destroy()
      }
      // 初始化 Highcharts 图表
      this.chart = new Highcharts.Chart('container', {
        title: {
          text: 'Highcharts 和弦图'
        },
        series: [{
          keys: ['from', 'to', 'weight'],
          data: [
            ['Brazil', 'Portugal', 5],
            ['Brazil', 'France', 1],
            ['Brazil', 'Spain', 1],
            ['Brazil', 'England', 1],
            ['Canada', 'Portugal', 1],
            ['Canada', 'France', 5],
            ['Canada', 'England', 1],
            ['Mexico', 'Portugal', 1],
            ['Mexico', 'France', 1],
            ['Mexico', 'Spain', 5],
            ['Mexico', 'England', 1],
            ['USA', 'Portugal', 1],
            ['USA', 'France', 1],
            ['USA', 'Spain', 1],
            ['USA', 'England', 5],
            ['Portugal', 'Angola', 2],
            ['Portugal', 'Senegal', 1],
            ['Portugal', 'Morocco', 1],
            ['Portugal', 'South Africa', 3],
            ['France', 'Angola', 1],
            ['France', 'Senegal', 3],
            ['France', 'Mali', 3],
            ['France', 'Morocco', 3],
            ['France', 'South Africa', 1],
            ['Spain', 'Senegal', 1],
            ['Spain', 'Morocco', 3],
            ['Spain', 'South Africa', 1],
            ['England', 'Angola', 1],
            ['England', 'Senegal', 1],
            ['England', 'Morocco', 2],
            ['England', 'South Africa', 7],
            ['South Africa', 'China', 5],
            ['South Africa', 'India', 1],
            ['South Africa', 'Japan', 3],
            ['Angola', 'China', 5],
            ['Angola', 'India', 1],
            ['Angola', 'Japan', 3],
            ['Senegal', 'China', 5],
            ['Senegal', 'India', 1],
            ['Senegal', 'Japan', 3],
            ['Mali', 'China', 5],
            ['Mali', 'India', 1],
            ['Mali', 'Japan', 3],
            ['Morocco', 'China', 5],
            ['Morocco', 'India', 1],
            ['Morocco', 'Japan', 3],
            ['Japan', 'Brazil', 1]
          ],
          type: 'dependencywheel',
          name: 'Dependency wheel series',
          dataLabels: {
            color: '#333',
            textPath: {
              enabled: true,
              attributes: {
                dy: 5
              }
            },
            distance: 10
          },
          size: '95%'
        }]
      })
    }
  }
}
</script>-->
<!--<script>
import Highcharts from 'highcharts/highstock'
import HighchartsExporting from 'highcharts/modules/exporting'
import HighchartsOfflineExporting from 'highcharts/modules/offline-exporting'
import HighchartsSankey from 'highcharts/modules/sankey'
import HighchartsOldie from 'highcharts/modules/oldie'
import HighchartsDependencyWheel from 'highcharts/modules/dependency-wheel'
HighchartsExporting(Highcharts)
HighchartsOfflineExporting(Highcharts)
HighchartsSankey(Highcharts)
HighchartsOldie(Highcharts)
HighchartsDependencyWheel(Highcharts)

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  mounted () {
    this.moreChart()
  },
  methods: {
    moreChart () {
      if (this.chart) {
        this.chart.destroy()
      }
      // 初始化 Highcharts 图表
      this.chart = new Highcharts.Chart('container', {
        title: {
          text: 'Highcharts 和弦图'
        },
        series: [{
          keys: ['from', 'to', 'weight'],
          data: [
            ['ALDOC', 'Glycolysis / Gluconeogenesis', 1],
            ['ENO2', 'Glycolysis / Gluconeogenesis', 1],
            ['HK2', 'Glycolysis / Gluconeogenesis', 1],
            ['PFKL', 'Glycolysis / Gluconeogenesis', 1],
            ['ALDOC', 'Fructose and mannose metabolism', 1],
            ['HK2', 'Fructose and mannose metabolism', 1],
            ['MPI', 'Fructose and mannose metabolism', 1],
            ['PFKFB3', 'Fructose and mannose metabolism', 1],
            ['PFKFB4', 'Fructose and mannose metabolism', 1],
            ['PFKL', 'Fructose and mannose metabolism', 1],
            ['GBE1', 'Starch and sucrose metabolism', 1],
            ['GYS1', 'Starch and sucrose metabolism', 1],
            ['HK2', 'Starch and sucrose metabolism', 1],
            ['AK4', 'Metabolic pathways', 1],
            ['ALDOC', 'Metabolic pathways', 1],
            ['BCKDHA', 'Metabolic pathways', 1],
            ['ENO2', 'Metabolic pathways', 1],
            ['GBE1', 'Metabolic pathways', 1],
            ['HK2', 'Metabolic pathways', 1],
            ['IPMK', 'Metabolic pathways', 1],
            ['KYNU', 'Metabolic pathways', 1],
            ['MPI', 'Metabolic pathways', 1],
            ['P4HA1', 'Metabolic pathways', 1],
            ['PFKL', 'Metabolic pathways', 1],
            ['PTGES', 'Metabolic pathways', 1],
            ['RDH10', 'Metabolic pathways', 1],
            ['RIMKLA', 'Metabolic pathways', 1],
            ['AK4', 'Biosynthesis of antibiotics', 1],
            ['ALDOC', 'Biosynthesis of antibiotics', 1],
            ['BCKDHA', 'Biosynthesis of antibiotics', 1],
            ['ENO2', 'Biosynthesis of antibiotics', 1],
            ['PFKL', 'Biosynthesis of antibiotics', 1],
            ['HK2', 'Biosynthesis of antibiotics', 1],
            ['ALDOC', 'Carbon metabolism', 1],
            ['ENO2', 'Carbon metabolism', 1],
            ['HK2', 'Carbon metabolism', 1],
            ['PFKL', 'Carbon metabolism', 1]
          ],
          type: 'dependencywheel',
          name: 'Dependency wheel series',
          dataLabels: {
            color: '#333',
            textPath: {
              enabled: true,
              attributes: {
                dy: 5
              }
            },
            distance: 10
          },
          size: '95%'
        }]
      })
    }
  }
}
</script>-->
<script>
import Highcharts from 'highcharts/highstock'
import HighchartsExporting from 'highcharts/modules/exporting'
import HighchartsOfflineExporting from 'highcharts/modules/offline-exporting'
import HighchartsSankey from 'highcharts/modules/sankey'
import HighchartsOldie from 'highcharts/modules/oldie'
import HighchartsDependencyWheel from 'highcharts/modules/dependency-wheel'
HighchartsExporting(Highcharts)
HighchartsOfflineExporting(Highcharts)
HighchartsSankey(Highcharts)
HighchartsOldie(Highcharts)
HighchartsDependencyWheel(Highcharts)

export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  mounted () {
    this.moreChart()
  },
  methods: {
    moreChart () {
      if (this.chart) {
        this.chart.destroy()
      }
      // 初始化 Highcharts 图表
      this.chart = new Highcharts.Chart('container', {
        title: {
          text: 'Highcharts 和弦图'
        },
        series: [{
          keys: ['from', 'to', 'weight'],
          data: [
            ['ALDOC', 'Glycolysis / Gluconeogenesis', 1],
            ['ENO2', 'Glycolysis / Gluconeogenesis', 1],
            ['HK2', 'Glycolysis / Gluconeogenesis', 1],
            ['PFKL', 'Glycolysis / Gluconeogenesis', 1],
            ['ALDOC', 'Fructose and mannose metabolism', 1],
            ['HK2', 'Fructose and mannose metabolism', 1],
            ['MPI', 'Fructose and mannose metabolism', 1],
            ['PFKFB3', 'Fructose and mannose metabolism', 1],
            ['PFKFB4', 'Fructose and mannose metabolism', 1],
            ['PFKL', 'Fructose and mannose metabolism', 1],
            ['GBE1', 'Starch and sucrose metabolism', 1],
            ['GYS1', 'Starch and sucrose metabolism', 1],
            ['HK2', 'Starch and sucrose metabolism', 1],
            ['AK4', 'Metabolic pathways', 1],
            ['ALDOC', 'Metabolic pathways', 1],
            ['BCKDHA', 'Metabolic pathways', 1],
            ['ENO2', 'Metabolic pathways', 1],
            ['GBE1', 'Metabolic pathways', 1],
            ['HK2', 'Metabolic pathways', 1],
            ['IPMK', 'Metabolic pathways', 1],
            ['KYNU', 'Metabolic pathways', 1],
            ['MPI', 'Metabolic pathways', 1],
            ['P4HA1', 'Metabolic pathways', 1],
            ['PFKL', 'Metabolic pathways', 1],
            ['PTGES', 'Metabolic pathways', 1],
            ['RDH10', 'Metabolic pathways', 1],
            ['RIMKLA', 'Metabolic pathways', 1],
            ['AK4', 'Biosynthesis of antibiotics', 1],
            ['ALDOC', 'Biosynthesis of antibiotics', 1],
            ['BCKDHA', 'Biosynthesis of antibiotics', 1],
            ['ENO2', 'Biosynthesis of antibiotics', 1],
            ['PFKL', 'Biosynthesis of antibiotics', 1],
            ['HK2', 'Biosynthesis of antibiotics', 1],
            ['ALDOC', 'Carbon metabolism', 1],
            ['ENO2', 'Carbon metabolism', 1],
            ['HK2', 'Carbon metabolism', 1],
            ['PFKL', 'Carbon metabolism', 1]
          ],
          type: 'dependencywheel',
          name: 'Dependency wheel series',
          dataLabels: {
            color: '#333',
            textPath: {
              enabled: true,
              attributes: {
                dy: 5
              }
            },
            distance: 10
          },
          size: '95%'
        }]
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit css to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
