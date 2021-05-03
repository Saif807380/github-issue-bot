import { createRouter, createWebHistory } from "vue-router";
import Dataset from "../views/Dataset.vue";
import Overview from "../views/Overview.vue";
import Tree from "../views/Tree.vue";

const routes = [
  { path: "/", component: Overview },
  { path: "/dataset", component: Dataset },
  { path: "/tree", component: Tree },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
  scrollBehavior(to, from, savedPosition) {
    console.log(to, from);
    if (savedPosition) {
      return savedPosition;
    } else {
      return { top: 0 };
    }
  },
});

export default router;
