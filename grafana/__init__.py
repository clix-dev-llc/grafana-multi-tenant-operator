import os

from grafana_api.grafana_face import GrafanaFace

MAIN_ORG_ID = 1

GRAFANA_MULTI_TENANT_OPERATOR_HOST = os.getenv(
    "GRAFANA_MULTI_TENANT_OPERATOR_HOST")
GRAFANA_MULTI_TENANT_OPERATOR_PORT = os.getenv(
    "GRAFANA_MULTI_TENANT_OPERATOR_PORT")
GRAFANA_MULTI_TENANT_OPERATOR_PROTOCOL = os.getenv(
    "GRAFANA_MULTI_TENANT_OPERATOR_PROTOCOL")
GRAFANA_MULTI_TENANT_OPERATOR_VERIFY = os.getenv(
    "GRAFANA_MULTI_TENANT_OPERATOR_VERIFY", True) in (True, 'true')
GRAFANA_MULTI_TENANT_OPERATOR_TIMEOUT = os.getenv(
"GRAFANA_MULTI_TENANT_OPERATOR_TIMEOUT")
GRAFANA_MULTI_TENANT_OPERATOR_ADMIN_USERNAME = os.getenv(
    "GRAFANA_MULTI_TENANT_OPERATOR_ADMIN_USERNAME", "admin")
GRAFANA_MULTI_TENANT_OPERATOR_ADMIN_PASSWORD = os.getenv(
    "GRAFANA_MULTI_TENANT_OPERATOR_ADMIN_PASSWORD")

api = GrafanaFace(
    auth=(GRAFANA_MULTI_TENANT_OPERATOR_ADMIN_USERNAME, GRAFANA_MULTI_TENANT_OPERATOR_ADMIN_PASSWORD),
    host=GRAFANA_MULTI_TENANT_OPERATOR_HOST,
    port=GRAFANA_MULTI_TENANT_OPERATOR_PORT,
    protocol=GRAFANA_MULTI_TENANT_OPERATOR_PROTOCOL,
    verify=GRAFANA_MULTI_TENANT_OPERATOR_VERIFY,
    timeout=GRAFANA_MULTI_TENANT_OPERATOR_TIMEOUT)