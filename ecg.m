thorax1 = preprocess(importdata('thorax1.txt'));
thorax2 = preprocess(importdata('thorax2.txt'));
abdomen1 = preprocess(importdata('abdomen1.txt'));
abdomen2 = preprocess(importdata('abdomen2.txt'));
abdomen3 = preprocess(importdata('abdomen3.txt'));

range = [1 20000];

% Sampling frequency (as per assignment text)
%Fs = 1000;

doPlot = true;

% Filter length
filterLength = 6;
% Learning rate/step size
mu = 0.01;

lms = dsp.LMSFilter('Method', 'LMS', 'Length', filterLength, 'StepSize', mu);
[y, err, weights] = lms(thorax1, abdomen3);

filterLengths = [1, 5, 6, 10, 11, 15, 16, 21, 22];
%filterLengths = [0.01, 0.005, 0.004, 0.003, 0.002, 0.001, 0.0005, 0.0001];
t = zeros(20e3, length(filterLengths));
for i = 1:length(filterLengths)
    l = filterLengths(i);
    lms = dsp.LMSFilter('Method', 'LMS', 'Length', l, 'StepSize', 0.005);
    [~, err, ~] = lms(thorax2, abdomen3);
    t(:,i) = err;
end

%lms2 = dsp.LMSFilter('Method', 'LMS', 'Length', 20, 'StepSize', 0.007);
%[y2, err2, weights2] = lms2(thorax1, abdomen3);

if doPlot == true
    subplot(5,1,1);
    plot(thorax1(range(1):range(2)));
    ylim([-5 5]);
    title('thorax1');
    
%     hold on;
%     plot(y(range(1):range(2)), 'Color', 'red');
%     hold off;

    subplot(5,1,2);
    plot(thorax2(range(1):range(2)));
    ylim([-5 5]);
    title('thorax2');
    
    subplot(5,1,3);
    plot(abdomen1(range(1):range(2)));
    ylim([-5 8]);
    title('abdomen1');
    
    subplot(5,1,4);
    plot(abdomen2(range(1):range(2)));
    ylim([-5 8]);
    title('abdomen2');
    
    subplot(5,1,5);
    plot(abdomen3(range(1):range(2)));
    ylim([-5 8]);
    title('abdomen3');
end

% normalize/detrend/smoothdata
function result = preprocess(data)
    result = data;
    Fs = 1000;
    result = highpass(result, 0.5, Fs);
%     Wo = 50/(Fs/2);
%     [b,a] = iirnotch(Wo, Wo/35);
%     result = filter(b, a, result);
    result = normalize(result);
end

% adaptiveNoiseCancellationExampleApp
signalAnalyzer