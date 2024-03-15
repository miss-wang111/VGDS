<template>
  <v-row>
    <v-col cols="12">
      <v-card
      elevation="5">

          <v-card height="100" width="100" color="green"
                  style="position: absolute;top:-20px;left:20px"
                  elevation="13">
            <v-icon color="white" class="mt-7" x-large>mdi-clipboard-text</v-icon>
          </v-card>

        <v-card-title class="ml-16 pl-16 ">Dataset Detail</v-card-title>
        <v-simple-table class="mt-5">
          <template v-slot:default>
            <thead>
            <tr>
              <th class="text-center ">Dataset Num</th>
              <th class="text-center">Dataset</th>
              <th class="text-center">Tag</th>
<!--              <th class="text-center">Title</th>-->
              <th class="text-center">Type</th>
              <th class="text-center">Platform</th>
              <th class="text-center">Genes Num</th>
              <th class="text-center">Sample Num</th>
              <th class="text-center">Detail</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="item in data" :key="item.Dataset">
              <td>{{ item.Dataset_Num }}</td>
              <td>{{ item.Dataset }}</td>
              <td>{{ item.Tag}}</td>
              <td>{{ item.Type }}</td>
              <td>{{ item.Platform }}</td>
              <td>{{ item.Genes_Num }}</td>
              <td>{{ item.Sample_Num }}</td>
              <td>
                <v-menu offset-y>
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn
                      color="primary"
                      dark
                      small
                      icon
                      v-bind="attrs"
                      v-on="on"
                    >
                      <v-icon>
                        mdi-file-settings-outline
                      </v-icon>
                    </v-btn>
                  </template>
                  <v-list>
                    <v-list-item
                      v-for="(item, index) in items"
                      :key="index"
                      @click=""
                    >
                      <v-list-item-title>{{ item.title }}</v-list-item-title>
                    </v-list-item>
                  </v-list>
                </v-menu>
              </td>
            </tr>
            </tbody>
          </template>
        </v-simple-table>
      </v-card>
      <v-dialog
        v-model = "flag"
      width="200"
      style="position: ">
        <v-card
          width="200"
        height="200">
          hello
        </v-card>
      </v-dialog>
    </v-col>
    <v-col cols="12">
      <v-card
        outlined
        class="mt-n6"
        flat>
        <v-simple-table >
          <template v-slot:default>
            <thead>
            <tr>
              <th class="text-center ">Dataset Num</th>
              <th class="text-center">Dataset</th>
              <th class="text-center">Tag</th>
              <!--              <th class="text-center">Title</th>-->
              <th class="text-center">Type</th>
              <th class="text-center">Platform</th>
              <th class="text-center">Genes Num</th>
              <th class="text-center">Sample Num</th>
              <th class="text-center">Detail</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="item in data" :key="item.Dataset">
              <td>{{ item.Dataset_Num }}</td>
              <td>{{ item.Dataset }}</td>
              <td>{{ item.Tag}}</td>
              <td>{{ item.Type }}</td>
              <td>{{ item.Platform }}</td>
              <td>{{ item.Genes_Num }}</td>
              <td>{{ item.Sample_Num }}</td>
              <td>
                <v-menu offset-y>
                  <template v-slot:activator="{ on, attrs }">
                    <v-btn
                      color="primary"
                      dark
                      small
                      icon
                      v-bind="attrs"
                      v-on="on"
                      @click="getSample(item.Dataset_Num)"
                    >
                      <v-icon>
                        mdi-file-settings-outline
                      </v-icon>
                    </v-btn>
                  </template>
                  <v-list>
                    <v-list-item
                      v-for="(item, index) in items"
                      :key="index"
                    >
                      <v-list-item-title>{{ item.title1 }}</v-list-item-title>
                    </v-list-item>
                  </v-list>
                </v-menu>
              </td>
            </tr>
            </tbody>
          </template>
        </v-simple-table>
      </v-card>
      <v-dialog
        v-model = "flag"
        width="200"
        >
        <v-card
          width="200"
          height="200">
          hello
        </v-card>
      </v-dialog>
    </v-col>
  </v-row>
