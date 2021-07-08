var btn=document.querySelector('#i1')
var sidenav=document.querySelector('.sideber')
var closebtn=document.querySelector('.i3')




btn.addEventListener('click',()=>{
   sidenav.style.width="250px";
})

closebtn.addEventListener('click',()=>{
    sidenav.style.width="0px";
})



var toggle1=document.querySelector('.toggle1')
var nasted1=document.querySelector('.nasted1')



toggle1.addEventListener('click',()=>{
    if (nasted1.style.display=="block"){
        nasted1.style.display="none"
    }
    else{
        nasted1.style.display="block"
    }
 })

// ############################  AJAX   #################################################


$('.plus-cart').click(function (){
    var id=$(this).attr("pid").toString();
    console.log(id)
    var eml=this.parentNode.children[2]
    $.ajax({
        type: "GET",
        url: "/pluscart",
        data:{
            prod_id:id
        },
        success: function (data){
            console.log(data)
            eml.innerText=data.quantity
            document.getElementById("amount").innerText=data.amount
            document.getElementById("totalamount").innerText=data.totalamount
        }
    })
})




$('.minus-cart').click(function (){
    var id=$(this).attr("pid").toString();
    console.log(id)
    var eml=this.parentNode.children[2]
    $.ajax({
        type: "GET",
        url: "/minuscart",
        data:{
            prod_id:id
        },
        success: function (data){
            console.log(data)
            eml.innerText=data.quantity
            document.getElementById("amount").innerText=data.amount
            document.getElementById("totalamount").innerText=data.totalamount
        }
    })
})





$('.remove-cart').click(function (){
    var id=$(this).attr("pid").toString();
    console.log(id)
    var eml=this
    $.ajax({
        type: "GET",
        url: "/removecart",
        data:{
            prod_id:id
        },
        success: function (data){
            console.log(data)
            document.getElementById("amount").innerText=data.amount
            document.getElementById("totalamount").innerText=data.totalamount
            eml.parentNode.parentNode.parentNode.parentNode.remove()
        }
    })
})