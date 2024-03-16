<template>
  <div class="allin">
    <!-- 气温图 -->
    <div id="chartDomw" class="chart"></div>
  </div>
</template>
  <!-- 折线图 -->
  <script>
import { inject, onMounted } from "vue";
import jsonData from "../assets/beijing.json";

export default {
  setup() {
    // 得到echarts对象
    let $echarts = inject("echarts");
    // 需要获取到element,所以是onMounted 别忘了上面引用
    onMounted(() => {
      // 初始化echarts 别忘了给上面echarts容器添加id
      let myChart = $echarts.init(document.getElementById("chartDomw"));
      // 绘制图表
      //let xdata = ["1", "2", "3", "4", "5", "6", "7"]; //改数据
      //let maxdata = [820, 932, 901, 934, 1290, 1330, 1320];
      //let mindata = [120, 132, 101, 134, 90, 230, 210];
      //let avgdata = [320, 332, 301, 334, 390, 330, 320];
      const xdata = jsonData.map((item) => item.DATE);
      const ydata = jsonData.map((item) => item.MAX);
      const y2data = jsonData.map((item) => item.MIN);
      const y3data = jsonData.map((item) => item.TEMP);

      myChart.setOption({
        //title属性
        title: {
          text: "该地区气温折线图",
          x: "center",
        },
        grid: {
          left: "2%",
          right: "5%",
          bottom: "15%",
        },
        xAxis: {
          type: "category",
          data: xdata,
        },
        yAxis: {
          type: "value",
        },
        toolbox: {
          right: 10,
          feature: {
            restore: {},
            saveAsImage: {},
          },
        },
        dataZoom: [
          {
            startValue: "2023/1/1",
          },
          {
            type: "inside",
          },
        ],
        visualMap: {
          top: 50,
          right: 10,
          pieces: [
            {
              gt: 0,
              lte: 20,
              color: "#93CE07",
            },
            {
              gt: 20,
              lte: 40,
              color: "#FBDB0F",
            },
            {
              gt: 40,
              lte: 60,
              color: "#FC7D02",
            },
            {
              gt: 60,
              lte: 80,
              color: "#FD0100",
            },
            {
              gt: 80,
              lte: 100,
              color: "#AA069F",
            },
            {
              gt: 100,
              color: "#AC3B2A",
            },
          ],
          outOfRange: {
            color: "#999",
          },
        },
        series: [
          {
            data: ydata, // 底部线条数据
            type: "line",
            smooth: true, // 平滑过渡
            markPoint: {
              data: [],
            },
          },
          {
            data: y2data, // 上部线条数据
            type: "line",
            smooth: true, // 平滑过渡
            markPoint: {
              data: [],
            },
          },
        ],
      });
    });
  },
};
</script>
  
<style scope>
#chartDomw {
  /* 高度360 */
  /*margin-top: 0.2rem;*/
  height: 4rem;
  padding: 0px;
  background-color: transparent;
  text-align: center;
}
</style>