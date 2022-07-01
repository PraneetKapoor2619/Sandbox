% A = {1/2 + 0.5/3 + 0.3/4 + 0.2/5}
% B = {0.5/2 + 0.7/3 + 0.2/4 + 0.4/5}

u = input('Enter the first matrix: ');
v = input('Enter the second matrix: ');

disp("1. Union, 2. Intersection, 3. Complement");
option = input("Enter the option: ");

if (option == 1)
        w = max(u, v);
        disp(w);
end

if (option == 2)
        p = min(u, v);
        disp(p);
end

if (option == 3)
        option1 = input("Complement matrix 1 or matrix 2? ");
        [m,n] = size(u);
        if (option1 == 1)
                q = ones(m) - u;
        else
                q = ones(m) - v;
        end
        disp(q);
end