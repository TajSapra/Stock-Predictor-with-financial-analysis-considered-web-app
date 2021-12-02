const express=require("express");
const path = require('path')
const request=require('request')
const cookiep=require('cookie-parser');
const db=require('./config/mongoose')
const googlestrat =require('./config/passport-google')
const passport = require('passport');
const flashm = require('./config/middleware');
const needle=require('needle')
const session=require('express-session')
const expresslayout=require('express-ejs-layouts')
const app=express();
const port= 3000;
const auth_controller=require('./Controllers/authcontroller')
const home_controller=require('./Controllers/homecontroller')
const predict_controller = require("./Controllers/predictcontroller")
const {PythonShell}=require('python-shell')
const profile_controller = require("./Controllers/profilecontroller")
const token=require('./tokens/tokens')
const flash = require('connect-flash');
const MongoStore = require('connect-mongo');
const { type } = require("os");
const tokens = require("./tokens/tokens");
// app.use(expresslayout)
app.use(cookiep())
var python_run=0
if(python_run==0){
    PythonShell.run("./python_scripts/connect_to_database_Create_data.py",null,function(err,results){
        console.log(results)
        console.log("Python done")
        if(err){
            console.log(err)
        }
    })
    python_run=1
}
app.use(express.static('assets'))
app.use(express.urlencoded());         
app.set('view engine','ejs');
app.set('views',path.join(__dirname,'views'))
app.use(session({
    name:'loginsessions',
    secret:'7237279abaca1981beee2bc5ca804aae',
    cookie: { maxAge: 3600*1000*1000 }, 
    resave: false, 
    saveUninitialized: false,
    store: MongoStore.create({mongoUrl:tokens.mongouri})
})); 
app.use(passport.initialize())
app.use(passport.session())
app.get('/login/oauth/google/', passport.authenticate('google',{scope:['profile','email'] }))
app.get('/login/outh/google/callback', passport.authenticate('google', {failureRedirect:'/auth'}), function(req,res){
    return res.redirect('/profile')
})
app.get("/", home_controller.home);
app.get("/auth/", auth_controller.options)
app.post("/auth/check_account", auth_controller.checkaccount)
app.post("/auth/create_account", auth_controller.createnewaccount)
app.get("/auth/logout", auth_controller.logout)
app.get("/admi/killpython", async function(req,res){
    if(req.email==token.emailid){///your admin email id
        child.kill();
        python_run=0
    }
    return res.redirect('/')
})
app.get("/prediction/everything", predict_controller.everything)
app.get("/prediction/prices", predict_controller.prices)
app.get("/prediction/reviews", predict_controller.reviews)
app.get("/profile", profile_controller.profile_page)
app.listen(port, function(err){
    if(err){
        console.error("error on loading server" ,err)
    }
    else{
        console.log(`working on port: ${port}`);
    }
})
