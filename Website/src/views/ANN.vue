<template>
  <div class="p-6">
    <div class="px-4">
      <div class="mt-3">
        <p class="text-4xl text-left font-semibold">ANN with BOW Embedding</p>
      </div>
      <div class="mt-5 text-justify text-lg">
        <p class="">
          An artificial neural network is a supervised learning algorithm which
          means that we provide it with the input data containing the
          independent variables and the output data that contains the dependent
          variable. This ANN consists of 1 Embedding Layer and 1 fully-connected
          output layer. The embedding layer turns positive integers (indexes)
          into dense vectors of fixed size. First a vocabulary is built from the
          raw dataset. Then the data is tokenized and converted into word
          vectors using the vocabulary. These word vectors are passed to the
          embedding layer and then the output is passed to the fully -connected
          layer which has output size 6 (number of output labels).
        </p>
        <p class="text-2xl font-bold mt-6 mb-3">Building a Vocabulary</p>
        <p>
          The size of the vocabulary is around 53,000 words. We tried removing
          words that occur only once but that didn’t improve the performance.
          This vocabulary is known as the
          <span class="font-semibold">Bag of Words (BOW)</span> where each word
          has an associated index.
        </p>
        <div class="my-6">
          <img
            class="object-contain mx-auto w-4/5"
            src="@/assets/images/snippets/ann-1.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic">Fig.1 - Building a vocabulary of words</small>
        </div>
        <br />
        <p class="text-2xl font-bold mt-6 mb-3">Building Word Vectors</p>
        <p>
          Building word vectors is the process of replacing tokens with their
          associated indices. Words that have similar meaning or are used in the
          same context, have a dot product closer to 1.
        </p>
        <div class="">
          <img
            class="object-contain mx-auto w-5/6"
            src="@/assets/images/snippets/ann-2.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic"
            >Fig.2 - Building word vectors from the bag of words.</small
          >
        </div>
        <p class="text-2xl font-bold mt-6 mb-3">Building the Model</p>
        <div class="">
          <img
            class="object-contain mx-auto w-1/2"
            src="@/assets/images/ann-arch.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic">Fig.3 - Model Architecture</small>
        </div>
        <div class="">
          <img
            class="object-contain mx-auto w-4/5"
            src="@/assets/images/snippets/ann-3.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic">Fig.4 - Building the Model</small>
        </div>
        <p class="text-2xl font-bold mt-6 mb-3">
          Parameters and Hyperparameters
        </p>
        <ul class="list-disc ml-12">
          <li class="mt-1">Number of Layers - 2</li>
          <li class="mt-1">Embedding layer dimensions - (Vocab Size, 64)</li>
          <li class="mt-1">Fully connected layer dimensions - (64, 6)</li>
          <li class="mt-1">Dropout - 0.5</li>
          <li class="mt-1">Loss Function - Categorical Cross Entropy</li>
          <li class="mt-1">Optimizer - Stochastic Gradient Descent</li>
          <li class="mt-1">Number of Epochs - 10</li>
          <li class="mt-1">Batch Size - 64</li>
          <li class="mt-1">Learning Rate - 1</li>
        </ul>
        <p class="text-2xl font-bold mt-6 mb-3">Results and Improvements</p>
        <p>
          This combination of parameters gave the best result among all other
          models. Building a deeper network or removing drop out made the net
          overfit the dataset. Using a lower learning rate, increasing batch
          size required the model to train for a longer period of time for the
          same results.
        </p>
        <div class="my-4">
          <ul class="list-disc ml-12">
            <li class="mt-1">Accuracy - 71.32%</li>
          </ul>
        </div>
      </div>
      <hr class="mt-6" />
      <div class="flex flex-row mt-2">
        <router-link
          class="text-lg font-semibold underline flex-1"
          style="color: #24292e"
          to="/svm"
          ><b-icon-arrow-left class="mr-1 inline"></b-icon-arrow-left>SVM
        </router-link>
        <router-link
          class="text-lg font-semibold underline flex-1 text-right"
          style="color: #24292e"
          to="/lstm"
          >RNN with LSTM<b-icon-arrow-right
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
