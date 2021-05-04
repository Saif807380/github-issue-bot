<template>
  <div class="p-6">
    <div class="px-4">
      <div class="mt-3">
        <p class="text-4xl text-left font-semibold">Random Forest Classifier</p>
      </div>
      <div class="mt-5 text-justify text-lg">
        <p class="">
          A random forest is an ensemble learning method that fits a number of
          decision tree classifiers on various sub-samples of the dataset and
          uses averaging to improve the predictive accuracy and control
          overfitting. Each tree in the ensemble is drawn from the training set
          with replacement. Furthermore, when splitting each node during the
          construction of a tree, the best split is found either from all input
          features or a random subset of size max_features. The purpose of these
          two sources of randomness is to decrease the variance of the forest
          estimator. Random forests achieve a reduced variance by combining
          diverse trees, sometimes at the cost of a slight increase in bias.
        </p>
        <p class="text-2xl font-bold mt-6 mb-3">Algorithm</p>
        <div class="my-6">
          <img
            class="object-contain mx-auto w-4/5"
            src="@/assets/images/forest-1.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic"
            >Fig.1 - Algorithm for Random Forest Classification</small
          >
        </div>
        <div class="">
          <img
            class="object-contain mx-auto w-5/6"
            src="@/assets/images/snippets/forest-bag.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic"
            >Fig.2 - Random Forest Classifier with Bag of Words
            Vectorization.</small
          >
        </div>
        <div class="">
          <img
            class="object-contain mx-auto w-5/6"
            src="@/assets/images/snippets/forest-tfidf.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic"
            >Fig.3 - Random Forest Classifier with TF-IDF Vectorization.</small
          >
        </div>
        <p class="text-2xl font-bold mt-6 mb-3">Results and Improvements</p>
        <p>
          By adjusting the number of trees in the forest (n_estimators), and
          increasing the maximum depth of the trees, accuracy was increased from
          48% to 52% for TF-IDF, and from 45% to 50.8% for Bag of Words.
        </p>
        <div class="my-4">
          <ul class="list-disc ml-12">
            <li class="mt-1">
              Random Forest Classifier with Bag of Word Vectorization - 50.8%
            </li>
            <li class="mt-1">
              Random Forest Classifier with TF-IDF Vectorization - 52%
            </li>
          </ul>
        </div>
      </div>
      <hr class="mt-6" />
      <div class="flex flex-row mt-2">
        <router-link
          class="text-lg font-semibold underline flex-1"
          style="color: #24292e"
          to="/tree"
          ><b-icon-arrow-left class="mr-1 inline"></b-icon-arrow-left>Decision
          Tree Classifier
        </router-link>
        <router-link
          class="text-lg font-semibold underline flex-1 text-right"
          style="color: #24292e"
          to="/knn"
          >KNN<b-icon-arrow-right class="ml-1 inline"></b-icon-arrow-right
        ></router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>
