function [C, sigma] = dataset3Params(X, y, Xval, yval)
%EX6PARAMS returns your choice of C and sigma for Part 3 of the exercise
%where you select the optimal (C, sigma) learning parameters to use for SVM
%with RBF kernel
%   [C, sigma] = EX6PARAMS(X, y, Xval, yval) returns your choice of C and 
%   sigma. You should complete this function to return the optimal C and 
%   sigma based on a cross-validation set.
%

% You need to return the following variables correctly.
C = 1;
sigma = 0.3;

% ====================== YOUR CODE HERE ======================
% Instructions: Fill in this function to return the optimal C and sigma
%               learning parameters found using the cross validation set.
%               You can use svmPredict to predict the labels on the cross
%               validation set. For example, 
%                   predictions = svmPredict(model, Xval);
%               will return the predictions on the cross validation set.
%
%  Note: You can compute the prediction error using 
%        mean(double(predictions ~= yval))
%

min_error = inf;
val = [0.01 0.03 0.1 0.3 1 3 10 30]; 
rezult = ones(64, 3);
j = 1;

for val_C = val
    for val_sigma = val
        train = svmTrain(X, y, val_C, @(x1, x2) gaussianKernel(x1, x2, val_sigma));
        train_error = mean(double(svmPredict(train, Xval) ~= yval));
        fprintf('C = %f and sigma = %f prediction error is %f\n', val_C, val_sigma, train_error);
        rezult(j,1) = val_C;
        rezult(j,2) = val_sigma;
        rezult(j,3) = train_error;
        j = j + 1;
        if train_error <= min_error
            min_error = train_error;
            C = val_C;
            sigma = val_sigma;
            fprintf('New value of C is %f and sigma is %f with error %f\n', C, sigma, min_error);
        end
    end
end


fprintf('----Done! C is %f\n sigma is %f\n prediction error is %f\n ', C, sigma, min_error);
fprintf('------- minimum prediction error is %f/n', min(rezult(:,3)));

% =========================================================================

end
