<template>
  <div class="p-6">
    <div class="px-4">
      <div class="mt-3">
        <p class="text-4xl text-left font-semibold">Dataset</p>
      </div>
      <div class="mt-5 text-justify text-lg">
        <p class="">
          Text Classification of software code issues is a very unique problem
          statement, hence there are not many reliable datasets out there. We
          felt it was best that we came up with our own dataset, using the
          <span class="font-semibold">GitHub API</span>. The GitHub API provides
          access to the all the repositories, code, issues, pull requests and so
          on hosted on GitHub. The main requirements for our dataset were the
          title, content and the ground-truth label of the issue. By querying
          the API, we generated a dataset comprising of issues from projects
          belonging to 3 programming languages - Python, JavaScript and Java.
          All the issues belong to 6 different categories -
        </p>
        <div class="my-4">
          <ul class="list-disc ml-12">
            <li class="mt-1">Bug</li>
            <li class="mt-1">Documentation</li>
            <li class="mt-1">Feature</li>
            <li class="mt-1">Question</li>
            <li class="mt-1">Design</li>
            <li class="mt-1">Help</li>
          </ul>
        </div>
        <div class="">
          <img
            class="object-contain mx-auto"
            src="@/assets/images/snippets/bash.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic"
            >Fig.1 - Script for downloading the dataset</small
          >
        </div>
        <br />
        <p class="">
          This bash script calls another python script which makes requests to
          the GitHub API. Separate scripts were required since GitHub API has
          rate-limiting.
        </p>
        <div class="">
          <img
            class="object-contain mx-auto"
            src="@/assets/images/snippets/data-py.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic">Fig.2 - GitHub API Request Syntax</small>
        </div>
        <br />
        <p class="">The final dataset consists of the following columns -</p>
        <div class="my-4">
          <ul class="list-disc ml-12">
            <li class="mt-1">url - The GitHub Repository URL</li>
            <li class="mt-1">
              repo - Repository name and repository owner name
            </li>
            <li class="mt-1">title - Title of the issue</li>
            <li class="mt-1">body - Body of the issue</li>
            <li class="mt-1">
              label - Original label assigned by the maintainer of the
              repository
            </li>
          </ul>
        </div>
        <br />
        <div class="">
          <img
            class="object-contain mx-auto w-5/6"
            src="@/assets/images/dataset.png"
          />
        </div>
        <div class="text-center mt-6">
          <small class="italic">Fig.3 - Dataset</small>
        </div>
      </div>
      <hr class="mt-4" />
      <div class="flex flex-row mt-2">
        <router-link
          class="text-lg font-semibold underline flex-1"
          style="color: #24292e"
          to="/demo"
          ><b-icon-arrow-left class="mr-1 inline"></b-icon-arrow-left
          >Implementation</router-link
        >
        <router-link
          class="text-lg font-semibold underline flex-1 text-right"
          style="color: #24292e"
          to="/preprocessing"
          >Data Preprocessing<b-icon-arrow-right
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
