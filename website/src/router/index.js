import { createRouter, createWebHistory } from "vue-router";
import Dataset from "../views/Dataset.vue";
import Overview from "../views/Overview.vue";
import Tree from "../views/Tree.vue";
import Forest from "../views/Forest.vue";
import Bayes from "../views/Bayes.vue";

const routes = [
  { path: "/", component: Overview, meta: { title: "Overview" } },
  { path: "/dataset", component: Dataset, meta: { title: "Dataset" } },
  { path: "/tree", component: Tree, meta: { title: "Decision Tree" } },
  { path: "/forest", component: Forest, meta: { title: "Random Forest" } },
  { path: "/bayes", component: Bayes, meta: { title: "Naive Bayes" } },
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
