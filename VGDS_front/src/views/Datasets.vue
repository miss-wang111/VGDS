<template>
  <div class="ml-5 mr-5">
    <v-container>
      <v-row>
        <v-col cols="8">
          <div class="d-flex justify-left">
            <h2 style="color:#6D819C " class="mt-n3 pt-3 pb-0 mb-0"> Choose Datasets</h2>
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
      <p style="color:#6D819C " class="d-flex justify-left ">In this page, You can select datasets to analyze.  </p>
      <p style="color:#6D819C;font-size:13px;text-align:left" class="d-flex justify-left ">This panel displays detailed information about the dataset, including the data source, sample volume, sequencing platform, and the number of raw data samples in the GEO database.
        You can click on the small square on the far left to select the dataset of interest, and click on the analysis entry on the left to enter the analysis page.
        These pages will display the dataset you have selected and allow you to analyze and visualize it.</p>
      <v-card
      flat>
        <v-data-table
          v-model="selected"
          :headers="headers"
          :items="desserts"
          :single-select="true"
          item-key="Dataset_Num"
          show-select
          hide-default-footer
          class="elevation-1"
        >
          <template v-slot:item.details="{item}">
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
          </template>
        </v-data-table>
      </v-card>
    </v-container>
  </div>

</template>

<script>
export default {
  name: 'Datasets',
  data () {
    return {
      items: [
        { title1: 'Click Me' },
        { title1: 'Click Me' },
        { title1: 'Click Me' },
        { title1: 'Click Me 2' }
      ],
      selected: [],
      dataset: {},
      headers: [
        {
          text: 'Dataset Num',
          align: 'start',
          value: 'Dataset_Num'
        },
        { text: 'Dataset', value: 'Dataset' },
        { text: 'Tag', value: 'Tag' },
        { text: 'Type', value: 'Type' },
        { text: 'Platform', value: 'Platform' },
        { text: 'Genes_Num', value: 'Genes_Num' },
        { text: 'Sample_Num', value: 'Sample_Num' },
        { text: 'Detail', value: 'details' }
      ],
      desserts: [
        {
          Dataset_Num: 'HCCMRDB1',
          Dataset: 'GSE27635',
          Tag: 'Metastasis',
          Title: 'Potential Prognostic Biomarkers for Bone Metastasis from Hepatocellular Carcinoma',
          Type: 'Microarray',
          Platform: 'GPL5858',
          Genes_Num: 502,
          Groups_Detail: 'tumor:Metastasis:24,Non_Metastasis:24 \n adjacent:Metastasis:24,Non_Metastasis:24',
          tumor_Metastasis: 24,
          adjacent_Metastasis: 24,
          Sample_Num: 96
        },
        {
          Dataset_Num: 'HCCMRDB2',
          Dataset: 'GSE28248',
          Tag: 'Metastasis',
          Title: 'Gene Expression Profiling of Fixed Tissues of Lymph Node Metastasis in Hepatocellular Carcinoma',
          Type: 'Microarray',
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
          Type: 'Microarray',
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
          Type: 'Microarray',
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
          Type: 'Microarray',
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
          Type: 'Microarray',
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
          Type: 'Microarray',
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
      ]
    }
  },
  methods: {
    getSample (dataset) {
      if (dataset === 'HCCMRDB1') {
        this.items = [
          { title1: 'tumor：Bone Metastasis 24' },
          { title1: 'tumor：Metastases-free 24' },
          { title1: 'adjacent：Bone Metastasis 24' },
          { title1: 'adjacent：Metastases-free 24' }
        ]
      } else if (dataset === 'HCCMRDB2') {
        this.items = [
          { title1: 'tumor：lymph node Metastasis 20' },
          { title1: 'tumor：Metastases-free 20' },
          { title1: 'adjacent：lymph node Metastasis 20' },
          { title1: 'adjacent：Metastases-free 20' }
        ]
      } else if (dataset === 'HCCMRDB3') {
        this.items = [
          { title1: 'metastasis tumor：20' },
          { title1: 'primary tumors:metastases-free 10' },
          { title1: 'primary tumors: metastasis 10' }
        ]
      } else if (dataset === 'HCCMRDB4') {
        this.items = [
          { title1: 'primary tumor：30' },
          { title1: 'Metastasis：28' },
          { title1: 'Metastases-free tumor：27' }
        ]
      } else if (dataset === 'HCCMRDB5') {
        this.items = [
          { title1: 'recurrent tumors： 9' },
          { title1: 'primary tumors :non-recurrent 12' },
          { title1: 'adjacent：recurrent tumors：9' },
          { title1: 'adjacent：non-recurrent tumors 12' }
        ]
      } else if (dataset === 'HCCMRDB6') {
        this.items = [
          { title1: 'primary tumors：17' },
          { title1: 'recurrent tumors：5' }
        ]
      } else if (dataset === 'HCCMRDB7') {
        this.items = [
          { title1: 'primary tumors: recurrent 15' },
          { title1: 'primary tumors :non-recurrent 6' },
          { title1: 'adjacent tissue：19' }
        ]
      } else if (dataset === 'HCCMRDB8') {
        this.items = [
          { title1: 'primary tumors: recurrent 121' },
          { title1: 'primary tumors :non-recurrent 100' },
          { title1: 'adjacent：220' }
        ]
      } else if (dataset === 'HCCMRDB9') {
        this.items = [
          { title1: 'primary tumors: recurrent 48' },
          { title1: 'primary tumors :non-recurrent 60' },
          { title1: 'adjacent: primary tumors-recurrent 20' },
          { title1: 'adjacent：non-recurrent 30' }
        ]
      } else if (dataset === 'HCCMRDB10') {
        this.items = [
          { title1: 'primary tumors:Metastasis：155' },
          { title1: 'primary tumors:Metastases-free：15' },
          { title1: 'primary tumors:recurrent 148' },
          { title1: 'primary tumors:non-recurrent 158' },
          { title1: 'adjacent:58' },
          { title1: 'normal tissue:102' }
        ]
      }
    },
    toAnalyze () {
      this.GLOBAL.Dataset = this.selected
      this.$router.push({ name: 'Differential' })
    }
  },
  watch: {
    selected (newName, oldName) {
      this.GLOBAL.Dataset = newName
    }
  }
}
</script>

<style scoped>

</style>
