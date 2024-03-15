<template>
  <div class="ml-5 mr-5">
    <v-container>
      <v-card
        shaped>
      <div v-for="item in detail" :key=item.gene_name>
        <v-card-title class="headline grey lighten-2 textGreen">
          {{item.gene_name}}
        </v-card-title>
      <v-card-text >
        <p class="text-justify textBlue">Basic Information</p>
        <div class="d-flex">
          <p class="justify-start font-weight-black">Gene Name:</p>
          <p class="pl-5">{{item.gene_name}}</p>
        </div>
        <div class="d-flex">
          <p class="text-justify font-weight-black ">Description:</p>
          <p class="text-justify pl-5">{{item.Description}}</p>
        </div>
        <div class="d-flex">
          <p class="text-justify font-weight-black">Alias:</p>
          <p class="text-justify pl-16">{{item.Alias}}</p>
        </div>
        <div class="d-flex">
          <p class="justify-start font-weight-black">Tag:</p>
          <v-chip class="ml-16 pl-2" small :color="getColor(item.tag)">{{item.tag}}</v-chip>
        </div>
        <p class="pl-2 text-justify" v-if="item.tag===1">{{explain1}}</p>
        <p class="pl-2 text-justify" v-else-if="item.tag===2">{{explain2}}</p>
        <p class="pl-2 text-justify" v-else-if="item.tag===3">{{explain3}}</p>
        <p class="pl-2 text-justify" v-else-if="item.tag===4">{{explain4}}</p>
        <p class="text-justify font-weight-black">Summary:</p>
        <p class="text-justify pl-2">{{item.Summary}}</p>
        <v-divider></v-divider>
        <p class="text-justify textBlue">Correlative Paper:</p>
        <div class="d-flex" v-if="item.Article_num">
          <p class="text-justify pl-2">A total of {{item.Article_num}} papers related to target {{item.gene_name}} were published</p>
          <v-btn icon x-large color="#03A6FF"
                 @click="toArticle ()">
            <v-icon>mdi-clipboard-text-multiple</v-icon>
          </v-btn>
        </div>
        <div v-else>
          <p class="text-justify pl-2"> There is no relevant literature in this database</p>
        </div>
        <v-divider></v-divider>
        <p class="text-justify textBlue">Involved Drug:</p>
        <v-row v-if="item.drugs">
            <p class="text-justify pl-2">{{item.drugs}}</p>
            <v-btn class="ml-5 text-justify  " icon x-large color="#03A6FF"
                   @click="toDrug(item.target)">
              <v-icon>mdi-pill</v-icon>
            </v-btn>
        </v-row>
        <v-row v-else>
          <p class="text-justify pl-4">No Compound Related Data Available</p>
        </v-row>
        <v-divider></v-divider>
        <p class="text-justify textBlue">Expression summary of {{item.gene_name}}:</p>
        <h2 class="text-center">Gene differential Expression  in GEO HCC Tumor Projects (Microarray)</h2>
        <v-row>
          <v-col cols="5" class="mt-10">
            <h3 class="text-left ">log2FC1: Replase/Replase-free</h3>
             <p class="text-left">fold change in log2 scale by compparing HCC replase tumors with HCC replase-free tumors</p>
            <h3 class="text-left">log2FC2: Replased/Adjacent</h3>
            <p class="text-left">fold change in log2 scale by compparing HCC primary tumor that will recur with HCC adjacent samples</p>
            <h3 class="text-left">log2FC3: Replased tumor/Primary</h3>
            <p class="text-left">fold change in log2 scale by compparing HCC replased tumors with HCC primary tumors</p>
            <h3 class="text-left">log2F4: Replase-free/Adjacent</h3>
            <p class="text-left">fold change in log2 scale by compparing HCC replase-free tumors with HCC adjacent samples</p>
            <h3 class="text-left">log2FC5: primary/Adjacent</h3>
            <p class="text-left">fold change in log2 scale by compparing HCC primary tumors with HCC adjacent samples</p>

          </v-col>
          <v-col cols="6">
            <div id="leida" style="width: 100% ;height:600px;"></div>
          </v-col>
        </v-row>
        <v-row>
          <div id="main" style="width: 100%;height:500px;"></div>
        </v-row>
        <h2 class="text-center mt-5 ">Gene  Expression level  in different cell(scRNA-seq)</h2>
        <v-row>
          <v-col cols="6" class="pb-0 mt-5" id="precell">
            <h4 class="text-center  pb-5 ">Normal Tissue</h4>
          </v-col>
          <v-col cols="6" class="pb-0 mt-5">
            <h4 class="text-center pb-5 ">Primary Tumor</h4>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="6" class="pt-0">
            <div id="normal" style="width: 100%;height:100%;"></div>
          </v-col>
          <v-col cols="6" class="pt-0">
            <div id="primary" style="width: 100%;height:350px;"></div>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="6" class="pb-0">
            <h4 class="text-center pb-0 ">Repleased Tumor</h4>
          </v-col>
          <v-col cols="6" class="pb-0">
            <h4 class="text-center mt-5 ">Metastasis Tumor</h4>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="6" class="pt-0">
            <div id="repleased" style="width: 100%;height:400px;"></div>
          </v-col>
          <v-col cols="6">
            <div id="meta" style="width: 100%;height:400px;"></div>
          </v-col>
        </v-row>
        <v-divider></v-divider>
<!--        <p class="text-justify textBlue">Survival Analyze</p>

        <v-divider></v-divider>-->
        <p class="text-justify textBlue">External Links</p>
        <div class="d-flex">
          <v-btn small color="primary "
                 class="mr-1"
                 @click="toGenecards(item.gene_name)">GenCard</v-btn>
          <v-btn small color="#fbd14b "
                 class="mr-1"
                 @click="toNCBI(item.ncbi_id)">NCBI</v-btn>
          <v-btn small color="#3ac569 "
                 class="mr-1"
                 @click="toCOSMIC(item.gene_name)">COSMIC</v-btn>
          <v-btn small color="#03A6FF "
                 class="mr-1"
                 @click="toGEPIA(item.gene_name)">GEPIA</v-btn>
        </div>

      </v-card-text>
    </div>
    <v-card-actions>
      <v-spacer></v-spacer>
    </v-card-actions>
  </v-card>
    </v-container>
  </div>
</template>

<script>

