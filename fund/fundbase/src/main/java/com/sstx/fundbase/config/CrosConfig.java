package com.sstx.fundbase.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.*;

@Configuration
public class CrosConfig extends WebMvcConfigurationSupport {
    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/**")      //添加映射路径，“/**”表示对所有的路径实行全局跨域访问权限的设置
//                .allowedOrigins("*")            //开放哪些ip、端口、域名的访问权限
                .allowedMethods( "GET", "POST", "PUT", "OPTIONS", "DELETE")        //开放哪些Http方法，允许跨域访问
                .allowCredentials(true)         //是否允许发送Cookie信息
                .maxAge(3600)
                .allowedOriginPatterns("*")
                .allowedHeaders("*");            //允许HTTP请求中的携带哪些Header信息
    }

}
