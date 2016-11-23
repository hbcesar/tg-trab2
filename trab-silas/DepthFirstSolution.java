/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package br.ufes.grafos.domain.algorithm;

import br.ufes.grafos.domain.Graph;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Stack;

public class DepthFirstSolution {

    private final Stack<Integer> stack;     //Stack
    private final int size;         //Sudoku size
    private int violations;       //Coloriu
    private final int[] color;     //Color of vertices
    private final HashMap<Integer, Integer> colorsMap; //To save initial configuration of the game

    public DepthFirstSolution(Graph g) {
        size = (int) Math.pow(g.V(), .25);
        stack = new Stack<>();
        color = new int[g.V()];
        colorsMap = new HashMap<>();
        for (int i = 0; i < g.V(); i++) {
            colorsMap.put(i, 0);
        }

    }

    public int getViolations() {
        return violations;
    }

    public void dfs(Graph g, int s) {
        for (int i = 0; i < g.V(); i++) {
            color[i] = colorsMap.get(i);
        }
        stack.clear();
        violations = 0;
        colorVertex(s, g);
        stack.add(s);
        while (!stack.isEmpty()) {
            int current = stack.pop();
            for (int aux : g.adj(current)) {
                if (color[aux] == 0) {
                    if (!colorVertex(aux, g)) {
                        violations++;
                    }
                    stack.add(current);
                    stack.add(aux);
                    break;
                }
            }

        }
    }

    private boolean colorVertex(int v, Graph g) {
        LinkedList<Integer> cores = new LinkedList<>();
        for (int i = 1; i < size * size + 1; i++) {
            boolean podeColorir = true;
            for (int ad : g.adj(v)) {
                if (color[ad] == i) {
                    podeColorir = false;
                    break;
                }
            }
            if (podeColorir) {
                cores.add(i);
            }
        }
        if (cores.isEmpty()) {
            color[v] = (int) (Math.random() * 9 + 1);
            return false;
        } else {
            color[v] = cores.get((int) (Math.random() * cores.size()));
            return true;
        }
    }

    public void addColor(int i, int j, int color) {

        int index = j * size * size + i;
        colorsMap.put(index, color);

    }

    @Override
    public String toString() {
        String saida = "-\t";
        for (int j = 0; j < size * size + size; j++) {
            saida += "-\t";
        }
        saida += "\n";
        for (int i = 0; i < size * size; i++) {
            saida += "|\t";
            for (int j = 0; j < size * size; j++) {
                saida += color[j * size * size + i] + "\t";
                if ((j + 1) % size == 0) {
                    saida += "|\t";
                }
            }
            saida += "\n";
            if ((i + 1) % size == 0) {
                for (int j = 0; j < size * size + size; j++) {
                    saida += "-\t";
                }
                saida += "\n";
            }
        }
        return saida;
    }
}
