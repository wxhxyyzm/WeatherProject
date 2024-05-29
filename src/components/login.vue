<template>
  <div class="login">
    <div class="mylogin" align="center">
      <h1 class="title">用户登录</h1>
      <el-form
        :model="loginForm"
        :rules="loginRules"
        ref="loginForm"
        label-width="0px"
      >
        <el-form-item label="" prop="account" style="margin-top: 10px">
          <el-row>
            <el-col :span="2">
              <span class="el-icon-s-custom"></span>
            </el-col>
            <el-col :span="22">
              <el-input
                class="inps"
                placeholder="账号"
                v-model="loginForm.account"
              >
              </el-input>
            </el-col>
          </el-row>
        </el-form-item>
        <el-form-item label="" prop="passWord">
          <el-row>
            <el-col :span="2">
              <span class="el-icon-lock"></span>
            </el-col>
            <el-col :span="22">
              <el-input
                class="inps"
                type="password"
                placeholder="密码"
                v-model="loginForm.passWord"
              ></el-input>
            </el-col>
          </el-row>
        </el-form-item>
        <el-form-item style="margin-top: 55px">
          <el-button type="primary" round class="submitBtn" @click="submitForm"
            >提交
          </el-button>
        </el-form-item>
        <div class="unlogin">
          <router-link :to="{ path: '/forgetpwd' }">
            <a href="register.vue" target="_blank" align="right">忘记密码?</a>
          </router-link>
          |
          <router-link :to="{ path: '/register' }">
            <a href="register.vue" target="_blank" align="right">注册新账号</a>
          </router-link>
        </div>
      </el-form>
    </div>
  </div>
</template>
<script>
import { mapMutations } from "vuex";
export default {
  name: "Login",
  data: function () {
    return {
      loginForm: {
        account: "",
        passWord: "",
      },
      loginRules: {
        account: [{ required: true, message: "请输入账号", trigger: "blur" }],
        passWord: [{ required: true, message: "请输入密码", trigger: "blur" }],
      },
    };
  },

  methods: {
    ...mapMutations(["changeLogin"]),
    submitForm() {
      const userAccount = this.loginForm.account;
      const userPassword = this.loginForm.passWord;
      if (!userAccount) {
        return this.$message({
          type: "error",
          message: "账号不能为空！",
        });
      }
      if (!userPassword) {
        return this.$message({
          type: "error",
          message: "密码不能为空！",
        });
      }
      console.log("用户输入的账号为：", userAccount);
      console.log("用户输入的密码为：", userPassword);
    },
  },
};
</script>
<style scoped>
.mylogin {
  width: 240px;
  height: 280px;
  position: absolute;
  top: 0;
  left: 50px;
  right: 0;
  bottom: 0;
  margin: auto;
  padding: 50px 40px 40px 40px;
  box-shadow: -15px 15px 15px rgba(6, 17, 47, 0.7);
  opacity: 1;
  background: rgba(225, 227, 240, 0.7);
  opacity: 0.9;
  box-shadow: 0 0 20px #ffffff;
  border-radius: 10px;
}
.title {
  color: #39f;
}
.inps input {
  border: none;
  color: #fff;
  background-color: transparent;
  font-size: 12px;
}

.submitBtn {
  background-color: transparent;
  color: #39f;
  width: 200px;
}
</style>