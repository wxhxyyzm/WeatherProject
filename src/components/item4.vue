<template>
  <div class="allin">
    <!-- 气温图 -->
    <div id="chartDoms" class="chart"></div>
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
      let myChart = $echarts.init(document.getElementById("chartDoms"));
      // 绘制图表
      //let xdata = ["1", "2", "3", "4", "5", "6", "7"]; //改数据
      //let maxdata = [820, 932, 901, 934, 1290, 1330, 1320];
      //let mindata = [120, 132, 101, 134, 90, 230, 210];
      //let avgdata = [320, 332, 301, 334, 390, 330, 320];
      const xdata = jsonData.map((item) => item.DATE);
      const ydata = jsonData.map((item) => item.VISIB);

      myChart.setOption({
        title: {
          text: "该地区可见度图",
          x: "center",
        },
        grid: {
          bottom: "10%",
        },
        visualMap: {
          min: 0,
          max: 10,
          dimension: 1,
          orient: "vertical",
          right: 0,
          top: "center",
          text: ["HIGH", "LOW"],
          calculable: true,
          inRange: {
            color: ["#f2c31a", "#24b7f2"],
          },
        },
        toolbox: {
          feature: {
            saveAsImage: {
              pixelRatio: 2,
            },
          },
        },
        xAxis: {
          data: xdata,
        },
        yAxis: {
          type: "value", // 使用数值轴作为 y 轴
        },
        series: [
          {
            type: "scatter",
            data: ydata,

            // itemStyle: {
            //   color: function (value) {
            //     // 根据可见度大小调整散点的颜色（越向上颜色越深）
            //     return {
            //       type: "linear",
            //       x: 0,
            //       y: 0,
            //       x2: 0,
            //       y2: 1,
            //       colorStops: [
            //         {
            //           offset: 0,
            //           color: "rgba(0, 0, 0, 0.2)", // 散点底色
            //         },
            //         {
            //           offset: 1,
            //           color: "rgba(0, 0, 0, 1)", // 散点顶色
            //         },
            //       ],
            //       global: false,
            //     };
            //   },
            // },
          },
        ],
      });
    });
  },
};
</script>
  
  <style scope>
#chartDoms {
  /* 高度360 */
  /* height: 3.9rem; */
  /*margin-top: 0.2rem;*/
  height: 4rem;
  padding: 0px;
  background-color: transparent;
}
</style>