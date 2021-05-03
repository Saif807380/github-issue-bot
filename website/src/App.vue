<template>
  <!-- #43379d -->
  <div class="grid grid-cols-5 grid-rows-1 h-screen">
    <div class="col-span-1 shadow-2xl" style="background-color: #252f3f">
      <div class="mt-4 pl-4">
        <p class="text-2xl text-left font-bold text-white">GitHub Issue Bot</p>
      </div>
      <div class="mt-3 mx-3">
        <div
          class="rounded mt-1 py-1 text-gray-300 hover:bg-white hover:text-gray-700"
          :class="{
            'bg-white': isActive(k),
            'text-gray-700': isActive(k),
            'shadow-2xl': isActive(k),
          }"
          v-for="(v, k) in sections"
          :key="k"
          @click="view(k)"
        >
          <p class="text-normal font-semibold text-left ml-2">{{ v }}</p>
        </div>
      </div>
    </div>
    <div class="col-span-4 overflow-auto">
      <router-view></router-view>
    </div>
  </div>
</template>

<script type="text/javascript">
export default {
  data() {
    return {
      sections: {
        "": "Overview",
        dataset: "Dataset",
        preprocessing: "Data Preprocessing",
        roccio: "Rocchio Classifier",
        knn: "KNN",
        tree: "Decision Tree Classifier",
        forest: "Random Forest Classifier",
        bagging: "Bagging",
        boosting: "Boosting",
        svm: "SVM",
        bayes: "Naive Bayes Classifier",
        ann: "ANN with BOW",
        lstm: "RNN with LSTM",
        rcnn: "RCNN",
        demo: "Implementation",
        papers: "Research Papers",
        about: "About Us",
      },
    };
  },
  methods: {
    view(route) {
      console.log(this.$route);
      this.$router.push(`/${route}`);
    },
    isActive(route) {
      return this.$route.path.split("/")[1] === route;
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
