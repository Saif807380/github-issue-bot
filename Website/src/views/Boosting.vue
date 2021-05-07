<template>
  <div class="p-6">
    <div class="px-4">
      <div class="mt-3">
        <p class="text-4xl text-left font-semibold">Boosting</p>
      </div>
      <div class="mt-5 text-justify text-lg">
        <p class="">
          Boosting considers homogeneous weak learners, learns them sequentially
          in a very adaptative way (a base model depends on the previous ones)
          and combines them following a deterministic strategy Boosting is a
          Ensemble learning meta-algorithm for primarily reducing variance in
          supervised learning. It is basically a family of machine learning
          algorithms that convert weak learners to strong ones.
        </p>
        <p class="text-2xl font-bold mt-6 mb-3">Types of Boosting Algorithms</p>
        <div class="my-4">
          <ul class="list-disc ml-12">
            <li class="mt-1">AdaBoost (Adaptive Boosting)</li>
            <li class="mt-1">Gradient Tree Boosting</li>
            <li class="mt-1">XGBoost</li>
          </ul>
        </div>
        <div class="my-6">
          <img
            class="object-contain mx-auto w-4/5"
            src="@/assets/images/boosting-1.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic">Fig.1 - AdaBoost</small>
        </div>
        <div class="my-6">
          <img
            class="object-contain mx-auto w-4/5"
            src="@/assets/images/boosting-2.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic">Fig.2 - Gradient Boosting</small>
        </div>
        <div class="my-6">
          <img
            class="object-contain mx-auto w-4/5"
            src="@/assets/images/boosting-3.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic">Fig.3 - XGBoost</small>
        </div>
        <p class="text-2xl font-bold mt-6 mb-3">Results and Improvements</p>
        <p>
          Scikit-Learn Boosting gave better results as compared to XGBoost.
          N-Gram range of (1, 2) was the best for TF-IDF.
        </p>
        <div class="my-4">
          <ul class="list-disc ml-12">
            <li class="mt-1">Scikit-Learn Boosting - 67%</li>
            <li class="mt-1">XGBoost - 64%</li>
          </ul>
        </div>
      </div>
      <hr class="mt-6" />
      <div class="flex flex-row mt-2">
        <router-link
          class="text-lg font-semibold underline flex-1"
          style="color: #24292e"
          to="/bagging"
          ><b-icon-arrow-left class="mr-1 inline"></b-icon-arrow-left>Bagging
        </router-link>
        <router-link
          class="text-lg font-semibold underline flex-1 text-right"
          style="color: #24292e"
          to="/svm"
          >SVM<b-icon-arrow-right class="ml-1 inline"></b-icon-arrow-right
        ></router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>
