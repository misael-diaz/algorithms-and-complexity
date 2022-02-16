% Algorithms and Complexity                               February 16, 2022
% IST 4310
% Prof. M Diaz-Maldonado
%
%
% Synopsis:
% Plots f(n) and g(n) to verify that g(n) = O(f). It also plots f(n) and
% its asymptotic approximation F(n) on the same loglog plot to show that
% these are the same as `n' grows towards infinity.
%
%
% Sinopsis:
% Grafica las funciones f(n) y g(n) para verificar que g(n) = O(f). Tambien
% grafica f(n) y su aproximacion asintotica F(n) en la misma figura en
% escala logaritmica para demostrar que estas son las mismas a medida que
% `n' crece hacia el infinito.
%
%
% Copyright (c) 2022 Misael Diaz-Maldonado
% This file is released under the GNU General Public License as published
% by the Free Software Foundation, either version 3 of the License, or
% (at your option) any later version.
%
%
% References:
% [0] JJ McConnell, Analysis of Algorithms, 2nd edition, 2007.


clear
close all
clc


n = (1:156)';
f = n + sqrt(n) .* log2( factorial(n) );
g = n + n .* log2(n);

N = logspace(0, 3)';
G = N + N .* log2(N);
F = N + N .* sqrt(N) .* log2(N);


figure(1)
plot(n, g ./ f, 'linestyle', '-',  'color', 'red',  ...
    'DisplayName','exact: $ g(n) / f(n) $')
hold on
plot(N, G ./ F, 'linestyle', '--', 'color', 'blue', ...
    'DisplayName', 'approximate: $ G(n) / F(n) $')
xlabel('$n$', 'interpreter', 'latex')
legend('interpreter', 'latex')


figure(2)
loglog(n, g ./ f, 'linestyle', '-',  'color', 'red',  ...
    'DisplayName', 'exact: $ g(n) / f(n) $')
hold on
loglog(N, G ./ F, 'linestyle', '--', 'color', 'blue', ...
    'DisplayName', 'approximate: $ G(n) / F(n) $')
xlabel('$n$', 'interpreter', 'latex')
legend('interpreter', 'latex')


% Figure shows that the asymptotic behavior of f(n) and its approximation,
% F(n), is the same. (Note: Respective slopes are the same.)
figure(3)
loglog(n, g, 'linestyle', '-.', 'color', 'blue',  'DisplayName', '$g(n)$')
hold on
loglog(n, f, 'linestyle', '-',  'color', 'black', 'DisplayName', '$f(n)$')
loglog(N, F, 'linestyle', '--', 'color', 'black', 'DisplayName', '$F(n)$')
xlabel('$n$', 'interpreter', 'latex')
legend('location', 'NorthWest', 'interpreter', 'latex')
