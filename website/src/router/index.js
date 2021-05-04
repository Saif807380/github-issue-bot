import { createRouter, createWebHistory } from "vue-router";
import Dataset from "../views/Dataset.vue";
import Overview from "../views/Overview.vue";
import Tree from "../views/Tree.vue";
import Forest from "../views/Forest.vue";
import Bayes from "../views/Bayes.vue";
import KNN from "../views/KNN.vue";
import RCNN from "../views/RCNN.vue";
import Papers from "../views/Papers.vue";
import Rocchio from "../views/Rocchio.vue";
import ANN from "../views/ANN.vue";
import Preprocessing from "../views/Preprocessing.vue";
import SVM from "../views/SVM.vue";
import Bagging from "../views/Bagging.vue";
import Summary from "../views/Summary.vue";
import Demo from "../views/Demo.vue";
import Boosting from "../views/Boosting.vue";
import LSTM from "../views/LSTM.vue";

const routes = [
  { path: "/", component: Overview, meta: { title: "Overview" } },
  { path: "/dataset", component: Dataset, meta: { title: "Dataset" } },
  { path: "/tree", component: Tree, meta: { title: "Decision Tree" } },
  { path: "/forest", component: Forest, meta: { title: "Random Forest" } },
  { path: "/bayes", component: Bayes, meta: { title: "Naive Bayes" } },
  { path: "/knn", component: KNN, meta: { title: "KNN" } },
  { path: "/rcnn", component: RCNN, meta: { title: "RCNN" } },
  { path: "/papers", component: Papers, meta: { title: "Research Papers" } },
  {
    path: "/rocchio",
    component: Rocchio,
    meta: { title: "Rocchio Classifier" },
  },
  { path: "/ann", component: ANN, meta: { title: "ANN with BOW" } },
  { path: "/svm", component: SVM, meta: { title: "SVM" } },
  { path: "/bagging", component: Bagging, meta: { title: "Bagging" } },
  {
    path: "/preprocessing",
    component: Preprocessing,
    meta: { title: "Data Preprocessing" },
  },
  { path: "/summary", component: Summary, meta: { title: "Summary" } },
  { path: "/demo", component: Demo, meta: { title: "Demo" } },
  { path: "/boosting", component: Boosting, meta: { title: "Boosting" } },
  { path: "/lstm", component: LSTM, meta: { title: "LSTM" } },
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
