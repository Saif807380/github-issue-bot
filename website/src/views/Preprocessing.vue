<template>
  <div class="p-6">
    <div class="px-4">
      <div class="mt-3">
        <p class="text-4xl text-left font-semibold">Data Preprocessing</p>
      </div>
      <div class="mt-5 text-justify text-lg">
        <p>We performed the following Preprocessing steps -</p>
        <div class="my-4">
          <ul class="list-disc ml-12">
            <li class="mt-1">Combining the issue title and body</li>
            <li class="mt-1">Removing Emojis from the dataset</li>
            <li class="mt-1">Removing Non-English words</li>
            <li class="mt-1">Removing Markdown symbols and HTML tags</li>
            <li class="mt-1">Removing URLs</li>
            <li class="mt-1">Removing Punctuations</li>
            <li class="mt-1">Removing Numbers</li>
            <li class="mt-1">Removing Stop-words</li>
            <li class="mt-1">Lowercasing</li>
            <li class="mt-1">Label Encoding the target variable</li>
          </ul>
        </div>
        <p class="text-2xl font-bold mt-6 mb-3">Removing Emojis</p>
        <div class="my-6">
          <img
            class="object-contain mx-auto w-4/5"
            src="@/assets/images/snippets/de-emoji.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic">Fig.1 - Removing Emojis from the dataset</small>
        </div>
        <p class="text-2xl font-bold mt-6 mb-3">Removing Non-English Words</p>
        <div class="">
          <img
            class="object-contain mx-auto w-5/6"
            src="@/assets/images/snippets/non-english.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic">Fig.2 - Removing Non-English Words</small>
        </div>
        <p class="text-2xl font-bold mt-6 mb-3">
          Removing Markdown symbols and HTML tags
        </p>
        <div class="">
          <img
            class="object-contain mx-auto w-5/6"
            src="@/assets/images/snippets/md.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic"
            >Fig.3 - Removing Markdown symbols and HTML tags</small
          >
        </div>
        <p class="text-2xl font-bold mt-6 mb-3">Additional Cleaning</p>
        <div class="my-6">
          <img
            class="object-contain mx-auto w-4/5"
            src="@/assets/images/snippets/clean.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic"
            >Fig.4 - Removing urls, punctuations, numbers, stopwords and
            lowercasing</small
          >
        </div>
        <p class="text-2xl font-bold mt-6 mb-3">Bag of Words</p>
        <p>
          The Bag of Words (BoW) model is the simplest form of text
          representation in numbers. Like the term itself, we can represent a
          sentence as a bag of words vector (a string of numbers). Bag of Words
          model is used to preprocess the text by converting it into a bag of
          words, which keeps a count of the total occurrences of most frequently
          used words. This model can be visualized using a table, which contains
          the count of words corresponding to the word itself.
        </p>
        <p class="text-2xl font-bold mt-6 mb-3">TF-IDF</p>
        <p>
          TF-IDF is a statistical measure that evaluates how relevant a word is
          to a document in a collection of documents. This is done by
          multiplying two metrics: how many times a word appears in a document,
          and the inverse document frequency of the word across a set of
          documents. It works by increasing proportionally to the number of
          times a word appears in a document, but is offset by the number of
          documents that contain the word. So, words that are common in every
          document, such as this, what, and if, rank low even though they may
          appear many times, since they don’t mean much to that document in
          particular. However, if the word Bug appears many times in a document,
          while not appearing many times in others, it probably means that it’s
          very relevant.
        </p>
        <br />
        <p>
          TF-IDF for a word in a document is calculated by multiplying two
          different metrics -
        </p>
        <div class="my-4">
          <ul class="list-disc ml-12">
            <li class="mt-1">
              The term frequency of a word in a document. There are several ways
              of calculating this frequency, with the simplest being a raw count
              of instances a word appears in a document. Then, there are ways to
              adjust the frequency, by length of a document, or by the raw
              frequency of the most frequent word in a document.
            </li>
            <li class="mt-1">
              The inverse document frequency of the word across a set of
              documents. This means, how common or rare a word is in the entire
              document set. The closer it is to 0, the more common a word is.
              This metric can be calculated by taking the total number of
              documents, dividing it by the number of documents that contain a
              word, and calculating the logarithm.
            </li>
          </ul>
        </div>
        <p>
          Multiplying these two numbers results in the TF-IDF score of a word in
          a document. The higher the score, the more relevant that word is in
          that particular document.
        </p>
        <p class="text-2xl font-bold mt-6 mb-3">Data Exploration</p>
        <p>
          All data exploration was done on the preprocessed dataset. First, the
          frequency counts of each kind of issue was visualized. As can be seen,
          the most common type of issue is ‘bug’, and the least common type of
          issue is ‘question’.
        </p>
        <div class="my-6">
          <img
            class="object-contain mx-auto w-3/4"
            src="@/assets/images/exp-1.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic"
            >Fig.5 - The frequency distribution of issue labels in the
            dataset</small
          >
        </div>
        <br />
        <p>
          Using LDA, the most common words in each topic were extracted. The
          different topics below are: Topic 0: bug, Topic 1: design, Topic 2:
          documentation, Topic 3: feature, Topic 4: help, Topic 5: question.
        </p>
        <div class="my-6">
          <img
            class="object-contain mx-auto w-1/2"
            src="@/assets/images/exp-2.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic"
            >Fig.6 - The common words present in each issue</small
          >
        </div>
        <br />
        <p>
          The 20 most common words in the dataset are shown below, along with
          their frequencies. This was obtained using the Bag of Words model. As
          can be seen, the top 3 most popular words used in issues are ‘java’,
          ‘add’, and ‘version’.
        </p>
        <div class="my-6">
          <img
            class="object-contain mx-auto w-4/5"
            src="@/assets/images/exp-3.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic"
            >Fig.7 - The 20 most common words in the dataset, along with their
            frequencies</small
          >
        </div>
        <br />
        <p>
          The 20 most common word pairs in the dataset are shown below, along
          with their frequencies. This was obtained using the Bag of Words
          model. As can be seen, the top 3 most popular word pairs used in
          issues are ‘py line’, ‘lib python’, and ‘site packages’.
        </p>
        <div class="my-6">
          <img
            class="object-contain mx-auto w-4/5"
            src="@/assets/images/exp-4.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic"
            >Fig.8 - The 20 most common word pairs in the dataset, along with
            their frequencies</small
          >
        </div>
      </div>

      <hr class="mt-6" />
      <div class="flex flex-row mt-2">
        <router-link
          class="text-lg font-semibold underline flex-1"
          style="color: #24292e"
          to="/dataset"
          ><b-icon-arrow-left class="mr-1 inline"></b-icon-arrow-left>Dataset
        </router-link>
        <router-link
          class="text-lg font-semibold underline flex-1 text-right"
          style="color: #24292e"
          to="/papers"
          >Research Papers<b-icon-arrow-right
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
