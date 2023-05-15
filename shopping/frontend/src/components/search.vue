<template>
  <div>

      <input type='text' v-model='text'>


      <button @click="search">
          搜索
    </button>

<ul>
                      <li class="item"
                        v-for="(g, index) of goods"
                        :key="index"
                      >
                        <div>
                          <img :src="g.img" />
                        </div>
                        <h1>{{ g.name }}</h1>
                        <h1>商品价格：￥{{ g.price }}</h1>
                        <h1>剩余数量：{{ g.amount }}</h1>
                      </li>
                  </ul>

  </div>
</template>

<script>
  export default {
    name: "Search",
    data() {
      return {
        text: '',
        goods: [],
      }
    },
    methods: {

      search() {
        this.$axios.get('api/sales/search/?text=' + this.text)
          .then(resp => {
            this.goods = resp.data
          })
      }
  }
}
</script>

<style>
img {
  height: 200px;
  width: 200px;
}
</style>
