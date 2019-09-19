FROM emqx/emqx:v3.2.3-alpine3.9-amd64

ADD loaded_plugins /opt/emqx/data/loaded_plugins
ADD emqx_auth_http.conf /opt/emqx/etc/plugins/emqx_auth_http.conf

USER emqx
CMD [ "emqx", "foreground" ]
