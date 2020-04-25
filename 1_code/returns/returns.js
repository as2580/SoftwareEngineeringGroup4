document.getElementById("employee_log_btn").style.display = "none";
document.getElementById("login").style.display = "none";
document.getElementById("verify").style.display= "none";
document.getElementById("payments").style.display= "none";
document.getElementById("finalGreet").style.display="none";



function scanFunction(){
	window.alert('No Scanner Found');
}

function callEmployee(){
	window.alert('A representative has been called. Please hold.');
	document.getElementById("employee_log_btn").style.display = "block";
}

	var refundTotal = 0;
	var products = [];

var refundController = (function(){
	var Product = function(id, prod_id,price,description){
		this.id = id;
		this.prod_id = prod_id;
		this.price = price;
		this.description = description;
	};



	var calculateTotal = function(){
			var sum = 0;
			products.forEach(function(current){
				sum = sum + current.price;
			});

			refundTotal = sum;
		}

	return{
		addItem: function(prod_id,price,description){
			var newItem, ID; 
			if(products.length>0){
				ID = (products.length-1) + 1
			}
			else {
				ID = 0;
			}

			newItem = new Product(ID, prod_id, price, description);
			products.push(newItem);
			return newItem;
		}, 

		calculateRefund: function(){
		calculateTotal();

		},
		testing: function(){
			console.log(products);
		}
	}

})();


var UIController = (function(){
	var DOMstrings = {
		inputID : '.add__id',
		inputPrice : '.add__price',
		inputDescription : '.add__description',
		inputBtn: '.add__btn',
		productsContainer : '.products__list',
		refundValue: '.refund__value'
	}

	return {
		getinput : function(){
			return{
				id: document.querySelector(DOMstrings.inputID).value,
				price: parseFloat(document.querySelector(DOMstrings.inputPrice).value),
				description: document.querySelector(DOMstrings.inputDescription).value
			};
		},

		addListItem: function(obj){
			var element, html, newHtml
			//Create HTML string with place holder text
			element = DOMstrings.productsContainer;
			html = '<div class="product clearfix" id="product-%id%"><div class="product__id">%prod_id%</div><div class="middle clearfix"><div class="product__price">%price%</div></div><div class ="right clearfix"><div class="product__description">%description%</div></div></div>'
			//Replace placeholder with actual data
			newHtml = html.replace('%id',obj.id);
			newHtml = newHtml.replace('%prod_id%',obj.prod_id);
			newHtml = newHtml.replace('%price%', ('$' + obj.price));
			newHtml = newHtml.replace('%description%',obj.description);
			//insert HTML into the DOM
			document.querySelector(element).insertAdjacentHTML('beforeend',newHtml);
		},

		clearFields: function(){
			fields = document.querySelectorAll(DOMstrings.inputID + ', ' + DOMstrings.inputPrice + ', ' + DOMstrings.inputDescription);
			fieldsArray = Array.prototype.slice.call(fields);

			fieldsArray.forEach(function(current, index, array){
				current.value = "";
			});
			fieldsArray[0].focus();
		},

		displayRefund: function(){
			document.querySelector(DOMstrings.refundValue).textContent = '$'  + refundTotal.toFixed(2);
		},

		

		getDOMstrings: function(){
			return DOMstrings;
		}
	}

})();

var controller = (function(refundCtrl, UICtrl){

	var setupEventListeners = function(){
		var DOM = UICtrl.getDOMstrings();
		document.querySelector(DOM.inputBtn).addEventListener('click',ctrlAddItem);


	};

	var updateRefunds = function(){
		//Calculate Refunds
		refundCtrl.calculateRefund();
		//Return the Refunds 
		var refunds = refundCtrl.calculateRefund();
		//Display the Refund on the UI
		console.log(refunds);
		UICtrl.displayRefund(refunds);
	}

	var ctrlAddItem = function(){
		var input, newItem;
		//1. Get the input data
		input = UICtrl.getinput();
		console.log(input);
		//2. Add the item to the refund controller
		if(input.id !== "" && !(isNaN(input.price)) && input.description !== ""){
		newItem = refundCtrl.addItem(input.id, input.price, input.description);
		console.log(newItem);
		//3.Add the new item to the user interface
		UICtrl.addListItem(newItem);
		//4.Clear input fields
		UICtrl.clearFields();
		//5.Calculate and update Refunds
		updateRefunds();
	} else {
		window.alert("Invalid Entry. Please Try Again.")
	}
};


return {
	init: function(){
		console.log('Application has started');
		setupEventListeners();
	}
}
})(refundController, UIController);


