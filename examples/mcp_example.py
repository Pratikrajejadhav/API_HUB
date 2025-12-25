from mcp.mcp_client import MCPClient
print(MCPClient().send('threat_enrichment',{'ip':'8.8.8.8'}).data)
