hold on

load('matlab_data.mat')

plot(Fitnessingenerations1(:, 1), Fitnessingenerations1(:, 2));
plot(Fitnessingenerations2(:, 1), Fitnessingenerations2(:, 2));
plot(Fitnessingenerations3(:, 1), Fitnessingenerations3(:, 2));
plot(Fitnessingenerations4(:, 1), Fitnessingenerations4(:, 2));
plot(Fitnessingenerations5(:, 1), Fitnessingenerations5(:, 2));
plot(Fitnessingenerations6(:, 1), Fitnessingenerations6(:, 2), '-.');
plot(Fitnessingenerations7(:, 1), Fitnessingenerations7(:, 2), '--*');
plot(Fitnessingenerations8(:, 1), Fitnessingenerations8(:, 2), '--.');
plot(Fitnessingenerations9(:, 1), Fitnessingenerations9(:, 2), '-*');
plot(Fitnessingenerations10(:, 1), Fitnessingenerations10(:, 2), '--');

TheoreticalMax = Theoreticalmaximum * ones(...
    size(Fitnessingenerations1(:, 1)));
plot(TheoreticalMax)

% title('遗传算法每代最大适值');
xlabel('代数');
ylabel('适应值');

legend('mutation rate = 0.01', 'mutation rate = 0.02', 'mutation rate = 0.03',...
    'mutation rate = 0.04', 'mutation rate = 0.05', 'mutation rate = 0.06',...
    'mutation rate = 0.07', 'mutation rate = 0.08', 'mutation rate = 0.09',...
    'mutation rate = 0.10', '理论最大值');

hold off