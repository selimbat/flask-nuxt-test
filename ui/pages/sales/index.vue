<template>
  <div>
    <h1 class="mb-10">Sales</h1>

    <v-data-table
      v-if="sales"
      :headers="headers"
      :items="sales"
      :items-per-page="5"
      class="elevation-1"
    >
      <template #item.progress="{ item }">
        <v-progress-linear
          :color="getColor(item.progress)"
          height="10"
          :value="100 * Math.min(1, item.progress)"
          striped
        ></v-progress-linear>
      </template>
      <template #item.route="{ item }">
        <v-btn nuxt depressed color="primary" :to="item.route">
          See
        </v-btn>
      </template>
    </v-data-table>
  </div>
</template>

<script>
  export default {
    name: "sales",
    data() {
      return {
        headers: [
          {
            text: "Name",
            align: "start",
            value: "name",
          },
          { text: "Target achievement of the month", value: "progress" },
          { text: "Target", value: "target" },
          { text: "Action", sortable: false, value: "route" },
        ],
        sales: undefined,
      };
    },
    created() {
      this.fetchSales();
    },
    methods: {
      fetchSales() {
        this.$axios
          .get("api/sales")
          .then((response) => {
            this.sales = [];
            for (let s of response.data.sales) {
              this.sales.push({
                ...s,
                route: `/sales/${s.name}`,
              });
            }
          })
          .catch(console.error);
      },
      getColor(progress) {
        if (progress < 0.5) return "deep-orange accent-2";
        else if (progress < 1) return "yellow accent-3";
        else return "green accent-3";
      },
    },
  };
</script>
