<template>
  <div class="allin">
    <!-- 可见度图 -->
    <div id="chartDoms" class="chart"></div>
  </div>
</template>
  <!-- 可见度折线图 -->
<script>
import { inject, onMounted } from "vue";
import jsonData from "../assets/beijing.json";
import bus from "../views/eventBus.js";
import echarts from "echarts";
import { roma } from "../assets/roma.js";
export default {
  name: "Bro5",
  data() {
    return {
      visionvalue: {
        TREASURE_DATE: [],
        VISIB: [],
      },
    };
  },
  created() {
    // bus.on 方法注册一个自定义事件，通过事件的处理函数形参接收数据
    bus.on("broSendMsgVision", (val) => {
      this.visionvalue = val;
      console.log(this.visionvalue);
    });
  },
  setup() {
    // 得到echarts对象
    const $echarts = inject("echarts");
    // 需要获取到element,所以是onMounted 别忘了上面引用
    onMounted(() => {
      // 初始化echarts 别忘了给上面echarts容器添加id
      const myChart = $echarts.init(document.getElementById("chartDoms"), roma);
      // 绘制图表
      // let xdata = ["1", "2", "3", "4", "5", "6", "7"]; //改数据
      // let maxdata = [820, 932, 901, 934, 1290, 1330, 1320];
      // let mindata = [120, 132, 101, 134, 90, 230, 210];
      // let avgdata = [320, 332, 301, 334, 390, 330, 320];
      const xdata = jsonData.map((item) => item.DATE);
      const ydata = jsonData.map((item) => item.VISIB);

      myChart.setOption({
        textStyle: {
          color: "white", // 设置文字颜色为红色
        },
        title: {
          text: "该地区可见度图",
          x: "center",
          textStyle: {
            color: "white", // 设置文字颜色为红色
          },
        },
        grid: {
          left: "10%",
          bottom: "15%",
        },
        visualMap: {
          min: 0,
          max: Math.max(...ydata),
          dimension: 1,
          orient: "vertical",
          right: 0,
          top: "center",
          text: ["HIGH", "LOW"],
          calculable: true,
          inRange: {
            color: ["#F7B70B", "#57B2F4"],
          },
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
          data: xdata,
        },
        yAxis: {
          name: "可见度(km)",
          type: "value",
          nameTextStyle: {
            color: "white", // 将名称文字颜色设置为白色
          },
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
  watch: {
    visionvalue: function (newvalue, oldvalue) {
      if (oldvalue !== newvalue) {
        const echarts = require("echarts");
        const myChart = echarts.init(
          document.getElementById("chartDoms"),
          roma
        );
        const xdata = this.visionvalue.TREASURE_DATE;
        const ydata = this.visionvalue.VISIB;
        myChart.setOption({
          textStyle: {
            color: "white", // 设置文字颜色为红色
          },
          title: {
            text: "该地区可见度图",
            x: "center",
            textStyle: {
              color: "white", // 设置文字颜色为红色
            },
          },
          grid: {
            left: "10%",
            bottom: "15%",
          },
          visualMap: {
            min: 0,
            max: Math.max(...ydata),
            dimension: 1,
            orient: "vertical",
            right: 0,
            top: "center",
            text: ["HIGH", "LOW"],
            calculable: true,
            inRange: {
              color: ["#F7B70B", "#57B2F4"],
            },
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
            data: xdata,
          },
          yAxis: {
            name: "可见度(km)",
            type: "value",
            nameTextStyle: {
              color: "white", // 将名称文字颜色设置为白色
            },
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
      }
    },
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
