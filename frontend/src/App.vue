<template>
  <div id="app">
    <NavBar Msg=""/>
    <div class="Get">
    <GetFeedback/>
    </div>
  </div>
</template>




<script>

import NavBar from './components/NavBar.vue'
//import SendFeedback from './components/SendFeedback.vue'
import GetFeedback from './components/GetFeedback.vue'

export default {
  name: 'App',
  components: {
    NavBar,
    GetFeedback,
  },
}
</script>




<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  height: 658px;
  width: 1084px;
  text-align: center;
  color: #2c3e50;
}
.Get {
  width: 50%;
  left: 20%;
}
</style>