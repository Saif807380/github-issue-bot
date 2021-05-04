<template>
  <div class="p-6">
    <div class="px-4">
      <div class="mt-3">
        <p class="text-4xl text-left font-semibold">
          K Nearest Neighbours Classifier
        </p>
      </div>
      <div class="mt-5 text-justify text-lg">
        <p class="">
          The k-nearest neighbors (KNN) algorithm is a simple, supervised
          machine learning algorithm that can be used to solve both
          classification and regression problems. It’s easy to implement and
          understand, but has a major drawback of becoming significantly slows
          as the size of that data in use grows. KNN works by finding the
          distances between a query and all the examples in the data, selecting
          the specified number examples (K) closest to the query, then votes for
          the most frequent label (in the case of classification) or averages
          the labels (in the case of regression). In the case of classification
          and regression, we saw that choosing the right K for our data is done
          by trying several Ks and picking the one that works best.
        </p>
        <br />
        <p>
          The algorithm assumes that it is possible to classify documents in the
          Euclidean space as points. Euclidean distance is the distance between
          two points in Euclidean space. The distance between two points in the
          plane with coordinates p = (x, y) and q = (a, b) can be calculated:
        </p>
        <div class="">
          <img
            class="object-contain mx-auto w-5/6"
            src="@/assets/images/knn.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic">Fig.1 - Euclidean Distance</small>
        </div>
        <div class="">
          <img
            class="object-contain mx-auto w-5/6"
            src="@/assets/images/snippets/knn-tfidf.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic"
            >Fig.2 - KNN Classifier with TF-IDF Vectorization.</small
          >
        </div>
        <p class="text-2xl font-bold mt-6 mb-3">Results and Improvements</p>
        <p>
          With only removing stopwords, blank spaces, lemmatization and
          tokenization, accuracy came to be 30%. But adding changes like
          removing tags, unknown languages and emojis since the language is not
          entirely natural language i.e. it is more or less code so the accuracy
          was able to reach 55%.
        </p>
        <div class="my-4">
          <ul class="list-disc ml-12">
            <li class="mt-1">
              KNN Classifier with TF-IDF Vectorization - 55.4%
            </li>
          </ul>
        </div>
      </div>
      <hr class="mt-6" />
      <div class="flex flex-row mt-2">
        <router-link
          class="text-lg font-semibold underline flex-1"
          style="color: #24292e"
          to="/forest"
          ><b-icon-arrow-left class="mr-1 inline"></b-icon-arrow-left>Random
          Forest Classifier
        </router-link>
        <router-link
          class="text-lg font-semibold underline flex-1 text-right"
          style="color: #24292e"
          to="/bayes"
          >Naive Bayes Classifier<b-icon-arrow-right
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
