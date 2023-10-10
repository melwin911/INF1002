<template>
  <!-- eslint-disable max-len -->
  <!--Folium map-->
  <div
    id="folium-map"
    style="position: relative; width: 100%; padding-top: 56.25%"
  >
    <iframe
      src="http://127.0.0.1:5000/map"
      style="position: absolute; width: 100%; height: 100%; top: 0; left: 0"
    ></iframe>
  </div>

  <!--Google Maps-->
</template>

<script>
export default {
  name: "Map",
  props: {
    msg: String,
  },
};
</script>
