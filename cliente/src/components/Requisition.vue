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
            <p class="card-text textColor" :class="{low: requi.priority == 'baja',
            medium: requi.priority == 'media', high: requi.priority == 'alta'}">{{ requi.priority }}</p>
          </div>
          <h3 class="card-title whiteText">Fecha</h3>
          <div class="whiteBackground border">
            <p class="card-text textColor">{{ requi.date }}</p>
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
  <div class="col-8 centerForm" v-if="editForm">
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
          <option value="baja">Baja</option>
          <option value="media">Media</option>
          <option value="alta">Alta</option>
        </select>
      </div>
      <label>Sistema</label>
      <div class="form-group">
        <select name="" class="form-control" id="select"  v-model="requisitionEdit.affected_system">
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
  </div>
</div>
</template>
<script>
import axios from 'axios';
import EventBus from '../bus/eventBus.js';
export default {
  data() {
    return {
      editForm: false,
      requisition: null,
      requisitionSection: true,
      requisitionEdit: {
        type: '',
        author: sessionStorage.getItem('idUser'),
        subject: '',
        date: '',
        details: '',
        priority: '',
        affected_system: '',
        module: '',
        attached_file: null
      }
    }
  },
  // computed: {
  //   isHigh: function() {
  //     return this.requisition.priority;
  //   },
  //   isMedium: function() {
  //     return this.requisition.priority === 'media';
  //   },
  //   isLow: function() {
  //     return this.requisition.priority === 'baja';
  //   }
  // },
  mounted() {
    //Devuelve todos los pedidos del usuario
    axios.get('http://127.0.0.1:8000/requisitions/' + sessionStorage.getItem('idUser'))
      .then((response) => {
        this.requisition = response.data;
      })
      .catch((error) => {
        console.log(error);
      });
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
          self.requisitionEdit = requi;
          self.requisitionSection = false;
          self.editForm = true;
          // EventBus.$emit('change_module');
        }
      })
      // for (var i = 0; i < this.requisition.length; i++) {
      //   if (this.requisition[i].id == id) {
      //     var prueba = this.requisition[i];
      //     // EventBus.$emit('edit_requisition', prueba);
      //     // EventBus.$emit('view_edit_form');
      //   }
      // }
    },
    update(id) {
      // EventBus.$emit('change_section');
      console.log("entra");
      this.editForm = false;
      this.requisitionSection = true;
      axios.put('http://127.0.0.1:8000/requisitions/update/' + id + '/', {
          type: this.requisitionEdit.type,
          author: this.requisitionEdit.author,
          subject: this.requisitionEdit.subject,
          date: this.requisitionEdit.date,
          details: this.requisitionEdit.details,
          priority: this.requisitionEdit.priority,
          affected_system: this.requisitionEdit.affected_system,
          module: this.requisitionEdit.module,
          attached_file: this.requisitionEdit.attached_file
        })
        .then((data) => {
          // EventBus.$emit('change_section');
          console.log(data);
        })
        .catch((error) => {
          console.log(error.response);
        });
    }
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
</style>
