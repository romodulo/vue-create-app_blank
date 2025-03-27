<script setup>
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" src="./assets/logo.svg" width="125" height="125" />
    <!-- <div>Hello</div> -->
  </header>
  <div>New section</div>
  <div>End:New secion</div>
  <h1 class="text-3xl font-bold underline text-clifford">
      Hello world!
  </h1>
  <h1 class="text-2xl font-bold text-clifford"></h1>
</template>

<style scoped>
header {
  display: flex;
  place-items: center;
  line-height: 1.5;
  background-color: coral;
}

header {
  border-radius: 50px;
}

.logo {
  /* display: block; */
  margin: 0.71rem auto;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    background-color: burlywood;
  }

  .logo {
    /* margin: 0 2rem; */
    /* below: */
    /* to make it look like width less-than 1024 */
    margin: 0 auto;
    /* note */
    /* :what makes it different is coming from another css-stylesheet: */
    /* :most likely base.css */
    /* :correction: it is main.css instead */
    /* :under the css-selector of id:app, */
    /* that is what is happening */
    
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
