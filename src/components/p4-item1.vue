<template>
  <!-- 降水信息 -->
  <div id="chartDomy" class="chart"></div>
</template>
    <!-- 折线图 -->
  <script>
import { inject, onMounted } from "vue";
import jsonData from "../assets/hangzhou.json";
import bus from "../views/eventBus.js";
// eslint-disable-next-line no-unused-vars
import echarts from "echarts";
import { roma } from "../assets/roma.js";
export default {
  // name: 'Bro3',
  data() {
    return {
      luvalue: {
        TREASURE_DATE: [],
        DEWP: [],
        TEMP: [],
      },
    };
  },
  created() {
    // bus.on 方法注册一个自定义事件，通过事件的处理函数形参接收数据
    bus.on("broSendMsgLu", (val) => {
      this.luvalue = val;
      console.log(this.tempvalue);
    });
  },
  setup() {
    // 得到echarts对象
    const $echarts = inject("echarts");
    // 需要获取到element,所以是onMounted 别忘了上面引用
    onMounted(() => {
      // 初始化echarts 别忘了给上面echarts容器添加id
      const myChart = $echarts.init(document.getElementById("chartDomy"), roma);
      // 绘制图表
      //const xdata = jsonData.map((item) => item.DATE);
      const startDate = new Date("2024-01-01");
      const endDate = new Date("2024-03-31");
      const xdata = [];

      for (
        let d = new Date(startDate);
        d <= endDate;
        d.setDate(d.getDate() + 1)
      ) {
        xdata.push(d.toISOString().split("T")[0].replace(/-/g, "/"));
      }
      //   console.log(xdata);
      //const xdata = jsonData.map((item) => item.TREASURE_DATE);
      const ydata = jsonData.map((item) => item.TEMP); // 平均温度
      const y2data = jsonData.map((item) => item.PRE_TEMP);
      console.log(ydata);
      myChart.setOption({
        title: {
          text: "日均温与预测日均温",
          left: "center",
          top: 3,
        },
        left: "center",
        grid: {
          left: "15%",
          bottom: "10%",
        },
        legend: {
          data: ["实际均温", "预测均温"],
          left: "center",
          top: 25,
        },
        toolbox: {
          feature: {
            restore: {},
            saveAsImage: {
              pixelRatio: 2,
              type: "jpeg",
            },
          },
        },
        dataZoom: [
          {
            show: false,
          },
          {
            type: "inside",
          },
        ],
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "cross",
            animation: false,
            label: {
              backgroundColor: "#505765",
            },
          },
        },
        xAxis: {
          data: xdata,
          splitLine: {
            show: false,
          },
        },
        yAxis: {
          name: "温度(°C)",
          type: "value",
          nameTextStyle: {
            color: "white", // 将名称文字颜色设置为白色
          },
        },
        series: [
          {
            name: "实际均温",
            type: "line",
            data: ydata,
            animationDelay: function (idx) {
              return idx * 5;
            },
            lineStyle: {
              width: 3,
            },
            emphasis: {
              focus: "series",
            },
          },
          {
            name: "预测均温",
            type: "line",
            data: y2data,
            animationDelay: function (idx) {
              return idx * 5;
            },
            lineStyle: {
              width: 2,
            },
            emphasis: {
              focus: "series",
            },
          },
        ],
        animationEasing: "elasticOut",
        animationDelayUpdate: function (idx) {
          return idx * 5;
        },
      });
    });
  },
};
</script>
  
    <style scope>
.chart {
  height: 4.2rem;
  margin: 0.05rem;
  align-items: center;
  background-color: rgba(240, 231, 231, 0.1);
  border-radius: 0.2rem;
  position: relative;
  overflow: hidden;
  box-shadow: inset 0 0 0 0.5px transparent;
  animation: flowLine 3s infinite linear;
}

@keyframes flowLine {
  0% {
    box-shadow: inset 0 0 0 0 transparent;
  }
  50% {
    box-shadow: inset 0 0 0 1px rgb(100, 250, 237);
  }
  100% {
    box-shadow: inset 0 0 0 0 transparent;
  }
}
</style>
  