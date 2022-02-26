<template>
<div class="footer">
  <h1>{{ info }}</h1>
  <p>
    footer: bottom text
  </p>
</div>
</template>

<script>
export default {
  name: 'Footer',
  props: {
    info: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
p {
  margin: 40px 0 0;
}
</style>
