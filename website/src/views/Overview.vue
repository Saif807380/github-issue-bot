<template>
  <div class="p-6">
    <div class="px-4">
      <div class="mt-3">
        <p class="text-4xl text-left font-semibold">Project Overview</p>
      </div>
      <div class="mt-5 text-justify text-lg">
        <p class="">
          GitHub is the world’s largest platform for open source development,
          where developers can manage and review their code and contribute to
          repositories. Contributors can open issues in repositories
          highlighting some problem with the codebase or the documentation. An
          issue is created with a title, a brief description of the issue.
          Issues can be classified using labels such as ‘bug’, ‘feature’,
          ‘documentation’, etc. Such classification makes it easy for the
          maintainers to triage issues, for example, by giving priority to
          resolving a ‘bug’ over ‘documentation’. Presently, most issues have to
          be labelled manually, which is a laborious task. An issue labelling
          bot would automatically label issues when they are created, making it
          easier to handle issue creation and prioritization.
        </p>
        <br />
        <div class="text-center">
          <img
            class="object-contain mx-auto w-2/3"
            src="@/assets/images/home.png"
          />
        </div>
        <br />
        <p class="">
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat. Duis aute irure dolor in
          reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
          pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
          culpa qui officia deserunt mollit anim id est laborum.
        </p>
        <br />
        <p class="">
          Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat. Duis aute irure dolor in
          reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
          pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
          culpa qui officia deserunt mollit anim id est laborum.
        </p>
      </div>
      <hr class="mt-4" />
      <div class="flex flex-row-reverse mt-2">
        <router-link
          class="text-lg font-semibold underline"
          style="color: #24292e"
          to="/dataset"
          >Dataset<b-icon-arrow-right class="ml-1 inline"></b-icon-arrow-right
        ></router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  mounted() {
    window.scrollTo(0, 0);
  },
};
</script>
