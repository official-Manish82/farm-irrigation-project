#include <iostream>
using namespace std;
#define INFINITY 9999
#define MAX 20
int main()
{
  int n, source;
  int cost[MAX][MAX], dist[MAX], visited[MAX] = {0};
  cout << "Enter number of nodes: ";
  cin >> n;
  cout << "Enter cost matrix:\n";
  for (int i = 0; i < n; i++)
  {
    for (int j = 0; j < n; j++)
    {
      cin >> cost[i][j];
      if (i != j && cost[i][j] == 0)
        cost[i][j] = INFINITY;
    }
  }
  cout << "Enter source node (0 to " << n - 1 << "): ";
  cin >> source;
  for (int i = 0; i < n; i++)
    dist[i] = INFINITY;
  dist[source] = 0;
  for (int count = 0; count < n - 1; count++)
  {
    int min = INFINITY, u = -1;
    for (int i = 0; i < n; i++)
    {
      if (!visited[i] && dist[i] < min)
      {
        min = dist[i];
        u = i;
      }
    }
    if (u == -1)
      break;
    visited[u] = 1;
    for (int v = 0; v < n; v++)
    {
      if (!visited[v] && dist[u] + cost[u][v] < dist[v])
      {
        dist[v] = dist[u] + cost[u][v];
      }
    }
  }
  cout << "\nShortest paths from node " << source << ":\n";
  for (int i = 0; i < n; i++)
  {
    if (dist[i] == INFINITY)
    {
      cout << source << " -> " << i << " = INF\n";
    }
    else
    {
      cout << source << " -> " << i << " = " << dist[i] << endl;
    }
  }
  return 0;
}