<template lang="pug">
  #confirm-del(class="modal fade", tabindex=-1, role="dialog")
    .modal-dialog
      .modal-content
        .modal-header Вы уверены?
        .modal-body ...
        .modal-footer
          button(type="button", class="btn btn-default", data-dismiss="modal") Отменить
          a(class="btn btn-default btn-danger btn-ok") Удалить          
</template>

<script>
export default {
  name: 'confirm-del'
}
</script>
