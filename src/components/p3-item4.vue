<template>
  <div id="chartDom" class="chart"></div>
</template>
<script>
import { inject, onMounted } from "vue";
import jsonData from "../assets/unclimate.json";
import bus from "../views/eventBus.js";
import { roma } from "../assets/roma.js";
import echarts from "echarts";
export default {
  // eslint-disable-next-line vue/multi-word-component-names
  name: "Bro2",
  data() {
    return {
      windvalue: {
        YearData: [],
        Grade_6_Wind: [],
        Grade_7_Wind: [],
        Grade_8_Wind: [],
        Grade_9_Wind: [],
        Grade_10_Wind: [],
        Grade_11_Wind: [],
        Grade_12_Wind: [],
      },
    };
  },
  created() {
    // bus.on 方法注册一个自定义事件，通过事件的处理函数形参接收数据
    bus.on("broSendMsgWind2", (val) => {
      this.windvalue = val;
    });
  },

  setup() {
    // 得到echarts对象
    const $echarts = inject("echarts");
    // 需要获取到element,所以是onMounted 别忘了上面引用
    onMounted(() => {
      // 初始化echarts 别忘了给上面echarts容器添加id
      const yChart = $echarts.init(document.getElementById("chartDom"), roma);
      // 绘制图表

      const year = jsonData.map((item) => item.YearData);
      const grade6 = jsonData.map((item) => item.Grade_6_Wind);
      const grade7 = jsonData.map((item) => item.Grade_7_Wind);
      const grade8 = jsonData.map((item) => item.Grade_8_Wind);
      const grade9 = jsonData.map((item) => item.Grade_9_Wind);
      const grade10 = jsonData.map((item) => item.Grade_10_Wind);
      const grade11 = jsonData.map((item) => item.Grade_11_Wind);
      const grade12 = jsonData.map((item) => item.Grade_12_Wind);

      // Create the line chart
      yChart.setOption({
        textStyle: {
          color: "white", // 设置文字颜色为红色
        },
        title: {
          text: "该地区热带气旋",
          x: "center",
          textStyle: {
            color: "white", // 设置文字颜色为红色
          },
        },
        grid: {
          left: "10%",
          bottom: "15%",
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
        tooltip: {
          trigger: "axis",
          axisPointer: {
            // Use axis to trigger tooltip
            type: "shadow", // 'shadow' as default; can also be 'line' or 'shadow'
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
        xAxis: {
          type: "category",
          data: year, // Extract the years from the data array
        },
        yAxis: {
          type: "value",
          name: "次数",
        },
        legend: {
          data: ["6级", "7级", "8级", "9级", "10级", "11级", "12级"],
          top: 30,
          left: "center",
        },
        series: [
          {
            type: "line",
            name: "6级",
            data: grade6, // Extract the corresponding wind grade data
          },
          {
            type: "line",
            name: "7级",
            data: grade7, // Extract the corresponding wind grade data
          },
          {
            type: "line",
            name: "8级",
            data: grade8, // Extract the corresponding wind grade data
          },
          {
            type: "line",
            name: "9级",
            data: grade9, // Extract the corresponding wind grade data
          },
          {
            type: "line",
            name: "10级",
            data: grade10, // Extract the corresponding wind grade data
          },
          {
            type: "line",
            name: "11级",
            data: grade11, // Extract the corresponding wind grade data
          },
          {
            type: "line",
            name: "12级",
            data: grade12, // Extract the corresponding wind grade data
          },
        ],

        // Create the radar chart
      });
    });
  },

  watch: {
    windvalue: function (newvalue, oldvalue) {
      if (oldvalue !== newvalue) {
        const echarts = require("echarts");
        const yChart = echarts.init(document.getElementById("chartDom"), roma);

        const year = this.windvalue.YearData;
        const grade6 = this.windvalue.Grade_6_Wind;
        const grade7 = this.windvalue.Grade_7_Wind;
        const grade8 = this.windvalue.Grade_8_Wind;
        const grade9 = this.windvalue.Grade_9_Wind;
        const grade10 = this.windvalue.Grade_10_Wind;
        const grade11 = this.windvalue.Grade_11_Wind;
        const grade12 = this.windvalue.Grade_12_Wind;

        yChart.setOption({
          textStyle: {
            color: "white", // 设置文字颜色为红色
          },
          title: {
            text: "该地区热带气旋",
            x: "center",
            textStyle: {
              color: "white", // 设置文字颜色为红色
            },
          },
          grid: {
            left: "10%",
            bottom: "15%",
          },
          toolbox: {
            feature: {
              restore: {},
              saveAsImage: {
                pixelRatio: 2,
              },
            },
          },
          tooltip: {
            trigger: "axis",
            axisPointer: {
              // Use axis to trigger tooltip
              type: "shadow", // 'shadow' as default; can also be 'line' or 'shadow'
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
          xAxis: {
            type: "category",
            data: year, // Extract the years from the data array
          },
          yAxis: {
            type: "value",
            name: "次数",
          },
          legend: {
            data: ["6级", "7级", "8级", "9级", "10级", "11级", "12级"],
            top: 30,
            left: "center",
          },
          series: [
            {
              type: "line",
              name: "6级",
              data: grade6, // Extract the corresponding wind grade data
            },
            {
              type: "line",
              name: "7级",
              data: grade7, // Extract the corresponding wind grade data
            },
            {
              type: "line",
              name: "8级",
              data: grade8, // Extract the corresponding wind grade data
            },
            {
              type: "line",
              name: "9级",
              data: grade9, // Extract the corresponding wind grade data
            },
            {
              type: "line",
              name: "10级",
              data: grade10, // Extract the corresponding wind grade data
            },
            {
              type: "line",
              name: "11级",
              data: grade11, // Extract the corresponding wind grade data
            },
            {
              type: "line",
              name: "12级",
              data: grade12, // Extract the corresponding wind grade data
            },
          ],

          // Create the radar chart
        });
      }
    },
  },
};
</script>
  <style scope>
#chartDom {
  /* 高度360 */
  /*margin-top: 0.2rem;*/
  height: 7rem;
  padding: 0px;
  padding: 10px;
  text-align: center;
}
.chart {
  background-color: rgba(240, 231, 231, 0.1);
  border-radius: 0.2rem;
  position: relative;
  overflow: hidden;
  box-shadow: inset 0 0 0 0 transparent;
  animation: flowLine 3s infinite linear;
}

@keyframes flowLine {
  0% {
    box-shadow: inset 0 0 0 0 transparent;
  }
  50% {
    box-shadow: inset 0 0 0 2px rgb(100, 250, 237);
  }
  100% {
    box-shadow: inset 0 0 0 0 transparent;
  }
}
</style>
