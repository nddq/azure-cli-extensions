# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "networkfabric l3domain wait",
)
class Wait(AAZWaitCommand):
    """Place the CLI in a waiting state until a condition is met.
    """

    _aaz_info = {
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.managednetworkfabric/l3isolationdomains/{}", "2024-06-15-preview"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.resource_name = AAZStrArg(
            options=["--resource-name"],
            help="Name of the L3 Isolation Domain.",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z]{1}[a-zA-Z0-9-_]{2,127}$",
            ),
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.L3IsolationDomainsGet(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=False)
        return result

    class L3IsolationDomainsGet(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200]:
                return self.on_200(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedNetworkFabric/l3IsolationDomains/{l3IsolationDomainName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "GET"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "l3IsolationDomainName", self.ctx.args.resource_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2024-06-15-preview",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        def on_200(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200
            )

        _schema_on_200 = None

        @classmethod
        def _build_schema_on_200(cls):
            if cls._schema_on_200 is not None:
                return cls._schema_on_200

            cls._schema_on_200 = AAZObjectType()

            _schema_on_200 = cls._schema_on_200
            _schema_on_200.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.location = AAZStrType(
                flags={"required": True},
            )
            _schema_on_200.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200.properties = AAZObjectType(
                flags={"required": True, "client_flatten": True},
            )
            _schema_on_200.system_data = AAZObjectType(
                serialized_name="systemData",
                flags={"read_only": True},
            )
            _schema_on_200.tags = AAZDictType()
            _schema_on_200.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200.properties
            properties.administrative_state = AAZStrType(
                serialized_name="administrativeState",
                flags={"read_only": True},
            )
            properties.aggregate_route_configuration = AAZObjectType(
                serialized_name="aggregateRouteConfiguration",
            )
            properties.annotation = AAZStrType()
            properties.configuration_state = AAZStrType(
                serialized_name="configurationState",
                flags={"read_only": True},
            )
            properties.connected_subnet_route_policy = AAZObjectType(
                serialized_name="connectedSubnetRoutePolicy",
            )
            properties.last_operation = AAZObjectType(
                serialized_name="lastOperation",
                flags={"read_only": True},
            )
            properties.network_fabric_id = AAZStrType(
                serialized_name="networkFabricId",
                flags={"required": True},
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.redistribute_connected_subnets = AAZStrType(
                serialized_name="redistributeConnectedSubnets",
            )
            properties.redistribute_static_routes = AAZStrType(
                serialized_name="redistributeStaticRoutes",
            )
            properties.route_prefix_limit = AAZObjectType(
                serialized_name="routePrefixLimit",
            )
            properties.static_route_route_policy = AAZObjectType(
                serialized_name="staticRouteRoutePolicy",
            )
            properties.unique_rd_configuration = AAZObjectType(
                serialized_name="uniqueRdConfiguration",
            )

            aggregate_route_configuration = cls._schema_on_200.properties.aggregate_route_configuration
            aggregate_route_configuration.ipv4_routes = AAZListType(
                serialized_name="ipv4Routes",
            )
            aggregate_route_configuration.ipv6_routes = AAZListType(
                serialized_name="ipv6Routes",
            )

            ipv4_routes = cls._schema_on_200.properties.aggregate_route_configuration.ipv4_routes
            ipv4_routes.Element = AAZObjectType()
            _WaitHelper._build_schema_aggregate_route_read(ipv4_routes.Element)

            ipv6_routes = cls._schema_on_200.properties.aggregate_route_configuration.ipv6_routes
            ipv6_routes.Element = AAZObjectType()
            _WaitHelper._build_schema_aggregate_route_read(ipv6_routes.Element)

            connected_subnet_route_policy = cls._schema_on_200.properties.connected_subnet_route_policy
            connected_subnet_route_policy.export_route_policy = AAZObjectType(
                serialized_name="exportRoutePolicy",
            )
            _WaitHelper._build_schema_l3_export_route_policy_read(connected_subnet_route_policy.export_route_policy)

            last_operation = cls._schema_on_200.properties.last_operation
            last_operation.details = AAZStrType(
                flags={"read_only": True},
            )

            route_prefix_limit = cls._schema_on_200.properties.route_prefix_limit
            route_prefix_limit.hard_limit = AAZIntType(
                serialized_name="hardLimit",
            )
            route_prefix_limit.threshold = AAZIntType()

            static_route_route_policy = cls._schema_on_200.properties.static_route_route_policy
            static_route_route_policy.export_route_policy = AAZObjectType(
                serialized_name="exportRoutePolicy",
            )
            _WaitHelper._build_schema_l3_export_route_policy_read(static_route_route_policy.export_route_policy)

            unique_rd_configuration = cls._schema_on_200.properties.unique_rd_configuration
            unique_rd_configuration.unique_rds = AAZListType(
                serialized_name="uniqueRds",
                flags={"read_only": True},
            )

            unique_rds = cls._schema_on_200.properties.unique_rd_configuration.unique_rds
            unique_rds.Element = AAZStrType()

            system_data = cls._schema_on_200.system_data
            system_data.created_at = AAZStrType(
                serialized_name="createdAt",
            )
            system_data.created_by = AAZStrType(
                serialized_name="createdBy",
            )
            system_data.created_by_type = AAZStrType(
                serialized_name="createdByType",
            )
            system_data.last_modified_at = AAZStrType(
                serialized_name="lastModifiedAt",
            )
            system_data.last_modified_by = AAZStrType(
                serialized_name="lastModifiedBy",
            )
            system_data.last_modified_by_type = AAZStrType(
                serialized_name="lastModifiedByType",
            )

            tags = cls._schema_on_200.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200


class _WaitHelper:
    """Helper class for Wait"""

    _schema_aggregate_route_read = None

    @classmethod
    def _build_schema_aggregate_route_read(cls, _schema):
        if cls._schema_aggregate_route_read is not None:
            _schema.prefix = cls._schema_aggregate_route_read.prefix
            return

        cls._schema_aggregate_route_read = _schema_aggregate_route_read = AAZObjectType()

        aggregate_route_read = _schema_aggregate_route_read
        aggregate_route_read.prefix = AAZStrType(
            flags={"required": True},
        )

        _schema.prefix = cls._schema_aggregate_route_read.prefix

    _schema_l3_export_route_policy_read = None

    @classmethod
    def _build_schema_l3_export_route_policy_read(cls, _schema):
        if cls._schema_l3_export_route_policy_read is not None:
            _schema.export_ipv4_route_policy_id = cls._schema_l3_export_route_policy_read.export_ipv4_route_policy_id
            _schema.export_ipv6_route_policy_id = cls._schema_l3_export_route_policy_read.export_ipv6_route_policy_id
            return

        cls._schema_l3_export_route_policy_read = _schema_l3_export_route_policy_read = AAZObjectType()

        l3_export_route_policy_read = _schema_l3_export_route_policy_read
        l3_export_route_policy_read.export_ipv4_route_policy_id = AAZStrType(
            serialized_name="exportIpv4RoutePolicyId",
        )
        l3_export_route_policy_read.export_ipv6_route_policy_id = AAZStrType(
            serialized_name="exportIpv6RoutePolicyId",
        )

        _schema.export_ipv4_route_policy_id = cls._schema_l3_export_route_policy_read.export_ipv4_route_policy_id
        _schema.export_ipv6_route_policy_id = cls._schema_l3_export_route_policy_read.export_ipv6_route_policy_id


__all__ = ["Wait"]
