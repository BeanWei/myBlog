<template>
  <div id="articleSpider">
    <el-carousel :interval="4000" type="card" :height="heightChange">
      <el-carousel-item v-for="(article,index) in articleList" :key="index">
        <div class="article">
          <div class="title">
            <h2>{{article.title}}</h2>
            <ul>
              <li>{{article.author}}</li>
              <li>{{article.category}}</li>
              <li>{{article.tag}}</li>
              <li>{{article.publishtime}}</li>
            </ul>
          </div>
          <div class="content">
            <p ref="contentHeight" v-html="article.content"></p><a href="{article.articleUrl}">阅读原文</a>
            <div class="hiddenBtn" @click="hiddenAll">收起</div>
          </div>
          <div class="moreBtn" v-if="index != flag" @click="getAll(index)">阅读全文</div>
        </div>
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<script>

import {articleSpider} from '../../../API/API'

export default {
  name: 'articleSpider',
  data() {
    return {
      flag: -1,
      heightChange: '300px',
      articleList: [],
    }
  },
  created() {
    this.getArticleList();
  },
  methods: {
    getArticleList() {
      articleSpider().then(res => {
        this.articleList = res.data
      })
    },
    getAll(index) {
      this.flag = index;
      this.heightChange = this.$refs.contentHeight.offsetHeight+150+'px';
    },
    hiddenAll() {
      this.heightChange = '300px';
      this.flag = -1;
    },
  }
}
</script>

<style scoped>
  .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
  }
  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }
  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }
  .article {
    margin: 0 0 20px;
    padding: 10px;
    text-align: justify;
  }
  ul {
    margin-top: 10px;
  }
  li {
    font-size: 10px;
    margin: 0 6px;
    display: inline;
  }
  .title {
    text-align: center;
    margin: 10px 5px 0;
  }
  .content {
    margin: 10px 20px;
  }
  .moreBtn {
    position: absolute;
    left: 0;
    right: 0;
    top: 260px;
    width: 100%;
    text-align: center;
    height: 40px;
    line-height: 40px;
    z-index: 996;
    background-color: #99a9bf;
    box-sizing: 100%;
    box-shadow: 0 0px 80px rgba(0,0,0,1);
  }
  .hiddenBtn {
    margin-top: 10px;
    height: 40px;
    line-height: 40px;
    width: 100%;
    text-align: center;
    background-color: #99a9bf;
    box-sizing: 100%;
    box-shadow: 0 10px 20px rgba(0,0,0,0.5);
  }
</style>