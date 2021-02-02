package com.sstx.fundbase.entity;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.Table;

@Entity
@Data
@AllArgsConstructor
@NoArgsConstructor
public class Fund {
    @Id
    private String id;
    private String name;
    private String code;
    private String dwjz;
    private String rzzl;
    private String jyz;
    private String jyy;
    private String jsy;
    private String jly;
    private String jyn;
    private String jln;
    private String jsn;
    private String jnl;
    private String cll;
    private String sxf;
}
