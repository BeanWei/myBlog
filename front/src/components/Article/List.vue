<template>
  <div id="List">
    <div class="one-artical">
      <h3 class="one-title">详解区块链！很详很长！</h3>
      <div class="one-body">
        <p>区块链从2008年聪哥提出到现在，因为中间很多币的热炒，加上这个东西偏技术很适合去忽悠人，尤其是经过了2017年区块链元年（确实有很多基于区块链的产品或公司诞生)。 所以最近区块链越来越火，火到了养鸡都用区块链，什么垃圾股粘上区块链都会暴涨，一个码农在婚恋网站个人资料里加了一句“区块链工程师”，短短几天，从无人问津立马收到了238封妹子的交友私信。  
          区块链从2008年聪哥提出到现在，因为中间很多币的热炒，加上这个东西偏技术很适合去忽悠人，尤其是经过了2017年区块链元年（确实有很多基于区块链的产品或公司诞生)。
          所以最近区块链越来越火，火到了养鸡都用区块链，什么垃圾股粘上区块链都会暴涨，一个码农在婚恋网站个人资料里加了一句“区块链工程师”，短短几天，从无人问津立马收到了238封妹子的交友私信。
          不过，存在即合理，虽然有过渡夸大，但不可否认区块链带来的技术变革，必然会带来一些产品或思维模式的变革.</p>
      </div>
      <div class="one-foot">
        <ul>
          <li><i class="el-icon-tickets">分类</i></li>
          <li><i class="el-icon-news">标签</i></li>
          <li><i class="el-icon-time">时间戳</i></li>
        </ul>
      </div>
    </div> 
    <div class="one-artical">
      <h3 class="one-title">详解区块链！很详很长！</h3>
      <div class="one-body">
        <p>区块链从2008年聪哥提出到现在，因为中间很多币的热炒，加上这个东西偏技术很适合去忽悠人，尤其是经过了2017年区块链元年（确实有很多基于区块链的产品或公司诞生)。 所以最近区块链越来越火，火到了养鸡都用区块链，什么垃圾股粘上区块链都会暴涨，一个码农在婚恋网站个人资料里加了一句“区块链工程师”，短短几天，从无人问津立马收到了238封妹子的交友私信。  
          区块链从2008年聪哥提出到现在，因为中间很多币的热炒，加上这个东西偏技术很适合去忽悠人，尤其是经过了2017年区块链元年（确实有很多基于区块链的产品或公司诞生)。
          所以最近区块链越来越火，火到了养鸡都用区块链，什么垃圾股粘上区块链都会暴涨，一个码农在婚恋网站个人资料里加了一句“区块链工程师”，短短几天，从无人问津立马收到了238封妹子的交友私信。
          不过，存在即合理，虽然有过渡夸大，但不可否认区块链带来的技术变革，必然会带来一些产品或思维模式的变革.</p>
      </div>
      <div class="one-foot">
        <ul>
          <li><i class="el-icon-tickets">分类</i></li>
          <li><i class="el-icon-news">标签</i></li>
          <li><i class="el-icon-time">时间戳</i></li>
        </ul>
      </div>
    </div> 
    <div class="pagination">
      <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :page-size="10"
        layout="prev, pager, next, jumper"
        :total="1000">
      </el-pagination>
    </div>
  </div>
</template>

<script>
export default {
  name: 'List'
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
