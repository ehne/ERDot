# the template for the dot output file

dTemp = """
digraph G {
    graph [
        nodesep=0.5;
        rankdir="LR";
        cencentrate=true;
        splines="spline";
        fontname="Helvetica";
        pad="0.2,0.2",
        label="{{lbl}}",
        {{gs}}
    ];
    
    node [shape=plain, fontname="Helvetica"];
    edge [
        dir=both,
        fontsize=12,
        arrowsize=0.9,
        penwidth=1.0,
        labelangle=32,
        labeldistance=1.8,
        fontname="Helvetica"
    ];
    
    % for i in tables:
    {{i}} [ label=<
        <table border="0" cellborder="1" cellspacing="0" >
        <tr><td><i>{{i}}</i></td></tr>
    % for k in tables[i]:
        <tr><td port="{{k.replace('+', '').replace('*', '')}}" align="left" cellpadding="5">{{k.replace("+","FK ").replace("*","PK ")}} <font color="grey60">{{tables[i][k]}}</font></td></tr>
    % end
    </table>>];
    % end

    % for i in relations:
    % q = i.split(" ")
    % k = q[1].split("--")
    % LeftCardinality = k[0]
    % RightCardinality = k[1]

    {{q[0]}}->{{q[2]}} [
    % if RightCardinality == "*":
        arrowhead=ocrow,
    % elif RightCardinality == "+":
        arrowhead=ocrowtee,
    % else:
        arrowhead=noneotee,
    % end

    % if LeftCardinality =="*":
        arrowtail=ocrow,
    % elif LeftCardinality == "+":
        arrowtail=ocrowtee,
    % else:
        arrowtail=noneotee,
    % end
    ];

    % end


    {{ra}}

}
"""