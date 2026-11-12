# Light CI/CD — DevOps Pilot

My team submitted our final-year project proposal under the name DevOps Pilot. The app we're building is called Light CI/CD. I think of deployment like putting a finished product on a shop shelf. Once the product is ready, you still need to put it somewhere people can reach it and keep it available. Light CI/CD is meant to do that for an app by putting it on a server and helping manage it after launch.

I built the initial deployment pipeline, including the Nixpacks setup and a manual configuration option. I tested the first version on smaller projects. A developer provides the GitHub repository link, configures a webhook, and authorizes SSH access to the server. With manual setup, they can specify commands for the front end and back end and select a database when needed. We've since added support for four database types and are testing the pipeline with stacks such as Next.js, React, Python, and Java.

My work also included queuing deployments, adding signed GitHub webhooks, and checking the health of a candidate release before switching traffic to it. I added start-command overrides for Nixpacks so a project can specify how it runs. I also worked on a live host telemetry dashboard and wrote a self-hosting and deployment guide.

Our next phase is the agent system. We want it to restore the last known working deployment when a release fails and send an alert. We're planning six specialist agents covering areas such as Docker, the database, CPU, and memory, with a coordinating agent that reviews their findings and produces a report. If the specialists can't resolve an issue, we plan to try an LLM-assisted step. If the problem still needs a person, we want the alert to explain what happened and what the system already tried.
