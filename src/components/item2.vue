<template>
  <!-- 降水信息 -->
  <div id="chartDomy" class="chart"></div>
</template>
  <!-- 折线图 -->
<script>
import { inject, onMounted } from "vue";
import jsonData from "../assets/beijing.json";
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
      const xdata = jsonData.map((item) => item.DATE);
      const y2data = jsonData.map((item) => item.DEWP); // 露点温度
      const ydata = jsonData.map((item) => item.TEMP); // 平均温度
      myChart.setOption({
        title: {
          text: "该地区日均温与露点温度",
          left: "center",
        },
        left: "center",
        grid: {
          left: "10%",
          bottom: "15%",
        },
        legend: {
          data: ["日均温", "露点温度"],
          left: "center",
          top: 25,
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
            name: "日均温",
            type: "bar",
            data: ydata,
            animationDelay: function (idx) {
              return idx * 5;
            },
            itemStyle: {
              barBorderRadius: [2, 2, 0, 0], //柱体圆角
              color: new $echarts.graphic.LinearGradient(
                //前四个参数用于配置渐变色的起止位置，这四个参数依次对应 右下左上 四个方位。也就是从右边开始顺时针方向。
                //通过修改前4个参数，可以实现不同的渐变方向
                /*第五个参数则是一个数组，用于配置颜色的渐变过程。
                          每项为一个对象，包含offset和color两个参数
                        */
                0,
                0,
                0,
                1,
                [
                  {
                    //代表渐变色从正上方开始
                    offset: 0, //offset范围是0~1，用于表示位置，0是指0%处的颜色
                    color: "#57B2F4",
                  }, //柱图渐变色
                  {
                    offset: 1, //指100%处的颜色
                    color: "#67E0FF",
                  },
                ]
              ),
            },
          },
          {
            name: "露点温度",
            type: "bar",
            data: y2data,
            animationDelay: function (idx) {
              return idx * 5 + 100;
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
        animationEasing: "elasticOut",
        animationDelayUpdate: function (idx) {
          return idx * 5;
        },
      });
    });
  },
  watch: {
    luvalue: function (newvalue, oldvalue) {
      if (oldvalue !== newvalue) {
        const echarts = require("echarts");
        const myChart = echarts.init(
          document.getElementById("chartDomy"),
          roma
        );
        const xdata = this.luvalue.TREASURE_DATE;
        const y2data = this.luvalue.DEWP;
        console.log(y2data);
        const ydata = this.luvalue.TEMP;
        console.log(ydata);
        myChart.setOption({
          title: {
            text: "该地区日均温与露点温度",
            left: "center",
          },
          left: "center",
          grid: {
            left: "10%",
            bottom: "15%",
          },
          legend: {
            data: ["日均温", "露点温度"],
            left: "center",
            top: 25,
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
              name: "日均温",
              type: "bar",
              data: ydata,
              animationDelay: function (idx) {
                return idx * 5;
              },
              itemStyle: {
                barBorderRadius: [2, 2, 0, 0], //柱体圆角
                color: new echarts.graphic.LinearGradient(
                  //前四个参数用于配置渐变色的起止位置，这四个参数依次对应 右下左上 四个方位。也就是从右边开始顺时针方向。
                  //通过修改前4个参数，可以实现不同的渐变方向
                  /*第五个参数则是一个数组，用于配置颜色的渐变过程。
                          每项为一个对象，包含offset和color两个参数
                        */
                  0,
                  0,
                  0,
                  1,
                  [
                    {
                      //代表渐变色从正上方开始
                      offset: 0, //offset范围是0~1，用于表示位置，0是指0%处的颜色
                      color: "#57B2F4",
                    }, //柱图渐变色
                    {
                      offset: 1, //指100%处的颜色
                      color: "#67E0FF",
                    },
                  ]
                ),
              },
            },
            {
              name: "露点温度",
              type: "bar",
              data: y2data,
              animationDelay: function (idx) {
                return idx * 5 + 100;
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
          animationEasing: "elasticOut",
          animationDelayUpdate: function (idx) {
            return idx * 5;
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
  /*margin-top: 0.2rem;*/
  height: 3.8rem;
  padding: 0px;
  background-color: transparent;
}
</style>
