export class user{
    fName;
    lName;
    email;

    constructor (fName, lName, email) {
        this.fName = fName;
        this.lName = lName;
        this.email = email;
    }

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

const user1 = new user('David', 'Brown', 'davidb@gmail.com');
console.log(user1.fullName);
console.log(user1.emailVerify('davcxidb@gmail.com'))
console.log(user1.emailVerify('davidb@gmail.com'))

