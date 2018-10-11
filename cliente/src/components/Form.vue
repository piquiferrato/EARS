<template>
<div class="col-8 centerForm">
  <form class="">
    <label method="post">asunto</label>
    <input type="text" id="asunto" class="form-control">
    <label method="post">detalle</label>
    <textarea class="form-control" rows="5"></textarea>
    <label method="post">prioridad</label>
    <div class="form-group">
      <select name="" class="form-control">
        <option value="uno">uno</option>
        <option value="cuatro">cuatro</option>
        <option value="tres">tres</option>
      </select>
    </div>
    <label for="sistema" method="post">sistema</label>
    <div class="form-group">
      <select name="" class="form-control">
        <option value="uno">uno</option>
        <option value="cuatro">cuatro</option>
        <option value="tres">tres</option>
      </select>
    </div>
    <button type="submit" class="btn btn-primary form-control">ENVIAR</button>
  </form>
</div>
</template>
<script>
export default {

  data: () => ({

  })
}
</script>
<style>
.formWidth {
  width:80%;
}

.centerForm {
  margin: 0 auto;
}
</style>
