<template>
  <div class="allin">
    <!-- 气温图 -->
    <div id="chartDomy" class="chart"></div>
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
      let myChart = $echarts.init(document.getElementById("chartDomy"));
      // 绘制图表
      //let xdata = ["1", "2", "3", "4", "5", "6", "7"]; //改数据
      //let maxdata = [820, 932, 901, 934, 1290, 1330, 1320];
      //let mindata = [120, 132, 101, 134, 90, 230, 210];
      //let avgdata = [320, 332, 301, 334, 390, 330, 320];
      const xdata = jsonData.map((item) => item.DATE);
      const ydata = jsonData.map((item) => item.PRCP);

      myChart.setOption({
        title: {
          text: "降水",
          x: "center",
        },
        grid: {
          left: "10%",
          bottom: "10%",
        },
        toolbox: {
          feature: {
            saveAsImage: {
              pixelRatio: 2,
            },
          },
        },
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "shadow",
          },
        },

        xAxis: {
          data: xdata,
          silent: false,
          splitLine: {
            show: false,
          },
          splitArea: {
            show: false,
          },
        },
        yAxis: {
          splitArea: {
            show: false,
          },
        },
        series: [
          {
            type: "line",
            data: ydata,
            // Set `large` for large data amount
            large: true,
            sort: "ascending",
            markPoint: {
              data: [
                {
                  type: "max",
                  name: "最大值",
                  label: {
                    show: true,
                    formatter: "{b}: {c}",
                  },
                },
                {
                  type: "min",
                  name: "最小值",
                  label: {
                    show: true,
                    formatter: "{b}: {c}",
                  },
                },
              ],
            },
          },
        ],
      });
    });
  },
};
</script>
  
  <style scope>
#chartDomy {
  /* 高度360 */
  /* height: 3.9rem; */
  /*margin-top: 0.2rem;*/
  height: 4rem;
  padding: 0px;
  background-color: transparent;
}
</style>