<template>
  <div ref="mychart" id=""></div>
  <!-- dom结点 注意需要同名 容器默认宽高是0 -->
</template>

<script>
import * as echarts from "echarts"
export default {
mounted(){
let myEcharts=echarts.init(this.$refs.mycharts)

}
}
</script>

<style>

</style>