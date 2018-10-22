<template>
<div>
  <div class="row" v-if="requisitionSection">
    <div v-for="(requi , index) in requisition" :key="index" class="col-md-12 col-lg-6 " v-if="requisition">
      <div class="card card-block backgroundColor text-center boldText marginCard">
        <div class="card-body">
          <h3 class="card-title whiteText">{{ requi.type }}</h3>
          <div class="whiteBackground border">
            <p class="card-text textColor">{{ requi.subject }}</p>
          </div>
          <h3 class="card-title whiteText">Prioridad</h3>
          <div class="whiteBackground border">
            <p class="card-text textColor" :class="{low: requi.priority == '3',
            medium: requi.priority == '2', high: requi.priority == '1'}"></p>
          </div>
          <h3 class="card-title whiteText">Fecha</h3>
          <div class="whiteBackground border">
            <p class="card-text textColor">{{ requi.date }}</p>
          </div>
          <h3 class="card-title whiteText">Estado</h3>
          <div class="whiteBackground border">
            <p class="card-text textColor" :class="{onHold: requi.status == '1',
            inProcess: requi.status == '2', cancelled: requi.status == '3',
            finished: requi.status == '4'}"></p>
          </div>
          <button type="button" class="boldText marginButton btn btn-light textColor" v-on:click="editRequisition(requi.id)">EDITAR</button>
          <button type="button" class="boldText marginButton btn btn-danger" v-on:click="deletRequisition(requi.id, index)">ELIMINAR</button>
        </div>
      </div>
    </div>
    <div class="textColor" id="dontExistRequisition" v-if="requisition.length == 0">
      <h1>NO HAY PEDIDOS</h1>
    </div>
  </div>
  <formEdit></formEdit>
  <!-- <div class="col-8 centerForm" v-if="editForm">
    <form v-on:submit.prevent id="form">
      <label>Tipo de pedido</label>
      <div class="form-group">
        <select name="" class="form-control" id="select" v-model="requisitionEdit.type">
          <option value="REQUERIMIENTO">Requerimiento</option>
          <option value="ERROR">Error</option>
        </select>
      </div>
      <label>Asunto</label>
      <input type="text" id="asunto" class="form-control" v-model="requisitionEdit.subject">
      <label>Detalle</label>
      <textarea class="form-control" rows="5" v-model="requisitionEdit.details"></textarea>
      <label>Prioridad</label>
      <div class="form-group">
        <select name="" class="form-control" id="select" v-model="requisitionEdit.priority">
          <option value="3">Baja</option>
          <option value="2">Media</option>
          <option value="1">Alta</option>
        </select>
      </div>
      <label>Sistema</label>
      <div class="form-group">
        <select name="" class="form-control" id="select"  v-model="requisitionEdit.affectedSystem">
          <option value="administration">Administracion</option>
          <option value="stock">Stock</option>
          <option value="human resources">Recurso Humanos</option>
        </select>
      </div>
      <label>Modulo</label>
      <div class="form-group">
        <select name="" class="form-control" id="select" v-model="requisitionEdit.module">
          <option value="uno">uno</option>
          <option value="dos">dos</option>
          <option value="tres">tres</option>
        </select>
      </div>
      <label for="inputFile">Archivo adjunto</label>
      <input id="inputFile" type="file" >
      <button type="submit" class="btn btn-primary form-control boldText" v-on:click="update(requisitionEdit.id)">ENVIAR</button>
    </form>
  </div> -->
</div>
</template>
<script>
import axios from 'axios'
import EventBus from '../bus/eventBus.js'
import formEdit from './FormEdit'
export default {
  components: {
    formEdit
  },
  data() {
    return {
      requisition: null,
      requisitionSection: true
    }
  },
  computed: {
    //   isHigh: function() {
    //     return this.requisition.priority;
    //   },
    //   isMedium: function() {
    //     return this.requisition.priority === 'media';
    //   },
    //   isLow: function() {
    //     return this.requisition.priority === 'baja';
    //   }
    //

  },
  mounted() {
    var self = this;
    //Devuelve todos los pedidos del usuario
    axios.get('http://127.0.0.1:8000/requisitions/' + sessionStorage.getItem('idUser'))
      .then((response) => {
        this.requisition = response.data
      })
      .catch((error) => {
        console.log(error);
      });
    EventBus.$on('change_section', () => {
      this.requisitionSection = true
    })

  },
  methods: {
    deletRequisition(id, index) {
      this.requisition.splice(index, 1)
      axios.delete('http://127.0.0.1:8000/requisitions/delete/' + id);
    },
    editRequisition(id) {
      var self = this;
      this.requisition.forEach(function(requi) {
        if (requi.id == id) {
          EventBus.$emit('edit_form', requi)
          self.requisitionSection = false;
          // EventBus.$emit('change_module');
        }
      })
    },
  }
}
</script>
<style>
.border {
  border-radius: 5px;
}

.marginButton {
  margin-top: 15px;
  margin-right: 25px;
  margin-left: 25px;
  width: 140px;
}

.marginCard {
  margin-top: 10px;
}

#dontExistRequisition {
  margin-top: 20px;
  margin: 0 auto;
}

.high {
  background-color: rgb(255, 0, 0);
  color: white;
  border: 1px solid rgb(255, 0, 0);
  border-radius: 5px;
}

.medium {
  background-color: rgb(255, 255, 0);
  color: black;
  border: 1px solid rgb(255, 255, 0);
  border-radius: 5px;
}

.low {
  background-color: rgb(0, 255, 0);
  color: white;
  border: 1px solid rgb(0, 255, 0);
  border-radius: 5px;
}

.low:before {
  content: "Baja";
}

.medium:before {
  content: "Media";
}

.high:before {
  content: "Alta";
}

.onHold:before {
  content: "En espera";
}

.inProcess:before {
  content: "En proceso";
}

.cancelled:before {
  content: "Cancelado";
}

.finished:before {
  content: "Terminado";
}
</style>
