//This program perfoms the functionalities of a Returns System 
//Written by Andrew Vincent 
//March 29, 2020

import java.util.Scanner; // import the Scanner class 

//Main Function
public class return_system{
  public static void main(String[] args) {
    Scanner myObj = new Scanner(System.in);
	int items; 
	
	System.out.println("Welcome to the Retuns System"); //Initial Greeting 
	System.out.print("How many products would you like to return: "); //This asks the user for the quantity of products 
	items = myObj.nextInt();

	System.out.println();

	//This creates an array of products with the size of the amount of products the user is returning 
	int prodArray[] = new int[items];

	//A for loop is run to ask the user of the product ID of each product they are returning each time for however many 
	//products that they are returning 
	for(int i=0; i<items; i++){
	System.out.print("Please scan/enter your products ID: ");
	prodArray[i]=myObj.nextInt();
		}

	returner(items, prodArray);
	}


//Returns Function -- 
	//This function returns the product IDs that the user intially entered to confirm 
	//Once the user confirms that the IDs they entered were correct, it will proceed to the Employee verification 
	//If the user finds an error, it will proceed to the redirected product ID entering function 
  public static void returner(int prod, int [] products){
  	Scanner myObj = new Scanner(System.in);
  	System.out.println();
  	System.out.println("Here are the Product IDs you have entered: ");
  	for(int j=0; j<prod; j++){
  		System.out.println(products[j]);
  	}

  	String confirm;
  	System.out.println("Would you like to procceed, [press 1 for Yes or other key for No]: ");
  	confirm = myObj.nextLine();

  	if(confirm.equals("1")){
  		System.out.println();
  		System.out.println("The System will now proceed to Employee Verification.");
  		employVerif();
  	}

  	else{
  		System.out.println();
  		System.out.println("You will now be redirected to enter your product ID.");
  		redirect(prod);
  	}
  }


//Redirected Products Entering -- 
  //This is incase the user has an error with the initial product IDs that they entered 
  //This uses the same program as the main to have the user re-enter the product IDs 
  //This function will then relay back to the returner function for validation testing again 
  public static void redirect(int a){
  	Scanner myObj = new Scanner(System.in);
  	int productArray[] = new int[a];

  	for(int i=0; i<a; i++){
	System.out.print("Please scan/enter your products ID: ");
	productArray[i]=myObj.nextInt();
		}

	returner(a,productArray);
  }


//Employee Verification-- 
  //This function takes the input of the employee_id and employee_password to confirm employee credentials 
  //If the credentials were entered wrong, the function will recall itself 
  //If correct, the function will then pass on the the employee instructions function 
public static void employVerif(){
	Scanner myObj = new Scanner(System.in);
	String employee_id; 
	String employee_password;

	System.out.println();
	System.out.print("Please enter your Employee ID: ");
	employee_id = myObj.nextLine();
	System.out.print("Please enter your Employee Password: ");
	employee_password = myObj.nextLine();

	//These are examples of employee_ids and employee_passwords pulled from our database
	//As of now this was inputted just for the demo 
	//For full functionality, we would have to enter in all of the credentials like below
	//To save lines of code, there is an option to link to the spreadsheet itself if needed 
	if((employee_id.equals("HalimahArnold"))&&employee_password.equals("yN0J06NWG1")
		||employee_id.equals("AmritaBernard")&&employee_password.equals("i76qEle7Fy")
		||employee_id.equals("VirgilBriggs")&&employee_password.equals("cFv4SuGQZm")
		||employee_id.equals("CaspianCampos")&&employee_password.equals("ZwOMpCh93N")
		||employee_id.equals("RoanCarson")&&employee_password.equals("3Xg3KbrV4l")
		||employee_id.equals("MiyaCastillo")&&employee_password.equals("3IdlSXGYsQ")
		||employee_id.equals("MyahClarke")&&employee_password.equals("kSrNQ93f7g")
		||employee_id.equals("IsmailCohen")&&employee_password.equals("EPTUkM5cR8")
		||employee_id.equals("AnnabelCurry")&&employee_password.equals("0ifQyWcY8I")
		||employee_id.equals("KerryDaniel")&&employee_password.equals("MUvx9MweoQ")
		||employee_id.equals("RebeccaEstrada")&&employee_password.equals("rqkmVTK5Aw")

){
		System.out.println();
		System.out.println("Employee Verification Passed.");
		System.out.println();
		System.out.println("Proceeding...");
		employeeInst();
	}
	else{
		System.out.println();
		System.out.println("Employee Verification Failed. Please Retry");
		employVerif();
	}
}

//Employee Instructions--
	//This was written to direct the employees on how to handle returns 
	//If its valid it gives a specific set of instructions
	//If the items are invalid it gives another set of instructions 
public static void employeeInst(){
	Scanner myObj = new Scanner(System.in);
	String employeeConfirm;

	System.out.println();
	System.out.println("Employees, Please Check if all returned items are valid");
	System.out.println("Type Valid if all items are valid, Other key if any errors");
	employeeConfirm = myObj.nextLine();

	if(employeeConfirm.equals("Valid")){
		System.out.println();
		System.out.println("Thank You for confirming.");
		System.out.println("The system will now complete repayment to the user.");
		finalGreet();
	}

	else{
		System.out.println();
		System.out.println("Please explain the errors to the customer.");
		System.out.println("If needed have them restart the Returns System.");
		finalGreet();
	}
}
//Greeting-- 
	//This was written to indictate that the program has finished running and will exit 
public static void finalGreet(){
	System.out.println();
	System.out.println("Thank You For Using the Returns System!");
}

}


