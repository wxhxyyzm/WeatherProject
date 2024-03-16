<template>
  <div class="block" size="small">
    <span class="demonstration">
      <el-button class="inline-item" round>更新图表</el-button>
      <el-date-picker
        class="inline-item"
        v-model="value2"
        type="daterange"
        unlink-panels
        range-separator="至"
        start-placeholder="开始日期"
        end-placeholder="结束日期"
        :shortcuts="shortcuts"
      ></el-date-picker>
    </span>
  </div>
</template>
  
  <script>
export default {
  data() {
    return {
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
    };
  },
};
</script>
  
  <style>
.inline-item {
  display: inline-block;
  margin-right: 10px; /* 调整按钮和日期选择器之间的间距 */
}
</style>