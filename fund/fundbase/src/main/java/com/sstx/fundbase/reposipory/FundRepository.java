package com.sstx.fundbase.reposipory;

import com.sstx.fundbase.entity.Fund;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface FundRepository extends JpaRepository<Fund, Integer> {
    Fund findByCode(String code);
}
