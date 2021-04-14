function cart() {
  const view = {
    container: document.querySelector(".cart"),
    rows: document.getElementsByClassName("cart-item"),

    showTotal(price, items) {
      document.querySelector(".total-price").innerHTML = price
        ? "$" + price
        : "";
      document.querySelector(".total-items").innerHTML = items;
    },
  };

  const data = {
    cart_items: cart,
  };

  function init() {
    getTotal();

    view.container.addEventListener("click", (evt) => {
      if (evt.target.classList.contains("remove")) handleRemove(evt);
    });
  }

  function getTotal() {
    let count = 0;
    for (row of view.rows) {
      count += +row.dataset.price;
    }
    const numb = view.rows.length;
    view.showTotal(count, numb);
  }

  function handleRemove(evt) {
    // console.log("here");
    const row = evt.target.closest(".cart-item");
    const id = row.dataset.id;

    row.remove();
    removeItem(id);
    getTotal();
  }

  function removeItem(id) {
    let cart = getCookie("cart");
    if (!cart) return 1;

    cart = JSON.parse(cart);
    // JSON. parse(string) is used to convert string form of cart to an array of JavaScript objects.

    const cartId = cart.findIndex((item) => item.id === id);
    cart.splice(cartId, 1);

    setCookie("cart", JSON.stringify(cart));
  }
  init();
}

document.addEventListener("DOMContentLoaded", cart);
