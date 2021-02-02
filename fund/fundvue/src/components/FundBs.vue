<template>
  <div>
    <table>
      <tr>
        <td>编号</td>
        <td>基金名称</td>
        <td>基金代码</td>
        <td>单位净值</td>
        <td>日增长率</td>
        <td>近一周</td>
        <td>近一月</td>
        <td>近三月</td>
        <td>近六月</td>
        <td>近一年</td>
        <td>近两年</td>
        <td>近三年</td>
        <td>今年来</td>
        <td>成立来</td>
        <td>手续费</td>
      </tr>
      <tr v-for="item in funds">
        <td>{{item.id}}</td>
        <td>{{item.name}}</td>
        <td>{{item.code}}</td>
        <td>{{item.dwjz}}</td>
        <td>{{item.rzzl}}</td>
        <td>{{item.jyz}}</td>
        <td>{{item.jyy}}</td>
        <td>{{item.jsy}}</td>
        <td>{{item.jly}}</td>
        <td>{{item.jyn}}</td>
        <td>{{item.jln}}</td>
        <td>{{item.jsn}}</td>
        <td>{{item.jnl}}</td>
        <td>{{item.cll}}</td>
        <td>{{item.sxf}}</td>
      </tr>
    </table>
    {{msg}}
  </div>
</template>

<script>
export default {
  name:"fund",
  data(){
    return{
      msg:'this webPage by shusuantianxia,z,t',
      funds: [
        {
          id: 1,
          name: "茅台",
          code: "no001",
          dwjz: 200,
          rzzl: 0.1,
          jyz: 0.2,
          jyy : 0.3,
          jsy: 0.4,
          jly: 0.5,
          jyn: 0.6,
          jln: 0.7,
          jsn: 0.8,
          jnl: 0.9,
          cll: 0.9,
          sxf: 500
        }
      ]
    }
  },
  created () {
    const _this = this;
    this.$axios.get('http://localhost:8081/fund/findAll').then(
      function(resp){
        _this.funds = resp.data;
      }
    )
  }
}
</script>

<style scoped>

</style>