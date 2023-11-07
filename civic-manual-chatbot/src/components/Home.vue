<template>
    <div class="container">
        <input type="email" v-model="query" placeholder="Ask a question about your car">
        <button type="button" class="btn btn-primary" @click="askQuestion">Ask</button>
        <br>
        <p>{{ chat }}</p>
    </div>
  </template>
  
<script>
import axios from 'axios';
  
export default {
    data() {
        return {
            chat: [],
        };
    },
    methods: {
        askQuestion() {
            const path = 'http://localhost:5001/question';
            const payload = { prompt: this.query };
            axios.post(path, payload)
            .then((res) => {
                this.chat.push(res.data.query)
                this.chat.push(res.data.response)
            })
            .catch((error) => {
                console.log(error);
            })
        }
    }
}
</script>