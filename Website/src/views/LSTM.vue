<template>
  <div class="p-6">
    <div class="px-4">
      <div class="mt-3">
        <p class="text-4xl text-left font-semibold">RNN with LSTM</p>
      </div>
      <div class="mt-5 text-justify text-lg">
        <p class="">
          Recurrent Neural Network is a generalization of feedforward neural
          network that has an internal memory. RNN is recurrent in nature as it
          performs the same function for every input of data while the output of
          the current input depends on the past one computation. After producing
          the output, it is copied and sent back into the recurrent network. For
          making a decision, it considers the current input and the output that
          it has learned from the previous input.
        </p>
        <br />
        <div class="">
          <ul class="list-disc ml-12">
            <li class="mt-1">
              RNNs become unable to learn to connect the information.
            </li>
            <li class="mt-1">
              RNNs are absolutely capable of handling such “long-term
              dependencies.
            </li>
            <li class="mt-1">RNNs don’t seem to be able to learn them</li>
          </ul>
        </div>
        <br />
        <p>
          Long Short-Term Memory (LSTM) networks are a modified version of
          recurrent neural networks, which makes it easier to remember past data
          in memory. LSTMs also have chain like structure, but the repeating
          module has a different structure. It trains the model by using
          back-propagation Instead of having a single neural network layer,
          there are 3 gates or four layers interacting in a very special way.
        </p>
        <div class="my-6">
          <img
            class="object-contain mx-auto w-4/5"
            src="@/assets/images/lstm-1.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic">Fig.1 - Forget Gate Layer</small>
        </div>
        <div class="my-6">
          <img
            class="object-contain mx-auto w-4/5"
            src="@/assets/images/lstm-2.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic">Fig.2 - Input Gate and Tanh Layer</small>
        </div>
        <div class="my-6">
          <img
            class="object-contain mx-auto w-4/5"
            src="@/assets/images/lstm-3.png"
          />
        </div>
        <div class="my-6">
          <img
            class="object-contain mx-auto w-4/5"
            src="@/assets/images/lstm-4.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic">Fig.3 - Output Layer</small>
        </div>
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
          <small class="italic">Fig.4 - Building a vocabulary of words</small>
        </div>
        <br />
        <p class="text-2xl font-bold mt-6 mb-3">Padding Sequences</p>
        <p>
          Pad shorted sequences and trim longer ones to come to fixed sequence
          length
        </p>
        <div class="">
          <img
            class="object-contain mx-auto w-5/6"
            src="@/assets/images/snippets/lstm-pad.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic"
            >Fig.5 - Padding sequences to fixed length</small
          >
        </div>
        <p class="text-2xl font-bold mt-6 mb-3">Building the Model</p>
        <div class="">
          <img
            class="object-contain mx-auto w-1/2"
            src="@/assets/images/snippets/lstm-model.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic">Fig.6 - Model Architecture</small>
        </div>
        <p class="text-2xl font-bold mt-6 mb-3">
          Parameters and Hyperparameters
        </p>
        <ul class="list-disc ml-12">
          <li class="mt-1">Number of Layers - 3</li>
          <li class="mt-1">Embedding layer dimensions - (Vocab Size, 64)</li>
          <li class="mt-1">Hidden layer dimensions - (64, 512)</li>
          <li class="mt-1">Fully connected layer dimensions - (512, 6)</li>
          <li class="mt-1">Dropout - 0.5</li>
          <li class="mt-1">Loss Function - Categorical Cross Entropy</li>
          <li class="mt-1">Optimizer - Adam Optimizer</li>
          <li class="mt-1">Number of Epochs - 10</li>
          <li class="mt-1">Batch Size - 64</li>
          <li class="mt-1">Learning Rate - 0.01</li>
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
            <li class="mt-1">Accuracy - 67.2%</li>
          </ul>
        </div>
      </div>
      <hr class="mt-6" />
      <div class="flex flex-row mt-2">
        <router-link
          class="text-lg font-semibold underline flex-1"
          style="color: #24292e"
          to="/ann"
          ><b-icon-arrow-left class="mr-1 inline"></b-icon-arrow-left>ANN with
          BoW
        </router-link>
        <router-link
          class="text-lg font-semibold underline flex-1 text-right"
          style="color: #24292e"
          to="/rcnn"
          >RCNN<b-icon-arrow-right class="ml-1 inline"></b-icon-arrow-right
        ></router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>
