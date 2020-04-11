+function ($) {
    // var asideLeft = $("#asideLeft")
    // var navList = $("#asideLeftList")
    // var branches = navList.children("")
    // var leaves
    $(function () {
    $("#example1").DataTable({
      "responsive": true,
      "autoWidth": false,
    });
    $('#example2').DataTable({
      "paging": true,
      "lengthChange": false,
      "searching": false,
      "ordering": true,
      "info": true,
      "autoWidth": false,
      "responsive": true,
    });
  });
}(jQuery)