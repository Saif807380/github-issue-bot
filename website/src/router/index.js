import { createRouter, createWebHistory } from "vue-router";
import Dataset from "../views/Dataset.vue";
import Overview from "../views/Overview.vue";

const routes = [
  { path: "/", component: Overview },
  { path: "/dataset", component: Dataset },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
