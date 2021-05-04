<template>
  <div class="p-6">
    <div class="px-4">
      <div class="mt-3">
        <p class="text-4xl text-left font-semibold">Implementation</p>
      </div>
      <div class="mt-5 text-justify text-lg">
        <iframe
          class="w-full"
          height="500"
          src="https://www.youtube.com/embed/fmD9Um_OHrY"
          title="YouTube video player"
          frameborder="0"
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
          allowfullscreen
        ></iframe>
      </div>
      <hr class="mt-6" />
      <div class="flex flex-row mt-2">
        <router-link
          class="text-lg font-semibold underline flex-1"
          style="color: #24292e"
          to="/"
          ><b-icon-arrow-left class="mr-1 inline"></b-icon-arrow-left>Overview
        </router-link>
        <router-link
          class="text-lg font-semibold underline flex-1 text-right"
          style="color: #24292e"
          to="/dataset"
          >Dataset<b-icon-arrow-right class="ml-1 inline"></b-icon-arrow-right
        ></router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {};
</script>
