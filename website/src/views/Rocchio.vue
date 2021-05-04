<template>
  <div class="p-6">
    <div class="px-4">
      <div class="mt-3">
        <p class="text-4xl text-left font-semibold">Rocchio Classifier</p>
      </div>
      <div class="mt-5 text-justify text-lg">
        <p class="">
          In machine learning, a nearest centroid classifier or nearest
          prototype classifier is a classification model that assigns to
          observations the label of the class of training samples whose mean
          (centroid) is closest to the observation. When applied to text
          classification using tf-idf vectors to represent documents, the
          nearest centroid classifier is known as the Rocchio classifier because
          of its similarity to the Rocchio algorithm for relevance feedback.
        </p>
        <div class="grid grid-cols-2 grid-rows-1">
          <div class="col-span-1">
            <div class="my-6">
              <img
                class="object-contain mx-auto h-64"
                src="@/assets/images/rocchio-1.png"
              />
            </div>
            <div class="text-center mt-6">
              <small class="italic">Fig.1 - Formula</small>
            </div>
          </div>
          <div class="col-span-1">
            <div class="my-6">
              <img
                class="object-contain mx-auto h-64"
                src="@/assets/images/rocchio-2.png"
              />
            </div>
            <div class="text-center mt-6">
              <small class="italic">Fig.2 - Notations</small>
            </div>
          </div>
        </div>
        <p class="text-2xl font-bold mt-6 mb-3">Algorithm</p>
        <div class="my-6">
          <img
            class="object-contain mx-auto"
            src="@/assets/images/rocchio-3.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic">Fig.3 - Nearest Centroid Classifier</small>
        </div>
        <div class="">
          <img
            class="object-contain mx-auto w-5/6"
            src="@/assets/images/snippets/rocchio-tfidf.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic"
            >Fig.4 - Rocchio Classifier with TF-IDF Vectorization.</small
          >
        </div>
        <p class="text-2xl font-bold mt-6 mb-3">Grid Search</p>
        <p>
          Grid search is a tuning technique that attempts to compute the optimum
          values of hyperparameters. It is an exhaustive search that is
          performed on a the specific parameter values of a model. The model is
          also known as an estimator.
        </p>
        <div class="">
          <img
            class="object-contain mx-auto w-5/6"
            src="@/assets/images/snippets/rocchio-grid.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic"
            >Fig.4 - Applying Grid Search on Rocchio Classifier</small
          >
        </div>
        <br />
        <p>Best Hyperparameter values suggested by grid search are -</p>
        <div class="my-4">
          <ul class="list-disc ml-12">
            <li class="mt-1">Max Features - None (No limit on max features)</li>
            <li class="mt-1">
              TF-IDF N-Gram range - (1, 2) (Both unigrams and bigrams)
            </li>
          </ul>
        </div>
        <p class="text-2xl font-bold mt-6 mb-3">Results and Improvements</p>
        <p>
          By applying grid search, we were able to improve the accuracy from 61%
          to 62%.
        </p>
        <div class="my-4">
          <ul class="list-disc ml-12">
            <li class="mt-1">
              Rocchio Classifier with TF-IDF Vectorization - 62%
            </li>
          </ul>
        </div>
      </div>
      <hr class="mt-6" />
      <div class="flex flex-row mt-2">
        <router-link
          class="text-lg font-semibold underline flex-1"
          style="color: #24292e"
          to="/papers"
          ><b-icon-arrow-left class="mr-1 inline"></b-icon-arrow-left>Research
          Papers
        </router-link>
        <router-link
          class="text-lg font-semibold underline flex-1 text-right"
          style="color: #24292e"
          to="/tree"
          >Decision Tree Classifier<b-icon-arrow-right
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
