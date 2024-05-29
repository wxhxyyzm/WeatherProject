<template>
  <div class="allin">
    <!-- 三个气温图 -->
    <div id="chartDomw" class="chart"></div>
  </div>
</template>
  <!-- 折线图 -->
<script>
import { inject, onMounted } from "vue";
import bus from "../views/eventBus.js";
import jsonData from "../assets/beijing.json";
import echarts from "echarts";
import { roma } from "../assets/roma.js";
export default {
  // name: 'Bro6',
  data() {
    return {
      tempvalue: {
        TREASURE_DATE: [],
        MAX_TEMPERATURE: [], // 最高温
        MIN_TEMPERATURE: [], // 最低温
        TEMP: [], // 平均气温
      },
    };
  },
  created() {
    // bus.on 方法注册一个自定义事件，通过事件的处理函数形参接收数据
    bus.on("broSendMsgTemp", (val) => {
      this.tempvalue = val;
      console.log(this.windvalue);
    });
  },
  setup() {
    // 得到echarts对象
    const $echarts = inject("echarts");
    // 需要获取到element,所以是onMounted 别忘了上面引用
    onMounted(() => {
      // 初始化echarts 别忘了给上面echarts容器添加id
      const myChart = $echarts.init(document.getElementById("chartDomw"), roma);
      // 绘制图表
      const xdata = jsonData.map((item) => item.DATE);
      const ydata = jsonData.map((item) => item.MAX);
      const y2data = jsonData.map((item) => item.MIN);
      const y3data = jsonData.map((item) => item.TEMP);

      myChart.setOption({
        // title属性
        textStyle: {
          color: "white", // 设置文字颜色为红色
        },
        title: {
          text: "该地区气温折线图",
          x: "center",
          textStyle: {
            color: "white", // 设置文字颜色为红色
          },
          padding: [20, 0, 0, 0],
        },
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
        grid: {
          left: "2%",
          right: "2%",
          bottom: "10%",
        },
        xAxis: {
          type: "category",
          data: xdata,
        },
        yAxis: {
          name: "温度(°C)",
          type: "value",
          nameTextStyle: {
            color: "white", // 将名称文字颜色设置为白色
          },
        },
        toolbox: {
          right: 10,
          feature: {
            restore: {},
            saveAsImage: {},
          },
        },
        dataZoom: [
          {},
          {
            type: "inside",
          },
        ],

        legend: {
          data: ["最高温", "最低温", "平均温"],
          left: 50,
          top: 10,
        },
        series: [
          {
            name: "平均温",
            data: y3data, // 上部线条数据
            type: "line",
            markPoint: {
              data: [],
            },
            lineStyle: {
              color: "#57B2F4", // 设置线条颜色为红色
            },
            symbol: "none",
          },

          {
            name: "最低温",
            data: y2data, // 上部线条数据
            type: "line",
            markPoint: {
              data: [],
            },
            lineStyle: {
              color: "#AEFF02", // 设置线条颜色为红色
            },
            symbol: "none",
          },
          {
            name: "最高温",
            data: ydata, // 底部线条数据
            type: "line",
            markPoint: {
              data: [],
            },
            lineStyle: {
              color: "#FFACF7", // 设置线条颜色为红色
            },
            symbol: "none",
          },
        ],
      });
    });
  },
  watch: {
    tempvalue: function (newvalue, oldvalue) {
      if (oldvalue !== newvalue) {
        const echarts = require("echarts");
        const myChart = echarts.init(
          document.getElementById("chartDomw"),
          roma
        );
        const xdata = this.tempvalue.TREASURE_DATE;
        const ydata = this.tempvalue.MAX_TEMPERATURE;
        const y2data = this.tempvalue.MIN_TEMPERATURE;
        const y3data = this.tempvalue.TEMP;
        myChart.setOption({
          // title属性
          textStyle: {
            color: "white", // 设置文字颜色为红色
          },
          title: {
            text: "该地区气温折线图",
            x: "center",
            textStyle: {
              color: "white", // 设置文字颜色为红色
            },
            padding: [20, 0, 0, 0],
          },
          grid: {
            left: "2%",
            right: "2%",
            bottom: "10%",
          },
          xAxis: {
            type: "category",
            data: xdata,
          },
          yAxis: {
            name: "温度(°C)",
            type: "value",
            nameTextStyle: {
              color: "white", // 将名称文字颜色设置为白色
            },
          },
          toolbox: {
            right: 10,
            feature: {
              restore: {},
              saveAsImage: {},
            },
          },
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
          dataZoom: [
            {},
            {
              type: "inside",
            },
          ],

          legend: {
            data: ["最高温", "最低温", "平均温"],
            left: 50,
            top: 10,
          },
          series: [
            {
              name: "平均温",
              data: y3data, // 上部线条数据
              type: "line",
              markPoint: {
                data: [],
              },
              lineStyle: {
                color: "#57B2F4", // 设置线条颜色为红色
              },
              symbol: "none",
            },

            {
              name: "最低温",
              data: y2data, // 上部线条数据
              type: "line",
              markPoint: {
                data: [],
              },
              lineStyle: {
                color: "#AEFF02", // 设置线条颜色为红色
              },
              symbol: "none",
            },
            {
              name: "最高温",
              data: ydata, // 底部线条数据
              type: "line",
              markPoint: {
                data: [],
              },
              lineStyle: {
                color: "#FFACF7", // 设置线条颜色为红色
              },
              symbol: "none",
            },
          ],
        });
      }
    },
  },
};
</script>

<style scope>
#chartDomw {
  /* 高度360 */
  /*margin-top: 0.2rem;*/
  height: 28vh;
  padding: 0px;
  text-align: center;
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
