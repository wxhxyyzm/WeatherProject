<template>
  <div id="chartDomdx" class="chart"></div>
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
      let myChart = $echarts.init(document.getElementById("chartDomdx"));
      // 绘制图表
      //let xdata = ["1", "2", "3", "4", "5", "6", "7"];
      //let ydata = [820, 932, 901, 934, 1290, 1330, 1320];
      //DEWP
      const xdata = jsonData.map((item) => item.DATE);
      const ydata = jsonData.map((item) => item.MXSPD);
      const y2data = jsonData.map((item) => item.WDSP);
      myChart.setOption({
        //title属性
        title: {
          text: "该地区DEWP(露点)折线图",
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
        xAxis: {
          type: "category",
          data: xdata,
        },
        yAxis: {
          type: "value",
        },
        legend: {
          data: ["平均风速", "最大持续风速"],
        },
        series: [
          {
            data: y2data,
            type: "line",
            smooth: true, //平滑过渡
            areaStyle: {},
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
          {
            data: ydata,
            type: "bar",
          },
        ],
      });
    });
  },
};
</script>

<style scope>
#chartDomdx {
  /* 高度360 */
  /*margin-top: 0.2rem;*/
  height: 4rem;
  padding: 0px;
  background-color: transparent;
  text-align: center;
}
</style>