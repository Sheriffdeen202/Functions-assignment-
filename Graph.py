% Coefficients
a = 2;
b = -3;
c = 1;

% Define the range for x
x = -10:0.1:10;

% Compute y using the quadratic formula
y = a*x.^2 + b*x + c;

% Plot the graph
plot(x, y, 'b-', 'LineWidth', 2);
grid on;

% Add title and labels
title('Quadratic Graph: y = 2x^2 - 3x + 1');
xlabel('x');
ylabel('y');

% Optionally, mark the vertex
vertex_x = -b/(2*a);
vertex_y = a*vertex_x^2 + b*vertex_x + c;
hold on;
plot(vertex_x, vertex_y, 'ro', 'MarkerSize', 8, 'MarkerFaceColor', 'r');
legend('Quadratic Curve', 'Vertex');
