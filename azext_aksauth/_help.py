from knack.help_files import helps  # pylint: disable=unused-import


helps['aksauth'] = """
    type: group
    short-summary: Commands to connect to AKS RBAC'd Clusters Non Interactively.
"""

helps['aksauth connect'] = """
    type: command
    short-summary: Create resources commonly used for a student hack, including a website, database, and artificial intelligence.
    examples:
        - name: Connect to an AKS RBAC's Cluster Non Interactively
          text: az aksauth connect --resource-group adrian-group --subscription xxxxxx–1ef5–4ba4-bdd0–xxxxxx --cluster-name adrian-cluster --tenant zzzzzz–6cd9–4672–9034-zzzz --username clusteruser@mydmn.com --password "hard2Guess"
"""
