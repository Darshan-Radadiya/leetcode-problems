"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.user = void 0;
var user = /** @class */ (function () {
    function user(fName, lName, email) {
        this.fName = fName;
        this.lName = lName;
        this.email = email;
    }
    Object.defineProperty(user.prototype, "fullName", {
        get: function () {
            return "".concat(this.fName, " ").concat(this.lName);
        },
        enumerable: false,
        configurable: true
    });
    user.prototype.emailVerify = function (email) {
        if (email == this.email) {
            return "Login Successful. WelCome!!";
        }
        else {
            return "Incorrect mail address. Try Again!!!";
        }
    };
    return user;
}());
exports.user = user;
var user1 = new user('David', 'Brown', 'davidb@gmail.com');
console.log(user1.fullName);
console.log(user1.emailVerify('davcxidb@gmail.com'));
console.log(user1.emailVerify('davidb@gmail.com'));
