<template>
  <div class="d-flex align-center justify-center" style="height:90vh">
    <v-card>
      <v-img
        :src="imgSrc"
        class="white--text align-end"
        gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
        height="70vh"
      >
        <v-card-title v-text="title"></v-card-title>
      </v-img>
    </v-card>
  </div>
</template>

<script>
  export default {
    name: "index",
    data() {
      return {
        imgSrc: "./img/snake-money.jpg",
        title: "Welcome to Serpentin",
      };
    },
  };
</script>
