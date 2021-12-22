<template>
  <v-app>
    <template>
      <v-navigation-drawer permanent app>
        <v-list-item>
          <v-list-item-content>
            <NuxtLink to="/">
              <v-list-item-title class="text-h6">
                Serpentin
              </v-list-item-title>
            </NuxtLink>
          </v-list-item-content>
        </v-list-item>

        <v-divider></v-divider>

        <v-list dense nav>
          <NuxtLink v-for="item in items" :key="item.title" :to="item.to">
            <v-list-item link>
              <v-list-item-icon>
                <v-icon>{{ item.icon }}</v-icon>
              </v-list-item-icon>

              <v-list-item-content>
                <v-list-item-title>{{ item.title }}</v-list-item-title>
              </v-list-item-content>
            </v-list-item>
          </NuxtLink>
        </v-list>
      </v-navigation-drawer>
    </template>

    <v-main>
      <v-container>
        <nuxt />
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
  export default {
    name: "default",
    data() {
      return {
        items: [
          { title: "Sales", to: "/sales", icon: "mdi-account-multiple" },
          { title: "Deals", to: "/deals", icon: "mdi-currency-usd" },
          {
            title: "Compensations",
            to: "/compensations",
            icon: "mdi-sack-percent",
          },
        ],
      };
    },
  };
</script>

<style scoped>
  a {
    text-decoration: none;
  }
</style>
