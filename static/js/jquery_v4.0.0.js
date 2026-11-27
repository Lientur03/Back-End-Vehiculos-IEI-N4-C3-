/* Utilidades jQuery/DOM para vistas CRUD manuales (19 modelos + extensión de User) */
(function (window, document) {
  'use strict';

  function getCsrfToken() {
    var meta = document.querySelector('meta[name="csrf-token"]');
    if (meta && meta.getAttribute('content')) {
      return meta.getAttribute('content');
    }
    var cookieMatch = document.cookie.match(/(?:^|;\s*)csrftoken=([^;]+)/);
    return cookieMatch ? decodeURIComponent(cookieMatch[1]) : '';
  }

  function bindDeleteConfirmations() {
    document.addEventListener('submit', function (event) {
      var form = event.target;
      if (!form || !form.matches('form[data-confirm-delete="true"], form.form-confirm-delete')) {
        return;
      }
      var label = form.getAttribute('data-item-label') || 'este registro';
      var ok = window.confirm('¿Confirmas que deseas eliminar ' + label + '? Esta acción no se puede deshacer.');
      if (!ok) {
        event.preventDefault();
      }
    });
  }

  window.CrudHelpers = {
    getCsrfToken: getCsrfToken,
    bindDeleteConfirmations: bindDeleteConfirmations
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', bindDeleteConfirmations);
  } else {
    bindDeleteConfirmations();
  }
})(window, document);
