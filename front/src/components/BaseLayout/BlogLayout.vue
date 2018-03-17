<template>
  <div id='BlogLayout'>
    <div class="web-top">
      <div id="logo">Logo</div>
      <div class="middle">
        <ul>
          <li><i class="el-icon-menu" @click="showPanle"></i></li>
          <li><router-link :to="{name: 'blog'}">博客</router-link></li>
          <li><router-link :to="{name: 'newsBoard'}">资讯</router-link></li>
          <li><router-link :to="{name: 'aboutMe'}">关于</router-link></li>
        </ul>
      </div>
      <div id="nav-search">
        <el-input placeholder="请输入内容" prefix-icon="el-icon-search"></el-input>
      </div>        
    </div>
    <div class="top-panel" v-show="panelShow" :panelShow="panelShow">
      <div class="panel-item">
        <h5>分类</h5>
        <ul>
          <li><el-tag>分类一00</el-tag></li>
          <li><el-tag>分类二</el-tag></li>
          <li><el-tag>分类三</el-tag></li>
        </ul>
      </div>
      <div class="panel-item">
        <h5>标签</h5>
        <ul>
          <li><el-tag>标签一</el-tag></li>
          <li><el-tag>标签二</el-tag></li>
          <li><el-tag>标签三</el-tag></li>
        </ul>
      </div>
      <div class="panel-item">
        <h5>归档</h5>
        <ul>
          <li><el-tag>归档一</el-tag></li>
          <li><el-tag>归档二</el-tag></li>
          <li><el-tag>归档三</el-tag></li>
        </ul>
      </div>
    </div>
    <router-view></router-view>
    <footer>
      <div class="page-foot">页脚</div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'BlogLayout',
  data() {
    return {
      panelShow: false
    }
  },
  methods: {
    showPanle() {
      this.panelShow =! this.panelShow
    }
  }
}
</script>

<style scoped>
  .middle ul li {
    margin: 30px;
  }
  .web-top {
    height: 50px;
    position: relative;
    border-bottom: 1px solid rgba(0, 0, 0, 0.1)
  }
  #logo {
    float: left;
    margin-left: 7px;
    line-height: 50px;
  }
  .middle {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%,-50%);
  }
  #nav-search {
    float: right;
    margin-right: 7px;
    line-height: 50px;
    width: 20%;
  }
  .top-panel {
    background-color: #F8F8FF;
    border-radius: 8px;
	  box-shadow: 0 10px 20px rgba(0,0,0,0.5);
    width: 50%;
    position: absolute;
    z-index: 999;
    margin-left: 25%;
    padding: 10px 5px;
    text-align: left;
  }
  .el-icon-menu {
    cursor: pointer;
  }
  .panel-item ul{
    margin: 10px 5px 10px 0;  
  }
  .panel-item {
    margin: 10px 5px;
  }
  footer {
    position: absolute;
    width: 100%;
    text-align: center;
    border-top: 1px solid#D3D3D3; 
    margin: 50px auto;
  }
</style>

