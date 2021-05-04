<template>
  <!-- #43379d -->
  <!-- 252f3f -->
  <div class="grid grid-cols-5 grid-rows-1 h-screen">
    <div
      class="col-span-1 shadow-2xl divide-y divide-white"
      style="background-color: #24292e"
    >
      <div class="mt-4 pl-4">
        <p class="text-xl font-bold text-white">
          <img
            src="@/assets/images/github-logo.png"
            alt=""
            class="h-5 w-5 mr-2 mb-1 inline"
          />GitHub Issue Bot
        </p>
      </div>
      <div class="mt-1 pt-2 mx-3">
        <div
          class="rounded mt-1 py-1 text-white hover:bg-white hover:text-gray-700"
          :class="{
            'bg-white': isActive(k),
            'text-gray-700': isActive(k),
            'shadow-2xl': isActive(k),
          }"
          v-for="(v, k) in sections"
          :key="k"
          @click="view(k)"
        >
          <p class="text-normal text-left ml-2">
            <b-icon-dot class="inline"></b-icon-dot>{{ v }}
          </p>
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
  watch: {
    $route: {
      handler(to, from) {
        console.log(from);
        document.title = to.meta.title || "GH Issue Bot";
      },
    },
  },
  data() {
    return {
      sections: {
        "": "Overview",
        demo: "Implementation",
        dataset: "Dataset",
        preprocessing: "Data Preprocessing",
        papers: "Research Papers",
        rocchio: "Rocchio Classifier",
        tree: "Decision Tree Classifier",
        forest: "Random Forest Classifier",
        knn: "KNN",
        bayes: "Naive Bayes Classifier",
        bagging: "Bagging",
        boosting: "Boosting",
        svm: "SVM",
        ann: "ANN with BOW",
        lstm: "RNN with LSTM",
        rcnn: "RCNN",
        summary: "Summary",
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

img {
  @apply shadow-xl;
}
</style>
