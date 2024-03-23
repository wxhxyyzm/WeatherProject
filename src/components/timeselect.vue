<template>
  <div
    class="block"
    size="small"
    style="background-color: $--color-primary; color: #000"
  >
    <!--    <div>{{ bro1msg }}</div>-->
    <span class="demonstration">
      <el-date-picker
        class="inline-item"
        v-model="value2"
        value-format="YYYY-MM-DD"
        type="daterange"
        unlink-panels
        range-separator="至"
        start-placeholder="2023-12-01"
        end-placeholder="2023-12-31"
        :shortcuts="shortcuts"
      ></el-date-picker>

      <!--查询城市-->
      <el-cascader
        class="inline-item2"
        size="small"
        :options="options"
        v-model="selectedOptions"
        @change="handleChange"
        placeholder="北京市"
      >
      </el-cascader>

      <el-button class="inline-item" round @click="getData">点击查询</el-button>
    </span>
  </div>
</template>

<script>
import { provinceAndCityData, CodeToText } from "element-china-area-data";
import axios from "axios";
import bus from "../views/eventBus.js";

export default {
  data() {
    return {
      name: "Bro1",
      shortcuts: [
        {
          text: "最近一周",
          value: () => {
            const end = new Date();
            const start = new Date();
            start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
            return [start, end];
          },
        },
        {
          text: "最近一个月",
          value: () => {
            const end = new Date();
            const start = new Date();
            start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
            return [start, end];
          },
        },
        {
          text: "最近三个月",
          value: () => {
            const end = new Date();
            const start = new Date();
            start.setTime(start.getTime() - 3600 * 1000 * 24 * 90);
            return [start, end];
          },
        },
      ],
      value1: "",
      value2: "",
      options: provinceAndCityData,
      selectedOptions: [],
    };
  },
  methods: {
    handleChange() {
      // let loc = "";
      // for (let i = 0; i < this.selectedOptions.length; i++) {
      //     loc += CodeToText[this.selectedOptions[i]];
      // }
      // console.log(loc)//打印区域码所对应的属性值即中文地址
    },
    getData() {
      // 这是跟后端请求数据的接口
      // 制作向服务器端发送的数据
      const star = this.value2[0];
      const end = this.value2[1];
      console.log("开始时间: ", star, "结束时间: ", end);
      const province = CodeToText[this.selectedOptions[0]];
      let city = "";
      if (this.selectedOptions.length > 1) {
        city = CodeToText[this.selectedOptions[1]];
      }
      console.log("省份: ", province, " 城市: ", city); // 打印区域码所对应的属性值即中文地址
      // 这是服务器通信的地址
      const path = "http://127.0.0.1:5000/getMessage";
      const dataToSend = {
        begin_time: star,
        end_time: end,
        province: province,
        city: city,
      };
      axios
        .get(path, { params: dataToSend })
        .then((res) => {
          // 这里服务器返回response为一个json对象
          // 通过.data来访返回的数据，然后在通过.变量名进行访问
          // 可以直接通过response.data取得key-value
          const msg = res.data.msg; // 返回的数据

          // 给第一个图表制作数据
          const figure1 = {
            TREASURE_DATE: msg.TREASURE_DATE,
            PRCP: msg.PRCP, // 降雨
            SNDP: msg.SNDP, // 降雪数据
          };
          bus.emit("broSendMsg", figure1);

          // 给第二个图表制作数据
          const figure2 = {
            TREASURE_DATE: msg.TREASURE_DATE,
            DEWP: msg.DEWP, // 露点温度
            TEMP: msg.TEMP, // 平均温度
          };
          bus.emit("broSendMsgLu", figure2);

          // 给第三个图表制作数据
          const figure3 = {
            TREASURE_DATE: msg.TREASURE_DATE,
            MXSPD: msg.MXSPD,
            WDSP: msg.WDSP,
            GUST: msg.GUST,
          };
          bus.emit("broSendMsgWind", figure3);

          // 给第四个图表制作数据
          const figure4 = {
            TREASURE_DATE: msg.TREASURE_DATE,
            VISIB: msg.VISIB,
          };
          bus.emit("broSendMsgVision", figure4);

          // 给第四个图表制作数据
          const figure5 = {
            TREASURE_DATE: msg.TREASURE_DATE,
            MAX_TEMPERATURE: msg.MAX_TEMPERATURE, // 最高温
            MIN_TEMPERATURE: msg.MIN_TEMPERATURE, // 最低温
            TEMP: msg.TEMP, // 平均气温
          };
          bus.emit("broSendMsgTemp", figure5);

          const figure6 = {
            LATITUDE: msg.LATITUDE,
            LONGITUDE: msg.LONGITUDE,
          };
          bus.emit("broSendMsgLocation", figure6);

          // console.log(msg) // 因为不能直接使用this作为指针，因此在这之前将this赋给了then指针
          // window.alter('Success' + this.serverResponse.status + ',' + this.serverResponse.data + ',' + msg); // 成功后显示提示
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
};
</script>

<style>
.inline-item {
  display: inline-block;
  margin-right: 20px; /* 调整按钮和日期选择器之间的间距 */
}
.inline-item2 {
  margin-right: 20px;
}
</style>
