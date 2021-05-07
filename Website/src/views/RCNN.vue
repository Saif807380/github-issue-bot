<template>
  <div class="p-6">
    <div class="px-4">
      <div class="mt-3">
        <p class="text-4xl text-left font-semibold">RCNN</p>
      </div>
      <div class="mt-5 text-justify text-lg">
        <p class="">
          Recurrent Convolutional Neural Network is an algorithm that applies a
          recurrent structure to capture contextual information as far as
          possible when learning word representations, which may introduce
          considerably less noise compared to traditional window-based neural
          networks. It also employs a max-pooling layer that automatically
          judges which words play key roles in text classification to capture
          the key components in texts. By combining the recurrent structure and
          max-pooling layer, the model utilizes the advantage of both recurrent
          neural models and convolutional neural models. Furthermore, it
          exhibits a time complexity of O(n), which is linearly correlated with
          the length of the text length.
        </p>
        <div class="my-6">
          <img
            class="object-contain mx-auto w-4/5"
            src="@/assets/images/rcnn-1.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic"
            >Fig.1 - Structure of Recurrent Convolutional Neural Network. This
            figure is a partial example of the sentence “A sunset stroll along
            the South Bank affords an array of stunning vantage points”, and the
            subscript denotes the position of the corresponding word in the
            original sentence.</small
          >
        </div>
        <p class="text-2xl font-bold mt-6 mb-3">Notations</p>
        <div class="my-4">
          <ul class="list-disc ml-12">
            <li class="mt-1">
              c<sub>l</sub> (w<sub>i</sub>) - Left context of word w<sub>i</sub>
            </li>
            <li class="mt-1">
              c<sub>l</sub> (w<sub>i</sub>) - Right context of word w<sub
                >i</sub
              >
            </li>
            <li class="mt-1">
              e(w<sub>i</sub>) - Word embedding of word w<sub>i</sub>
              pre-trained with the Skip-gram model. Dense vector with |e| real
              value elements.
            </li>
            <li class="mt-1">
              W<sup>(l)</sup> - Matrix that transforms the hidden layer
              (context) into the next hidden layer.
            </li>
            <li class="mt-1">
              W<sup>(sl)</sup> - Matrix that used to combine the semantic of the
              current word with the next word’s left context.
            </li>
            <li class="mt-1">f - non-linear activation function.</li>
          </ul>
        </div>
        <p>
          The recurrent structure can obtain all c <sub>l</sub> in a forward
          scan of the text and c <sub>r</sub> in a backward scan of the text.
          The time complexity is O(n). After the representation x
          <sub>i</sub> of the word w <sub>i</sub> is obtained, a linear
          transformation is applied along with the tanh activation function to x
          <sub>i</sub>, and the result is sent to the next layer.
        </p>
        <div class="">
          <img
            class="object-contain mx-auto w-5/6"
            src="@/assets/images/rcnn-2.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic"
            >Fig.2 - Equations for word representation</small
          >
        </div>
        <br />
        <div class="">
          <img
            class="object-contain mx-auto w-5/6"
            src="@/assets/images/rcnn-3.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic"
            >Fig.3 - Equations for text representation learning using
            max-pooling</small
          >
        </div>
        <br />
        <p>All of the parameters to be trained is defined as theta.</p>
        <br />
        <div class="">
          <img
            class="object-contain mx-auto w-5/6"
            src="@/assets/images/rcnn-4.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic"
            >Fig.4 - Network parameters. Word Embeddings E, Bias vectors b,
            Initial contexts c, Transformation matrices W</small
          >
        </div>
        <br />
        <div class="">
          <img
            class="object-contain mx-auto w-5/6"
            src="@/assets/images/rcnn-5.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic">Fig.5 - Optimization objective</small>
        </div>
        <div class="">
          <img
            class="object-contain mx-auto w-5/6"
            src="@/assets/images/snippets/rcnn-model.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic">Fig.6 - RCNN Model using Keras</small>
        </div>
        <div class="">
          <img
            class="object-contain mx-auto w-5/6"
            src="@/assets/images/snippets/rcnn.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic">Fig.6 - Model Training</small>
        </div>
        <p class="text-2xl font-bold mt-6 mb-3">Results and Improvements</p>
        <div class="">
          <img
            class="object-contain mx-auto w-5/6"
            src="@/assets/images/rcnn-6.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic">Fig.6 - Classification Results</small>
        </div>
      </div>
      <hr class="mt-6" />
      <div class="flex flex-row mt-2">
        <router-link
          class="text-lg font-semibold underline flex-1"
          style="color: #24292e"
          to="/lstm"
          ><b-icon-arrow-left class="mr-1 inline"></b-icon-arrow-left>RNN with
          LSTM
        </router-link>
        <router-link
          class="text-lg font-semibold underline flex-1 text-right"
          style="color: #24292e"
          to="/summary"
          >Summary<b-icon-arrow-right class="ml-1 inline"></b-icon-arrow-right
        ></router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>
