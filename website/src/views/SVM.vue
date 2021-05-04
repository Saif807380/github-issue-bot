<template>
  <div class="p-6">
    <div class="px-4">
      <div class="mt-3">
        <p class="text-4xl text-left font-semibold">SVM</p>
      </div>
      <div class="mt-5 text-justify text-lg">
        <p class="">
          In SVM, we plot data points as points in an n-dimensional space (n
          being the number of features you have) The classification into
          respective categories is done by finding the optimal hyperplane that
          differentiates the two classes in the best possible manner. SVM is
          known as a large margin classifier. The distance between the line and
          the closest data points is referred to as the margin. The best or
          optimal line that can separate the two classes is the line that has
          the largest margin. The optimal hyperplane will be the one with the
          biggest margin. Support vectors are data points that are closer to the
          hyperplane and influence the position and orientation of the
          hyperplane. Using these support vectors, we maximize the margin of the
          classifier.
        </p>
        <div class="my-4">
          <ul class="list-disc ml-12">
            <li class="mt-1">C smooths the curve of the hyperplane.</li>
            <li class="mt-1">
              The function of kernel is to take data as input and transform it
              into the required form For example linear, nonlinear, polynomial,
              radial basis function (RBF), and sigmoid.
            </li>
            <li class="mt-1">
              Setting gamma low considers the points far away from the
              hyperplane will also be considered for hyperplane tuning.
            </li>
          </ul>
        </div>
        <div class="my-6">
          <img
            class="object-contain mx-auto w-4/5"
            src="@/assets/images/svm-1.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic">Fig.1 - Hypothesis</small>
        </div>
        <div class="my-6">
          <img
            class="object-contain mx-auto w-4/5"
            src="@/assets/images/svm-2.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic">Fig.2 - Cost Function</small>
        </div>
        <div class="my-6">
          <img
            class="object-contain mx-auto w-4/5"
            src="@/assets/images/snippets/svm.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic">Fig.3 - Building an SVM Classifier</small>
        </div>
        <p class="text-2xl font-bold mt-6 mb-3">Results</p>
        <div class="my-6">
          <img
            class="object-contain mx-auto w-4/5"
            src="@/assets/images/svm-result.jpeg"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic">Fig.4 - Results</small>
        </div>
      </div>
      <hr class="mt-6" />
      <div class="flex flex-row mt-2">
        <router-link
          class="text-lg font-semibold underline flex-1"
          style="color: #24292e"
          to="/boosting"
          ><b-icon-arrow-left class="mr-1 inline"></b-icon-arrow-left>Boosting
        </router-link>
        <router-link
          class="text-lg font-semibold underline flex-1 text-right"
          style="color: #24292e"
          to="/ann"
          >ANN with BoW<b-icon-arrow-right
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
