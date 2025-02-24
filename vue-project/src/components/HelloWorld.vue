<script setup>
defineProps({
  msg: {
    type: String,
    required: true,
  },
  superMsg : {
    type: String,
    required: true,
  },
})

const link_1 = {"link" :"https://vite.dev", "label" :"Vite_modified!!!"}
const link_2 = {"link" :"https://vuejs.org", "label" :"Vue-3_Modified"}
</script>

<template>
  <div class="greetings">
    <h1 class="green">{{ msg }}<br><span style="padding-top: 10px;">{{ superMsg }}</span></h1>
    <h3>
      You’ve successfully created a project with
      <a v-bind:href="link_1.link" target="_blank" rel="noopener">{{ link_1.label }}</a> +
      <a v-bind:href="link_2.link" target="_blank" rel="noopener">{{ link_2.label }}</a>.
    </h3>
  </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
