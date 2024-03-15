<template>
  <div id="app">
    <v-app id="inspire">
      <v-app id="inspire">
        <v-navigation-drawer
          app
          color="#192d47"
          dark
          width="200"
          permanent
        >
          <v-list>
            <v-list-item>
              <img width="150" src="@/assets/logo6.png"/>
            </v-list-item>
            <v-list-item>
              <v-list-item-content>
                <v-list-item-subtitle class=" blue-grey--text text--lighten-2">
                  An Effective Database System
                </v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
          </v-list>
          <v-divider></v-divider>
          <v-list dense>
            <template v-for="item in items">
              <v-row
                v-if="item.heading"
                :key="item.heading"
                align="left"
              >
                <v-col cols="6">
                  <v-subheader v-if="item.heading">
                    {{ item.heading }}
                  </v-subheader>
                </v-col>
                <v-col
                  cols="6"
                  class="text-center"
                >
                  <a
                    href="#!"
                    class="body-2 black--text"
                  >EDIT</a>
                </v-col>
              </v-row>
              <v-list-group
                color="#55967e"
                v-else-if="item.children"
                :key="item.text"
                align="left"
                prepend-icon="mdi-chart-box-outline"
                append-icon="mdi-chevron-down"
              >
                <template v-slot:activator>
                  <v-list-item-content>
                    <v-list-item-title>
                      {{ item.text }}
                    </v-list-item-title>
                  </v-list-item-content>
                </template>
                <v-list-item
                  v-for="(child, i) in item.children"
                  :key="i"
                  :to="child.path"
                  link
                >
                  <v-list-item-action v-if="child.icon">
                    <v-icon>{{ child.icon }}</v-icon>
                  </v-list-item-action>
                  <v-list-item-content>
                    <v-list-item-title>
                      {{ child.text }}
                    </v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list-group>
              <v-list-item
                v-else
                :key="item.text"
                :to="item.path"
                link
                color="#55967e"
              >
                <v-list-item-action>
                  <v-icon>{{ item.icon }}</v-icon>
                </v-list-item-action>
                <v-list-item-content>
                  <v-list-item-title align="left">
                    {{ item.text }}
                  </v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </template>
          </v-list>
            <v-divider></v-divider>
<!--          <v-list
              nav
              dense
            >
              <v-list-item-group
                v-model="selectedItem"
                color="#55967e"
              >
                <v-list-item
                  v-for="(item, i) in items"
                  :key="i"
                  :to="item.path"
                >
                  <v-list-item-icon>
                    <v-icon v-text="item.icon"></v-icon>
                  </v-list-item-icon>
                  <v-list-item-content>
                    <v-list-item-title align="left" v-text="item.text" ></v-list-item-title>
                  </v-list-item-content>
                </v-list-item>
              </v-list-item-group>
            </v-list>-->
        </v-navigation-drawer>

<!--        <v-app-bar-->
<!--          app-->
<!--          color="#e4e7ec"-->
<!--        >-->
        <div>
          <v-row class="mt-2">
            <!--            <v-col cols="6" class="d-flex">
                          <v-app-bar-nav-icon class="my-auto" @click.stop="drawer = !drawer" ></v-app-bar-nav-icon>
                          <v-toolbar-title class="d-flex align-center">{{ items[selectedItem].text}}</v-toolbar-title>
                        </v-col>-->
            <v-col cols="3" class="d-flex"></v-col>
            <v-col cols="8" class="d-flex ">
              <template>
                <div class="text-center">
                  <v-menu offset-y>
                    <template v-slot:activator="{ on, attrs }">
                      <v-btn
                        class="rounded-0 swidth"
                        color="#55967e"
                        v-bind="attrs"
                        v-on="on"
                        v-model="choice"
                        width="100px"
                        height="48px"
                      >
                        {{choice}}
                      </v-btn>
                    </template>
                    <v-list>
                      <v-list-item
                        v-for="(item, index) in options"
                        :key="index"
                        @click="getChoice(item)"
                      >
                        <v-list-item-title>{{ item.title }}</v-list-item-title>
                      </v-list-item>
                    </v-list>
                  </v-menu>
                </div>
              </template>
              <v-autocomplete
                flat
                solo-inverted
                hide-details
                auto-select-first
                class="align-center rounded-0"
                placeholder="Enter the target name(such as AFP)"
                v-model="search"
                @keyup.enter="searchBegin"
                :items="info"
              >