controller.init();




function employeeLogin(){
	document.getElementById("login").style.display = "block";
	document.getElementById("add").style.display = "none";
	document.getElementById("container").style.display = "none";


/********************************************** 
**********************************************
*********DATABASE IMPLEMENTATION NEEDED*******
*********************************************
*********************************************
*********************************************/
	
	document.querySelector('.login_btn').addEventListener('click', function(){
		var employee_id = document.querySelector('.employee__id').value;
		var employee_pass = document.querySelector('.employee__pass').value;
		if((employee_id === "HamilahArnold" && employee_pass === "yN0J06NWG1")||
			(employee_id === "AmritaBernard" && employee_pass === "i76qEle7Fy")||
			(employee_id === "VirgilBriggs" && employee_pass === "cFv4SuGQZm")||
			(employee_id === "CaspianCampos" && employee_pass === "ZwOMpCh93N")||
			(employee_id === "EvangelineCarr" && employee_pass === "wQfh55wS6o")||
			(employee_id === "RoanCarson" && employee_pass === "3Xg3KbrV4l")||
			(employee_id === "MiyaCastillo" && employee_pass === "3IdlSXGYsQ")||
			(employee_id === "MyahClarke" && employee_pass === "kSrNQ93f7g")||
			(employee_id === "IsmailCohen" && employee_pass === "EPTUkM5cR8")||
			(employee_id === "AnnabelCurry" && employee_pass === "0ifQyWcY8I")||
			(employee_id === "KerryDaniel" && employee_pass === "MUvx9MweoQ")||
			(employee_id === "JadenDunn" && employee_pass === "7NnqKfJshv")||
			(employee_id === "RebeccaEstrada" && employee_pass === "rqkmVTK5Aw")||
			(employee_id === "IshaaqFrazier" && employee_pass === "H6jEtIWTmp")||
			(employee_id === "MiltonFrench" && employee_pass === "q2M5huph2N")||
			(employee_id === "BevanGraham" && employee_pass === "zwEAHBOMJg")||
			(employee_id === "KhloeGriffith" && employee_pass === "v185SeT5mt")||
			(employee_id === "ZahraHammond" && employee_pass === "CfZK5R09LG")){
			document.getElementById("loginstatus").innerHTML = ""
			employeeVerify();
		} else {
			document.getElementById("loginstatus").innerHTML = "Login Failed";
		}
	});

}

function employeeVerify(){
	document.getElementById("login").style.display="none";
	document.getElementById("container").style.display="block";
	document.getElementById("verify").style.display="block";

	document.querySelector('.dnverify_btn').addEventListener('click',function(){
		location.reload();
	});

	document.querySelector('.verify_btn').addEventListener('click',function(){
		payments();
	});


}

function payments(){
	document.getElementById("container").style.display="none";
	document.getElementById("verify").style.display = "none";
	document.getElementById("payments").style.display="block";
	document.getElementById("readcard_btn").style.display="none";


		document.querySelector('.card1_btn').addEventListener('click',function(){
			final();
		});

		document.querySelector('.card2_btn').addEventListener('click', function(){
			document.getElementById("readcard_btn").style.display="block";
		});
		
		document.querySelector('.readcard_btn').addEventListener('click', function(){
			final();
		});

		document.querySelector('.reset').addEventListener('click', function(){
			payments();
		});	


}


function final(){
	document.getElementById("payments").style.display="none";
	document.getElementById("finalGreet").style.display="block";

	document.querySelector('.done_btn').addEventListener('click',function(){
		location.reload();
	})
}



