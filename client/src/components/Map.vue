<template>
<!-- eslint-disable max-len -->
<!--Google map-->
        <div id="map-container-google-2" class="z-depth-1-half map-container" style="width: 800; height: 600; ">
          <iframe src="http://127.0.0.1:5000/map" frameborder="0"
            style="border:0" allowfullscreen></iframe>
        </div>

<!--Google Maps-->
</template>

<script>

export default {
  name: "Map",
  props: {
    msg: String
  },
}
</script>