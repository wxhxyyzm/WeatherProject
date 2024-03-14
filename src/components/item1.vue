<template>
  <div>
    <p>降雪（？）没有数据</p>
    <div id="chartDom" class="chart"></div>
<div class="chart"> </div>
</div>
  
</template>

<script>
import { inject, onMounted } from 'vue';
export default {
setup() {
// 2得到echarts对象
let $echarts= inject("echarts")
//3.需要获取到element,所以是onMounted 别忘了上面引用
onMounted(() => {
// 4.初始化echarts 别忘了给上面echarts容器添加id
let myChart = $echarts.init(document.getElementById("chartDom"));
// 5.绘制图表
myChart.setOption({
  xAxis: {
    type: 'category',
    data: ['1', '2', '3', '4', '5', '6', '7']
  },
  yAxis: {
    type: 'value'
  },
  series: [
    {
      data: [820, 932, 901, 934, 1290, 1330, 1320],
      type: 'line',
      smooth: true
    }
  ]
})
})
}
}
</script>

<style>
.chart{
/* 高度360 */
height: 3.3rem;
background-color: transparent;
}
</style>