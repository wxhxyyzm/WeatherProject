<template>
  <div id="chartDomdx" class="chart"></div>
</template>
<!-- 风力折线图 -->
<script>
import { inject, onMounted } from "vue";
import jsonData from "../assets/beijing.json";
import bus from "./eventBus.js";
import echarts from "echarts";
export default {
  name: "Bro4",
  data() {
    return {
      windvalue: {
        TREASURE_DATE: [],
        "": [], //平均风速
        MXSPD: [], //最大持续风速
        GUST: [], //最大阵风
      },
    };
  },
  created() {
    // bus.on 方法注册一个自定义事件，通过事件的处理函数形参接收数据
    bus.on("broSendMsgWind", (val) => {
      this.windvalue = val;
      console.log(this.windvalue);
    });
  },
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
      const xdata = jsonData.map((item) => item.DATE); //日期
      const ydata = jsonData.map((item) => item.MXSPD); //最大持续风速
      const y2data = jsonData.map((item) => item.WDSP); //平均风速
      const y3data = jsonData.map((item) => item.GUST); //最大阵风
      myChart.setOption({
        //title属性
        textStyle: {
          color: "white", // 设置文字颜色为红色
        },
        title: {
          text: "该地区风速相关信息折线图",
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
  watch: {
    windvalue: function (newvalue, oldvalue) {
      if (oldvalue !== newvalue) {
        var echarts = require("echarts");
        var yChart = echarts.init(document.getElementById("chartDomdx"));
        const xdata = this.windvalue["TREASURE_DATE"];
        const ydata = this.windvalue["MXSPD"];
        const y2data = this.windvalue["WDSP"];
        const y3data = this.windvalue["GUST"];
        yChart.setOption({
          //title属性
          title: {
            text: "该地区风速相关信息折线图",
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
      }
    },
  },
};
</script>

<style scope>
#chartDomdx {
  /* 高度360 */
  /*margin-top: 0.2rem;*/
  height: 6rem;
  padding: 0px;
  background-color: transparent;
  text-align: center;
}
</style>
