% Ex 1
% inference of additional facts
%child(X,Y):-parent(Y,X).
%parent(ann,bob).  parent(bob, carol). parent(bob, dan).

%#show child/2.

% Ex 2  - 
% some more enumeration of all possible assignments
%p(1..5).
%p(1..2,1..4).
%p(1..4,1..2).

% Ex 3   (2.11)
%p(N,K):-N=0..4, K=-1*(2*(N\2)-1).

% choice rules
%{p(a); q(b)}.
% same as saying all non-empty subsets of  {p(1);p(2);...;p(10)}
%{p(1..10)}.
% all subsets of size 1 and 2
%1 {p(1..3)} 2.
% 1 {p(1);p(2);p(3)} 2.
%  all subsets
% {p(4)}.

% choice and constaints
%1 { p(1..3) } 2.
%:-p(1), not p(2).

% interesting - answers need to satisfy both choice rules
%{p;q}=1.
%{q;r}=1.

% X and Y go through all possible assignments
p(a).
p(b).
{q(X,Y) : p(X), p(Y)}=1.

