<template>
  <div>
    <h1 class="mb-10">Compensations</h1>

    <v-data-table
      v-if="compensations"
      :headers="headers"
      :items="compensations"
      :items-per-page="5"
      class="elevation-1"
    >
      <template #item.draft="{ item }">
        <v-checkbox :input-value="item.draft" disabled></v-checkbox>
      </template>
    </v-data-table>
  </div>
</template>

<script>
  export default {
    name: "compensations",
    data() {
      return {
        headers: [
          {
            text: "Name",
            align: "start",
            value: "name",
          },
          { text: "Type", value: "type" },
          { text: "Draft", value: "draft" },
        ],
        compensations: undefined,
      };
    },
    created() {
      this.fetchCompensations();
    },
    methods: {
      fetchCompensations() {
        this.$axios
          .get("api/compensations")
          .then((response) => {
            this.compensations = response.data.compensations;
          })
          .catch(console.error);
      },
    },
  };
</script>