import axios from 'axios'
// eslint-disable-next-line no-unused-vars
import dataTool from 'echarts/extension/dataTool'
// eslint-disable-next-line no-unused-vars
// import dataTool from 'echarts/extension/dataTool'
const echarts = require('echarts')
export default {
  name: 'Detail',
  data () {
    return {
      preWidth: 0,
      /* test: [
        [850, 740, 900, 1070, 930, 850, 950, 980, 980, 880, 1000, 980, 930, 650, 760, 810, 1000, 1000, 960, 960],
        [960, 940, 960, 940, 880, 800, 850, 880, 900, 840, 830, 790, 810, 880, 880, 830, 800, 790, 760, 800],
        [880, 880, 880, 860, 720, 720, 620, 860, 970, 950, 880, 910, 850, 870, 840, 840, 850, 840, 840, 840],
        [890, 810, 810, 820, 800, 770, 760, 740, 750, 760, 910, 920, 890, 860, 880, 720, 840, 850, 850, 780],
        [890, 840, 780, 810, 760, 810, 790, 810, 820, 850, 870, 870, 810, 740, 810, 940, 950, 800, 810, 870],
        [890, 840, 780, 810, 760, 810, 790, 810, 820, 850, 870, 870, 810, 740, 810, 940, 950, 800, 810, 870]
      ], */
      target: '',
      detail: [],
      expr0: [],
      expr1: [],
      expr2: [],
      expr3: [],
      expr4: [],
      flag: true,
      Log2FC1: 0,
      Log2FC2: 0,
      Log2FC3: 0,
      Log2FC4: 0,
      Log2FC5: 0,
      leida_num: [],
      leida_num_abs: [],
      chart_num: ['missing', -2.8273, -1.58097, -2.37209],
      url: '',
      drugs: '',
      FC1: 0,
      boxplot_num: [],
      normal: [],
      primary: [],
      replased: [],
      primaryTN: [],
      primaryTcell: [],
      meta: [],
      boxplot1: [[2.774902154, 2.630478164, 5.001970637, 5.804560603, 4.684142105, 1.700514292, 5.308083054, 4.236517875, 3.208354315, 5.672832634, 4.29524768, 5.195429496, 2.119129379, 3.94871297, 5.473679452, 5.549800991, 3.361098221, 3.186789733, 5.088262043, 4.559606833, 3.499802526, 1.403123173, 4.200293257, 2.710319347, 4.186910932, 5.147852491, 2.613487806, 3.783908146, 4.63155891, 3.038158362, 0.836080701, 5.907208194, 4.88262202, 4.04632429, 1.642685401, 4.77784365, 3.644406617, 3.87310447, 3.580180466, 4.770577477, 3.722447444, 3.425035458, 5.392069395, 2.002442938, 5.404972926, 2.030885505, 5.932904954, 2.168935935, 1.792687132, 3.819787722, 3.217801011, 1.366214209, 3.547298049, 1.674948699, 0.21924635, 3.834248039, 4.519372691, 1.656003871, 3.387839638, 3.684428282, 4.574463651, 4.611016532, 4.207405626, 5.142980275, 2.105975033, 3.997983327, 5.735868729, 3.018045689, 5.056777724, 5.674490594, 5.227952814, 4.767550988, 3.404672779, 0.176417758, 0.09079308, 3.679339342, 3.780625064, 4.162920572, 4.720840985, 2.670579322, 5.27570736, 4.86596631, 4.948965213, 3.148721019, 6.27123965, 5.776287736, 3.846994687, 4.779039044, 3.959457661, 0.046033977, 6.451738959, 0.813905855, 4.981972264, 5.817953965, 4.682852484, 2.65195039, 3.351498158, 4.371590922, 3.925482993, 1.802621308, 5.267152976, 5.230190714, 3.169129537, 5.433695261, 5.126852296, 2.100055912, 4.105725005, 2.655701239, 3.026341865, 3.888994512, 1.581449111, 4.001712184, 2.989484559, 4.824597306, 1.604829963, 4.016918797, 4.245084883, 5.014508839, 5.133420499, 4.647670246, 4.611947237, 5.731116157, 0.043632329, 5.431903048, 1.930043921, 5.212654544, 4.232616247, 4.626849691, 3.223032784, 4.606593241, 5.235776833, 4.626289019, 6.29886173, 3.88767928, 5.2538006, 4.226173249, 4.478359662, 1.50879321, 3.942344656, 2.876387086, 5.394268207, 6.666875865, 0.120625522, 4.908919041, 3.314022579, 2.747020395, 4.461281672, 5.644136045], [5.795207961, 5.30244445, 4.867425535, 4.779551802, 2.61205048, 2.214269068, 1.932597923, 3.638962356, 5.205560249, 5.06662784, 1.563375373, 3.941452854, 1.499421401, 3.902121829, 4.447359007, 0.700903703, 5.253256769, 4.10889491, 3.58325069, 5.47898248, 5.45366013, 4.925691864, 4.280361748, 3.629898622, 5.091206441, 3.904455196, 4.1902656, 3.415748933, 0.977339499, 2.684939668, 3.556458845, 5.384091608, 3.356490635, 3.794081018, 2.85416066, 5.312998729, 1.961764813, 3.891616523, 6.271263932, 3.118167498, 4.530618892, 5.606154371, 6.16710659, 4.201895718, 3.739308071, 4.06050745, 5.284232792, 3.753316781, 3.910282709, 0.037058811, 4.218301481, 4.48307667, 4.065801484, 0.127475704, 5.428917544, 4.135095658, 4.865861422, 2.820353812, 4.052712367, 5.450548144, 5.555567404, 3.642151649, 4.430810463, 5.324475087, 5.272647326, 4.74229084, 0.057953812, 6.039414138, 0.639009837, 1.56675915, 4.210736404, 5.483636517, 6.409759031, 5.50181235, 4.667695742, 4.860093742, 5.057989124, 5.380871758, 5.50619347, 3.489869149, 5.666178262, 5.007941329, 4.166350709, 2.660935232, 5.543624866, 2.582692318, 4.323053679, 4.537690549, 5.111941059, 2.576836038, 6.056959326, 2.945193225, 5.504442746, 5.124498535, 4.964196216, 4.354019061, 6.717147224, 5.306548067, 5.800884373, 1.279653144, 2.72026336, 3.788494661, 4.968294466, 2.720812098, 4.119685685, 6.029193566, 3.566782282, 4.304233574, 4.751524243, 5.371972446, 4.568806768, 3.526945183, 4.76224356, 3.846273661, 0.21503901, 4.249829099, 4.641992756, 4.417188216, 3.489120289, 3.868501083, 4.859011905, 5.23595945, 5.513417472, 0.926864776, 4.618632758, 5.055729276, 4.254815479, 3.596496306, 5.629749446, 4.402214634, 0.094300655, 5.576323799, 4.407250766, 2.088035732, 5.687557369, 3.592186712, 5.096008786, 1.910958641, 4.085373665, 3.670033579, 3.036545533, 4.370941229, 5.079960448, 5.309692799, 5.503586302, 0.069620606, 5.402921666, 4.323698638, 5.989303436, 3.475767147, 5.926328021, 2.259896139, 4.586157038, 2.246542773, 2.391667926, 5.496604874, 3.422244171], [5.078682839, 5.340300552, 4.675193225, 4.895255112, 5.187831473, 5.186976676, 5.305570771, 5.597236169, 5.331758593, 4.647791107, 4.459552275, 4.933330438, 5.043557988, 5.330550871, 5.110557433, 4.850351886, 5.318293339, 5.32288861, 5.584400341, 5.605474777, 5.527925775, 5.145420682, 5.380454485, 5.397977129, 5.727346529, 5.118345189, 5.197637397, 5.572848751, 4.624068132, 5.105158426, 4.846439157, 5.253497698, 5.030983557, 5.627396138, 5.061106528, 5.218320083, 5.115473195, 5.558725293, 5.0184962, 5.563063229, 4.730461714, 5.209971473, 4.817117714, 5.424178385, 4.733263763, 5.395165992, 5.284326455, 5.421532006, 4.987966114, 5.007408122, 4.966505221, 5.383618592, 5.161329437, 5.301983748, 5.519745375, 5.095952683, 5.551701187, 4.512214242], [2.774902154, 2.630478164, 5.795207961, 5.001970637, 5.804560603, 4.042269608, 4.684142105, 5.30244445, 4.846851814, 4.867425535, 1.700514292, 4.478325359, 5.308083054, 0.007935467, 4.779551802, 4.236517875, 3.208354315, 5.672832634, 2.61205048, 2.214269068, 4.29524768, 5.004483415, 5.195429496, 2.119129379, 0.093501696, 1.932597923, 3.638962356, 5.205560249, 5.06662784, 0.134729047, 3.94871297, 5.473679452, 4.732216549, 1.563375373, 5.549800991, 3.941452854, 1.499421401, 3.459289965, 3.361098221, 3.902121829, 3.186789733, 5.088262043, 4.447359007, 4.559606833, 3.499802526, 1.403123173, 4.200293257, 2.565584503, 0.700903703, 5.253256769, 2.710319347, 4.186910932, 5.147852491, 0.345454514, 4.10889491, 3.58325069, 3.664746779, 5.47898248, 0.091622933, 5.45366013, 4.925691864, 0.948042349, 4.280361748, 3.629898622, 1.451786097, 2.613487806, 0.857766545, 3.783908146, 5.091206441, 3.904455196, 4.1902656, 5.991172609, 3.415748933, 0.977339499, 2.464265197, 4.63155891, 3.038158362, 0.836080701, 2.684939668, 3.556458845, 5.384091608, 3.356490635, 0.13829587, 4.623368831, 5.907208194, 3.325028719, 3.794081018, 4.392604559, 2.85416066, 4.88262202, 4.04632429, 1.642685401, 5.312998729, 4.77784365, 3.644406617, 3.87310447, 1.961764813, 3.580180466, 4.770577477, 4.28245908, 3.891616523, 6.271263932, 0.122978823, 0.187892252, 0.097813946, 3.118167498, 4.682824399, 4.879718507, 3.722447444, 4.530618892, 5.606154371, 3.425035458, 6.16710659, 4.201895718, 3.739308071, 5.392069395, 4.06050745, 2.002442938, 5.284232792, 0.276745342, 5.404972926, 2.914650049, 2.030885505, 5.932904954, 3.753316781, 3.910282709, 2.168935935, 0.037058811, 1.792687132, 5.850180836, 4.218301481, 3.819787722, 3.217801011, 4.48307667, 4.065801484, 1.366214209, 3.547298049, 4.263035909, 1.674948699, 4.307518144, 0.21924635, 5.062849612, 4.750246322, 3.683181034, 3.834248039, 4.519372691, 0.127475704, 4.495138697, 1.656003871, 3.387839638, 5.428917544, 4.135095658, 3.684428282, 4.574463651, 4.865861422, 3.785986747, 4.611016532, 4.207405626, 2.820353812, 4.052712367, 5.230432836, 5.142980275, 4.815350503, 5.450548144, 2.105975033, 0.535076413, 0.203143009, 0.470026385, 3.997983327, 5.555567404, 5.640592587, 3.642151649, 5.735868729, 4.430810463, 5.324475087, 5.272647326, 3.018045689, 5.056777724, 5.674490594, 5.227952814, 4.767550988, 3.404672779, 4.74229084, 5.30657723, 0.057953812, 6.039414138, 0.176417758, 0.639009837, 3.115192257, 1.56675915, 0.09079308, 3.679339342, 4.210736404, 5.483636517, 3.780625064, 4.22845701, 4.162920572, 6.409759031, 5.50181235, 4.720840985, 2.670579322, 4.804386617, 5.27570736, 4.86596631, 4.667695742, 4.860093742, 5.057989124, 5.380871758, 5.50619347, 4.948965213, 2.181667111, 3.489869149, 5.666178262, 5.007941329, 3.148721019, 4.166350709, 6.27123965, 2.660935232, 2.980504291, 5.776287736, 5.543624866, 5.453941239, 3.846994687, 4.779039044, 2.582692318, 4.323053679, 4.537690549, 3.959457661, 5.111941059, 2.576836038, 0.046033977, 6.451738959, 2.010088038, 6.056959326, 0.813905855, 3.649751101, 4.981972264, 5.817953965, 0.165728677, 2.945193225, 0.637085281, 0.13138553, 4.682852484, 6.154052113, 2.65195039, 3.351498158, 4.371590922, 5.504442746, 0.069468278, 3.925482993, 5.124498535, 4.964196216, 1.802621308, 4.354019061, 6.717147224, 0.105981052, 5.267152976, 5.306548067, 5.230190714, 0.123577248, 5.800884373, 1.279653144, 2.72026336, 3.788494661, 0.064805143, 3.169129537, 5.433695261, 0.027135689, 5.126852296, 4.968294466, 2.100055912, 4.105725005, 2.720812098, 2.655701239, 2.247923869, 0.423089965, 5.845353051, 3.026341865, 2.461885784, 5.196982697, 4.971349036, 2.211224687, 3.888994512, 4.119685685, 1.581449111, 0.063670575, 3.599753393, 6.029193566, 3.566782282, 4.001712184, 2.989484559, 4.304233574, 4.751524243, 4.824597306, 0.104525916, 5.371972446, 4.419410122, 1.604829963, 4.016918797, 1.379190085, 0.710829043, 4.568806768, 3.526945183, 0.338029791, 0.04551762, 4.245084883, 5.014508839, 5.133420499, 2.758944848, 4.76224356, 3.846273661, 4.647670246, 0.088442903, 2.809217681, 4.611947237, 0.713181895, 0.21503901, 5.731116157, 4.249829099, 3.069368432, 4.641992756, 4.417188216, 0.043632329, 5.431903048, 0.087780769, 3.489120289, 1.930043921, 3.868501083, 4.859011905, 5.212654544, 4.146468683, 5.23595945, 5.513417472, 0.926864776, 4.618632758, 0.234130084, 4.232616247, 4.626849691, 5.842269877, 5.055729276, 4.254815479, 3.596496306, 3.691212538, 3.223032784, 3.025048999, 5.629749446, 4.606593241, 4.402214634, 5.161589441, 0.094300655, 5.576323799, 5.235776833, 4.626289019, 6.29886173, 2.660276743, 3.88767928, 0.036062633, 0.061097173, 5.2538006, 4.015920339, 4.407250766, 4.226173249, 4.478359662, 2.088035732, 1.50879321, 3.942344656, 5.687557369, 3.592186712, 5.096008786, 2.876387086, 4.592726714, 5.394268207, 6.666875865, 1.910958641, 4.085373665, 3.670033579, 0.120625522, 4.466625163, 4.183228442, 3.036545533, 4.370941229, 5.079960448, 4.908919041, 5.309692799, 3.841310977, 5.172245072, 5.503586302, 0.069620606, 3.314022579, 2.747020395, 4.461281672, 5.402921666, 4.323698638, 5.989303436, 3.475767147, 5.926328021, 2.259896139, 4.586157038, 2.246542773, 2.391667926, 5.496604874, 0.219110145, 3.875657213, 0.520244211, 3.422244171, 5.644136045], [4.085373665, 2.391667926, 5.205560249, 0.037058811, 0.345454514, 2.576836038, 4.323053679, 4.478359662, 5.312998729, 3.642151649, 5.096008786, 4.254815479, 5.272647326, 5.629749446, 5.483636517, 6.717147224, 5.504442746, 3.846273661, 5.306548067, 4.76224356, 3.036545533, 4.323698638, 3.629898622, 5.640592587, 6.056959326, 3.875657213, 3.526945183, 3.891616523, 3.638962356, 1.499421401, 4.430810463, 5.284232792, 5.989303436, 4.48307667, 4.249829099, 3.566782282, 6.039414138, 3.422244171, 3.753316781, 5.111941059, 5.30244445, 5.380871758, 4.618632758, 3.489120289, 0.127475704, 6.409759031, 0.639009837, 4.119685685, 1.604829963, 2.660935232, 5.402921666, 6.16710659, 2.088035732, 4.74229084, 1.961764813, 5.253256769, 4.183228442, 4.925691864, 2.945193225, 2.684939668, 2.61205048, 4.568806768, 1.910958641, 5.50181235, 3.475767147, 5.576323799, 5.50619347, 3.58325069, 4.586157038, 3.904455196, 6.271263932, 1.279653144, 1.563375373, 2.820353812, 3.910282709, 3.596496306, 5.503586302, 5.666178262, 5.384091608, 5.324475087, 5.453941239, 1.932597923, 3.941452854, 5.06662784, 5.795207961, 3.794081018, 4.447359007, 4.859011905, 4.207405626, 4.201895718, 5.124498535, 5.309692799, 4.867425535, 2.720812098, 4.407250766, 0.057953812, 5.926328021, 4.417188216, 4.135095658, 3.356490635, 4.210736404, 5.428917544, 3.556458845, 4.641992756, 5.687557369, 4.860093742, 5.079960448, 2.582692318, 5.606154371, 4.065801484, 5.496604874, 5.062849612, 5.091206441, 4.1902656, 4.537690549, 3.788494661, 5.800884373, 4.968294466, 4.166350709, 4.751524243, 1.56675915, 5.450548144, 2.259896139, 4.667695742, 0.21503901, 6.029193566, 0.069620606, 4.218301481, 5.057989124, 4.06050745, 3.739308071, 5.055729276, 4.370941229, 3.868501083, 4.865861422, 4.779551802, 5.007941329, 2.72026336, 0.700903703, 5.371972446, 5.45366013, 4.22845701, 3.118167498, 3.592186712, 4.052712367, 2.246542773, 0.977339499, 4.28245908, 3.415748933, 3.902121829, 5.23595945, 4.280361748, 4.530618892], [4.684142105, 2.168935935, 2.747020395, 4.226173249, 4.200293257, 3.018045689, 4.606593241, 0.813905855, 3.580180466, 5.267152976, 4.824597306, 4.626289019, 0.176417758, 2.613487806, 4.236517875]],
      explain1: 'This target has been approved as an anticancer drug target or as a drug candidate in preclinical development',
      explain2: 'There are currently no drugs in clinical development for these targets, but there is evidence to support their operability',
      explain3: 'There is currently no information or lack of information to support the operability of this target',
      explain4: 'This target is not a priority target'
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
    getBoxplot () {
      axios.post('/api/ldb/Boxplot', { gene_name: this.target })
        .then(res => {
          // this.boxplot_num = res.data.data
          // eslint-disable-next-line no-eval,no-unused-expressions
          this.flag = false
          // eslint-disable-next-line no-eval
          this.boxplot_num.push(eval(res.data.data))
          this.expr0 = this.boxplot_num[0][0]
          this.expr1 = this.boxplot_num[0][1]
          this.expr2 = this.boxplot_num[0][2]
          this.expr3 = this.boxplot_num[0][3]
          this.expr4 = this.boxplot_num[0][4]
          // console.log('箱线图')
          // console.log(this.boxplot_num[0])
          this.$nextTick(() => {
            this.myEcharts2()
          })
        })
    },
    getDetail () {
      axios.post('/api/ldb/Gene', { gene: this.target })
        .then(res => {
          this.detail = res.data.gene
          console.log('LOG的值')
          console.log(this.detail)
          // eslint-disable-next-line brace-style
          if (this.detail[0].Log2FC1 === 'missing') { this.leida_num.push('missing') }
          // eslint-disable-next-line no-eval
          else this.leida_num.push(eval(this.detail[0].Log2FC1))
          // eslint-disable-next-line brace-style
          if (this.detail[0].Log2FC2 === 'missing') { this.leida_num.push('missing') }
          // eslint-disable-next-line no-eval
          else this.leida_num.push(eval(this.detail[0].Log2FC2))
          // eslint-disable-next-line brace-style
          if (this.detail[0].Log2FC3 === 'missing') { this.leida_num.push('missing') }
          // eslint-disable-next-line no-eval
          else this.leida_num.push(eval(this.detail[0].Log2FC3))
          // eslint-disable-next-line brace-style
          if (this.detail[0].Log2FC4 === 'missing') { this.leida_num.push('missing') }
          // eslint-disable-next-line no-eval
          else this.leida_num.push(eval(this.detail[0].Log2FC4))
          // eslint-disable-next-line brace-style
          if (this.detail[0].Log2FC5 === 'missing') { this.leida_num.push('missing') }
          // eslint-disable-next-line no-eval
          else this.leida_num.push(eval(this.detail[0].Log2FC5))
          console.log('雷达的值', this.leida_num)
          console.log('绝对值', this.leida_num_abs)
          this.leida_num_abs = this.leida_num.map(Math.abs)
          this.$nextTick(() => {
            this.myEcharts1()
            // this.getHightOfCell()
          })
        })
    },
    /* getCellExp () {
      axios.post('/api/ldb/cellCluster2', { gene_name: this.target })
        .then(res => {
          this.normal = res.data.normal_list
          this.primary = res.data.primary_list
          this.replased = res.data.replased_list
          this.$nextTick(() => {
            this.myEchartCellNor()
            this.myEchartCellPri()
            this.myEchartCellRep()
          })
        })
    }, */
    // const cellEl = document.getElementById('precell')
    // this.preWidth = window.getComputedStyle(cellEl).width
    // console.log(this.preWidth)
    /*   getHightOfCell () {
      const cellEl = document.getElementById('precell')
      this.preWidth = window.getComputedStyle(cellEl).width
      console.log(this.preWidth)
    }, */
    getCellNor () {
      // const cellEl = document.getElementById('precell')
      // this.preWidth = window.getComputedStyle(cellEl).width
      // console.log(this.preWidth)
      axios.post('/api/ldb/cell_cluster_nor', { gene_name: this.target })
        .then(res => {
          this.normal = res.data.nor_list
          console.log(this.normal)
          this.$nextTick(() => {
            this.myEchartCellNor()
          })
        })
    },
    getCellPri () {
      axios.post('/api/ldb/cell_cluster_pri_TN', { gene_name: this.target })
        .then(res => {
          this.primaryTN = res.data.pri_TN_list
          this.$nextTick(() => {
            this.myEchartCellPri()
          })
        })
      axios.post('/api/ldb/cell_cluster_pri_other', { gene_name: this.target })
        .then(res => {
          this.primary = res.data.pri_other_list
          this.$nextTick(() => {
            this.myEchartCellPri()
          })
        })
      axios.post('/api/ldb/cell_cluster_pri_Tcell', { gene_name: this.target })
        .then(res => {
          this.primaryTcell = res.data.pri_Tcell_list
          this.$nextTick(() => {
            this.myEchartCellPri()
          })
        })
    },
    getCellRep () {
      axios.post('/api/ldb/cell_cluster_rep', { gene_name: this.target })
        .then(res => {
          this.replased = res.data.rep_list
          this.$nextTick(() => {
            this.myEchartCellRep()
          })
        })
    },
    getCellMeta () {
      axios.post('/api/ldb/cell_cluster_Meta', { gene_name: this.target })
        .then(res => {
          this.meta = res.data.meta_list
          console.log(this.meta)
          this.$nextTick(() => {
            this.myEchartCellMeta()
          })
        })
    },
    toArticle () {
      this.$router.push({ name: 'Article' })
    },
    myEchartCellNor () {
      // 基于准备好的dom，初始化echarts实例
      var myChart1 = this.$echarts.init(document.getElementById('normal'))
      // myChart1.resize({ width: this.preWidth, height: this.preWidth })
      // eslint-disable-next-line camelcase
      var tumor_list = this.normal.tumor_list
      // eslint-disable-next-line camelcase
      var nk_list = this.normal.nk_list
      // eslint-disable-next-line camelcase
      var endo_list = this.normal.endo_list
      // eslint-disable-next-line camelcase
      var mye_list = this.normal.mye_list
      // eslint-disable-next-line camelcase
      var tcell_list = this.normal.tcell_list
      // eslint-disable-next-line camelcase
      var hsc_list = this.normal.hsc_list
      // eslint-disable-next-line camelcase
      var bcell_list = this.normal.bcell_list
      // eslint-disable-next-line camelcase
      var hep_list = this.normal.hep_list
      // eslint-disable-next-line camelcase
      var und_list = this.normal.und_list
      // 指定图表的配置项和数据
      var option = {
        grid: {
          show: true,
          borderWidth: 1,
          borderColor: 'grey',
          left: '10%',
          right: '7%',
          top: 0,
          bottom: 25,
          containLabel: true
        },
        tooltip: {
          position: 'top',
          formatter: function (params) {
            var str =
              'Cell Type:' +
              params.seriesName
            return str
          }
        },
        xAxis: [
          {
            type: 'value',
            scale: false,
            axisLabel: { show: false },
            axisLine: { show: false },
            axisTick: { show: false },
            splitLine: {
              show: false
            },
            name: 'UMAP_1',
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
            axisLabel: { show: false },
            axisLine: { show: false },
            axisTick: { show: false },
            splitLine: {
              show: false
            },
            name: 'UMAP_2',
            nameLocation: 'middle',
            nameTextStyle: {
              color: 'black',
              fontSize: 10,
              padding: 2
            }
          }
        ],
        visualMap: { // visualMap 是视觉映射组件，用于进行『视觉编码』，也就是将数据映射到视觉元素（视觉通道）。
          show: false, // 是否显示组件
          type: 'continuous',
          max: 11, // 指定 visualMapContinuous 组件的允许的最大值
          min: 0,
          reeltime: true,
          dimension: 2,
          itemHeight: 140,
          itemWidth: 20,
          right: 'right',
          top: 'bottom',
          width: '20%',
          orient: 'horizontal',
          text: ['High', 'Low'],
          inRange: { // 定义 在选中范围中 的视觉元素。
            color: ['#D0CECD', '#AE3627']// 图元的颜色。
          }
        },
        dataZoom: [
          {
            type: 'inside',
            xAxisIndex: [0],
            start: 0,
            end: 100
          }],
        series: [
          {
            name: 'Tumor cell',
            type: 'scatter',
            symbolSize: 5,
            emphasis: {
              focus: 'series'
            },
            data: tumor_list
          },
          {
            name: 'NK cell',
            type: 'scatter',
            symbolSize: 5,
            emphasis: {
              focus: 'series'
            },
            data: nk_list
          },
          {
            name: 'Endothelial cell',
            type: 'scatter',
            symbolSize: 5,
            emphasis: {
              focus: 'series'
            },
            data: endo_list
          },
          {
            name: 'Myeloid cell',
            type: 'scatter',
            symbolSize: 5,
            emphasis: {
              focus: 'series'
            },
            data: mye_list
          },
          {
            name: 'T cell',
            type: 'scatter',
            symbolSize: 5,
            emphasis: {
              focus: 'series'
            },
            data: tcell_list
          },
          {
            name: 'Hepatic stellate cell',
            type: 'scatter',
            symbolSize: 5,
            emphasis: {
              focus: 'series'
            },
            data: hsc_list
          },
          {
            name: 'B cell',
            type: 'scatter',
            symbolSize: 5,
            emphasis: {
              focus: 'series'
            },
            data: bcell_list
          },
          {
            name: 'Hepatocytes',
            type: 'scatter',
            symbolSize: 5,
            emphasis: {
              focus: 'series'
            },
            data: hep_list
          },
          {
            name: 'undifine',
            type: 'scatter',
            symbolSize: 5,
            emphasis: {
              focus: 'series'
            },
            data: und_list
          }
        ]
      }

      // 使用刚指定的配置项和数据显示图表。
      myChart1.setOption(option)
    },
    myEchartCellPri () {
      // 基于准备好的dom，初始化echarts实例
      var myChart2 = this.$echarts.init(document.getElementById('primary'))
      // eslint-disable-next-line camelcase
      var tumor_list = this.primaryTN.tumor_list
      // eslint-disable-next-line camelcase
      var nk_list = this.primaryTN.nk_list
      // eslint-disable-next-line camelcase
      var endo_list = this.primary.endo_list
      // eslint-disable-next-line camelcase
      var mye_list = this.primary.mye_list
      // eslint-disable-next-line camelcase
      var tcell_list = this.primaryTcell.tcell_list
      // eslint-disable-next-line camelcase
      var hsc_list = this.primary.hsc_list
      // eslint-disable-next-line camelcase
      var bcell_list = this.primary.bcell_list
      // eslint-disable-next-line camelcase
      var hep_list = this.primary.hep_list
      // eslint-disable-next-line camelcase
      var und_list = this.primary.und_list
      // eslint-disable-next-line no-unused-vars
      var data = this.char_list
      // 指定图表的配置项和数据
      var option = {
        grid: {
          show: true,
          borderWidth: 1,
          borderColor: 'grey',
          left: '10%',
          right: '7%',
          top: 0,
          bottom: 25,
          containLabel: true
        },
        tooltip: {
          position: 'top',
          formatter: function (params) {
            var str =
              'Cell Type:' +
              params.seriesName
            return str
          }
        },
        xAxis: [
          {
            type: 'value',
            scale: false,
            axisLabel: { show: false },
            axisLine: { show: false },
            axisTick: { show: false },
            splitLine: {
              show: false
            },
            name: 'UMAP_1',
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
            axisLabel: { show: false },
            axisLine: { show: false },
            axisTick: { show: false },
            splitLine: {
              show: false
            },
            name: 'UMAP_2',
            nameLocation: 'middle',
            nameTextStyle: {
              color: 'black',
              fontSize: 10,
              padding: 2
            }
          }
        ],
        visualMap: { // visualMap 是视觉映射组件，用于进行『视觉编码』，也就是将数据映射到视觉元素（视觉通道）。
          show: false, // 是否显示组件
          type: 'continuous',
          max: 11, // 指定 visualMapContinuous 组件的允许的最大值
          min: 0,
          reeltime: true,
          dimension: 2,
          itemHeight: 140,
          itemWidth: 20,
          right: 'right',
          top: 'bottom',
          width: '20%',
          orient: 'horizontal',
          text: ['High', 'Low'], // 两端的文本，如 ['High', 'Low']
          inRange: { // 定义 在选中范围中 的视觉元素。
            color: ['#D0CECD', '#AE3627']// 图元的颜色。
          }
        },
        dataZoom: [
          {
            type: 'inside',
            xAxisIndex: [0],
            start: 0,
            end: 100
          }],
        series: [
          {
            name: 'Tumor cell',
            type: 'scatter',
            symbolSize: 5,
            emphasis: {
              focus: 'series'
            },
            data: tumor_list
          },
          {
            name: 'NK cell',
            type: 'scatter',
            symbolSize: 5,
            emphasis: {
              focus: 'series'
            },
            data: nk_list
          },
          {
            name: 'Endothelial cell',
            type: 'scatter',
            symbolSize: 5,
            emphasis: {
              focus: 'series'
            },
            data: endo_list
          },
          {
            name: 'Myeloid cell',
            type: 'scatter',
            symbolSize: 5,
            emphasis: {
              focus: 'series'
            },
            data: mye_list
          },
          {
            name: 'T cell',
            type: 'scatter',
            symbolSize: 5,
            emphasis: {
              focus: 'series'
            },
            data: tcell_list
          },
          {
            name: 'Hepatic stellate cell',
            type: 'scatter',
            symbolSize: 5,
            emphasis: {
              focus: 'series'
            },
            data: hsc_list
          },
          {
            name: 'B cell',
            type: 'scatter',
            symbolSize: 5,
            emphasis: {
              focus: 'series'
            },
            data: bcell_list
          },
          {
            name: 'Hepatocytes',
            type: 'scatter',
            symbolSize: 5,
            emphasis: {
              focus: 'series'
            },
            data: hep_list
          },
          {
            name: 'undifine',
            type: 'scatter',
            symbolSize: 5,
            emphasis: {
              focus: 'series'
            },
            data: und_list
          }
        ]
      }

      // 使用刚指定的配置项和数据显示图表。
      myChart2.setOption(option)
    },
    myEchartCellRep () {
      // 基于准备好的dom，初始化echarts实例
      var myChart3 = this.$echarts.init(document.getElementById('repleased'))
      /* eslint-disable */
      var tumor_list = this.replased.tumor_list
      var nk_list = this.replased.nk_list
      var endo_list = this.replased.endo_list
      var mye_list = this.replased.mye_list
      var tcell_list = this.replased.tcell_list
      var hsc_list = this.replased.hsc_list
      var bcell_list = this.replased.bcell_list
      var hep_list = this.replased.hep_list
      var und_list = this.replased.und_list
      /* eslint-enable */
      // 指定图表的配置项和数据
      var option = {
        grid: {
          show: true,
          borderWidth: 1,
          borderColor: 'grey',
          left: '10%',
          right: '7%',
          top: '0%',
          containLabel: true
        },
        tooltip: {
          position: 'top',
          formatter: function (params) {
            var str =
              'Cell Type:' +
              params.seriesName
            return str
          }
        },
        xAxis: [
          {
            type: 'value',
            scale: false,
            axisLabel: { show: false },
            axisLine: { show: false },
            axisTick: { show: false },
            splitLine: {
              show: false
            },
            name: 'UMAP_1',
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
            axisLabel: { show: false },
            axisLine: { show: false },
            axisTick: { show: false },
            splitLine: {
              show: false
            },
            name: 'UMAP_2',
            nameLocation: 'middle',
            nameTextStyle: {
              color: 'black',
              fontSize: 10,
              padding: 2
            }
          }
        ],
        visualMap: { // visualMap 是视觉映射组件，用于进行『视觉编码』，也就是将数据映射到视觉元素（视觉通道）。
          show: false, // 是否显示组件
          type: 'continuous',
          max: 11, // 指定 visualMapContinuous 组件的允许的最大值
          min: 0,
          reeltime: true,
          dimension: 2,
          itemHeight: 140,
          itemWidth: 20,
          right: 'right',
          top: 'bottom',
          width: '20%',
          orient: 'horizontal',
          text: ['High', 'Low'], // 两端的文本，如 ['High', 'Low']
          inRange: { // 定义 在选中范围中 的视觉元素。
            color: ['#D0CECD', '#AE3627']// 图元的颜色。
          }
        },
        dataZoom: [
          {
            type: 'inside',
            xAxisIndex: [0],
            start: 0,
            end: 100
          }],
        series: [
          {
            name: 'Tumor cell',
            type: 'scatter',
            symbolSize: 5,
            emphasis: {
              focus: 'series'
            },
            data: tumor_list
          },
          {
            name: 'NK cell',
            type: 'scatter',
            symbolSize: 5,
            emphasis: {
              focus: 'series'
            },
            data: nk_list
          },
          {
            name: 'Endothelial cell',
            type: 'scatter',
            symbolSize: 5,
            emphasis: {
              focus: 'series'
            },
            data: endo_list
          },
          {
            name: 'Myeloid cell',
            type: 'scatter',
            symbolSize: 5,
            emphasis: {
              focus: 'series'
            },
            data: mye_list
          },
          {
            name: 'T cell',
            type: 'scatter',
            symbolSize: 5,
            emphasis: {
              focus: 'series'
            },
            data: tcell_list
          },
          {
            name: 'Hepatic stellate cell',
            type: 'scatter',
            symbolSize: 5,
            emphasis: {
              focus: 'series'
            },
            data: hsc_list
          },
          {
            name: 'B cell',
            type: 'scatter',
            symbolSize: 5,
            emphasis: {
              focus: 'series'
            },
            data: bcell_list
          },
          {
            name: 'Hepatocytes',
            type: 'scatter',
            symbolSize: 5,
            emphasis: {
              focus: 'series'
            },
            data: hep_list
          },
          {
            name: 'undifine',
            type: 'scatter',
            symbolSize: 5,
            emphasis: {
              focus: 'series'
            },
            data: und_list
          }
        ]
      }

      // 使用刚指定的配置项和数据显示图表。
      myChart3.setOption(option)
    },
    myEchartCellMeta () {
      // 基于准备好的dom，初始化echarts实例
      var myChart4 = this.$echarts.init(document.getElementById('meta'))
      /* eslint-disable */
      var tumor_list = this.meta.tumor_list
      var nk_list = this.meta.nk_list
      var endo_list = this.meta.endo_list
      var mye_list = this.meta.mye_list
      var tcell_list = this.meta.tcell_list
      var hsc_list = this.meta.hsc_list
      var bcell_list = this.meta.bcell_list
      var hep_list = this.meta.hep_list
      var und_list = this.meta.und_list
      /* eslint-enable */
      // 指定图表的配置项和数据
      var option = {
        grid: {
          show: true,
          borderWidth: 1,
          borderColor: 'grey',
          left: '10%',
          right: '7%',
          top: '0%',
          containLabel: true
        },
        tooltip: {
          position: 'top',
          formatter: function (params) {
            var str =
              'Cell Type:' +
              params.seriesName
            return str
          }
        },
        xAxis: [
          {
            type: 'value',
            scale: false,
            axisLabel: { show: false },
            axisLine: { show: false },
            axisTick: { show: false },
            splitLine: {
              show: false
            },
            name: 'UMAP_1',
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
            axisLabel: { show: false },
            axisLine: { show: false },
            axisTick: { show: false },
            splitLine: {
              show: false
            },
            name: 'UMAP_2',
            nameLocation: 'middle',
            nameTextStyle: {
              color: 'black',
              fontSize: 10,
              padding: 2
            }
          }
        ],
        visualMap: { // visualMap 是视觉映射组件，用于进行『视觉编码』，也就是将数据映射到视觉元素（视觉通道）。
          show: false, // 是否显示组件
          type: 'continuous',
          max: 11, // 指定 visualMapContinuous 组件的允许的最大值
          min: 0,
          reeltime: true,
          dimension: 2,
          itemHeight: 140,
          itemWidth: 20,
          right: 'right',
          top: 'bottom',
          width: '20%',
          orient: 'horizontal',
          text: ['High', 'Low'], // 两端的文本，如 ['High', 'Low']
          inRange: { // 定义 在选中范围中 的视觉元素。
            color: ['#D0CECD', '#AE3627']// 图元的颜色。
          }
        },
        dataZoom: [
          {
            type: 'inside',
            xAxisIndex: [0],
            start: 0,
            end: 100
          }],
        series: [
          {
            name: 'Tumor cell',
            type: 'scatter',
            symbolSize: 5,
            emphasis: {
              focus: 'series'
            },
            data: tumor_list
          },
          {
            name: 'NK cell',
            type: 'scatter',
            symbolSize: 5,
            emphasis: {
              focus: 'series'
            },
            data: nk_list
          },
          {
            name: 'Endothelial cell',
            type: 'scatter',
            symbolSize: 5,
            emphasis: {
              focus: 'series'
            },
            data: endo_list
          },
          {
            name: 'Myeloid cell',
            type: 'scatter',
            symbolSize: 5,
            emphasis: {
              focus: 'series'
            },
            data: mye_list
          },
          {
            name: 'T cell',
            type: 'scatter',
            symbolSize: 5,
            emphasis: {
              focus: 'series'
            },
            data: tcell_list
          },
          {
            name: 'Hepatic stellate cell',
            type: 'scatter',
            symbolSize: 5,
            emphasis: {
              focus: 'series'
            },
            data: hsc_list
          },
          {
            name: 'B cell',
            type: 'scatter',
            symbolSize: 5,
            emphasis: {
              focus: 'series'
            },
            data: bcell_list
          },
          {
            name: 'Hepatocytes',
            type: 'scatter',
            symbolSize: 5,
            emphasis: {
              focus: 'series'
            },
            data: hep_list
          },
          {
            name: 'undifine',
            type: 'scatter',
            symbolSize: 5,
            emphasis: {
              focus: 'series'
            },
            data: und_list
          }
        ]
      }

      // 使用刚指定的配置项和数据显示图表。
      myChart4.setOption(option)
    },
    myEcharts1 () {
      var myChart = this.$echarts.init(document.getElementById('leida'))
      // 指定图表的配置项和数据
      var option
      var i = -1

      option = {
        tooltip: {
          trigger: 'axis'
        },
        legend: {
          left: 'center',
          data: [
            '基因'
          ]
        },
        radar: [{
          indicator: [
            { text: 'Relapse/relapse-free\nlog2FC1', max: 4, min: -4 },
            { text: 'Relapse/Adjacent\nlog2FC2', max: 6, min: -6, axisLabel: { show: true } },
            { text: 'Relapse/Primary\nlog2FC3', max: 4, min: -4 },
            { text: 'relapse-free/Adjacent\nlog2FC4', max: 6, min: -6 },
            { text: 'primary tumor/Adjacent\nlog2FC5', max: 6, min: -6 }
          ],
          center: ['50%', '50%'], // 圆心位置
          radius: 100, // 图的大小
          splitNumber: 6, // 分割环数
          splitLine: { // (这里是指所有圆环)坐标轴在 grid 区域中的分隔线。
            lineStyle: {
              color: ['blue', 'blue', 'green', 'black', 'orange', 'pink', 'red'], // 分隔线颜色，可设置成数组
              width: 1 // 分隔线线宽
            }
          },
          axisTick: {
            show: true,
            length: 3
          },
          name: {
            rich: {
              a: {
                color: 'black',
                lineHeight: 20
              },
              b: {
                color: 'black',
                align: 'center',
                padding: 2,
                borderRadius: 4
              }
            },
            formatter: (a, b) => {
              i++
              return `{a|${a}}={b|${this.leida_num[i]}}`
            }
          }
        }
        ],
        series: [
          {
            type: 'radar',
            areaStyle: {},
            data: [
              {
                value: this.leida_num_abs
              }
            ]
          }
        ]
      }
      // 使用刚指定的配置项和数据显示图表。
      myChart.setOption(option)
    },
    myEcharts2 () {
      var myChart = this.$echarts.init(document.getElementById('main'))
      // 指定图表的配置项和数据
      var option
      var data = echarts.dataTool.prepareBoxplotData(this.boxplot_num[0])
      // var data = this.boxplot_num[0]
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
          data: ['Recurrence', 'Recurrence-free', 'Normal', 'Tumor', 'Metastasis', 'Metastasis-free'],
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
            color: 'black',
            textStyle: {
              color: '#333'
            }

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
                  'tissue ' + param.name + ': ',
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
    /* myEcharts2 () {
      var myChart = this.$echarts.init(document.getElementById('main'))
      // 指定图表的配置项和数据
      var option
      // var data = echarts.dataTool.prepareBoxplotData(this.boxplot_num[0])
      // var data = [this.boxplot_num[0]]
      var data = this.test
      console.log('数据')
      console.log(data)
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
        dataset: [
          {
            // prettier-ignore
            source: data
          },
          {
            transform: {
              type: 'boxplot',
              config: { itemNameFormatter: 'expr {value}' }
            }
          },
          {
            fromDatasetIndex: 1,
            fromTransformResult: 1
          }
        ],
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
            datasetIndex: 1,
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
            datasetIndex: 2
          }
        ]
      }
      // 使用刚指定的配置项和数据显示图表。
      myChart.setOption(option)
    }, */
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
      window.open(this.url, '_blank')
    },
    toDrug: function (target) {
      this.url = 'https://www.genecards.org/cgi-bin/carddisp.pl?gene=' + target + '#drugs_compounds'
      window.open(this.url, '_blank')
    }
  },
  props: ['search'], // 接受父组件的传值，
  beforeUpdate () {
    console.log(this.search)
  },
  created () {
    this.target = this.search.toUpperCase()
    this.getBoxplot()
    this.getDetail()
    // this.getCellExp()
    this.getCellNor()
    this.getCellPri()
    this.getCellRep()
    this.getCellMeta()
  },
  mounted () {
    const cellEl = document.getElementById('precell')
    this.preWidth = window.getComputedStyle(cellEl).width
    console.log(this.preWidth)
    // this.getCellNor()
    // this.getCellPri()
    // this.getCellRep()
    // this.getCellMeta()
  },
  watch: {
    // 监听相同路由下参数变化的时候，从而实现异步刷新
    '$route' (to, from) {
      this.target = this.search.toUpperCase()
      // this.getCellExp()
      this.getBoxplot()
      this.getDetail()
      this.getCellNor()
      this.getCellPri()
      this.getCellRep()
      this.getCellMeta()
    }
  }
  /* beforeDestroy () {
    this.bus.$emit('change', this.target)// 通过$emit向外层触发事件并传递参数；第一个参数是事件名字随便起但需跟$on中的事件名字一样
    console.log('传值了', this.target)
  } */
}
</script>

<style scoped>
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

</style>
