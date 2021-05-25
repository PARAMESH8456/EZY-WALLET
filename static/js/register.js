const date = document.querySelector('#dob')
const submit = document.querySelector('#submit_btn')

date.addEventListener('change', e => {
    if (e.target.value) {
        const dob = new Date(e.target.value)
        const curr = new Date()

        const diff = curr.getTime() - dob.getTime();
        const age = Math.floor(diff / (1000 * 60 * 60 * 24 * 365.25));
        if (age >= 18) {
            console.log('over 18')
            submit.removeAttribute('disabled')

        } else {
            console.log('under 18')
            submit.setAttribute('disabled', 'disabled')
        }
    }else{
        submit.removeAttribute('disabled')
    }
})