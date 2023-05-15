<!--  frontend/src/components/home.vue  -->

<template>
    <div id="header">
        <div class="grid">
            <h1>My Drf-Vue Shopping</h1>
            <div class="search">
                  <form>
                    <input type="text" placeholder="输入搜索商品..." v-model="searchStr" />
                    <button></button>
                  </form>
                    <ul>
                      <li class="item"
                        v-for="(commodity, index) of resultCommodities"
                        :key="index"
                      >
                        <div>
                          <img :src="commodity.img" />
                        </div>
                        <h1>{{ commodity.name }}</h1>
                        <h1>商品价格：￥{{ commodity.price }}</h1>
                        <h1>剩余数量：{{ commodity.amount }}</h1>
                      </li>
                  </ul>
            </div>
        </div>
        <hr>
    </div>
</template>

<script>
    export default {
        name: 'home',
        data () {
          return {
            msg: 'Welcome to Your Vue.js App',
            searchStr: "",
            commodities: [
              {name: '水杯', price: '15', amount: '60', img: "../static/水杯.png"},
              {name: '雨伞', price: '35', amount: '10', img: "../static/雨伞.png"},
              {name: '帆布包', price: '10', amount: '35', img: "../static/帆布包.png"},
              {name: '帽子', price: '26', amount: '88', img: "../static/帽子.png"},
              {name: 'U盘', price: '62', amount: '36', img: "../static/U盘.png"}
            ],
        }
      },
        computed: {

    				resultCommodities: function() {
    					var commodities = this.commodities;
    					if (this.searchStr == " ") {
    						return commodities;
    					}

    					var searchStr = this.searchStr.trim().toLowerCase();
    					commodities = commodities.filter(function(item) {

							//若存在返回对象
    						if (item.name.toLowerCase().indexOf(searchStr) != -1) {

    							return item;
    						}
    					});
    					return commodities;
    				}

    			}

    		}
</script>

<style scoped>
    #header {
        text-align: center;
        margin-top: 20px;
    }

    .grid {
        display: grid;
        grid-template-columns: 1fr 4fr 1fr;
    }

    .search {
        padding-top: 22px;
    }

    * {
        box-sizing: border-box;
    }

    form {
        position: relative;
        width: 400px;
        margin: 0 auto;
    }

    input, button {
        border: none;
        outline: none;
    }

    input {
        width: 100%;
        height: 35px;
        padding-left: 13px;
        padding-right: 46px;
    }

    button {
        height: 35px;
        width: 35px;
        cursor: pointer;
        position: absolute;
    }

    .search input {
        border: 2px solid gray;
        border-radius: 5px;
        background: transparent;
        top: 0;
        right: 0;
    }

    .search button {
        background: gray;
        border-radius: 0 5px 5px 0;
        width: 45px;
        top: 0;
        right: 0;
    }

    .search button:before {
        content: "搜索";
        font-size: 13px;
        color: white;
    }

</style>
