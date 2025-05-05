package com.rewanshicodes.hello;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class HelloController {

    @RequestMapping("/hello")
    public String hello(){
        return "whatever way it goes, it's going to end with me WINNING, CICD DONE SUCCESSFULLY";
    }
    
}
