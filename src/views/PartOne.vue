!<template>
  <div class="p1body">
    <div class="title">观云图志</div>
    <div class="en-title">Weather detection map</div>
    <div class="sub-title">「以多彩数据，绘中国气象」</div>
    <router-link to="/p2" class="p2-link">地区简报</router-link>
    <router-link to="/p3" class="p3-link">极端天气</router-link>
  </div>
</template>

<script>
export default {}
</script>

<style scoped>
.p1body {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: url("../assets/p1bg.svg");
  background-size: 100% auto;
}
.title {
  /* 观云图志 */

  position: absolute;
  width: 420px;
  height: 106px;
  left: 394px;
  top: 266px;

  font-family: "Microsoft YaHei";
  font-style: normal;
  font-weight: 700;
  font-size: 90px;
  line-height: 106px;
  /* identical to box height */

  background: linear-gradient(
    269.84deg,
    #bffff2 -29.43%,
    #67e0ff 29.95%,
    #7cceff 69.54%,
    #69c9ff 97.25%
  );
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  text-fill-color: transparent;
}
.en-title {
  /* Weather detection map */

  position: absolute;
  width: 400px;
  height: 26px;
  left: 394px;
  top: 367px;

  font-family: "Microsoft YaHei";
  font-style: normal;
  font-weight: 400;
  font-size: 20px;
  line-height: 26px;
  letter-spacing: 0.25em;
  text-transform: capitalize;

  color: rgba(103, 224, 255, 0.6);
}
.sub-title {
  /* 「以多彩数据，绘中国气象」 */

  position: absolute;
  width: 600px;
  height: 40px;
  left: 378px;
  top: 420px;

  font-family: "Microsoft YaHei";
  font-style: normal;
  font-weight: 400;
  font-size: 32px;
  line-height: 40px;
  /* identical to box height */
  letter-spacing: 0.23em;
  text-transform: capitalize;

  color: #ffffff;
}
.p2-link {
  position: absolute;
  width: 227px;
  height: 53px;
  left: 394px;
  top: 503px;
  background: linear-gradient(
    90deg,
    #67ffff -8.13%,
    #67e0ff -8.12%,
    rgba(103, 227, 255, 0.71) 2.34%,
    rgba(103, 238, 255, 0.533462) 20.19%,
    rgba(103, 242, 255, 0.398869) 29.99%,
    rgba(103, 246, 255, 0.296379) 43.35%,
    rgba(103, 250, 255, 0.149433) 60.69%,
    rgba(103, 255, 255, 0) 93.77%
  );
  border-radius: 47px;
  display: flex;
  align-items: center;
  font-size: 24px;
  text-decoration: none;
  color: white;
  font-family: "Microsoft YaHei";
  letter-spacing: 0.25em;
  padding-left: 30px; /* 调整左侧内边距 */
}
.p3-link {
  position: absolute;
  width: 227px;
  height: 53px;
  left: 654px;
  top: 503px;
  background: linear-gradient(
    90deg,
    #67ffff -8.13%,
    #67e0ff -8.12%,
    rgba(103, 227, 255, 0.71) 2.34%,
    rgba(103, 238, 255, 0.533462) 20.19%,
    rgba(103, 242, 255, 0.398869) 29.99%,
    rgba(103, 246, 255, 0.296379) 43.35%,
    rgba(103, 250, 255, 0.149433) 60.69%,
    rgba(103, 255, 255, 0) 93.77%
  );
  border-radius: 47px;
  display: flex;
  align-items: center;
  font-size: 24px;
  text-decoration: none;
  color: white;
  font-family: "Microsoft YaHei";
  letter-spacing: 0.25em;
  padding-left: 30px; /* 调整左侧内边距 */
}
</style>
