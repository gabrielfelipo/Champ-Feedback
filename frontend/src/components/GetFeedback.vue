<template>
    <table class="table">
        <thead>
            <th>Name</th>
            <th>Rating</th>
            <th>Comment</th>
        </thead>
        <tbody>
            <tr v-for="feedback in feedbacks" :key="feedback.id">
                <td>{{feedback.name}}</td>
                <td>{{feedback.rating}}</td>
                <td>{{feedback.comment}}</td>
            </tr>
        </tbody>
    </table>
</template>

<script>
export default {
    name: 'GetFeedback',
    data(){
        return {
            feedbacks: []
        }
    },
        async created(){
            var response = await fetch("http://127.0.0.1:8000/api/feedbackChamp/");
            this.feedbacks = await response.json();
        },
}
</script>



<style scoped>
.table {
    width: 500px;
    right: 0px;
}
</style>