<!--                <template v-slot:append >
                  <v-btn  icon large
                          @click="searchBegin"
                          color="#03A6FF">
                    <v-icon>mdi-magnify</v-icon>
                  </v-btn>
                </template>-->
              </v-autocomplete>
              <v-btn
                icon
                class="rounded-0 swidth"
                @click="searchBegin"
                color="#03A6FF"
                width="50px"
                height="48px">
                <v-icon>
                  mdi-magnify
                </v-icon>
              </v-btn>
            </v-col>
            <v-col cols="2" class="d-flex"></v-col>
          </v-row>

          <!--        </v-app-bar>-->
        </div>

        <v-main>
          <v-container
          >
            <router-view  :search="search"  ></router-view>
<!--            <router-view :searchArticle="searchArticle" :totalnum="totalnum" :search="search" :detail="detail"></router-view>-->
          </v-container>
        </v-main>
<!--        <span >&copy; BIT Lab 2021</span>-->
<!--        <v-footer
          color="#e4e7ec"
          app
          class="d-flex justify-center"
        >
            <span >&copy; BIT Lab 2021</span>
        </v-footer>-->
      </v-app>
    </v-app>
  </div>
</template>

<script>
// import axios from 'axios'

import axios from 'axios'

export default {
  name: 'App',
  data () {
    return {
      info: ['AFP', 'A1BG', 'STAT3', '7SK', 'AFP'],
      drawer: null,
      selectedItem: 0,
      choice: 'TARGET',
      search: '',
      myText: 'hello',
      totalnum: 0,
      searchArticle: [],
      detail: [],
      items: [
        { text: 'HOME', icon: 'mdi-home-city-outline', path: '/' },
        { text: 'TARGET', icon: 'mdi-chart-donut-variant', path: '/target' },
        { text: 'ARTICLE', icon: 'mdi-file-document-multiple-outline', path: '/article' },
        {
          text: 'ANALYZE',
          icon: 'mdi-chart-box-outline',
          children: [{ text: 'Dataset', icon: 'mdi-database', path: '/datasets' },
            { text: 'Differential Genes', icon: 'mdi-tune-vertical', path: '/differential' },
            { text: 'Correlation Analysis', icon: 'mdi-transit-detour', path: '/correlation' },
            { text: 'Survival Analysis', icon: 'mdi-run', path: '/survival' }
            // { text: 'KEGG enrichment ', icon: 'mdi-run', path: '/enrichment' }
          ]
        },
        // { text: 'SEARCH', icon: 'mdi-magnify', path: '/search' },
        { text: 'HELP', icon: 'mdi-help-circle-outline', path: '/help' }
        // { text: 'ABOUT', icon: 'mdi-information-outline', path: '/about' }

      ],
      options: [
        { title: 'TARGET' },
        { title: 'ARTICLE' }
      ]
    }
  },
  /* computed: { // 设置计算属性
    // eslint-disable-next-line vue/return-in-computed-property
    fSearch () { //过滤元素实现模糊查找
      if (this.search) {
        return this.info.filter((value) => { // 过滤数组元素
          return value.includes(this.search) // 如果包含字符返回true
        })
      }
    }
  }, */
  methods: {
    getChoice: function (item) {
      this.choice = item.title
    },
    getGene: function (item) {
      this.gene = item
    },
    cor_deff () {
      axios.get('/api/ldb/CorDeff2')
        .then(res => {
          this.info = res.data.gene
          console.log(this.info)
        })
    },
    searchBegin: function () {
      this.search = this.search.toUpperCase()
      if (this.choice === 'ARTICLE') {
        this.$router.push({ name: 'Article' })
      } else if (this.choice === 'TARGET') {
        // eslint-disable-next-line no-undef
        this.$router.push({ name: 'Detail', query: { gene: this.search } })
        // this.$router.push({ name: 'Detail' })
      }
    }

  },
  created () {
    this.cor_deff()
  }
}
</script>
<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.v-autocomplete.v-select.v-input--is-focused input {
  min-width: 10px;
}
.v-autocomplete__content {
  background-color: #FFF !important;
  .v-list {
    background-color: #FFF  !important;
    max-height: 100px;
  }
}
/*.v-select-list {
  max-height: 100px;
}*/
#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
.swidth {
  display:inline-block;
  width: 100px;
}
</style>
