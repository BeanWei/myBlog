<template>
  <div id="aboutMe">
    <div class="top">
      <div class="myIcon">头像</div>
      <div class="myTarget">
        <h5>求职意向</h5>
        <h2>XXXXXXX</h2>
      </div>
    </div>
    <div class="body">
      <div class="bodyLeft">
        <div class="leftTitle"><h2>项目经验</h2></div>
        <ul>
          <li>项目一</li>
          <li>项目二</li>
          <li>项目三</li>
        </ul>
      </div>
      <div class="bodyRight">
        <h2>个人信息</h2>
        <ul>
          <li><i class="el-icon-bell">出生日期</i></li>
          <li><i class="el-icon-location-outline">住址</i></li>
          <li><i class="el-icon-phone-outline">联系电话</i></li>
          <li><i class="el-icon-message">邮箱</i></li>
          <li><i class="el-icon-view">Github</i></li>
        </ul>
      </div>
    </div>
    <div class="body">
      <div class="bodyLeft">
        <div class="bodyLeftUp">
          <div class="leftTitle"><h2>工作经历</h2></div>
          <div style="height: 300px;margin-left: 20px;width: 150px;">
            <el-steps direction="vertical" :active="1">
              <el-step title="公司一" description="这是一段时间"></el-step>
              <el-step title="公司二" description="这是一段时间"></el-step>
              <el-step title="公司三" description="这是一段时间"></el-step>
            </el-steps>
            <div class="stepContent">123</div>
          </div>
        </div>
        <div class="bodyLeftDown">
          <div class="leftTitle"><h2>教育背景</h2></div>
          <div style="height: 105px;margin-left: 20px;">
            <el-steps direction="vertical" :active="1">
              <el-step title="大学" description="这是一段时间"></el-step>
              <el-step title="高中" description="这是一段时间"></el-step>
            </el-steps>
          </div>
        </div>
      </div>
      <div class="bodyRight">
        <div class="bodyRightUp">
          <h2>技术栈</h2>
          <ul>
            <li>1</li>
            <li>2</li>
            <li>3</li>
            <li>4</li>
            <li>5</li>
          </ul>
        </div>
        <div class="bodyRightMiddle">
          <h2>荣誉&证书</h2>
          <ul>
            <li>荣誉一</li>
            <li>荣誉一</li>
            <li>荣誉一</li>
          </ul>
        </div>
        <div class="bodyRightDown">
          <h2>自我概述</h2>
          <p>自我概述</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'aboutMe',
}
</script>

<style scoped>
.bodyLeft h2 {
  margin-bottom: 20px;
}
.body .bodyLeft ul {
  padding: 2px 4px 2px 52px;
  text-align: left;
  margin-bottom: 20px;
}
  .bodyRight li {
    text-align: left;
  }
  #aboutMe {
    width: 50%;
    margin: 0 auto;
    padding: 40px 20px;
  }
  .top {
    box-shadow: 1px 1px 1px 1px rgba(0,0,0,0.1); 
    display: grid;
    grid-template-columns: auto 1fr; 
  }
  .myIcon {
    height: 100px;
    text-align: center;
    background-color: red;
  }
  .myTarget {
    height: 100px;
    line-height: 50px;
    background-color: green;
  }
  .body {
    box-shadow: 1px 1px 1px 1px rgba(0,0,0,0.1); 
    display: grid;
    grid-template-columns: 1fr auto; 
  }
  .bodyLeft {
    height: auto;
    background-color: green;
  }
  .bodyRight {
    height: auto;
    text-align: center;
    background-color: red;
  }
  .bodyLeftDown {
    margin-top: 20px;
  }
  .leftTitle {
    padding: 2px 4px 2px 52px;
    text-align: left;
  }
  .stepContent {
    position: relative;
    margin-top: 0 auto;
    float: right;
  }
</style>
