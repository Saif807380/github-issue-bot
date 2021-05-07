<template>
  <div class="p-6">
    <div class="px-4">
      <div class="mt-3">
        <p class="text-4xl text-left font-semibold">Summary</p>
      </div>
      <div class="mt-5 text-justify text-lg">
        <table class="table-auto mx-auto border-2 border-gray-700 mt-12">
          <thead class="text-white" style="background-color: #24292e">
            <tr>
              <th class="text-center border-2 border-gray-700 px-3">No.</th>
              <th class="text-center border-2 border-gray-700">Model Name</th>
              <th class="text-center border-2 border-gray-700 px-3">
                Accuracy
              </th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>1</td>
              <td>Rocchio Classifier</td>
              <td>62%</td>
            </tr>
            <tr>
              <td>2</td>
              <td>KNN</td>
              <td>55%</td>
            </tr>
            <tr>
              <td>3</td>
              <td>Decision Tree Classifier with BoW</td>
              <td>59.4%</td>
            </tr>
            <tr>
              <td>4</td>
              <td>Decision Tree Classifier with TF-IDF</td>
              <td>58%</td>
            </tr>
            <tr>
              <td>5</td>
              <td>Random Forest Classifier with BoW</td>
              <td>50.8%</td>
            </tr>
            <tr>
              <td>6</td>
              <td>Random Forest Classifier with TF-IDF</td>
              <td>52%</td>
            </tr>
            <tr>
              <td>7</td>
              <td>Bagging with KNN</td>
              <td>58%</td>
            </tr>
            <tr>
              <td>8</td>
              <td>Bagging with Decision Tree</td>
              <td>62%</td>
            </tr>
            <tr>
              <td>9</td>
              <td>Gradient Boosting</td>
              <td>67%</td>
            </tr>
            <tr>
              <td>10</td>
              <td>XGBoost</td>
              <td>65%</td>
            </tr>
            <tr>
              <td>11</td>
              <td>SVM</td>
              <td>65%</td>
            </tr>
            <tr>
              <td>12</td>
              <td>Naive Bayes Classifier</td>
              <td>62%</td>
            </tr>
            <tr>
              <td>13</td>
              <td>RNN with LSTM</td>
              <td>67.2%</td>
            </tr>
            <tr>
              <td>14</td>
              <td>RCNN</td>
              <td>57%</td>
            </tr>
            <tr>
              <td>15</td>
              <td>ANN with BoW</td>
              <td>71.32%</td>
            </tr>
          </tbody>
        </table>
        <br />
        <p class="text-2xl font-bold mt-6 mb-3">Tools and Libraries Used</p>
        <div class="my-4">
          <ul class="list-disc ml-12">
            <li class="mt-1" v-for="(v, i) in tools" :key="i">{{ v }}</li>
          </ul>
        </div>
        <p class="text-2xl font-bold mt-6 mb-3">Team Members</p>
        <div class="my-4">
          <ul class="list-disc ml-12">
            <li class="mt-1">Saif Kazi - 181070030</li>
            <li class="mt-1">Palak Mantry - 181071035</li>
            <li class="mt-1">Sarakshi Phate - 181071055</li>
            <li class="mt-1">Shreya Dhananjay - 181071063</li>
          </ul>
        </div>
      </div>
      <hr class="mt-6" />
      <div class="flex flex-row mt-2">
        <router-link
          class="text-lg font-semibold underline flex-1"
          style="color: #24292e"
          to="/RCNN"
          ><b-icon-arrow-left class="mr-1 inline"></b-icon-arrow-left>RCNN
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tools: [
        "Numpy",
        "Pandas",
        "Matplotlib",
        "Scikit-Learn",
        "Polyglot",
        "Beautiful Soup",
        "Markdown",
        "NLTK",
        "Pickle",
        "XGBoost",
        "PyTorch",
        "Keras",
      ],
    };
  },
};
</script>

<style scoped>
td {
  @apply border-2;
  @apply border-gray-700;
  @apply text-center;
  @apply px-2;
}
</style>
