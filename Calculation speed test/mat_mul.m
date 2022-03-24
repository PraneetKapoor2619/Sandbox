clc;
c = 75;
lim = 1.0;
m = zeros(c, c);
for i = 1:c
    for j = 1:c
        m(i, j) = rand();
    end
end

fprintf("Starting Computations...");
count = 0;
tic;
while(toc < lim)
    m*m;
    count = count + 1;
end

fprintf("\nTotal computations performed = %.2e\nComputations per second = %.2e\n", count, count / lim);