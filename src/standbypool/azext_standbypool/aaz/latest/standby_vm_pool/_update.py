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
    "standby-vm-pool update",
)
class Update(AAZCommand):
    """Update a StandbyVirtualMachinePoolResource

    :example: StandbyVirtualMachinePool_Update
        az standby-vm-pool update --resource-group rgstandbypool --name pool --max-ready-capacity 304 --min-ready-capacity 300 --vm-state Running --vmss-id /subscriptions/00000000-0000-0000-0000-000000000009/resourceGroups/rgstandbypool/providers/Microsoft.Compute/virtualMachineScaleSets/myVmss --tags "{}" --location West US --subscription 00000000-0000-0000-0000-000000000009
    """

    _aaz_info = {
        "version": "2025-03-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.standbypool/standbyvirtualmachinepools/{}", "2025-03-01"],
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
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.name = AAZStrArg(
            options=["-n", "--name"],
            help="Name of the standby virtual machine pool",
            required=True,
            id_part="name",
            fmt=AAZStrArgFormat(
                pattern="^[a-zA-Z0-9-]{3,24}$",
            ),
        )

        # define Arg Group "ElasticityProfile"

        _args_schema = cls._args_schema
        _args_schema.max_ready_capacity = AAZIntArg(
            options=["--max-ready-capacity"],
            arg_group="ElasticityProfile",
            help="Specifies the maximum number of virtual machines in the standby virtual machine pool.",
            fmt=AAZIntArgFormat(
                maximum=2000,
                minimum=0,
            ),
        )
        _args_schema.min_ready_capacity = AAZIntArg(
            options=["--min-ready-capacity"],
            arg_group="ElasticityProfile",
            help="Specifies the desired minimum number of virtual machines in the standby virtual machine pool. MinReadyCapacity cannot exceed MaxReadyCapacity.",
            fmt=AAZIntArgFormat(
                maximum=2000,
                minimum=0,
            ),
        )

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.vmss_id = AAZResourceIdArg(
            options=["--vmss-id"],
            arg_group="Properties",
            help="Specifies the fully qualified resource ID of a virtual machine scale set the pool is attached to.",
        )
        _args_schema.vm_state = AAZStrArg(
            options=["--vm-state"],
            arg_group="Properties",
            help="Specifies the desired state of virtual machines in the pool.",
            enum={"Deallocated": "Deallocated", "Hibernated": "Hibernated", "Running": "Running"},
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="Properties",
            help="Resource tags.",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.StandbyVirtualMachinePoolsUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class StandbyVirtualMachinePoolsUpdate(AAZHttpOperation):
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
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.StandbyPool/standbyVirtualMachinePools/{standbyVirtualMachinePoolName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PATCH"

        @property
        def error_format(self):
            return "MgmtErrorFormat"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "standbyVirtualMachinePoolName", self.ctx.args.name,
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
                    "api-version", "2025-03-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("properties", AAZObjectType, typ_kwargs={"flags": {"client_flatten": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("attachedVirtualMachineScaleSetId", AAZStrType, ".vmss_id")
                properties.set_prop("elasticityProfile", AAZObjectType)
                properties.set_prop("virtualMachineState", AAZStrType, ".vm_state")

            elasticity_profile = _builder.get(".properties.elasticityProfile")
            if elasticity_profile is not None:
                elasticity_profile.set_prop("maxReadyCapacity", AAZIntType, ".max_ready_capacity", typ_kwargs={"flags": {"required": True}})
                elasticity_profile.set_prop("minReadyCapacity", AAZIntType, ".min_ready_capacity")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

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
                flags={"client_flatten": True},
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
            properties.attached_virtual_machine_scale_set_id = AAZStrType(
                serialized_name="attachedVirtualMachineScaleSetId",
            )
            properties.elasticity_profile = AAZObjectType(
                serialized_name="elasticityProfile",
            )
            properties.provisioning_state = AAZStrType(
                serialized_name="provisioningState",
                flags={"read_only": True},
            )
            properties.virtual_machine_state = AAZStrType(
                serialized_name="virtualMachineState",
                flags={"required": True},
            )

            elasticity_profile = cls._schema_on_200.properties.elasticity_profile
            elasticity_profile.max_ready_capacity = AAZIntType(
                serialized_name="maxReadyCapacity",
                flags={"required": True},
            )
            elasticity_profile.min_ready_capacity = AAZIntType(
                serialized_name="minReadyCapacity",
            )

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


class _UpdateHelper:
    """Helper class for Update"""


__all__ = ["Update"]
