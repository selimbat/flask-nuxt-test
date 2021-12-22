<template>
  <v-card class="mx-auto" outlined>
    <v-list-item three-line>
      <v-list-item-content>
        <div class="text-overline mb-4">
          SALES
        </div>
        <v-list-item-title class="text-h5 mb-1">
          {{ sales ? sales.name : "Loading" }}
        </v-list-item-title>
        <v-list-item-subtitle
          >Total compensation of the month:
          {{ monthlyTotal }}</v-list-item-subtitle
        >
      </v-list-item-content>

      <v-list-item-avatar tile size="80" color="grey"></v-list-item-avatar>
    </v-list-item>
  </v-card>
</template>

<script>
  export default {
    name: "SalesCard",
    props: {
      sales: Object,
      monthlyTotal: Number,
    },
  };
</script>
