package com.sstx.fundbase.controller;

import com.sstx.fundbase.entity.Fund;
import com.sstx.fundbase.reposipory.FundRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/fund")
public class FundController {

    @Autowired
    private FundRepository fundRepository;

    @GetMapping("/findAll")
    public List<Fund> findAll(){
        return fundRepository.findAll();
    }
}
