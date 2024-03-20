<template>
  <div id="chartDom" class="chart"></div>
</template>
  <!-- 折线图 -->
  <script>
import { inject, onMounted } from "vue";
import jsonData from "../assets/beijing.json";
import bus from "./eventBus.js";
export default {
  name: "Bro2",
  data() {
    return {
      newvalue: {
        TREASURE_DATE: [],
        DEWP: [],
      },
    };
  },
  created() {
    // bus.on 方法注册一个自定义事件，通过事件的处理函数形参接收数据
    bus.on("broSendMsg", (val) => {
      this.newvalue = val;
      console.log(this.newvalue);
    });
  },

  setup() {
    // 得到echarts对象
    let $echarts = inject("echarts");
    // 需要获取到element,所以是onMounted 别忘了上面引用
    onMounted(() => {
      // 初始化echarts 别忘了给上面echarts容器添加id
      let yChart = $echarts.init(document.getElementById("chartDom"));
      // 绘制图表
      //let xdata = ["1", "2", "3", "4", "5", "6", "7"];
      //let ydata = [820, 932, 901, 934, 1290, 1330, 1320];
      //DEWP
      const xdata = jsonData.map((item) => item.DATE);
      const ydata = jsonData.map((item) => item.DEWP);
      yChart.setOption({
        textStyle: {
          color: "white", // 设置文字颜色为红色
        },
        //title属性
        title: {
          text: "该地区DEWP(露点温度)折线图",
          x: "center",
          textStyle: {
            color: "white", // 设置标题文字颜色为蓝色
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
        series: [
          {
            data: ydata,
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
        ],
      });
    });
  },
};
</script>
  
  <style scope>
#chartDom {
  /* 高度360 */
  /*margin-top: 0.2rem;*/
  height: 6rem;
  padding: 0px;
  background-color: transparent;
  text-align: center;
}
</style>
  