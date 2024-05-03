
<a href="https://rapidfort.com?utm_source=github&utm_medium=ci_rf_link&utm_campaign=sep_01_sprint&utm_term=ci_main_landing&utm_content=main_landing_logo">
<img src="/contrib/github_logo.png" alt="RapidFort" width="200" />
</a>

<h1> community-images </h1>


[![RF Hardened][rf-h-badge]][rf-link-hardened-badge]
[![Dockerhub][dh-rf-badge]][dh-rf]
[![Slack][slack-badge]][slack-link]
[![License][license-badge]][license]
[![FOSSA Status][fossa-badge]][fossa-link]
[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/6087/badge)](https://bestpractices.coreinfrastructure.org/projects/6087)
[![CodeQL](https://github.com/rapidfort/community-images/actions/workflows/codeql.yml/badge.svg)](https://github.com/rapidfort/community-images/actions/workflows/codeql.yml)


[Getting started](#getting-started) ·
[Supported containers](#supported-containers) ·
[Contributing](CONTRIBUTING.md) ·
[Build Process](#how-community-images-are-built) ·
[Additional resources](#additional-resources)

**RapidFort is a solution for building secure, optimized Docker containers.**

Every day, we scan the most popular Docker Hub container images and remove unused code. Then we publish the results to share with you.

Our container optimization process reduces the software attack surface and the chance of a vulnerability exploit.

Stop downloading container images with thousands of vulnerabilities. Start using secure containers with minimized attack surfaces.


## Getting Started

![Demo][demo]

[RapidFort][rf-link-getting-started] scans your Docker containers for vulnerabilities and looks for unused components that can be removed.

<h2 id="supported-containers">What containers are supported?</h2>

We’ve optimized and hardened some of the most popular container images on Docker Hub and are making them available to the community.

| Repository                        | View Report                                   | RapidFort Image                     | Pull Count |
|-----------------------------------| ------------------------------------------     | ------------------------------- | ------------------------------- |
| [MariaDB][ mariadb-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fmariadb?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=mariadb&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/mariadb"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 381,885 </b> |
| [PostgreSQL][ postgresql-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fpostgresql?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=postgresql&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/postgresql"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 293,613 </b> |
| [PostgreSQL Official][ postgresql-official-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Flibrary%2Fpostgres?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=postgresql-official&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/postgresql-official"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 203,995 </b> |
| [MongoDB®][ mongodb-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fmongodb?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=mongodb&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/mongodb"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 175,043 </b> |
| [Redis™ Cluster][ redis-cluster-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fredis-cluster?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=redis-cluster&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/redis-cluster"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 174,675 </b> |
| [Redis™][ redis-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fredis?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=redis&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/redis"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 159,270 </b> |
| [MySQL][ mysql-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fmysql?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=mysql&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/mysql"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 149,569 </b> |
| [MongoDB® Official][ mongodb-official-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Flibrary%2Fmongo?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=mongodb-official&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/mongodb-official"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 148,488 </b> |
| [Envoy][ envoy-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fenvoy?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=envoy&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/envoy"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 130,586 </b> |
| [NGINX IronBank][ nginx-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fnginx%2Fnginx?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=nginx-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/nginx-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 127,895 </b> |
| [Microsoft SQL Server 2019][ microsoft-sql-server-2019-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fmicrosoft%2Fmicrosoft%2Fmicrosoft-sql-server-2019-rhel8?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=microsoft-sql-server-2019-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/microsoft-sql-server-2019-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 123,423 </b> |
| [NGINX][ nginx-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fnginx?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=nginx&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/nginx"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 121,999 </b> |
| [Consul IronBank][ consul-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fhashicorp%2Fconsul?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=consul-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/consul-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 120,704 </b> |
| [Redis™ IronBank][ redis-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fredis%2Fredis6?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=redis-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/redis6-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 113,525 </b> |
| [Etcd][ etcd-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fetcd?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=etcd&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/etcd"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 109,300 </b> |
| [MongoDB® IronBank][ mongodb-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fmongodb%2Fmongodb?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=mongodb-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/mongodb-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 107,253 </b> |
| [PostgreSQL IronBank][ postgresql-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fpostgres%2Fpostgresql12?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=postgresql-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/postgresql12-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 106,598 </b> |
| [HAProxy Official][ haproxy-official-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Flibrary%2Fhaproxy?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=haproxy-official&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/haproxy-official"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 103,779 </b> |
| [Apache][ apache-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fapache?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=apache&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/apache"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 103,272 </b> |
| [Grafana Oncall][ oncall-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fgrafana%2Foncall?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=oncall&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/oncall"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 98,181 </b> |
| [Zookeeper][ zookeeper-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fzookeeper?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=zookeeper&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/zookeeper"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 97,305 </b> |
| [Redis™ Official][ redis-official-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Flibrary%2Fredis?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=redis-official&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/redis-official"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 93,799 </b> |
| [MySQL IronBank][ mysql-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fmysql%2Fmysql8?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=mysql-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/mysql8-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 92,923 </b> |
| [RabbitMQ][ rabbitmq-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Frabbitmq?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=rabbitmq&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/rabbitmq"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 91,650 </b> |
| [MariaDB IronBank][ mariadb-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fmariadb%2Fmariadb?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=mariadb-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/mariadb-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 87,448 </b> |
| [Zookeeper IronBank][ zookeeper-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fapache%2Fzookeeper?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=zookeeper-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/zookeeper-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 81,924 </b> |
| [Consul Official][ consul-official-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fhashicorp%2Fconsul?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=consul-official&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/consul-official"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 80,936 </b> |
| [Fluentd][ fluentd-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Ffluentd?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=fluentd&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/fluentd"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 80,861 </b> |
| [InfluxDB™][ influxdb-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Finfluxdb?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=influxdb&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/influxdb"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 80,594 </b> |
| [Kong][ kong-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Flibrary%2Fkong?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=kong&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/kong"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 70,669 </b> |
| [Apache Airflow Scheduler][ airflow-scheduler-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fairflow-scheduler?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=airflow-scheduler&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/airflow-scheduler"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 70,470 </b> |
| [Prometheus][ prometheus-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fprometheus?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=prometheus&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/prometheus"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 70,261 </b> |
| [HAProxy IronBank][ haproxy-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fhaproxy%2Fhaproxy24?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=haproxy-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/haproxy24-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 66,417 </b> |
| [Zookeeper Official][ zookeeper-official-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Flibrary%2Fzookeeper?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=zookeeper-official&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/zookeeper-official"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 65,846 </b> |
| [Cassandra Official][ cassandra-official-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Flibrary%2Fcassandra?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=cassandra-official&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/cassandra-official"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 65,664 </b> |
| [Apache Airflow Worker][ airflow-worker-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fairflow-worker?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=airflow-worker&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/airflow-worker"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 65,167 </b> |
| [Apache Official][ apache-official-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Flibrary%2Fhttpd?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=apache-official&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/apache-official"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 64,540 </b> |
| [Apache IronBank][ apache-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fapache%2Fapache2?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=apache-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/apache2-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 63,947 </b> |
| [Ghost][ ghost-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fghost?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=ghost&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/ghost"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 63,917 </b> |
| [NATS][ nats-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fnats?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=nats&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/nats"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 62,143 </b> |
| [NGINX Official][ nginx-official-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Flibrary%2Fnginx?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=nginx-official&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/nginx-official"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 61,274 </b> |
| [Consul][ consul-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fconsul?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=consul&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/consul"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 59,774 </b> |
| [Wordpress][ wordpress-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fwordpress?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=wordpress&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/wordpress"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 57,549 </b> |
| [Fluent-Bit][ fluent-bit-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Ffluent-bit?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=fluent-bit&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/fluent-bit"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 56,588 </b> |
| [HAProxy][ haproxy-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fhaproxy?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=haproxy&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/haproxy"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 53,070 </b> |
| [Apache Airflow][ airflow-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fairflow?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=airflow&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/airflow"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 52,735 </b> |
| [Memcached IronBank][ memcached-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fmemcached%2Fmemcached?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=memcached-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/memcached-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 52,560 </b> |
| [MySQL Official][ mysql-official-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Flibrary%2Fmysql?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=mysql-official&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/mysql-official"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 51,896 </b> |
| [Couchdb Database Server Official][ couchdb-official-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Flibrary%2Fcouchdb?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=couchdb-official&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/couchdb-official"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 50,388 </b> |
| [Memcached][ memcached-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fmemcached?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=memcached&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/memcached"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 48,969 </b> |
| [Envoy Official][ envoy-official-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fenvoyproxy%2Fenvoy?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=envoy-official&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/envoy-official"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 46,103 </b> |
| [Curl][ curl-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fcurlimages%2Fcurl?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=curl&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/curl"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 44,697 </b> |
| [Fluentd IronBank][ fluentd-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Ffluentd%2Ffluentd?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=fluentd-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/fluentd-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 44,575 </b> |
| [TRAEFIK][ traefik-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Flibrary%2Ftraefik?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=traefik&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/traefik"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 43,140 </b> |
| [Couchdb Database Server IronBank][ couchdb-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fapache%2Fcouchdb_3?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=couchdb-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/couchdb_3-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 43,100 </b> |
| [ElasticSearch][ elasticsearch-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Felasticsearch?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=elasticsearch&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/elasticsearch"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 42,300 </b> |
| [Fluentd Official][ fluentd-official-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Flibrary%2Ffluentd?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=fluentd-official&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/fluentd-official"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 41,927 </b> |
| [Memcached Official][ memcached-official-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Flibrary%2Fmemcached?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=memcached-official&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/memcached-official"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 40,779 </b> |
| [MariaDB Official][ mariadb-official-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Flibrary%2Fmariadb?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=mariadb-official&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/mariadb-official"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 39,459 </b> |
| [NATS Official][ nats-official-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Flibrary%2Fnats?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=nats-official&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/nats-official"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 34,712 </b> |
| [YOURLS][ yourls-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Flibrary%2Fyourls?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=yourls&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/yourls"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 30,969 </b> |
| [Couchdb Database Server][ couchdb-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fcouchdb?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=couchdb&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/couchdb"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 30,087 </b> |
| [Vault][ vault-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Flibrary%2Fvault?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=vault&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/vault"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 28,204 </b> |
| [Etcd Ironbank][ etcd-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fetcd%2Fetcd?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=etcd-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/etcd-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 27,529 </b> |
| [NATS Ironbank][ nats-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fsynadia%2Fnats-server?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=nats-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/nats-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 25,665 </b> |
| [ElasticSearch Official][ elasticsearch-official-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Flibrary%2Felasticsearch?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=elasticsearch-official&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/elasticsearch-official"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 25,361 </b> |
| [Telegraf][ telegraf-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Ftelegraf?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=telegraf&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/telegraf"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 24,639 </b> |
| [Grafana Ironbank][ grafana-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fgrafana%2Fgrafana?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=grafana-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/grafana-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 18,573 </b> |
| [Wordpress Ironbank][ wordpress-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fwordpress%2Fwordpress?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=wordpress-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/wordpress-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 16,582 </b> |
| [TRAEFIK Ironbank][ traefik-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Ftraefik%2Ftraefik?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=traefik-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/traefik-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 15,505 </b> |
| [Keycloak Official][ keycloak-official-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fkeycloak%2Fkeycloak?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=keycloak-official&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/keycloak-official"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 15,346 </b> |
| [Prometheus Ironbank][ prometheus-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fprometheus%2Fprometheus?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=prometheus-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/prometheus-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 14,896 </b> |
| [Apache Airflow Ironbank][ airflow-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fapache%2Fairflow%2Fairflow?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=airflow-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/airflow-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 12,894 </b> |
| [Fluent-Bit Ironbank][ fluent-bit-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Ffluent%2Ffluent-bit?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=fluent-bit-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/fluent-bit-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 10,692 </b> |
| [Apache Nifi IronBank][ nifi-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fapache%2Fnifi?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=nifi-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/nifi-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 9,065 </b> |
| [Node Exporter][ node-exporter-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fnode-exporter?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=node-exporter&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/node-exporter"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 8,839 </b> |
| [Node-Exporter IronBank][ node-exporter-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fprometheus%2Fnode-exporter?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=node-exporter-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/node-exporter-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 8,256 </b> |
| [Moodle Ironbank][ moodle-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fmoodle?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=moodle-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/moodle-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 5,255 </b> |
| [Argo CD Quay][ argocd-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/quay.io%2Fargoproj%2Fargocd?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=argocd&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/argocd"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 4,072 </b> |
| [PAUSE IronBank][ pause-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fpause%2Fpause?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=pause-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/pause-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 3,402 </b> |
| [Vault Ironbank][ vault-k8s-ib-github-link]| <a href="https://frontrow.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fhashicorp%2Fvault%2Fvault-k8s?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=vault-k8s-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/vault-k8s-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 1,440 </b> |
| [Logstash Ironbank][ logstash-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Felastic%2Flogstash%2Flogstash?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=logstash-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/logstash-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 1,096 </b> |
| [Terraform IronBank][ terraform-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fhashicorp%2Fterraform%2F1.7?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=terraform-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/terraform-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 939 </b> |
| [Kibana Iron-Bank][ kibana-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Felastic%2Fkibana%2Fkibana?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=kibana-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/kibana-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 639 </b> |
| [Apacha Kafka Ironbank][ kafka-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fbitnami%2Fkafka?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=kafka-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/kafka-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 622 </b> |
| [Filebeat Ironbank][ filebeat-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Felastic%2Fbeats%2Ffilebeat?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=filebeat-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/filebeat-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 487 </b> |
| [Metricbeat Iron-Bank][ metricbeat-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Felastic%2Fbeats%2Fmetricbeat?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=metricbeat-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/metricbeat-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 468 </b> |
| [Ansible IronBank][ ansible-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fansible%2Fansible?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=ansible-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/ansible-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 425 </b> |
| [Helm Chart Testing Ironbank][ chart-testing-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fhelm%2Fchart-testing?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=chart-testing-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/chart-testing-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 263 </b> |
| [Tika Iron Bank][ tika-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fapache%2Ftika?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=tika-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/tika-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 225 </b> |

<h2 id="supported-iron-bank-containers">What IronBank containers are supported?</h2>

We’ve optimized and hardened some of the most popular container images on IronBank and are making them available to the community.

| Repository                        | View Report                                   | RapidFort Image                     | Pull Count |
|-----------------------------------| ------------------------------------------     | ------------------------------- | ------------------------------- |
| [NGINX IronBank][ nginx-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fnginx%2Fnginx?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=nginx-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/nginx-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 127,895 </b> |
| [Microsoft SQL Server 2019][ microsoft-sql-server-2019-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fmicrosoft%2Fmicrosoft%2Fmicrosoft-sql-server-2019-rhel8?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=microsoft-sql-server-2019-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/microsoft-sql-server-2019-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 123,423 </b> |
| [Consul IronBank][ consul-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fhashicorp%2Fconsul?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=consul-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/consul-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 120,704 </b> |
| [Redis™ IronBank][ redis-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fredis%2Fredis6?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=redis-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/redis6-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 113,525 </b> |
| [MongoDB® IronBank][ mongodb-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fmongodb%2Fmongodb?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=mongodb-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/mongodb-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 107,253 </b> |
| [PostgreSQL IronBank][ postgresql-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fpostgres%2Fpostgresql12?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=postgresql-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/postgresql12-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 106,598 </b> |
| [MySQL IronBank][ mysql-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fmysql%2Fmysql8?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=mysql-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/mysql8-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 92,923 </b> |
| [MariaDB IronBank][ mariadb-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fmariadb%2Fmariadb?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=mariadb-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/mariadb-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 87,448 </b> |
| [Zookeeper IronBank][ zookeeper-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fapache%2Fzookeeper?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=zookeeper-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/zookeeper-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 81,924 </b> |
| [HAProxy IronBank][ haproxy-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fhaproxy%2Fhaproxy24?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=haproxy-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/haproxy24-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 66,417 </b> |
| [Apache IronBank][ apache-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fapache%2Fapache2?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=apache-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/apache2-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 63,947 </b> |
| [Memcached IronBank][ memcached-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fmemcached%2Fmemcached?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=memcached-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/memcached-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 52,560 </b> |
| [Fluentd IronBank][ fluentd-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Ffluentd%2Ffluentd?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=fluentd-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/fluentd-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 44,575 </b> |
| [Couchdb Database Server IronBank][ couchdb-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fapache%2Fcouchdb_3?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=couchdb-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/couchdb_3-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 43,100 </b> |
| [Etcd Ironbank][ etcd-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fetcd%2Fetcd?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=etcd-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/etcd-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 27,529 </b> |
| [NATS Ironbank][ nats-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fsynadia%2Fnats-server?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=nats-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/nats-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 25,665 </b> |
| [Grafana Ironbank][ grafana-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fgrafana%2Fgrafana?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=grafana-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/grafana-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 18,573 </b> |
| [Wordpress Ironbank][ wordpress-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fwordpress%2Fwordpress?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=wordpress-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/wordpress-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 16,582 </b> |
| [TRAEFIK Ironbank][ traefik-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Ftraefik%2Ftraefik?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=traefik-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/traefik-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 15,505 </b> |
| [Prometheus Ironbank][ prometheus-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fprometheus%2Fprometheus?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=prometheus-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/prometheus-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 14,896 </b> |
| [Apache Airflow Ironbank][ airflow-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fapache%2Fairflow%2Fairflow?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=airflow-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/airflow-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 12,894 </b> |
| [Fluent-Bit Ironbank][ fluent-bit-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Ffluent%2Ffluent-bit?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=fluent-bit-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/fluent-bit-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 10,692 </b> |
| [Apache Nifi IronBank][ nifi-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fapache%2Fnifi?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=nifi-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/nifi-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 9,065 </b> |
| [Node-Exporter IronBank][ node-exporter-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fprometheus%2Fnode-exporter?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=node-exporter-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/node-exporter-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 8,256 </b> |
| [Moodle Ironbank][ moodle-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fmoodle?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=moodle-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/moodle-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 5,255 </b> |
| [PAUSE IronBank][ pause-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fpause%2Fpause?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=pause-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/pause-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 3,402 </b> |
| [Vault Ironbank][ vault-k8s-ib-github-link]| <a href="https://frontrow.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fhashicorp%2Fvault%2Fvault-k8s?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=vault-k8s-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/vault-k8s-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 1,440 </b> |
| [Logstash Ironbank][ logstash-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Felastic%2Flogstash%2Flogstash?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=logstash-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/logstash-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 1,096 </b> |
| [Terraform IronBank][ terraform-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fhashicorp%2Fterraform%2F1.7?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=terraform-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/terraform-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 939 </b> |
| [Kibana Iron-Bank][ kibana-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Felastic%2Fkibana%2Fkibana?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=kibana-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/kibana-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 639 </b> |
| [Apacha Kafka Ironbank][ kafka-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fbitnami%2Fkafka?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=kafka-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/kafka-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 622 </b> |
| [Filebeat Ironbank][ filebeat-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Felastic%2Fbeats%2Ffilebeat?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=filebeat-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/filebeat-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 487 </b> |
| [Metricbeat Iron-Bank][ metricbeat-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Felastic%2Fbeats%2Fmetricbeat?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=metricbeat-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/metricbeat-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 468 </b> |
| [Ansible IronBank][ ansible-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fansible%2Fansible?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=ansible-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/ansible-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 425 </b> |
| [Helm Chart Testing Ironbank][ chart-testing-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fhelm%2Fchart-testing?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=chart-testing-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/chart-testing-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 263 </b> |
| [Tika Iron Bank][ tika-ib-github-link]| <a href="https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fapache%2Ftika?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=tika-ib&utm_content=landing_get_full_report_button"> <img src="/contrib/github_button_3.svg" alt="View Report" height="25" /> </a> | <a href="https://hub.docker.com/r/rapidfort/tika-ib"> <img src="/contrib/view_on_dockerhub.svg" alt="View on Dockerhub" height="25" /> </a> | <b> 225 </b> |

### How to use Community Images

Here’s what you can do with Community Images.

```sh
# Docker
$ docker run --name redis -e ALLOW_EMPTY_PASSWORD=yes rapidfort/redis:latest

# Docker compose
$ docker-compose up -d

# Kubernetes Helm
$ helm repo add bitnami https://charts.bitnami.com/bitnami

# install redis, just replace repository with RapidFort registry
$ helm install my-redis bitnami/redis --set image.repository=rapidfort/redis

# install postgresql
$ helm install my-postgresql bitnami/postgresql --set image.repository=rapidfort/postgresql

```
## How Community Images are Built

Source images are run through an optimization process that identifies and removes unused components from the image.
You can contribute to this project by adding new images, improving coverage scripts, and adding regression and benchmark tests.

![Demo](contrib/workflow.png)

## Need support

<a href="https://join.slack.com/t/rapidfortcommunity/shared_invite/zt-1g3wy28lv-DaeGexTQ5IjfpbmYW7Rm_Q">
<img src="/contrib/github_banner.png" alt="RapidFort Community Slack" width="600" />
</a>


## Stargazers over time

[![Stargazers over time](https://starchart.cc/rapidfort/community-images.svg)](https://starchart.cc/rapidfort/community-images)

## 🌟 Star this project

[![](https://user-images.githubusercontent.com/48997634/174794647-0c851917-e5c9-4fb9-bf88-b61d89dc2f4f.gif)](https://github.com/rapidfort/community-images/stargazers)

### [⏫⭐️ Scroll to the star button](#start-of-content)

If you believe this project has potential, feel free to **star this repo** just like many [amazing people](https://github.com/rapidfort/community-images/stargazers)
have.

## Additional Resources

[![RapidFort](https://raw.githubusercontent.com/rapidfort/community-images/main/contrib/github_logo_footer.png)][rf-link-main-landing-footer-logo]


Learn more about container optimization at [RapidFort.com][rf-link-additonal-resource].


[rf-link-hardened-badge]: https://rapidfort.com?utm_source=github&utm_medium=ci_rf_link&utm_campaign=sep_01_sprint&utm_term=ci_main_landing&utm_content=rf_hardened_badge
[rf-link-getting-started]: https://rapidfort.com?utm_source=github&utm_medium=ci_rf_link&utm_campaign=sep_01_sprint&utm_term=ci_main_landing&utm_content=getting_started_link
[rf-link-additonal-resource]: https://rapidfort.com?utm_source=github&utm_medium=ci_rf_link&utm_campaign=sep_01_sprint&utm_term=ci_main_landing&utm_content=additonal_resource
[rf-link-main-landing-footer-logo]: https://rapidfort.com?utm_source=github&utm_medium=ci_rf_link&utm_campaign=sep_01_sprint&utm_term=ci_main_landing&utm_content=main_landing_footer_logo

[rf-h-badge]: https://img.shields.io/static/v1?label=RapidFort&labelColor=333F48&message=hardened&color=50B4C4&logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACcAAAAkCAYAAAAKNyObAAAACXBIWXMAACE4AAAhOAFFljFgAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAHvSURBVHgB7ZjvTcMwEMUvEgNkhNuAjOAR2IAyQbsB2YAyQbsBYoKwQdjA3aAjHA514Xq1Hf9r6QeeFKVJ3tkv+cWOVYCAiKg124b82gZqe0+NNlsHJbLBxthg1o+RASetIEdTJxnBRvtUMCHgM6TIBtMZwY7SiQFfrhUsN+Ao/TJYR3WC5QY88/Nge6oXLBRwO+P/GcnNMZzZteBR0zQfogM0O4Q47Uz9TtSrUIHs71+paugw16Dn+qt5xJ/TD4viEcrE25tepaXPaHxP350GXtD10WwHQWjQxKhl7YUGRg/MuPaY9vxuzPFA+RpEW9rj0yCMbcCsmG9B+Xpk7YRo4RnjQEEttBiBtAefyI23BtoYpBrmRO6ZX0EZWo60c1yfaGBMOKRzdKVocYZO/NpuMss7E9cHitcc0gFS5Qig2LUUtCGkmmJwOsJJvLlokdWtfMFzAvLGctCOooYPtg2USoRQ7HwM2hXzIzuvKQenIxzHm4oWmZ9TKF1AnAR8sI2moB093nKcjoBvtnHFzoXQ8qeMDGcLtUW/i4NYtJ3jJhRcSnRYHMSg1Q5PD5cWHT4/ih0vIpDOf9QrhZtQLsWxlILT8AjXEol/iQRaiVTBX4pO57D6U0WJBFoFtyaLtuqLfwf19G62e7hFWbQKKuoLYovGDo9dW28AAAAASUVORK5CYII=

[fossa-badge]: https://app.fossa.com/api/projects/git%2Bgithub.com%2Frapidfort%2Fcommunity-images.svg?type=shield
[fossa-link]: https://app.fossa.com/projects/git%2Bgithub.com%2Frapidfort%2Fcommunity-images?ref=badge_shield

[dh-rf-badge]: https://img.shields.io/badge/dockerhub-images-important.svg?logo=Docker
[dh-rf]: https://hub.docker.com/u/rapidfort
[license-badge]: https://img.shields.io/github/license/rapidfort/community-images?color=lightgray&style=flat-square
[license]: https://github.com/rapidfort/community-images/blob/main/LICENSE
[demo]: contrib/demo.gif

[slack-badge]: https://img.shields.io/static/v1?label=Join&message=slack&logo=slack&logoColor=E01E5A&color=4A154B
[slack-link]: https://join.slack.com/t/rapidfortcommunity/shared_invite/zt-1g3wy28lv-DaeGexTQ5IjfpbmYW7Rm_Q

[ image-ft-badge]: https://github.com/rapidfort/community-images/actions/workflows/image_run_v3.yml/badge.svg
[ image-ft-badge-link]: https://github.com/rapidfort/community-images/actions/workflows/image_run_v3.yml


[airflow-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/airflow/airflow/bitnami
[airflow-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/airflow?logo=docker&logoColor=white
[airflow-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fairflow?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=airflow&utm_content=landing_view_report

[airflow-ib-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/airflow/airflow/ironbank
[airflow-ib-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/airflow-ib?logo=docker&logoColor=white
[airflow-ib-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fapache%2Fairflow%2Fairflow?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=airflow-ib&utm_content=landing_view_report

[airflow-scheduler-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/airflow/airflow-scheduler/bitnami
[airflow-scheduler-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/airflow-scheduler?logo=docker&logoColor=white
[airflow-scheduler-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fairflow-scheduler?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=airflow-scheduler&utm_content=landing_view_report

[airflow-worker-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/airflow/airflow-worker/bitnami
[airflow-worker-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/airflow-worker?logo=docker&logoColor=white
[airflow-worker-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fairflow-worker?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=airflow-worker&utm_content=landing_view_report

[ansible-ib-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/ansible/ironbank
[ansible-ib-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/ansible-ib?logo=docker&logoColor=white
[ansible-ib-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fansible%2Fansible?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=ansible-ib&utm_content=landing_view_report

[apache-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/apache/bitnami
[apache-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/apache?logo=docker&logoColor=white
[apache-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fapache?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=apache&utm_content=landing_view_report

[apache-ib-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/apache/ironbank
[apache-ib-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/apache2-ib?logo=docker&logoColor=white
[apache-ib-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fapache%2Fapache2?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=apache-ib&utm_content=landing_view_report

[apache-official-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/apache/official
[apache-official-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/apache-official?logo=docker&logoColor=white
[apache-official-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Flibrary%2Fhttpd?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=apache-official&utm_content=landing_view_report

[argocd-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/argocd/quay
[argocd-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/argocd?logo=docker&logoColor=white
[argocd-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/quay.io%2Fargoproj%2Fargocd?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=argocd&utm_content=landing_view_report

[cassandra-official-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/cassandra/official
[cassandra-official-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/cassandra-official?logo=docker&logoColor=white
[cassandra-official-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Flibrary%2Fcassandra?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=cassandra-official&utm_content=landing_view_report

[chart-testing-ib-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/chart-testing/ironbank
[chart-testing-ib-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/chart-testing-ib?logo=docker&logoColor=white
[chart-testing-ib-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fhelm%2Fchart-testing?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=chart-testing-ib&utm_content=landing_view_report

[consul-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/consul/bitnami
[consul-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/consul?logo=docker&logoColor=white
[consul-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fconsul?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=consul&utm_content=landing_view_report

[consul-ib-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/consul/ironbank
[consul-ib-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/consul-ib?logo=docker&logoColor=white
[consul-ib-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fhashicorp%2Fconsul?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=consul-ib&utm_content=landing_view_report

[consul-official-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/consul/official
[consul-official-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/consul-official?logo=docker&logoColor=white
[consul-official-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fhashicorp%2Fconsul?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=consul-official&utm_content=landing_view_report

[couchdb-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/couchdb/bitnami
[couchdb-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/couchdb?logo=docker&logoColor=white
[couchdb-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fcouchdb?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=couchdb&utm_content=landing_view_report

[couchdb-ib-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/couchdb/ironbank
[couchdb-ib-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/couchdb_3-ib?logo=docker&logoColor=white
[couchdb-ib-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fapache%2Fcouchdb_3?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=couchdb-ib&utm_content=landing_view_report

[couchdb-official-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/couchdb/official
[couchdb-official-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/couchdb-official?logo=docker&logoColor=white
[couchdb-official-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Flibrary%2Fcouchdb?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=couchdb-official&utm_content=landing_view_report

[curl-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/curl/curlimages
[curl-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/curl?logo=docker&logoColor=white
[curl-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fcurlimages%2Fcurl?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=curl&utm_content=landing_view_report

[elasticsearch-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/elasticsearch/bitnami
[elasticsearch-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/elasticsearch?logo=docker&logoColor=white
[elasticsearch-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Felasticsearch?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=elasticsearch&utm_content=landing_view_report

[elasticsearch-official-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/elasticsearch/official
[elasticsearch-official-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/elasticsearch-official?logo=docker&logoColor=white
[elasticsearch-official-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Flibrary%2Felasticsearch?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=elasticsearch-official&utm_content=landing_view_report

[envoy-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/envoy/bitnami
[envoy-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/envoy?logo=docker&logoColor=white
[envoy-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fenvoy?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=envoy&utm_content=landing_view_report

[envoy-official-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/envoy/official
[envoy-official-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/envoy-official?logo=docker&logoColor=white
[envoy-official-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fenvoyproxy%2Fenvoy?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=envoy-official&utm_content=landing_view_report

[etcd-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/etcd/bitnami
[etcd-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/etcd?logo=docker&logoColor=white
[etcd-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fetcd?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=etcd&utm_content=landing_view_report

[etcd-ib-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/etcd/ironbank
[etcd-ib-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/etcd-ib?logo=docker&logoColor=white
[etcd-ib-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fetcd%2Fetcd?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=etcd-ib&utm_content=landing_view_report

[filebeat-ib-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/filebeat/ironbank
[filebeat-ib-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/filebeat-ib?logo=docker&logoColor=white
[filebeat-ib-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Felastic%2Fbeats%2Ffilebeat?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=filebeat-ib&utm_content=landing_view_report

[fluent-bit-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/fluent-bit/bitnami
[fluent-bit-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/fluent-bit?logo=docker&logoColor=white
[fluent-bit-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Ffluent-bit?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=fluent-bit&utm_content=landing_view_report

[fluent-bit-ib-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/fluent-bit/ironbank
[fluent-bit-ib-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/fluent-bit-ib?logo=docker&logoColor=white
[fluent-bit-ib-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Ffluent%2Ffluent-bit?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=fluent-bit-ib&utm_content=landing_view_report

[fluentd-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/fluentd/bitnami
[fluentd-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/fluentd?logo=docker&logoColor=white
[fluentd-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Ffluentd?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=fluentd&utm_content=landing_view_report

[fluentd-ib-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/fluentd/ironbank
[fluentd-ib-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/fluentd-ib?logo=docker&logoColor=white
[fluentd-ib-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Ffluentd%2Ffluentd?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=fluentd-ib&utm_content=landing_view_report

[fluentd-official-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/fluentd/official
[fluentd-official-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/fluentd-official?logo=docker&logoColor=white
[fluentd-official-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Flibrary%2Ffluentd?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=fluentd-official&utm_content=landing_view_report

[ghost-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/ghost/bitnami
[ghost-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/ghost?logo=docker&logoColor=white
[ghost-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fghost?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=ghost&utm_content=landing_view_report

[grafana-ib-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/grafana/ironbank
[grafana-ib-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/grafana-ib?logo=docker&logoColor=white
[grafana-ib-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fgrafana%2Fgrafana?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=grafana-ib&utm_content=landing_view_report

[haproxy-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/haproxy/bitnami
[haproxy-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/haproxy?logo=docker&logoColor=white
[haproxy-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fhaproxy?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=haproxy&utm_content=landing_view_report

[haproxy-ib-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/haproxy/ironbank
[haproxy-ib-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/haproxy24-ib?logo=docker&logoColor=white
[haproxy-ib-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fhaproxy%2Fhaproxy24?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=haproxy-ib&utm_content=landing_view_report

[haproxy-official-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/haproxy/official
[haproxy-official-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/haproxy-official?logo=docker&logoColor=white
[haproxy-official-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Flibrary%2Fhaproxy?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=haproxy-official&utm_content=landing_view_report

[influxdb-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/influxdb/bitnami
[influxdb-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/influxdb?logo=docker&logoColor=white
[influxdb-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Finfluxdb?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=influxdb&utm_content=landing_view_report

[kafka-ib-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/kafka/ironbank
[kafka-ib-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/kafka-ib?logo=docker&logoColor=white
[kafka-ib-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fbitnami%2Fkafka?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=kafka-ib&utm_content=landing_view_report

[keycloak-official-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/keycloak/official
[keycloak-official-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/keycloak-official?logo=docker&logoColor=white
[keycloak-official-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fkeycloak%2Fkeycloak?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=keycloak-official&utm_content=landing_view_report

[kibana-ib-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/kibana/ironbank
[kibana-ib-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/kibana-ib?logo=docker&logoColor=white
[kibana-ib-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Felastic%2Fkibana%2Fkibana?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=kibana-ib&utm_content=landing_view_report

[kong-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/kong/official
[kong-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/kong?logo=docker&logoColor=white
[kong-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Flibrary%2Fkong?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=kong&utm_content=landing_view_report

[logstash-ib-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/logstash/ironbank
[logstash-ib-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/logstash-ib?logo=docker&logoColor=white
[logstash-ib-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Felastic%2Flogstash%2Flogstash?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=logstash-ib&utm_content=landing_view_report

[mariadb-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/mariadb/bitnami
[mariadb-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/mariadb?logo=docker&logoColor=white
[mariadb-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fmariadb?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=mariadb&utm_content=landing_view_report

[mariadb-ib-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/mariadb/ironbank
[mariadb-ib-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/mariadb-ib?logo=docker&logoColor=white
[mariadb-ib-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fmariadb%2Fmariadb?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=mariadb-ib&utm_content=landing_view_report

[mariadb-official-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/mariadb/official
[mariadb-official-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/mariadb-official?logo=docker&logoColor=white
[mariadb-official-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Flibrary%2Fmariadb?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=mariadb-official&utm_content=landing_view_report

[memcached-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/memcached/bitnami
[memcached-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/memcached?logo=docker&logoColor=white
[memcached-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fmemcached?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=memcached&utm_content=landing_view_report

[memcached-ib-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/memcached/ironbank
[memcached-ib-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/memcached-ib?logo=docker&logoColor=white
[memcached-ib-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fmemcached%2Fmemcached?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=memcached-ib&utm_content=landing_view_report

[memcached-official-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/memcached/official
[memcached-official-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/memcached-official?logo=docker&logoColor=white
[memcached-official-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Flibrary%2Fmemcached?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=memcached-official&utm_content=landing_view_report

[metricbeat-ib-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/metricbeat/ironbank
[metricbeat-ib-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/metricbeat-ib?logo=docker&logoColor=white
[metricbeat-ib-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Felastic%2Fbeats%2Fmetricbeat?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=metricbeat-ib&utm_content=landing_view_report

[microsoft-sql-server-2019-ib-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/microsoft-sql-server-2019/ironbank
[microsoft-sql-server-2019-ib-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/microsoft-sql-server-2019-ib?logo=docker&logoColor=white
[microsoft-sql-server-2019-ib-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fmicrosoft%2Fmicrosoft%2Fmicrosoft-sql-server-2019-rhel8?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=microsoft-sql-server-2019-ib&utm_content=landing_view_report

[mongodb-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/mongodb/bitnami
[mongodb-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/mongodb?logo=docker&logoColor=white
[mongodb-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fmongodb?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=mongodb&utm_content=landing_view_report

[mongodb-ib-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/mongodb/ironbank
[mongodb-ib-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/mongodb-ib?logo=docker&logoColor=white
[mongodb-ib-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fmongodb%2Fmongodb?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=mongodb-ib&utm_content=landing_view_report

[mongodb-official-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/mongodb/official
[mongodb-official-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/mongodb-official?logo=docker&logoColor=white
[mongodb-official-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Flibrary%2Fmongo?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=mongodb-official&utm_content=landing_view_report

[moodle-ib-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/moodle/ironbank
[moodle-ib-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/moodle-ib?logo=docker&logoColor=white
[moodle-ib-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fmoodle?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=moodle-ib&utm_content=landing_view_report

[mysql-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/mysql/bitnami
[mysql-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/mysql?logo=docker&logoColor=white
[mysql-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fmysql?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=mysql&utm_content=landing_view_report

[mysql-ib-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/mysql/ironbank
[mysql-ib-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/mysql8-ib?logo=docker&logoColor=white
[mysql-ib-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fmysql%2Fmysql8?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=mysql-ib&utm_content=landing_view_report

[mysql-official-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/mysql/official
[mysql-official-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/mysql-official?logo=docker&logoColor=white
[mysql-official-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Flibrary%2Fmysql?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=mysql-official&utm_content=landing_view_report

[nats-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/nats/bitnami
[nats-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/nats?logo=docker&logoColor=white
[nats-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fnats?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=nats&utm_content=landing_view_report

[nats-ib-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/nats/ironbank
[nats-ib-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/nats-ib?logo=docker&logoColor=white
[nats-ib-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fsynadia%2Fnats-server?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=nats-ib&utm_content=landing_view_report

[nats-official-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/nats/official
[nats-official-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/nats-official?logo=docker&logoColor=white
[nats-official-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Flibrary%2Fnats?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=nats-official&utm_content=landing_view_report

[nginx-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/nginx/bitnami
[nginx-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/nginx?logo=docker&logoColor=white
[nginx-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fnginx?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=nginx&utm_content=landing_view_report

[nginx-ib-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/nginx/ironbank
[nginx-ib-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/nginx-ib?logo=docker&logoColor=white
[nginx-ib-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fnginx%2Fnginx?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=nginx-ib&utm_content=landing_view_report

[nginx-official-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/nginx/official
[nginx-official-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/nginx-official?logo=docker&logoColor=white
[nginx-official-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Flibrary%2Fnginx?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=nginx-official&utm_content=landing_view_report

[nifi-ib-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/nifi/ironbank
[nifi-ib-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/nifi-ib?logo=docker&logoColor=white
[nifi-ib-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fapache%2Fnifi?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=nifi-ib&utm_content=landing_view_report

[node-exporter-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/node-exporter/bitnami
[node-exporter-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/node-exporter?logo=docker&logoColor=white
[node-exporter-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fnode-exporter?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=node-exporter&utm_content=landing_view_report

[node-exporter-ib-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/node-exporter/ironbank
[node-exporter-ib-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/node-exporter-ib?logo=docker&logoColor=white
[node-exporter-ib-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fprometheus%2Fnode-exporter?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=node-exporter-ib&utm_content=landing_view_report

[oncall-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/oncall/grafana
[oncall-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/oncall?logo=docker&logoColor=white
[oncall-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fgrafana%2Foncall?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=oncall&utm_content=landing_view_report

[pause-ib-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/pause/ironbank
[pause-ib-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/pause-ib?logo=docker&logoColor=white
[pause-ib-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fpause%2Fpause?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=pause-ib&utm_content=landing_view_report

[postgresql-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/postgresql/bitnami
[postgresql-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/postgresql?logo=docker&logoColor=white
[postgresql-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fpostgresql?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=postgresql&utm_content=landing_view_report

[postgresql-ib-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/postgresql/ironbank
[postgresql-ib-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/postgresql12-ib?logo=docker&logoColor=white
[postgresql-ib-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fpostgres%2Fpostgresql12?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=postgresql-ib&utm_content=landing_view_report

[postgresql-official-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/postgresql/official
[postgresql-official-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/postgresql-official?logo=docker&logoColor=white
[postgresql-official-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Flibrary%2Fpostgres?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=postgresql-official&utm_content=landing_view_report

[prometheus-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/prometheus/bitnami
[prometheus-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/prometheus?logo=docker&logoColor=white
[prometheus-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fprometheus?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=prometheus&utm_content=landing_view_report

[prometheus-ib-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/prometheus/ironbank
[prometheus-ib-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/prometheus-ib?logo=docker&logoColor=white
[prometheus-ib-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fprometheus%2Fprometheus?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=prometheus-ib&utm_content=landing_view_report

[rabbitmq-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/rabbitmq/bitnami
[rabbitmq-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/rabbitmq?logo=docker&logoColor=white
[rabbitmq-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Frabbitmq?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=rabbitmq&utm_content=landing_view_report

[redis-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/redis/bitnami
[redis-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/redis?logo=docker&logoColor=white
[redis-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fredis?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=redis&utm_content=landing_view_report

[redis-cluster-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/redis-cluster/bitnami
[redis-cluster-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/redis-cluster?logo=docker&logoColor=white
[redis-cluster-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fredis-cluster?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=redis-cluster&utm_content=landing_view_report

[redis-ib-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/redis/ironbank
[redis-ib-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/redis6-ib?logo=docker&logoColor=white
[redis-ib-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fredis%2Fredis6?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=redis-ib&utm_content=landing_view_report

[redis-official-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/redis/official
[redis-official-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/redis-official?logo=docker&logoColor=white
[redis-official-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Flibrary%2Fredis?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=redis-official&utm_content=landing_view_report

[telegraf-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/telegraf/bitnami
[telegraf-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/telegraf?logo=docker&logoColor=white
[telegraf-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Ftelegraf?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=telegraf&utm_content=landing_view_report

[terraform-ib-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/terraform/ironbank
[terraform-ib-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/terraform-ib?logo=docker&logoColor=white
[terraform-ib-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fhashicorp%2Fterraform%2F1.7?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=terraform-ib&utm_content=landing_view_report

[tika-ib-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/tika/ironbank
[tika-ib-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/tika-ib?logo=docker&logoColor=white
[tika-ib-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fapache%2Ftika?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=tika-ib&utm_content=landing_view_report

[traefik-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/traefik/traefik
[traefik-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/traefik?logo=docker&logoColor=white
[traefik-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Flibrary%2Ftraefik?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=traefik&utm_content=landing_view_report

[traefik-ib-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/traefik/ironbank
[traefik-ib-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/traefik-ib?logo=docker&logoColor=white
[traefik-ib-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Ftraefik%2Ftraefik?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=traefik-ib&utm_content=landing_view_report

[vault-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/vault/hashicorp
[vault-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/vault?logo=docker&logoColor=white
[vault-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Flibrary%2Fvault?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=vault&utm_content=landing_view_report

[vault-k8s-ib-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/vault-k8s/ironbank
[vault-k8s-ib-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/vault-k8s-ib?logo=docker&logoColor=white
[vault-k8s-ib-rf-link]:https://frontrow.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fhashicorp%2Fvault%2Fvault-k8s?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=vault-k8s-ib&utm_content=landing_view_report

[wordpress-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/wordpress/bitnami
[wordpress-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/wordpress?logo=docker&logoColor=white
[wordpress-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fwordpress?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=wordpress&utm_content=landing_view_report

[wordpress-ib-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/wordpress/ironbank
[wordpress-ib-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/wordpress-ib?logo=docker&logoColor=white
[wordpress-ib-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fwordpress%2Fwordpress?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=wordpress-ib&utm_content=landing_view_report

[yourls-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/yourls/official
[yourls-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/yourls?logo=docker&logoColor=white
[yourls-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Flibrary%2Fyourls?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=yourls&utm_content=landing_view_report

[zookeeper-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/zookeeper/bitnami
[zookeeper-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/zookeeper?logo=docker&logoColor=white
[zookeeper-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Fbitnami%2Fzookeeper?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=zookeeper&utm_content=landing_view_report

[zookeeper-ib-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/zookeeper/ironbank
[zookeeper-ib-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/zookeeper-ib?logo=docker&logoColor=white
[zookeeper-ib-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/registry1.dso.mil%2Fironbank%2Fopensource%2Fapache%2Fzookeeper?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=zookeeper-ib&utm_content=landing_view_report

[zookeeper-official-github-link]: https://github.com/rapidfort/community-images/tree/main/community_images/zookeeper/official
[zookeeper-official-dh-img-pulls-badge]: https://img.shields.io/docker/pulls/rapidfort/zookeeper-official?logo=docker&logoColor=white
[zookeeper-official-rf-link]:https://us01.rapidfort.com/app/community/imageinfo/docker.io%2Flibrary%2Fzookeeper?utm_source=github&utm_medium=ci_view_report&utm_campaign=sep_01_sprint&utm_term=zookeeper-official&utm_content=landing_view_report

