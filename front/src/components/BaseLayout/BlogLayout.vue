<template>
  <div id='BlogLayout'>
    <div class="web-top">
      <div id="logo">Logo</div>
      <div class="middle">
        <ul>
          <li><a href="#">博客</a></li>
          <li><a href="#">资讯</a></li>
          <li><a href="#">归档</a></li>
          <li><a href="#">分类</a></li>
          <li><a href="#">标签</a></li>
          <li><a href="#">关于</a></li>
        </ul>
      </div>
      <div id="nav-search">
        <el-input placeholder="请输入内容" prefix-icon="el-icon-search"></el-input>
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
  name: 'BlogLayout'
}
</script>

<style scoped>
  li {
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
  footer {
    position: absolute;
    width: 100%;
    text-align: center;
    border-top: 1px solid#D3D3D3; 
    margin: 50px auto;
  }
</style>
