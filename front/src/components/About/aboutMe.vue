<template>
  <div id="aboutMe">
    <div class="top">
      <div class="myIcon"><img :src="myIcon"></div>
      <div class="myTarget">
        <el-carousel height="150px">
          <el-carousel-item>
            <h3>
              <h3>求职意向</h3>
              <h1>Web全干工程师</h1>
            </h3>
          </el-carousel-item>
          <el-carousel-item>
            <h3>
              <h1>你在找Web全干工程师？</h1>
            </h3>
          </el-carousel-item>
          <el-carousel-item>
            <h3>
              <h1>没错！就是我了</h1>
            </h3>
          </el-carousel-item>
        </el-carousel>
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
          <li><i class="el-icon-star-off"></i>魏超群(Bean.Wei)</li>
          <li><i class="el-icon-arrow-right"></i>男</li>
          <li><i class="el-icon-bell"></i>1995/01/27</li>
          <li><i class="el-icon-location-outline"></i>重庆市沙坪坝大学城</li>
          <li><i class="el-icon-phone-outline"></i>18523152354</li>
          <li><i class="el-icon-message"></i>157318439@qq.com</li>
          <li><i class="el-icon-view"></i><a href="https://github.com/BeanWei" title="Github" target="_blank">@BeanWei(Github)</a></li>
        </ul>
      </div>
    </div>
    <div class="body">
      <div class="bodyLeft">
        <div class="bodyLeftUp">
          <div class="leftTitle"><h2>工作经历</h2></div>
          <div style="height: 300px;margin-left: 20px;width: 150px;">
            <el-steps direction="vertical" :active="1">
              <div class="stepContentUp">
                <p>如果不能够很好的安抚这些离职员工的情绪，他们弄一波公关危机出来，也够你喝一壶的。
                   如果说董事会已经做出裁员来优化公司成本的决定，你作为CEO要去执行这一决定.</p>
                <p>如果不能够很好的安抚这些离职员工的情绪，他们弄一波公关危机出来，也够你喝一壶的。
                   如果说董事会已经做出裁员来优化公司成本的决定，你作为CEO要去执行这一决定.</p>
                <p>如果不能够很好的安抚这些离职员工的情绪，他们弄一波公关危机出来，也够你喝一壶的。
                   如果说董事会已经做出裁员来优化公司成本的决定，你作为CEO要去执行这一决定.</p>
              </div>
              <el-step title="公司一" description="这是一段时间"></el-step>
              <el-step title="公司二" description="这是一段时间"></el-step>
              <el-step title="公司三" description="这是一段时间"></el-step>
            </el-steps>
          </div>
        </div>
        <div class="bodyLeftDown">
          <div class="leftTitle"><h2>教育背景</h2></div>
          <div style="height: 120px;margin-left: 20px;width: 180px;">
            <el-steps direction="vertical" :active="1">
              <div class="stepContentDown">
                <p>电子信息工程&emsp;&emsp;&emsp;&emsp;&emsp;本科</p>
              </div>
              <el-step title="三峡大学科技学院" description="2013/9--2017/6"></el-step>
            </el-steps>
          </div>
        </div>
      </div>
      <div class="bodyRight">
        <div class="bodyRightUp">
          <h2>技术栈</h2>
          <ul>
            <li>Python</li>
            <li>Django</li>
            <li>Html+CSS+JS</li>
            <li>Vue</li>
            <li>UI库</li>
          </ul>
        </div>
        <div class="bodyRightUp">
          <h2>荣誉&证书</h2>
          <ul>
            <li>英语四级</li>
            <li>二等奖学金</li>
            <li>电子科技大赛省赛三等奖</li>
          </ul>
        </div>
        <div class="bodyRightUp">
          <h2>自我概述</h2>
          <ul>
            <li>1/坚持不凑合</li>
            <li>2/成就感大于畏惧</li>
            <li>3/重感情但不感情用事</li>
            <li>4/重视团队协作</li>
            <li>5/不断成为更好的自己</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'aboutMe',
  data() {
    return {
      myIcon: require('../../../static/images/myIcon.jpg'),
    }
  }
}
</script>

<style scoped>
  #aboutMe {
    width: 50%;
    margin: 0 auto;
    padding: 40px 20px;
  }
  h2 {
    font-size: 20px;
  }
  li {
    margin: 10px 0 10px;
  }
  [class^="el-icon"] {
    margin-right: 10px;
  }
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
  .top {
    box-shadow: 1px 1px 1px 1px rgba(0,0,0,0.1); 
    display: grid;
    grid-template-columns: auto 1fr; 
  }
  .myIcon {
    height: 100px;
    text-align: center;
  }
  .myIcon img {
    width: 100px;
    height: 100px;
  }
  .myTarget {
    height: 100px;
    line-height: 28px;
  }
  .myTarget h1 {
    line-height: 100px;
  }
  .body {
    margin-top: 14px;
    display: grid;
    grid-template-columns: 1fr auto; 
  }
  .bodyLeft {
    height: auto;
  }
  .bodyRight {
    height: auto;
    text-align: justify;
  }
  .bodyRight h2 {
    padding-bottom: 10px;
  }
  .bodyLeftDown {
    margin-top: 60px;
  }
  .leftTitle {
    padding: 2px 4px 2px 52px;
    text-align: left;
  }
  .stepContentUp {
    position: absolute;
    left: 35%;
    width: 25%;
  }
  .stepContentUp p {
    height: 126px;
    text-align: justify;
  }
  .stepContentDown {
    position: absolute;
    left: 40%;
    width: 30%;
  }
  .stepContentDown p {
    text-align: justify;
  }
  .bodyRightUp {
    margin: 20px 0;
  }
  .bodyRightUp h2 {
    padding-bottom: 10px;
  }
</style>
