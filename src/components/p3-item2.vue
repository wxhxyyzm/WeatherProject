<template>
  <!-- 降水信息 -->
  <div id="chartDomy" class="chart"></div>
</template>
    <!-- 折线图 -->
<script>
import { inject, onMounted } from "vue";
import jsonData from "../assets/unclimate.json";
import bus from "../views/eventBus.js";
import echarts from "echarts";
import { roma } from "../assets/roma.js";
export default {
  // name: 'Bro3',
  data() {
    return {
      rainvalue: {
        YearData: [],
        Heavy_Rainfall: [],
        Severe_Rainfall: [],
        Extreme_Rainfall: [],
      },
    };
  },
  created() {
    // bus.on 方法注册一个自定义事件，通过事件的处理函数形参接收数据
    bus.on("broSendMsgRain", (val) => {
      this.rainvalue = val;
      console.log(this.rainvalue);
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
      // let xdata = ["1", "2", "3", "4", "5", "6", "7"]; //改数据
      // let maxdata = [820, 932, 901, 934, 1290, 1330, 1320];
      // let mindata = [120, 132, 101, 134, 90, 230, 210];
      // let avgdata = [320, 332, 301, 334, 390, 330, 320];
      const xdata = jsonData.map((item) => item.YearData);
      const ydata = jsonData.map((item) => item.Heavy_Rainfall);
      const y2data = jsonData.map((item) => item.Severe_Rainfall);
      const y3data = jsonData.map((item) => item.Extreme_Rainfall);
      myChart.setOption({
        title: {
          text: "该地区暴雨",
          left: "center",
        },
        left: "center",
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
        angleAxis: {
          type: "category",
          data: xdata,
        },
        radiusAxis: {},
        polar: {},
        series: [
          {
            type: "bar",
            data: ydata,
            coordinateSystem: "polar",
            name: "暴雨",
            stack: "a",
            emphasis: {
              focus: "series",
            },
            itemStyle: {
              barBorderRadius: [2, 2, 0, 0], //柱体圆角
              color: new $echarts.graphic.LinearGradient(0, 0, 0, 1, [
                {
                  //代表渐变色从正上方开始
                  offset: 0, //offset范围是0~1，用于表示位置，0是指0%处的颜色
                  color: "#57B2F4",
                }, //柱图渐变色
                {
                  offset: 1, //指100%处的颜色
                  color: "#67E0FF",
                },
              ]),
            },
          },
          {
            type: "bar",
            data: y2data,
            coordinateSystem: "polar",
            name: "大暴雨",
            stack: "a",
            emphasis: {
              focus: "series",
            },
            itemStyle: {
              barBorderRadius: [2, 2, 0, 0], //柱体圆角
              color: new $echarts.graphic.LinearGradient(0, 0, 0, 1, [
                {
                  //代表渐变色从正上方开始
                  offset: 0, //offset范围是0~1，用于表示位置，0是指0%处的颜色
                  color: "#659400",
                }, //柱图渐变色
                {
                  offset: 1, //指100%处的颜色
                  color: "#AEFF02",
                },
              ]),
            },
          },
          {
            type: "bar",
            data: y3data,
            coordinateSystem: "polar",
            name: "特大暴雨",
            stack: "a",
            emphasis: {
              focus: "series",
            },
            itemStyle: {
              barBorderRadius: [2, 2, 0, 0], //柱体圆角
              color: new $echarts.graphic.LinearGradient(0, 0, 0, 1, [
                {
                  //代表渐变色从正上方开始
                  offset: 0, //offset范围是0~1，用于表示位置，0是指0%处的颜色
                  color: "#F7B70B",
                }, //柱图渐变色
                {
                  offset: 1, //指100%处的颜色
                  color: "#FFF26D",
                },
              ]),
            },
          },
        ],
        legend: {
          show: true,
          data: ["暴雨", "大暴雨", "特大暴雨"],
          left: 0,
          textStyle: {
            fontSize: 11, // 设置主标题字体大小为18px
          },
        },
      });
    });
  },
  watch: {
    rainvalue: function (newvalue, oldvalue) {
      if (oldvalue !== newvalue) {
        const echarts = require("echarts");
        const myChart = echarts.init(
          document.getElementById("chartDomy"),
          roma
        );
        const xdata = this.rainvalue.YearData;
        const ydata = this.rainvalue.Heavy_Rainfall;
        const y2data = this.rainvalue.Severe_Rainfall;
        const y3data = this.rainvalue.Extreme_Rainfall;

        myChart.setOption({
          title: {
            text: "该地区暴雨",
            left: "center",
          },
          left: "center",
          grid: {
            left: "8%",
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
          angleAxis: {
            type: "category",
            data: xdata,
          },
          radiusAxis: {},
          polar: {},
          series: [
            {
              type: "bar",
              data: ydata,
              coordinateSystem: "polar",
              name: "暴雨",
              stack: "a",
              emphasis: {
                focus: "series",
              },
              itemStyle: {
                barBorderRadius: [2, 2, 0, 0], //柱体圆角
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                  {
                    //代表渐变色从正上方开始
                    offset: 0, //offset范围是0~1，用于表示位置，0是指0%处的颜色
                    color: "#57B2F4",
                  }, //柱图渐变色
                  {
                    offset: 1, //指100%处的颜色
                    color: "#67E0FF",
                  },
                ]),
              },
            },
            {
              type: "bar",
              data: y2data,
              coordinateSystem: "polar",
              name: "大暴雨",
              stack: "a",
              emphasis: {
                focus: "series",
              },
              itemStyle: {
                barBorderRadius: [2, 2, 0, 0], //柱体圆角
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                  {
                    //代表渐变色从正上方开始
                    offset: 0, //offset范围是0~1，用于表示位置，0是指0%处的颜色
                    color: "#659400",
                  }, //柱图渐变色
                  {
                    offset: 1, //指100%处的颜色
                    color: "#AEFF02",
                  },
                ]),
              },
            },
            {
              type: "bar",
              data: y3data,
              coordinateSystem: "polar",
              name: "特大暴雨",
              stack: "a",
              emphasis: {
                focus: "series",
              },
              itemStyle: {
                barBorderRadius: [2, 2, 0, 0], //柱体圆角
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
                  {
                    //代表渐变色从正上方开始
                    offset: 0, //offset范围是0~1，用于表示位置，0是指0%处的颜色
                    color: "#F7B70B",
                  }, //柱图渐变色
                  {
                    offset: 1, //指100%处的颜色
                    color: "#FFF26D",
                  },
                ]),
              },
            },
          ],
          legend: {
            show: true,
            data: ["暴雨", "大暴雨", "特大暴雨"],
            left: 0,
            textStyle: {
              fontSize: 11, // 设置主标题字体大小为18px
            },
          },
        });
      }
    },
  },
};
</script>

    <style scope>
#chartDomy {
  /* 高度360 */
  /* height: 3.9rem; */
  /* margin-top: 0.2rem; */
  height: 7rem;
  padding: 10px;
  background-color: transparent;
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
