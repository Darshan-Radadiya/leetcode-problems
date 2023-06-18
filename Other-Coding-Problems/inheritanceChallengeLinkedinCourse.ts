export class User{
    fName;
    lName;
    email;

    get fullName(): string {
        return `${this.fName} ${this.lName}`;
    }

    emailVerify(email) {
        if (email == this.email) {
            return `Login Successful. WelCome!!`;
        }
        else {
            return `Incorrect mail address. Try Again!!!`
        }
    }
}

// EXTEND its Child
export class Admin extends User {
    constructor(fName, lName, email){
        super();
        this.fName = fName;
        this.lName = lName;
        this.email = email;
    }
}

// matching the SHAPE (not child) of parent User class. IMPLEMENT
export class Guest implements User {
    fName;
    lName;
    email;

    constructor(fName, lName, email) {
        this.fName = fName;
        this.lName = lName;
        this.email = email;
    }

    get fullName(): string {
        return `${this.lName} ${this.fName}`;
    }

    emailVerify(email) {
        if (email == this.email) {
            return `Login Successful. WelCome!!`;
        }
        else {
            return `Incorrect mail address. Try Again!!!`
        }
    }
}


const user1 = new Admin('Admin', 'Davis', 'DavisAdmin@gmail.com');
console.log(user1.fullName);
console.log(user1.emailVerify('davcxidb@gmail.com'))

const user2 = new Guest('Sami', 'Rane', 'sami@gmail.com');
console.log(user2.fullName);
console.log(user2.emailVerify('sami@gmail.com'))

