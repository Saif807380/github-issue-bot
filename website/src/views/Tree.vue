<template>
  <div class="p-6">
    <div class="px-4">
      <div class="mt-3">
        <p class="text-4xl text-left font-semibold">Decision Tree Classifier</p>
      </div>
      <div class="mt-5 text-justify text-lg">
        <p class="">
          A decision tree consists of nodes and edges built from the dataset,
          and is used for classification tasks. Internal nodes are used to make
          a decision, and leaf nodes represent the outcome of the decisions made
          through the tree, which is the class name in case of classification
          problems. CART (Classification and Regression Trees) is a decision
          tree algorithm which supports numerical target variables (regression)
          and does not compute rule sets. It constructs binary trees using the
          feature and threshold that yield the largest information gain at each
          node. Sklearn’s DecisionTreeClassifier uses a modified version of the
          CART algorithm.
        </p>
        <div class="my-4">
          <img
            class="object-contain mx-auto w-4/5"
            src="@/assets/images/tree-1.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic"
            >Fig.1 - Mathematics behind decision tree induction</small
          >
        </div>
        <br />
        <p class="">
          The quality of the split can be measured using entropy or gini index.
        </p>
        <div class="my-4">
          <img
            class="object-contain mx-auto w-4/5"
            src="@/assets/images/tree-2.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic"
            >Fig.2 - Impurity measures used for splitting attributes</small
          >
        </div>
        <div class="">
          <img
            class="object-contain mx-auto w-5/6"
            src="@/assets/images/snippets/tree-tfidf.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic"
            >Fig.3 - Decision Tree Classifier with Bag of Words
            Vectorization.</small
          >
        </div>
        <div class="">
          <img
            class="object-contain mx-auto w-5/6"
            src="@/assets/images/snippets/tree-bag.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic"
            >Fig.4 - Decision Tree Classifier with TF-IDF Vectorization.</small
          >
        </div>
        <p class="text-2xl font-bold mt-6 mb-3">Results and Improvements</p>
        <p>
          By adjusting the maximum depth of the tree to avoid overfitting,
          accuracy was increased from 54% to 59.4% for Bag of Words, and 53% to
          58% for TF-IDF.
        </p>
        <div class="my-4">
          <ul class="list-disc ml-12">
            <li class="mt-1">
              Decision Tree Classifier with Bag of Word Vectorization - 59.4%
            </li>
            <li class="mt-1">
              Decision Tree Classifier with TF-IDF Vectorization - 58%
            </li>
          </ul>
        </div>
      </div>
      <hr class="mt-6" />
      <div class="flex flex-row mt-2">
        <router-link
          class="text-lg font-semibold underline flex-1"
          style="color: #24292e"
          to="/rocchio"
          ><b-icon-arrow-left class="mr-1 inline"></b-icon-arrow-left>Rocchio
          Classifier
        </router-link>
        <router-link
          class="text-lg font-semibold underline flex-1 text-right"
          style="color: #24292e"
          to="/forest"
          >Random Forest Classifier<b-icon-arrow-right
            class="ml-1 inline"
          ></b-icon-arrow-right
        ></router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>
