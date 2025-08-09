STAGE=local

# local環境　コンテナ作成
.PHONY: mysql_container_up_local
mysql_container_up_local: # local環境
	docker-compose --env-file ./env/.${STAGE}.env up -d mysql

# local環境　コンテナ停止
.PHONY: mysql_container_stop_local
mysql_container_stop_local: # local環境
	docker-compose --env-file ./env/.${STAGE}.env stop mysql

# local環境　コンテナ削除
.PHONY: mysql_container_down_local
mysql_container_down_local: # local環境
	docker-compose --env-file ./env/.${STAGE}.env down mysql

# local環境　接続
.PHONY: mysql_container_cli_local
mysql_container_cli_local: # local環境
	docker-compose --env-file ./env/.${STAGE}.env run --rm cli