<template>
  <div id="List">
    <div class="one-artical" v-for="(article,index) in articleList" :key='index'>
      <h3 class="one-title"><router-link :to="{name:'article',params:{slug:article.slug}}">{{article.title}}</router-link></h3>
      <div class="one-body">
        <p>{{article.synopsis}}</p>
      </div>
      <div class="one-foot">
        <ul>
          <li><i class="el-icon-tickets"><router-link :to="{name:'blog',query:{category:article.categorySlug}}">{{article.category}}</router-link></i></li>
          <li><i class="el-icon-news">{{article.tags}}</i></li>
          <li><i class="el-icon-time">{{article.timestamp}}</i></li>
        </ul>
      </div>
    </div>  
    <div class="pagination">
      <el-pagination
        @current-change="handleCurrentChange"
        :current-page="currentPage"
        :page-size="5"
        background
        layout="prev, pager, next, jumper"
        :total="blogCount">
      </el-pagination>
    </div>
  </div>
</template>

<script>

import {articles} from '../../API/API'

export default {
  name: 'List',
  data() {
    return {
      articleList: [],
      blogCount: 0,
      currentPage: 1
    }
  },
  created() {
    this.getArticleList(this.$route.params.page,this.$route.query.category,this.$route.query.tag,this.$route.query.archive);
  },
  watch: {
    '$route'(to,from) {
      this.getArticleList(to.params.page)
    },
    deep: true
  },
  methods: {
    getArticleList(page=1) {
      const limit = 5
      const offset = limit * (page - 1)
      articles(limit,offset,this.$route.query.category,this.$route.query.tag,this.$route.query.archive).then(res => {
        this.articleList = res.data.results
        this.blogCount = res.data.count
        this.currentPage = Number(page)
      })
    },
    handleCurrentChange(val) {
      this.$router.push({path: `/blog/page/${val}/`,query: this.$route.query})
    }
  },
}
</script>

<style scoped>
  .one-artical {
    margin: 0 auto;
    width: 50%;
    border-bottom: 2px solid #e9eaec;
    padding-top: 25px;
    padding-bottom: 20px;
    text-align: left;
  }
  .one-title {
    margin-bottom: 20px;
  }
  .one-body {
    font-size: 14px;
  }
  .one-foot {
    margin-top: 15px;
  }
  .one-foot ul li {
    margin-right: 20px;
  }
  .pagination {
    position: absolute;
    /* bottom: 70px; */
    margin: 10px auto;
    text-align: center;
    width: 100%;
    height: 30px;
    line-height: 30px;
  }
</style>