</template>
<script>
export default {
  name: 'datatable',
  data () {
    return {
      flag: false,
      data: [
        {
          Dataset_Num: 'HCCMRDB1',
          Dataset: 'GSE27635',
          Tag: 'Metastasis',
          Title: 'Potential Prognostic Biomarkers for Bone Metastasis from Hepatocellular Carcinoma',
          Type: 'Affymetrix',
          Platform: 'GPL5858',
          Genes_Num: 502,
          Groups_Detail: 'tumor:Metastasis:24,Non_Metastasis:24 \n adjacent:Metastasis:24,Non_Metastasis:24',
          Sample_Num: 96
        },
        {
          Dataset_Num: 'HCCMRDB2',
          Dataset: 'GSE28248',
          Tag: 'Metastasis',
          Title: 'Gene Expression Profiling of Fixed Tissues of Lymph Node Metastasis in Hepatocellular Carcinoma',
          Type: 'Affymetrix',
          Platform: 'GPL5858',
          Genes_Num: 502,
          Groups_Detail: 'tumor:Metastasis:24,Non_Metastasis:24 \n adjacent:Metastasis:24,Non_Metastasis:24',
          Sample_Num: 80
        },
        {
          Dataset_Num: 'HCCMRDB3',
          Dataset: 'GSE40367',
          Tag: 'Metastasis',
          Title: 'Gene expression analysis of liver and colon cancer primary tumors and metastasis',
          Type: 'Affymetrix',
          Platform: 'GPL570',
          Genes_Num: 23346,
          Groups_Detail: 'tumor:Metastasis:24,Non_Metastasis:24 \n adjacent:Metastasis:24,Non_Metastasis:24',
          Sample_Num: 40
        },
        {
          Dataset_Num: 'HCCMRDB4',
          Dataset: 'GSE364',
          Tag: 'Metastasis',
          Title: 'Molecular profiling of human hepatocarcinogenesis',
          Type: 'Affymetrix',
          Platform: 'GPL257',
          Genes_Num: 7672,
          Groups_Detail: 'tumor:Metastasis:24,Non_Metastasis:24 \n adjacent:Metastasis:24,Non_Metastasis:24',
          Sample_Num: 85
        },
        {
          Dataset_Num: 'HCCMRDB5',
          Dataset: 'GSE56545',
          Tag: 'Recurence',
          Title: 'mRNA profiling of Hepatocellular carcinoma (HCC)',
          Type: 'RNA_seq',
          Platform: 'GPL15433',
          Genes_Num: 51061,
          Groups_Detail: 'tumor:Metastasis:24,Non_Metastasis:24 \n adjacent:Metastasis:24,Non_Metastasis:24',
          Sample_Num: 59
        },
        {
          Dataset_Num: 'HCCMRDB6',
          Dataset: 'GSE101432',
          Tag: 'Recurence',
          Title: 'Comprehensive transcriptome analysis in human liver',
          Type: 'RNA_seq',
          Platform: 'GPL11154',
          Genes_Num: 59346,
          Groups_Detail: 'tumor:Metastasis:24,Non_Metastasis:24 \n adjacent:Metastasis:24,Non_Metastasis:24',
          Sample_Num: 22
        },
        {
          Dataset_Num: 'HCCMRDB7',
          Dataset: 'GSE14520',
          Tag: 'Recurence',
          Title: 'Comprehensive transcriptome analysis in human liver',
          Type: 'Affymetrix',
          Platform: 'GPL571',
          Genes_Num: 12491,
          Groups_Detail: 'tumor:Metastasis:24,Non_Metastasis:24 \n adjacent:Metastasis:24,Non_Metastasis:24',
          Sample_Num: 40
        },
        {
          Dataset_Num: 'HCCMRDB8',
          Dataset: 'GSE14520',
          Tag: 'Recurence',
          Title: 'Comprehensive transcriptome analysis in human liver',
          Type: 'Affymetrix',
          Platform: 'GPL3921',
          Genes_Num: 12491,
          Groups_Detail: 'tumor:Metastasis:24,Non_Metastasis:24 \n adjacent:Metastasis:24,Non_Metastasis:24',
          Sample_Num: 441
        },
        {
          Dataset_Num: 'HCCMRDB9',
          Dataset: 'GSE76427',
          Tag: 'Recurence',
          Title: 'Microarray expression data for tumor and adjacent non-tumor tissues from hepatocellular carcinoma patients',
          Type: 'Affymetrix',
          Platform: 'GPL10558',
          Genes_Num: 20446,
          Groups_Detail: 'tumor:Metastasis:24,Non_Metastasis:24 \n adjacent:Metastasis:24,Non_Metastasis:24',
          Sample_Num: 158
        },
        {
          Dataset_Num: 'HCCMRDB10',
          Dataset: 'TCGA_GTEX',
          Tag: 'Recurence,',
          Title: 'Microarray expression data for tumor and adjacent non-tumor tissues from hepatocellular carcinoma patients',
          Type: 'RNA_seq',
          Platform: 'GPL10558',
          Genes_Num: 28633,
          Groups_Detail: 'tumor:Metastasis:24,Non_Metastasis:24 \n adjacent:Metastasis:24,Non_Metastasis:24',
          Sample_Num: 465
        }

      ],
      group: [

      ],
      items: [
        { title1: 'Click Me' },
        { title1: 'Click Me' },
        { title1: 'Click Me' },
        { title1: 'Click Me 2' }
      ]
    }
  },
  methods: {
    get_group (Dataset) {
      this.flag = true
    },
    getSample (dataset) {
      if (dataset === 'HCCMRDB1') {
        this.items = [
          { title1: '瘤内：骨转移24' },
          { title1: '瘤内：非转移24' },
          { title1: '瘤周：骨转移24' },
          { title1: '瘤周：非转移24' }
        ]
      } else if (dataset === 'HCCMRDB2') {
        this.items = [
          { title1: '瘤内：淋巴转移20' },
          { title1: '瘤内：非转移20' },
          { title1: '瘤周：淋巴转移20' },
          { title1: '瘤周：非转移20' }
        ]
      } else if (dataset === 'HCCMRDB3') {
        this.items = [
          { title1: '转移：20' },
          { title1: '非转移： 10' },
          { title1: '原发： 10' }
        ]
      } else if (dataset === 'HCCMRDB4') {
        this.items = [
          { title1: '原发：30' },
          { title1: '转发：28' },
          { title1: '非转移：27' }
        ]
      } else if (dataset === 'HCCMRDB5') {
        this.items = [
          { title1: '复发：17' },
          { title1: '非复发：13' },
          { title1: '复发临近：16' },
          { title1: '非复发临近：13' }
        ]
      } else if (dataset === 'HCCMRDB6') {
        this.items = [
          { title1: '原发：17' },
          { title1: '复发（继发）：5' }
        ]
      } else if (dataset === 'HCCMRDB7') {
        this.items = [
          { title1: '复发：15' },
          { title1: '不复发：6' },
          { title1: '邻近：19' }
        ]
      } else if (dataset === 'HCCMRDB8') {
        this.items = [
          { title1: '复发：121' },
          { title1: '不复发：100' },
          { title1: '邻近：220' }
        ]
      } else if (dataset === 'HCCMRDB9') {
        this.items = [
          { title1: '复发：48' },
          { title1: '不复发：60' },
          { title1: '复发临近:20' },
          { title1: '不复发临近：30' }
        ]
      } else if (dataset === 'HCCMRDB10') {
        this.items = [
          { title1: '转移：155' },
          { title1: '非转移：15' },
          { title1: '复发：148' },
          { title1: '不复发：158' }
        ]
      }
    }

  }
}
</script>
<style scoped lang="scss">
.head1{
  font-family: "Times New Roman";

}
.content{
  font-family: "Garamond";
  font-size: large;

}

</style>
