<template>
  <div class="p-6">
    <div class="px-4">
      <div class="mt-3">
        <p class="text-4xl text-left font-semibold">Research Papers</p>
      </div>
      <div class="mt-5 text-justify text-lg">
        <p class="">
          Jing Jiang, Qiudi Wu, Jin Cao, Xin Xia, Li Zhang,
          <span class="font-semibold"
            >Recommending tags for pull requests in GitHub</span
          >, Information and Software Technology, Volume 129, 2021.
        </p>
        <div class="my-4">
          <ul class="list-disc ml-12">
            <li class="mt-1">
              A survey was conducted to understand the usage of tags in pull
              requests in GitHub, and most respondents felt that it was time
              consuming to manually label pull requests, and that a tag
              recommendation tool would be useful.
            </li>
            <li class="mt-1">
              Tags are used to mark functions of pull requests, define their
              priority or current status, or to mention the architectural
              components affected by the pull request.
            </li>
            <li class="mt-1">
              Proposed method uses a feedforward neural network which analyses
              titles, descriptions, file paths and contributors, to recommend
              tags for pull requests.
            </li>
            <li class="mt-1">
              The dataset was extracted using GitHub’s API from 10 projects and
              included 68497 tagged pull requests.
            </li>
            <li class="mt-1">
              The dataset is converted to word vectors and then fed to the
              neural network for training, whose output is the tag vector, which
              describes probabilities that tags are assigned to new pull
              requests. Tags with the highest probabilities are recommended to
              the new pull request.
            </li>
            <li class="mt-1">
              Performance was measured in terms of precision, recall and
              F1-scores.
            </li>
          </ul>
        </div>
        <div class="my-6">
          <img
            class="object-contain mx-auto w-4/5"
            src="@/assets/images/papers-1.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic"
            >Fig.1 - Framework used for the feedforward neural network</small
          >
        </div>
        <br />
        <hr />
        <br />
        <p class="">
          Jesús M. Alonso-Abad, Carlos López-Nozal, Jesús M. Maudes-Raedo, Raúl
          Marticorena-Sánchez,
          <span class="font-semibold"
            >Label prediction on issue tracking systems using text mining</span
          >, Progress in Artificial Intelligence volume 8, pages 325–342, 2019.
        </p>
        <div class="my-4">
          <ul class="list-disc ml-12">
            <li class="mt-1">
              Text mining techniques were applied to assist in issue label
              prediction for issue tracking systems like GitHub.
            </li>
            <li class="mt-1">
              The dataset obtained from GHTorrent was loaded into a MongoDB
              database, and preprocessed using Node.js scripts.
            </li>
            <li class="mt-1">
              All the different text features (title, body, commentBodies) were
              merged into a single feature, and the boolean feature
              ‘isPullRequest’ was added.
            </li>
            <li class="mt-1">
              In addition, words were stemmed to reduce them to the root word.
            </li>
            <li class="mt-1">
              The data was transformed into word vectors using a number of
              methods, namely, boolean (word present in the document or not),
              RawTF (number of occurrences of the word in the document),
              LogarithmicTF (log of the frequency), IDF (inverse document
              frequency which assigns greater weight to infrequent word in the
              corpus), and TF-IDF (combining TF and IDF).
            </li>
            <li class="mt-1">
              SVM and Multinomial Naive Bayes were the two techniques used for
              text classification.
            </li>
            <li class="mt-1">
              Performance metrics used were F1-score (harmonic mean of precision
              and recall) and AUROC (values ranging from 0.5, indicating random
              classification, to 1, indicating perfect classification). These
              scores were averaged across the data which was extracted from the
              different open-source projects.
            </li>
          </ul>
        </div>
      </div>
      <hr class="mt-6" />
      <div class="flex flex-row mt-2">
        <router-link
          class="text-lg font-semibold underline flex-1"
          style="color: #24292e"
          to="/preprocessing"
          ><b-icon-arrow-left class="mr-1 inline"></b-icon-arrow-left>Data
          Preprocessing
        </router-link>
        <router-link
          class="text-lg font-semibold underline flex-1 text-right"
          style="color: #24292e"
          to="/rocchio"
          >Rocchio<b-icon-arrow-right class="ml-1 inline"></b-icon-arrow-right
        ></router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>
