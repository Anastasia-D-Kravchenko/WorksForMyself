/*
 jQuery jqCart Plugin v1.1.2
 requires jQuery v1.9 or later

 http://incode.pro/

 Date: Date: 2016-05-18 19:15
*/
(function(d) {
  var a, k, g = "",
    n = 0,
    p = !1,
    l = d('<div class="jqcart-cart-label"><span class="jqcart-title">\u041e\u0444\u043e\u0440\u043c\u0438\u0442\u044c \u0437\u0430\u043a\u0430\u0437</span><span class="jqcart-total-cnt">0</span></div>'),
    h = {
      buttons: ".add_item1",
      cartLabel: "body",
      visibleLabel: !1,
      openByAdding: !1,
      handler: "/",
      currency: "$"
    },
    c = {
      init: function(b) {
        h = d.extend(h, b);
        a = c.getStorage();
        if (null !== a && Object.keys(a).length) {
          for (var e in a) a.hasOwnProperty(e) && (n += a[e].count);
          p = !0
        }
        l.prependTo(h.cartLabel)[p ||
          h.visibleLabel ? "show" : "hide"]().on("click", c.openCart).find(".jqcart-total-cnt").text(n);
        d(document).on("click", h.buttons, c.addToCart).on("click", ".jqcart-layout", function(b) {
          b.target === this && c.hideCart()
        }).on("click", ".jqcart-incr", c.changeAmount).on("input keyup", ".jqcart-amount", c.changeAmount).on("click", ".jqcart-del-item", c.delFromCart).on("submit", ".jqcart-orderform", c.sendOrder).on("reset", ".jqcart-orderform", c.hideCart).on("click", ".jqcart-print-order", c.printOrder);
        return !1
      },
      addToCart: function(b) {
        b.preventDefault();
        k = d(this).data();
        if ("undefined" === typeof k.id) return console.log("\u041e\u0442\u0441\u0443\u0442\u0441\u0442\u0432\u0443\u0435\u0442 ID \u0442\u043e\u0432\u0430\u0440\u0430"), !1;
        a = c.getStorage() || {};
        a.hasOwnProperty(k.id) ? a[k.id].count++ : (k.count = 1, a[k.id] = k);
        c.setStorage(a);
        c.changeTotalCnt(1);
        l.show();
        h.openByAdding && c.openCart();
        return !1
      },
      delFromCart: function() {
        var b = d(this).closest(".jqcart-tr"),
          e = b.data("id");
        a = c.getStorage();
        c.changeTotalCnt(-a[e].count);
        delete a[e];
        c.setStorage(a);
        b.remove();
        c.recalcSum();
        return !1
      },
      changeAmount: function() {
        var b = d(this),
          e = b.hasClass("jqcart-amount"),
          g = +(e ? b.val() : b.data("incr")),
          f = b.closest(".jqcart-tr").data("id");
        a = c.getStorage();
        a[f].count = e ? isNaN(g) || 1 > g ? 1 : g : a[f].count + g;
        1 > a[f].count && (a[f].count = 1);
        e ? b.val(a[f].count) : b.siblings("input").val(a[f].count);
        c.setStorage(a);
        c.recalcSum();
        return !1
      },
      recalcSum: function() {
        var b = 0,
          e, a = 0,
          f = 0;
        d(".jqcart-tr").each(function() {
          e = +d(".jqcart-amount", this).val();
          a = Math.ceil(e * d(".jqcart-price", this).text() * 100) / 100;
          d(".jqcart-sum", this).html(a + " " + h.currency);
          b = Math.ceil(100 * (b + a)) / 100;
          f += e
        });
        d(".jqcart-subtotal strong").text(b);
        d(".jqcart-total-cnt").text(f);
        0 >= f && (c.hideCart(), h.visibleLabel || l.hide());
        return !1
      },
      changeTotalCnt: function(b) {
        var e = d(".jqcart-total-cnt");
        e.text(+e.text() + b);
        return !1
      },
      openCart: function() {
        var b = 0;
        a = c.getStorage();
        g = '<p class="jqcart-cart-titlee">\u041a\u043e\u0440\u0437\u0438\u043d\u0430 <span class="jqcart-print-order"></span></p><div class="jqcart-table-wrapper"><div class="jqcart-manage-order" id="pkb"><div class="jqcart-thead"><div>ID</div><div></div><div>\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435</div><div>\u0426\u0435\u043d\u0430</div><div>\u041a\u043e\u043b-\u0432\u043e</div><div>\u0421\u0443\u043c\u043c\u0430</div><div></div></div>';
        var e;
        for (e in a)
          if (a.hasOwnProperty(e)) {
            var k = Math.ceil(a[e].count * a[e].price * 100) / 100;
            b = Math.ceil(100 * (b + k)) / 100;
            g += '<div class="jqcart-tr" data-id="' + a[e].id + '">';
            g += '<div class="jqcart-small-td">' + a[e].id + "</div>";
            g += '<div class="jqcart-small-td jqcart-item-img"><img src="' + a[e].img + '" alt=""></div>';
            g += "<div>" + a[e].title + "</div>";
            g += '<div class="jqcart-price">' + a[e].price + "</div>";
            g += '<div><span class="jqcart-incr" data-incr="-1">&#8211;</span><input type="text" class="jqcart-amount" value="' +
              a[e].count + '"><span class="jqcart-incr" data-incr="1">+</span></div>';
            g += '<div class="jqcart-sum">' + k + " " + h.currency + "</div>";
            g += '<div class="jqcart-small-td"><span class="jqcart-del-item"></span></div>';
            g += "</div>"
          } g += "</div></div>";
        g += '<div class="jqcart-subtotal">\u0418\u0442\u043e\u0433\u043e: <strong>' + b + "</strong> " + h.currency + "</div>";
        b = b ? g + '<p class="jqcart-cart-title">\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f:</p><form class="jqcart-orderform"><p><input type="button" onclick="poty20()" id="naz" value="Вернуться к покупкам"></p></form>' :
          '<h2 class="jqcart-empty-cart">\u041a\u043e\u0440\u0437\u0438\u043d\u0430 \u043f\u0443\u0441\u0442\u0430</h2>';
        d('<div class="" id="org1"><div class="jqcart-checkout" id="red2">123</div></div>').appendTo("body").find(".jqcart-checkout").html(b)
      },
      hideCart: function() {
        d(".jqcart-layout").fadeOut("fast", function() {
          d(this).remove()
        });
        return !1
      },
      sendOrder: function(b) {
        b.preventDefault();
        b = d(this);
        if ("" === d.trim(d("[name=user_name]", b).val()) || "" === d.trim(d("[name=user_phone]", b).val())) return d('<p class="jqcart-error">\u041f\u043e\u0436\u0430\u043b\u0443\u0439\u0441\u0442\u0430, \u0443\u043a\u0430\u0436\u0438\u0442\u0435 \u0441\u0432\u043e\u0435 \u0438\u043c\u044f \u0438 \u043a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u044b\u0439 \u0442\u0435\u043b\u0435\u0444\u043e\u043d!</p>').insertBefore(b).delay(3E3).fadeOut(),
          !1;
        d.ajax({
          url: h.handler,
          type: "POST",
          dataType: "json",
          data: {
            orderlist: d.param(c.getStorage()),
            userdata: b.serialize()
          },
          error: function() {},
          success: function(b) {
            d(".jqcart-checkout").html("<p>" + b.message + "</p>");
            b.errors || setTimeout(m.clearCart, 2E3)
          }
        })
      },
      printOrder: function() {
        var b = d(this).closest(".jqcart-checkout").prop("outerHTML");
        if (!b) return !1;
        var a = window.open("", "\u041f\u0435\u0447\u0430\u0442\u044c \u0437\u0430\u043a\u0430\u0437\u0430", "width=" + screen.width + ",height=" + screen.height),
          c = d(a.opener.document).find('link[href$="jqcart.css"]').attr("href"),
          f = new Date,
          f = ("0" + f.getDate()).slice(-2) + "-" + ("0" + (f.getMonth() + 1)).slice(-2) + "-" + f.getFullYear() + " " + ("0" + f.getHours()).slice(-2) + ":" + ("0" + f.getMinutes()).slice(-2) + ":" + ("0" + f.getSeconds()).slice(-2);
        a.document.write("<html><head><title>\u0417\u0430\u043a\u0430\u0437 " + f + "</title>");
        a.document.write('<link rel="stylesheet" href="' + c + '" type="text/css" />');
        a.document.write("</head><body >");
        a.document.write(b);
        a.document.write("</body></html>");
        setTimeout(function() {
          a.document.close();
          a.focus();
          a.print();
          a.close()
        }, 100);
        return !0
      },
      setStorage: function(a) {
        localStorage.setItem("jqcart", JSON.stringify(a));
        return !1
      },
      getStorage: function() {
        return JSON.parse(localStorage.getItem("jqcart"))
      }
    },
    m = {
      clearCart: function() {
        localStorage.removeItem("jqcart");
        l[h.visibleLabel ? "show" : "hide"]().find(".jqcart-total-cnt").text(0);
        c.hideCart()
      },
      openCart: c.openCart,
      printOrder: c.printOrder,
      test: function() {
        c.getStorage()
      }
    };
  d.jqCart = function(a) {
    if (m[a]) return m[a].apply(this, Array.prototype.slice.call(arguments, 1));
    if ("object" !== typeof a && a) d.error('\u041c\u0435\u0442\u043e\u0434 \u0441 \u0438\u043c\u0435\u043d\u0435\u043c "' + a + '" \u043d\u0435 \u0441\u0443\u0449\u0435\u0441\u0442\u0432\u0443\u0435\u0442!');
    else return c.init.apply(this, arguments)
  }
})(jQuery);
