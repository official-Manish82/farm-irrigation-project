#include <iostream>
#include <vector>
#include <unordered_map>
#include <queue>
#include <stack>
using namespace std;

class Graph {
private:
    unordered_map<char, vector<char>> adjList;

public:
    // Add an edge to the graph
    void addEdge(char u, char v) {
        adjList[u].push_back(v);
    }

    // Display the adjacency list
    void display() {
        cout << "Adjacency List:" << endl;
        for (auto& pair : adjList) {
            cout << pair.first << ": ";
            for (char neighbor : pair.second) {
                cout << neighbor << ",";
            }
            cout << "\b \n"; // Remove last comma
        }
    }

    // Depth-First Search (DFS)
    void dfs(char start) {
        cout << "\nDFS Traversal starting from " << start << ": ";
        unordered_map<char, bool> visited;
        stack<char> s;
        
        s.push(start);
        visited[start] = true;

        while (!s.empty()) {
            char node = s.top();
            s.pop();
            cout << node << " ";

            for (char neighbor : adjList[node]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    s.push(neighbor);
                }
            }
        }
        cout << endl;
    }

    // Breadth-First Search (BFS)
    void bfs(char start) {
        cout << "\nBFS Traversal starting from " << start << ": ";
        unordered_map<char, bool> visited;
        queue<char> q;
        
        q.push(start);
        visited[start] = true;

        while (!q.empty()) {
            char node = q.front();
            q.pop();
            cout << node << " ";

            for (char neighbor : adjList[node]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    q.push(neighbor);
                }
            }
        }
        cout << endl;
    }
};

int main() {
    Graph g;

    // Add edges based on the given adjacency list
    g.addEdge('A', 'F');
    g.addEdge('A', 'C');
    g.addEdge('A', 'B');
    g.addEdge('B', 'G');
    g.addEdge('B', 'C');
    g.addEdge('C', 'F');
    g.addEdge('D', 'C');
    g.addEdge('E', 'D');
    g.addEdge('E', 'C');
    g.addEdge('E', 'J');
    g.addEdge('F', 'D');
    g.addEdge('G', 'C');
    g.addEdge('G', 'E');
    g.addEdge('J', 'D');
    g.addEdge('J', 'K');
    g.addEdge('K', 'E');
    g.addEdge('K', 'G');

    // Display the graph
    g.display();

    // Perform DFS and BFS
    g.dfs('A');
    g.bfs('A');

    return 0;
}