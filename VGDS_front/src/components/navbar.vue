<template>
  <div class="nav">
    <v-card>
      <v-tabs
        background-color="#263959"
        color="#55967E"
        slider-color="#55967E"
        right
        dark
        height="50"
      >
        <router-link to="/" tag="v-tab"><img src="@/assets/logo4.png" style="width: 350px; height: 50px; float:left"/></router-link>
        <router-link to="/target" tag="v-tab">Target</router-link>
        <router-link to="/article" tag="v-tab">Article</router-link>
        <router-link to="/analyze" tag="v-tab">Analyze</router-link>
        <router-link to="/help" tag="v-tab">Help</router-link>
        <router-link to="/about" tag="v-tab">About</router-link>
      </v-tabs>
    </v-card>
  </div>
</template>

<script>
export default {
  name: 'navbar'
}
</script>

<style scoped>

</style>
