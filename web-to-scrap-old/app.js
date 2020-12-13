const app = new Vue({
  el: "#app",
  data() {
    return {
      tableData: DATA.sort(() => 0.5 - Math.random()).map((item, idx) => ({
        id: idx + 1,
        ...item,
        price: this.randomPrice().toFixed(2),
      })),
    };
  },
  methods: {
    randomPrice() {
      return (Math.random() + 1) * 100;
    },
  },
});
