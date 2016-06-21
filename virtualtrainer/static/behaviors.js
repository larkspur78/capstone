
function addEvents() {
  document.querySelector('.muscle-group-imgs').addEventListener('click', function (evt) {
        var forAttr;
        if (evt.target.matches('label')) {
          forAttr = evt.target.getAttribute('for');
          document.querySelector('[value=' + forAttr + ']').checked = true;
        }
  });
}

document.addEventListener('DOMContentLoaded', function (evt) {
  addEvents();
});
