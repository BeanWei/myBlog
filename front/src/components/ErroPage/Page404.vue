<template>
  <div id="Page404">
    <div class="page404"><img :src="page404" @click="PgUp"></div>
  </div>
</template>

<script>
export default {
  name: 'Page404',
  data() {
    return {
      page404: require('../../../static/images/page404.jpg'),
    }
  },
  methods: {
    PgUp() {
      this.$router.go(-1)
    }
  },
}
</script>

<style scoped>
 
</style>
