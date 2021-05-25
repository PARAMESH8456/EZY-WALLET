const mobile_field = document.querySelector('#m_no');
const submit = document.querySelector('#submit');

if (mobile_field) {
    mobile_field.addEventListener('keyup', (e) => {
        let val = e.target.value;
        let len = val.length;
        if (len === 0){
            mobile_field.classList.remove('is-invalid');
            mobile_field.classList.remove('is-valid');
        } else if (len > 10 || len < 10){
            mobile_field.classList.add('is-invalid');
            mobile_field.classList.remove('is-valid');
            submit.setAttribute('disabled', 'disabled')
        }else if(len === 10){
            mobile_field.classList.remove('is-invalid');
            mobile_field.classList.add('is-valid');
            submit.removeAttribute('disabled');
        }
    })
}