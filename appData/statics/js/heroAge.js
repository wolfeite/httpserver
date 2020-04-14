+function ($) {

    $.extend({
        cookie: {
            set: function (cname, cvalue, exdays) {
                var str = cname + "=" + cvalue + ";"
                if (exdays) {
                    var d = new Date();
                    d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
                    var expires = "expires=" + d.toUTCString();
                    str = str + expires
                }
                str = str + ";path=/";
                document.cookie = str;
                //document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
                //即document.cookie= name+"="+value+";path=/";  时间默认为当前会话可以不要，但路径要填写，因为JS的默认路径是当前页，如果不填，此cookie只在当前页面生效！
            },
            get: function (name) {
                var arr, reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)"); //匹配字段
                if (arr = document.cookie.match(reg)) {
                    return unescape(arr[2]);
                } else {
                    return null;
                }
            },
            check: function () {
                var user = getCookie("username");
                if (user != "") {
                    alert("Welcome again " + user);
                } else {
                    user = prompt("Please enter your name:", "");
                    if (user != "" && user != null) {
                        setCookie("username", user, 365);
                    }
                }
            },
            delete: function (name) {
                /**
                 * 清除指定cookie值
                 * */
                var exp = new Date();
                exp.setTime(exp.getTime() - 1);
                var cval = setCookie(name);
                if (cval && cval != null) {
                    document.cookie = name + "=" + cval + ";expires=" + exp.toGMTString()
                }
            },
            clear: function () {
                /**
                 * 清除全部cookie值
                 * */
                var keys = document.cookie.match(/[^ =;]+(?=\=)/g);
                if (keys) {
                    for (var i = keys.length; i--;) {
                        // document.cookie = keys[i] +'=0;expires=' + new Date( 0).toUTCString()
                        document.cookie = keys[i] + '=0;expires=' + new Date(0).toUTCString() + ";path=/" + ";domain=localhost";
                    }
                }
            }
        }
    })

    var asideLeft = $("#asideLeft")
    var navList = $("#asideLeftList")
    var branches = navList.children("li")
    navList.on("click", "li>a", function (e) {
        var el = $(this), branch = el.data("branch"), leave = 0;
        if (el.attr("leave")) {
            branch = $(this.parentNode.parentNode.parentNode).children("a").data("branch")
            leave = el.data("leave")
        }
        if (el.attr("href") != "#") {
            $.cookie.set("branch", branch)
            $.cookie.set("leave", leave)
        }
    })


}(jQuery)


// $(function () {
//     $("#example1").DataTable({
//       "responsive": true,
//       "autoWidth": false,
//     });
//     $('#example2').DataTable({
//       "paging": true,
//       "lengthChange": false,
//       "searching": false,
//       "ordering": true,
//       "info": true,
//       "autoWidth": false,
//       "responsive": true,
//     });
// });