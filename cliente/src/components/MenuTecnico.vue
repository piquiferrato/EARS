<template>
  <div id="container">
    <div  id="barraSuperior">
        <div class="row colorFondo">
          <div class="textoBlanco col-12">
            <a href="#" id="logOut" class="textoNegrita textoBlanco ">LOGOUT</a>
            <p class="textoNegrita text-center">BIENVENIDO "tecnico"</p>
          </div>
        </div>
        <div class="row navegacion tamaño colorFondo" >
          <div class="btn margen ajustarTamaño colorTexto borde fondoBlanco hover col-3 ">
            <p class="textoNegrita text-center mt-1">PEDIDO</p>
          </div>
          <div class="btn  margen ajustarTamaño colorTexto borde fondoBlanco hover col-3">
            <p class="textoNegrita text-center mt-1">EN PROCESO</p>
          </div>
          <div class="btn margen mBottom ajustarTamaño colorTexto borde fondoBlanco hover col-3">
            <p class="textoNegrita text-center mt-1">CANCELADO</p>
          </div>
          <div class="btn margen mBottom ajustarTamaño colorTexto borde fondoBlanco hover col-3">
            <p class="textoNegrita text-center mt-1">TERMINADO</p>
          </div>
        </div>
      </div>
    </div>
</template>
<script>
export default {
  name: "",
  data: () => ({

  })
}
</script>
<style>

.colorFondo {
  background-color: #2699FB;
}

.textoBlanco {
  color: #FFFFFF;

}

.hover:hover {
  background-color: #2699FB;
  color: #FFFFFF;
  border: 1px solid #FFFFFF;
  transition:   background-color 0.5s, color 0.5s, border 0.5s;
}

.textoNegrita {
  font-weight: bold;
}

.borde {
  border: 1px solid #2699FB;
}

.colorFondo {
  background-color: #2699FB;
}

.fondoBlanco {
  background-color: #FFFFFF;
}

.colorTexto {
  color: #2699FB;
}

#logOut {
  padding-left: 10px;
}

/* @media (max-width:768px) {
  .margen {
    margin-top: 40px;
    border-radius: 5px;
  }
  .mBottom {
    margin-bottom: 20px;
  }

  .ajustarTamaño {
    max-width: 70%;
    margin-left: 15%;
    max-height: 60px;
    font-size: 1.3em;
  }
  .container{
    height: 630px;
  }
  .navegacion{
    height: 80%;
  }

} */
</style>
