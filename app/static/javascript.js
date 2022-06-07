(function(win,doc){
    'use strict';

    //Verifica se o usuário realmente quer deletar o dado
    if(doc.querySelector('.btnDel')){
        let btnDel = doc.querySelectorAll('.btnDel');
        for(let i=0; i < btnDel.length; i++){
            btnDel[i].addEventListener('click', function(event){
                if(confirm('Deseja mesmo deletar este dado?')){
                    return true;
                }else{
                    event.preventDefault();
                }
            });
        }
    }

    //Ajax do form
    if(doc.querySelector('#form')){
        let form=doc.querySelector('#form');
        function sendForm(event)
        {
            event.preventDefault();
            let data = new FormData(form);
            let ajax = new XMLHttpRequest();
            let token = doc.querySelectorAll('input')[0].value;
            ajax.open('POST', form.action);
            ajax.setRequestHeader('X-CSRF-TOKEN',token);
            ajax.onreadystatechange = function()
            {
                if(ajax.status === 200 && ajax.readyState === 4){
                    let result = doc.querySelector('#result');
                    result.innerHTML = 'Operação realizada com sucesso!';
                    result.classList.add('alert');
                    result.classList.add('alert-success');
                }
            }
            ajax.send(data);
            form.reset();
        }
        form.addEventListener('submit',sendForm,false);
    }
})(window,document);

$("form").on("change", ".file-upload-field", function(){ 
    $(this).parent(".file-upload-wrapper").attr("data-text",  $(this).val().replace(/.*(\/|\\)/, '') );
});

function preencheCampos(json) { 
    document.querySelector('#id_logradouro').value = json.logradouro; 
    document.querySelector('#id_localidade').value = json.localidade; 
    document.querySelector('#id_uf').value = json.uf; 
}

const inputValue = document.querySelector("#id_cep");
let zipCode = "";

inputValue.addEventListener("keyup", () => {
    zipCode = inputValue.value;
    if(zipCode)
    if(zipCode.length === 8) {
        if(!isNaN(zipCode)){
            inputValue.value = `${zipCode.substr(0,5)}-${zipCode.substr(5,9)}`;

            var xmlhttp = new XMLHttpRequest();
            xmlhttp.onreadystatechange = function() {
                if (xmlhttp.readyState == XMLHttpRequest.DONE ) {
                    if (!xmlhttp.response.includes("erro")) {
                        preencheCampos(JSON.parse(xmlhttp.responseText));
                    } else {
                        alert("Digite somente o formato válido!<br> 00000000");
                    }
                }
            };
            xmlhttp.open("GET", "https://viacep.com.br/ws/"+zipCode+"/json", true);
            xmlhttp.send();
        } 
       
    }
});

