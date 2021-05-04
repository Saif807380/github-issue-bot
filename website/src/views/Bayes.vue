<template>
  <div class="p-6">
    <div class="px-4">
      <div class="mt-3">
        <p class="text-4xl text-left font-semibold">Naive Bayes Classifier</p>
      </div>
      <div class="mt-5 text-justify text-lg">
        <p class="">
          Naive Bayes is a simple technique for constructing classifiers: models
          that assign class labels to problem instances, represented as vectors
          of feature values, where the class labels are drawn from some finite
          set. There is not a single algorithm for training such classifiers,
          but a family of algorithms based on a common principle: all naive
          Bayes classifiers assume that the value of a particular feature is
          independent of the value of any other feature, given the class
          variable. For example, a fruit may be considered to be an apple if it
          is red, round, and about 10 cm in diameter. A naive Bayes classifier
          considers each of these features to contribute independently to the
          probability that this fruit is an apple, regardless of any possible
          correlations between the color, roundness, and diameter features.
        </p>
        <br />
        <p class="">
          An advantage of naive Bayes is that it only requires a small number of
          training data to estimate the parameters necessary for classification.
        </p>
        <p class="text-2xl font-bold mt-6 mb-3">Bayes Theorem</p>
        <p>
          Bayes’ theorem describes the probability of an event, based on prior
          knowledge of conditions that might be related to the event. Formula of
          conditional probability where probability of B given A, meaning what
          is the probability of event B when event A is already taken place,
          equals probability of A intersection B.
        </p>
        <p class="font-semibold text-center my-2">P(B|A) = P(A∩B)/P(B)</p>
        <p>
          So, when we want to find probability of A given B we can write our
          equation this way -
        </p>
        <p class="font-semibold text-center my-2">
          P(A|B) = P(B|A) * P(A) / P(B)
        </p>
        <hr />
        <div class="my-6">
          <img
            class="object-contain mx-auto w-4/5"
            src="@/assets/images/bayes-1.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic">Fig.1 - Bayes Theorem</small>
        </div>
        <div class="">
          <img
            class="object-contain mx-auto w-5/6"
            src="@/assets/images/snippets/bayes.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic"
            >Fig.2 - Random Forest Classifier with Bag of Words
            Vectorization.</small
          >
        </div>
        <p class="text-2xl font-bold mt-6 mb-3">Results and Improvements</p>
        <p>
          With only removing stopwords, blank spaces, lemmatization and
          tokenization, accuracy came to be 58%. But adding changes like
          removing tags, unknown languages and emojis since the language is not
          entirely natural language i.e. it is more or less code so the accuracy
          was able to reach 62%.
        </p>
        <div class="my-4">
          <ul class="list-disc ml-12">
            <li class="mt-1">
              Naive Bayes Classifier with TF-IDF Vectorization - 62%
            </li>
          </ul>
        </div>
      </div>
      <hr class="mt-6" />
      <div class="flex flex-row mt-2">
        <router-link
          class="text-lg font-semibold underline flex-1"
          style="color: #24292e"
          to="/knn"
          ><b-icon-arrow-left class="mr-1 inline"></b-icon-arrow-left>KNN
        </router-link>
        <router-link
          class="text-lg font-semibold underline flex-1 text-right"
          style="color: #24292e"
          to="/bagging"
          >Bagging<b-icon-arrow-right class="ml-1 inline"></b-icon-arrow-right
        ></router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>
