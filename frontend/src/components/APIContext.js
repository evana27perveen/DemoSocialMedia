import React from "react";

export class APIContext {
    static LoginMethod(body){
        return fetch(`http://127.0.0.1:8000/auth/token/`,{
            method:'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body:JSON.stringify(body)
        }).then(resp => resp.json())
    }

    static LogoutMethod(token) {
        return fetch(`http://127.0.0.1:8000/auth/logout/`,{
            method:'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + {token}
            },
        }).then(resp => resp.json())
    }

    static RegisterNewUser(body_){
        return fetch(`http://127.0.0.1:8000/auth/register/`, {
            method:'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body:JSON.stringify({
                'name': body_['name'],
                'email': body_['email'],
                'password': body_['password1'],
                'password2': body_['password2'],
            })
        }).then(resp => resp.json())
    }
}

export default APIContext