<template>
  <div id="app">
    <div class="sideBar">
      <NavBar Msg=""/>
    </div>
    <div class="form-table">
    <form @submit.prevent="createfeedback">
      <div class="row g-3">
        <div class="col">
          <input type="text" class="form-control" placeholder="Name" v-model="feedback.name">
        </div>
        <div class="col">
          <input type="text" class="form-control" placeholder="Rating" v-model="feedback.rating">
        </div>
        <div class="col">
          <input type="text" class="form-control col-3 mx-0" placeholder="Comment" v-model="feedback.comment">
        </div>
        <div class="col">
          <button class="btn btn-success">Submit</button>
        </div>
      </div>
    </form>
    </div>


    <table class="table">
        <thead>
          <th>Name</th>
          <th>Rating</th>
          <th>Comment</th>
        </thead>
        <tbody>
          <tr v-for="feedback in feedbacks" :key="feedback.id">
            <th>{{feedback.name}}</th>
            <th>{{feedback.rating}}</th>
            <th>{{feedback.comment}}</th>
          </tr>
        </tbody>
    </table>
  </div>
</template>




<script>

import NavBar from './components/NavBar.vue'
//import SendFeedback from './components/SendFeedback.vue'
//import GetFeedback from './components/GetFeedback.vue'

export default {
  name: 'App',
  components: {
    NavBar,
  },
  data(){
    return {
      feedback: {
        'name': '',
        'rating': '',
        'comment': '',
      },
      feedbacks: []
    }
  },
  async created(){
    await this.getfeedbacks();
  },

  methods: {
    async getfeedbacks(){
      var response = await fetch("http://127.0.0.1:8000/api/feedbackChamp/");
      this.feedbacks = await response.json();
    },
    async createfeedback(){
      await this.getfeedbacks();

      await fetch("http://127.0.0.1:8000/api/feedbackChamp/", {
        method: 'post',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(this.feedback)
      });

      await this.getfeedbacks();
    }
  }
}
</script>




<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.sideBar {
  position: absolute;
  height: 100%;
}

.form-table {
  position: relative;
  left: 7vh;
  top: 10vh;
  z-index: -1;
}
</style>