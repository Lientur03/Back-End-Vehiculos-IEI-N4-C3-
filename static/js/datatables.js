/* Helper local de DataTables para tablas CRUD manuales (19 modelos + extensión de User) */
(function (window, document) {
  'use strict';

  var SPANISH_LABELS = {
    search: 'Buscar:',
    lengthMenu: 'Mostrar _MENU_ registros',
    info: 'Mostrando _START_ a _END_ de _TOTAL_ registros',
    infoEmpty: 'Mostrando 0 a 0 de 0 registros',
    infoFiltered: '(filtrado de _MAX_ registros totales)',
    zeroRecords: 'No se encontraron registros coincidentes',
    paginate: {
      first: 'Primero',
      last: 'Último',
      next: 'Siguiente',
      previous: 'Anterior'
    }
  };

  function initCrudTables(selector, customOptions) {
    var targetSelector = selector || 'table[data-crud-table="true"], table.crud-table';
    var tables = document.querySelectorAll(targetSelector);

    tables.forEach(function (table) {
      if (window.DataTable && typeof window.DataTable.isDataTable === 'function') {
        if (window.DataTable.isDataTable(table)) {
          return;
        }
        new window.DataTable(table, Object.assign({
          pageLength: 10,
          language: SPANISH_LABELS
        }, customOptions || {}));
      } else if (window.jQuery && window.jQuery.fn && typeof window.jQuery.fn.DataTable === 'function') {
        var $tbl = window.jQuery(table);
        if (!window.jQuery.fn.dataTable.isDataTable(table)) {
          $tbl.DataTable(Object.assign({
            pageLength: 10,
            language: SPANISH_LABELS
          }, customOptions || {}));
        }
      }
    });
  }

  window.CrudDataTables = {
    init: initCrudTables,
    language: SPANISH_LABELS
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () {
      initCrudTables();
    });
  } else {
    initCrudTables();
  }
})(window, document);
