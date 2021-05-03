import { createRouter, createWebHistory } from "vue-router";
import Dataset from "../views/Dataset.vue";

const routes = [{ path: "/dataset", component: Dataset }];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
