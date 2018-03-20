<template>
  <div id='Detail'>
    <div class="title">
      <h1>{{title}}</h1>
    </div>
    <div class="sub-info">
      <ul>
          <li><i class="el-icon-tickets"><router-link :to="{name: 'blog',query: {category:categorySlug}}">{{category}}</router-link></i></li>
          <li><i class="el-icon-news">{{tags}}</i></li>
          <li><i class="el-icon-time">{{timestamp}}</i></li>
        </ul>
    </div>
    <div class="content">
      <p>{{content}}</p>
    </div>
  </div>
</template>

<script>

import {articleDetail} from '../../API/API'

export default {
  name: 'Detail',
  data() {
    return {
      title: '',
      category: '',
      categorySlug: '',
      tags: '',
      timestamp: '',
      content: ''
    }
  },
  created() {
    this.fetchArticle()
  },
  methods: {
    async fetchArticle() {
      const {data} = await articleDetail(this.$route.params.slug)
      this.title = data.title
      this.category = data.category
      this.categorySlug = data.categorySlug
      this.tags = data.tags
      this.timestamp = data.timestamp
      this.content = data.html
    }
  }
}
</script>

<style scoped>
  .title , .content{
    width: 50%;
    margin: 0 auto;
  }
  .sub-info {
    width: 50%;
    margin: 0 auto;
    padding: 0 0 20px;
  }
  .sub-info ul li {
    margin-right: 20px;
    display: inline; 
  }
  h1 {
    padding: 40px 15px 25px;
  }
  .content {
    text-align: justify;
    padding: 20px 0;
    border-top: 2px solid #e9eaec;
  }
  
</style>
