import java.util.ArrayList;

public class Vertice {

	public int cor;
	int linha;
	int coluna;
	boolean fixed;
	public String label;
	ArrayList<Vertice> vizinhos;
	
	public Vertice(){
		this.fixed = false;
		this.cor = 0;
		this.vizinhos = new ArrayList<Vertice>();
	}
	
	public Vertice(String s) {
		this.fixed = false;
		this.cor = 0;
		this.label = s;
		this.vizinhos = new ArrayList<Vertice>();
	}

	public Vertice(int cor) {
		this.fixed = false;
		this.cor = cor;
		this.vizinhos = new ArrayList<Vertice>();
	}

	void addVizinho(Vertice v){
		this.vizinhos.add(v);
	}
	
	public void imprimeVizinhos(){
		for(Vertice v: this.vizinhos){
			System.out.print("-> " + v.label);
		}
	}

}
