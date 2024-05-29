<template>
  <div id="chartDomdx" class="chart"></div>
</template>
<!-- 风力折线图 -->
<script>
import { inject, onMounted } from "vue";
import jsonData from "../assets/unclimate.json";
import bus from "../views/eventBus.js";
import echarts from "echarts";
import { roma } from "../assets/roma.js";
export default {
  name: "Bro4",
  data() {
    return {
      heatvalue: {
        YearData: [],
        High_Threshold: [],
        Weak_Heatwave: [],
        Moderate_Heatwave: [],
        Strong_Heatwave: [],
      },
    };
  },
  created() {
    // bus.on 方法注册一个自定义事件，通过事件的处理函数形参接收数据
    bus.on("broSendMsgHeat", (val) => {
      this.heatvalue = val;
      console.log(this.heatvalue);
    });
  },
  setup() {
    // 得到echarts对象
    const $echarts = inject("echarts");
    // 需要获取到element,所以是onMounted 别忘了上面引用
    onMounted(() => {
      // 初始化echarts 别忘了给上面echarts容器添加id
      const myChart = $echarts.init(
        document.getElementById("chartDomdx"),
        roma
      );
      // 绘制图表
      // DEWP
      const xdata = jsonData.map((item) => item.YearData); // 日期
      const ydata = jsonData.map((item) => item.High_Threshold); // 高温
      const y2data = jsonData.map((item) => item.Weak_Heatwave); // 小
      const y3data = jsonData.map((item) => item.Moderate_Heatwave); // 中
      const y4data = jsonData.map((item) => item.Strong_Heatwave); // 强
      myChart.setOption({
        // title属性
        textStyle: {
          color: "white", // 设置文字颜色为红色
        },
        title: {
          text: "该地区热浪",
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
          data: xdata,
        },
        yAxis: [
          {
            type: "value",
            name: "次数",
          },
          {
            type: "value",
          },
        ],
        legend: {
          data: ["阈值", "弱高温热浪", "中强高温热浪", "强高温热浪"],
          top: 30,
          left: "center",
        },
        tooltip: {
          trigger: "axis",
          axisPointer: {
            // Use axis to trigger tooltip
            type: "shadow", // 'shadow' as default; can also be 'line' or 'shadow'
          },
        },
        series: [
          {
            name: "阈值",
            data: ydata,
            type: "line",
            smooth: true, // 平滑过渡
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
            yAxisIndex: 0,
          },

          {
            name: "弱高温热浪",
            data: y2data,
            type: "bar",
            yAxisIndex: 1,
            itemStyle: {
              barBorderRadius: [2, 2, 0, 0], //柱体圆角
              color: new $echarts.graphic.LinearGradient(0, 0, 1, 0, [
                {
                  //代表渐变色从正上方开始
                  offset: 0, //offset范围是0~1，用于表示位置，0是指0%处的颜色
                  color: "#996794",
                }, //柱图渐变色
                {
                  offset: 1, //指100%处的颜色
                  color: "#FFACF7",
                },
              ]),
            },
          },
          {
            name: "中强高温热浪",
            data: y3data,
            type: "bar",
            yAxisIndex: 1,
            itemStyle: {
              barBorderRadius: [2, 2, 0, 0], //柱体圆角
              color: new $echarts.graphic.LinearGradient(0, 0, 1, 0, [
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
            name: "强高温热浪",
            data: y4data,
            type: "bar",
            yAxisIndex: 1,
            itemStyle: {
              barBorderRadius: [2, 2, 0, 0], //柱体圆角
              color: new $echarts.graphic.LinearGradient(0, 0, 1, 0, [
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
      });
    });
  },
  watch: {
    heatvalue: function (newvalue, oldvalue) {
      if (oldvalue !== newvalue) {
        const echarts = require("echarts");
        const yChart = echarts.init(
          document.getElementById("chartDomdx"),
          roma
        );
        const xdata = this.heatvalue.YearData;
        const ydata = this.heatvalue.High_Threshold;
        const y2data = this.heatvalue.Weak_Heatwave;
        const y3data = this.heatvalue.Moderate_Heatwave;
        const y4data = this.heatvalue.Strong_Heatwave;

        yChart.setOption({
          // title属性
          textStyle: {
            color: "white", // 设置文字颜色为红色
          },
          title: {
            text: "该地区热浪",
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
            data: xdata,
          },
          yAxis: [
            {
              type: "value",
              name: "次数",
            },
            {
              type: "value",
            },
          ],
          legend: {
            data: ["阈值", "弱高温热浪", "中强高温热浪", "强高温热浪"],
            top: 30,
            left: "center",
          },
          tooltip: {
            trigger: "axis",
            axisPointer: {
              // Use axis to trigger tooltip
              type: "shadow", // 'shadow' as default; can also be 'line' or 'shadow'
            },
          },
          series: [
            {
              name: "阈值",
              data: ydata,
              type: "line",
              smooth: true, // 平滑过渡
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
              yAxisIndex: 0,
            },

            {
              name: "弱高温热浪",
              data: y2data,
              type: "bar",
              yAxisIndex: 1,
              itemStyle: {
                barBorderRadius: [2, 2, 0, 0], //柱体圆角
                color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [
                  {
                    //代表渐变色从正上方开始
                    offset: 0, //offset范围是0~1，用于表示位置，0是指0%处的颜色
                    color: "#996794",
                  }, //柱图渐变色
                  {
                    offset: 1, //指100%处的颜色
                    color: "#FFACF7",
                  },
                ]),
              },
            },
            {
              name: "中强高温热浪",
              data: y3data,
              type: "bar",
              yAxisIndex: 1,
              itemStyle: {
                barBorderRadius: [2, 2, 0, 0], //柱体圆角
                color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [
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
              name: "强高温热浪",
              data: y4data,
              type: "bar",
              yAxisIndex: 1,
              itemStyle: {
                barBorderRadius: [2, 2, 0, 0], //柱体圆角
                color: new echarts.graphic.LinearGradient(0, 0, 1, 0, [
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
        });
      }
    },
  },
};
</script>

<style scope>
#chartDomdx {
  /* 高度360 */
  /*margin-top: 0.2rem;*/
  height: 7rem;
  padding: 10px;
  background-color: transparent;
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
