<template>
  <div>
    <h1 class="mb-10">Sales {{ sales ? sales.name : "" }}</h1>

    <SalesCard :sales="sales" :monthlyTotal="monthlyTotal" class="py-3 my-5" />

    <v-row justify="center" class="my-5" style="position: relative">
      <v-btn large @click="showPicker = !showPicker" :depressed="showPicker">
        <v-icon>
          mdi-calendar
        </v-icon>
        {{ month }}
      </v-btn>
      <v-row justify="end" v-if="showPicker" style="position: absolute">
        <v-date-picker
          v-model="month"
          type="month"
          class="elevation-3"
          style="z-index:1"
          @change="
            showPicker = false;
            getSales();
          "
        ></v-date-picker>
      </v-row>
    </v-row>

    <h3>Statement of the month</h3>
    <v-data-table
      v-if="statement.compensations"
      :headers="compensationHeaders"
      :items="statement.compensations"
      :items-per-page="5"
      class="elevation-1 my-5"
    >
      <template #item.progress="{ item }">
        <v-progress-linear
          v-if="item.progress"
          :color="getColor(item.progress)"
          height="10"
          :value="100 * Math.min(1, item.progress)"
          striped
        ></v-progress-linear>
      </template>
    </v-data-table>

    <h3>Deals of the month</h3>
    <v-data-table
      v-if="deals"
      :headers="dealHeaders"
      :items="deals"
      :items-per-page="10"
      class="elevation-1"
    >
    </v-data-table>
  </div>
</template>

<script>
  import SalesCard from "@/components/SalesCard.vue";

  export default {
    name: "sales",
    components: {
      SalesCard,
    },
    data() {
      return {
        sales: undefined,
        deals: [],
        statement: {
          compensations: [],
        },
        showPicker: false,
        month: new Date(Date.now()).toISOString().substr(0, 7),
        compensationHeaders: [
          {
            text: "Compensation",
            align: "start",
            value: "compensation.name",
          },
          { text: "Type", value: "compensation.type" },
          { text: "Target achievement", value: "progress" },
          { text: "Amount", value: "amount" },
        ],
        dealHeaders: [
          {
            text: "Name",
            align: "start",
            value: "name",
          },
          { text: "Modified", value: "modified" },
          { text: "Closed", value: "closed" },
          { text: "Close date", value: "close_date" },
          { text: "Amount", value: "amount" },
        ],
      };
    },
    computed: {
      monthlyTotal() {
        if (
          !this.statement.compensations ||
          this.statement.compensations.length === 0
        ) {
          return 0;
        }
        return this.statement.compensations
          .map((s) => s.amount)
          .reduce((a, b) => a + b);
      },
    },
    created() {
      this.getSales();
    },
    methods: {
      getSales() {
        this.$axios
          .get(`api/sales/${this.$route.params.name}/${this.month}`)
          .then((response) => {
            this.sales = response.data.sales;
            this.deals = response.data.deals;
            this.statement.compensations = response.data.compensations.map(
              (c) => {
                return {
                  ...c,
                  progress:
                    c.compensation.type === "Complex"
                      ? this.sales.progress
                      : undefined,
                };
              }
            );
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
