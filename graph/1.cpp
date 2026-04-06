#include <iostream>
using namespace std;
int main(){
  int n,edges;
  cout<<"Enter number of vertices: ";
  cin>>n;
  // create adjacency matrix and initialize with 0
  int adj[50][50]={0};
  cout<<"Enter number of edges: ";
  cin>>edges;
  cout<<"Enter edges (u v) format:\n";
  for(int i=0;i<edges;i++){
    int u,v;
    cin>>u>>v;
    adj[u][v]=1;
    adj[v][u]=1; // for undirected graph
  }
  // display adjacency matrix
  cout<<"Adjacency Matrix:\n";  
  for(int i=0;i<n;i++){
    for(int j=0;j<n;j++){
      cout<<adj[i][j]<<" ";
    }
    cout<<endl;
  }
}