% rebase('tables.tpl')

% for i in relations:
% q = i.split(" ")
% k = q[1].split("--")
% print(k)
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