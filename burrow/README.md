# Agent Check: burrow

## Overview

This check monitors [burrow][1] through the Datadog Agent.

## Setup

### Installation

To install the burrow check on your host:

1. Install the [developer toolkit](https://docs.datadoghq.com/developers/integrations/new_check_howto/#developer-toolkit) on any machine.
2. Run `ddev release build burrow` to build the package.
3. [Download the Datadog Agent](https://app.datadoghq.com/account/settings#agent).
4. Upload the build artifact to any host with an Agent andrun `datadog-agent integration install -w path/to/burrow/dist/<ARTIFACT_NAME>.whl`.

### Configuration

1. Edit the `burrow.d/conf.yaml` file, in the `conf.d/` folder at the root of your Agent's configuration directory to start collecting your burrow performance data. See the [sample burrow.d/conf.yaml][2] for all available configuration options.

2. [Restart the Agent][3].

### Validation

[Run the Agent's status subcommand][4] and look for `burrow` under the Checks section.

## Data Collected

### Metrics

burrow does not include any metrics.

### Service Checks

burrow does not include any service checks.

### Events

burrow does not include any events.

## Troubleshooting

Need help? Contact [Datadog support][5].

[1]: **LINK_TO_INTEGRATION_SITE**
[2]: https://github.com/DataDog/integrations-core/blob/master/burrow/datadog_checks/burrow/data/conf.yaml.example
[3]: https://docs.datadoghq.com/agent/guide/agent-commands/?tab=agentv6#start-stop-and-restart-the-agent
[4]: https://docs.datadoghq.com/agent/guide/agent-commands/?tab=agentv6#agent-status-and-information
[5]: https://docs.datadoghq.com/help
