hold on

load('matlab_data.mat')

plot(Fitnessingenerations1(:, 1), Fitnessingenerations1(:, 2));
plot(Fitnessingenerations2(:, 1), Fitnessingenerations2(:, 2));
plot(Fitnessingenerations3(:, 1), Fitnessingenerations3(:, 2));
plot(Fitnessingenerations4(:, 1), Fitnessingenerations4(:, 2));
plot(Fitnessingenerations5(:, 1), Fitnessingenerations5(:, 2));

TheoreticalMax = Theoreticalmaximum * ones(...
    size(Fitnessingenerations1(:, 1)));
plot(TheoreticalMax)

% title('遗传算法每代最大适值');
xlabel('代数');
ylabel('适应值');

legend('mutation rate = 0.1', 'mutation rate = 0.3', 'mutation rate = 0.5',...
    'mutation rate = 0.7', 'mutation rate = 0.9', '理论最大值');

hold off