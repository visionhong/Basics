<template>
<div class="head">
  <h1>{{ title }}</h1>

</div>
</template>

<script>
export default {
  name: 'Header',

  props: {
    title: String
  }
}
</script>
