"use strict";
var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
exports.Guest = exports.Admin = exports.User = void 0;
var User = /** @class */ (function () {
    function User() {
    }
    Object.defineProperty(User.prototype, "fullName", {
        get: function () {
            return "".concat(this.fName, " ").concat(this.lName);
        },
        enumerable: false,
        configurable: true
    });
    User.prototype.emailVerify = function (email) {
        if (email == this.email) {
            return "Login Successful. WelCome!!";
        }
        else {
            return "Incorrect mail address. Try Again!!!";
        }
    };
    return User;
}());
exports.User = User;
// EXTEND
var Admin = /** @class */ (function (_super) {
    __extends(Admin, _super);
    function Admin(fName, lName, email) {
        var _this = _super.call(this) || this;
        _this.fName = fName;
        _this.lName = lName;
        _this.email = email;
        return _this;
    }
    return Admin;
}(User));
exports.Admin = Admin;
// matching the shape of parent User class. IMPLEMENT
var Guest = /** @class */ (function () {
    function Guest(fName, lName, email) {
        this.fName = fName;
        this.lName = lName;
        this.email = email;
    }
    Object.defineProperty(Guest.prototype, "fullName", {
        get: function () {
            return "".concat(this.lName, " ").concat(this.fName);
        },
        enumerable: false,
        configurable: true
    });
    Guest.prototype.emailVerify = function (email) {
        if (email == this.email) {
            return "Login Successful. WelCome!!";
        }
        else {
            return "Incorrect mail address. Try Again!!!";
        }
    };
    return Guest;
}());
exports.Guest = Guest;
var user1 = new Admin('Admin', 'Davis', 'DavisAdmin@gmail.com');
console.log(user1.fullName);
console.log(user1.emailVerify('davcxidb@gmail.com'));
var user2 = new Guest('Sami', 'Rane', 'sami@gmail.com');
console.log(user2.fullName);
console.log(user2.emailVerify('sami@gmail.com'));
