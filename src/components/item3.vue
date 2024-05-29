<template>
  <div id="chartDomdx" class="chart"></div>
</template>
<!-- 风力折线图 -->
<script>
import { inject, onMounted } from "vue";
import jsonData from "../assets/beijing.json";
import bus from "../views/eventBus.js";
import { roma } from "../assets/roma.js";
// eslint-disable-next-line no-unused-vars
import echarts from "echarts";
export default {
  // name: 'Bro4',
  data() {
    return {
      windvalue: {
        TREASURE_DATE: [],
        WDSP: [], // 平均风速
        MXSPD: [], // 最大持续风速
        GUST: [], // 最大阵风
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
    const $echarts = inject("echarts");
    // 需要获取到element,所以是onMounted 别忘了上面引用
    onMounted(() => {
      // 初始化echarts 别忘了给上面echarts容器添加id
      const myChart = $echarts.init(
        document.getElementById("chartDomdx"),
        roma
      );
      // 绘制图表
      // let xdata = ["1", "2", "3", "4", "5", "6", "7"];
      // let ydata = [820, 932, 901, 934, 1290, 1330, 1320];
      // DEWP
      const xdata = jsonData.map((item) => item.DATE); // 日期
      const ydata = jsonData.map((item) => item.MXSPD); // 最大持续风速
      const y2data = jsonData.map((item) => item.WDSP); // 平均风速
      const y3data = jsonData.map((item) => item.GUST); // 最大阵风
      myChart.setOption({
        // title属性
        textStyle: {
          color: "white", // 设置文字颜色为红色
        },
        title: {
          text: "该地区风速相关信息",
          x: "center",
          textStyle: {
            color: "white", // 设置文字颜色为红色
          },
        },
        grid: {
          left: "10%",
          bottom: "14%",
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
            type: "cross",
            animation: false,
            label: {
              backgroundColor: "#505765",
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
          name: "风速(m/s)",
          type: "value",
          nameTextStyle: {
            color: "white", // 将名称文字颜色设置为白色
          },
        },
        legend: {
          data: ["最大持续风速", "平均风速", "最大阵风"],
          left: "center",
          top: 18,
          textStyle: {
            fontSize: 10, // 设置标题字体大小为16px
          },
        },
        series: [
          {
            name: "最大持续风速",
            type: "bar",
            data: ydata,
            markLine: {
              data: [{ type: "average", name: "Avg" }],
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
            name: "平均风速",
            type: "bar",
            data: y2data,
            markLine: {
              data: [{ type: "average", name: "Avg" }],
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
          {
            name: "最大阵风",
            type: "bar",
            data: y3data,
            markLine: {
              data: [{ type: "average", name: "Avg" }],
            },
            itemStyle: {
              barBorderRadius: [2, 2, 0, 0], //柱体圆角
              color: new $echarts.graphic.LinearGradient(0, 0, 0, 1, [
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
        ],
      });
    });
  },
  watch: {
    windvalue: function (newvalue, oldvalue) {
      if (oldvalue !== newvalue) {
        const echarts = require("echarts");
        const myChart = echarts.init(
          document.getElementById("chartDomdx"),
          roma
        );
        const xdata = this.windvalue.TREASURE_DATE;
        const ydata = this.windvalue.MXSPD;
        const y2data = this.windvalue.WDSP;
        const y3data = this.windvalue.GUST;
        myChart.setOption({
          // title属性
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
            name: "风速(m/s)",
            type: "value",
            nameTextStyle: {
              color: "white", // 将名称文字颜色设置为白色
            },
          },
          legend: {
            data: ["最大持续风速", "平均风速", "最大阵风"],
            left: "center",
            top: 20,
          },
          series: [
            {
              name: "最大持续风速",
              type: "bar",
              data: ydata,
              markLine: {
                data: [{ type: "average", name: "Avg" }],
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
              name: "平均风速",
              type: "bar",
              data: y2data,
              markLine: {
                data: [{ type: "average", name: "Avg" }],
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
            {
              name: "最大阵风",
              type: "bar",
              data: y3data,
              markLine: {
                data: [{ type: "average", name: "Avg" }],
              },
              itemStyle: {
                barBorderRadius: [2, 2, 0, 0], //柱体圆角
                color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [
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
  height: 3.7rem;
  padding: 0px;
  background-color: transparent;
  text-align: center;
}
</style>
