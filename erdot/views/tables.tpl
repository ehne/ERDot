% rebase('base.tpl')

% for i in tables:
{{i}} [ label=<
    <table border="0" cellborder="1" cellspacing="0" >
    <tr><td><i>{{i}}</i></td></tr>
% for k in tables[i]:
    <tr><td port="{{k.replace('+', '').replace('*', '')}}" align="left" cellpadding="5">{{k.replace("+","FK ").replace("*","PK ")}} <font color="grey60">{{tables[i][k]}}</font></td></tr>
% end
</table>>];
% end

{{!base}}