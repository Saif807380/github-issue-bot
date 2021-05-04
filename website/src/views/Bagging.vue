<template>
  <div class="p-6">
    <div class="px-4">
      <div class="mt-3">
        <p class="text-4xl text-left font-semibold">Bagging</p>
      </div>
      <div class="mt-5 text-justify text-lg">
        <p class="">
          Bagging considers homogeneous weak learners, learns them independently
          from each other in parallel and combines them following some kind of
          deterministic averaging process The idea of bagging is then simple: we
          want to fit several independent models and “average” their predictions
          in order to obtain a model with a lower variance. For classification
          problem the class outputted by each model can be seen as a vote and
          the class that receives the majority of the votes is returned by the
          ensemble model (this is called hard-voting).
        </p>
        <div class="my-6">
          <img
            class="object-contain mx-auto w-4/5"
            src="@/assets/images/bagging-1.png"
          />
        </div>
        <div class="my-6">
          <img
            class="object-contain mx-auto w-4/5"
            src="@/assets/images/bagging-2.png"
          />
        </div>
        <div class="my-6">
          <img
            class="object-contain mx-auto w-4/5"
            src="@/assets/images/bagging-3.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic">Fig.1 - Math</small>
        </div>
        <div class="my-6">
          <img
            class="object-contain mx-auto w-4/5"
            src="@/assets/images/snippets/bagging-knn.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic">Fig.2 - Bagging with KNN</small>
        </div>
        <div class="my-6">
          <img
            class="object-contain mx-auto w-4/5"
            src="@/assets/images/snippets/bagging-dec.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic"
            >Fig.3 - Bagging with Decision Tree Classifier</small
          >
        </div>
        <p class="text-2xl font-bold mt-6 mb-3">Results and Improvements</p>
        <p>
          Bagging with Decision Tree Classifier gave better results than with
          KNN. N-Gram range of (1, 2) was the best for TF-IDF.
        </p>
        <div class="my-4">
          <ul class="list-disc ml-12">
            <li class="mt-1">Bagging with KNN - 58%</li>
            <li class="mt-1">Bagging with Decision Tree Classifier - 62%</li>
          </ul>
        </div>
      </div>
      <hr class="mt-6" />
      <div class="flex flex-row mt-2">
        <router-link
          class="text-lg font-semibold underline flex-1"
          style="color: #24292e"
          to="/bayes"
          ><b-icon-arrow-left class="mr-1 inline"></b-icon-arrow-left>Naive
          Bayes Classifier
        </router-link>
        <router-link
          class="text-lg font-semibold underline flex-1 text-right"
          style="color: #24292e"
          to="/boosting"
          >Boosting<b-icon-arrow-right class="ml-1 inline"></b-icon-arrow-right
        ></router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>
