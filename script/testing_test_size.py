import Evaluation as Eva
import Utils
import Graphs

'''Ex: start = 5 % (training) , increment = 5% (training) , finish = 20 % (train) '''


def testing_percentage(dataFrame, start, increment, finish, feature_vector):
    fold_quantity = 10
    maxEnt_accuracy_test = []
    svm_accuracy_test = []
    naive_accuracy_test = []

    maxEnt_precision_test = []
    svm_precision_test = []
    naive_precision_test = []

    maxEnt_recall_test = []
    svm_recall_test = []
    naive_recall_test = []

    x_axis = []
    df_sliced = Utils.remove_concerns_under_quantity_threshold(dataFrame)
    for start in range(start, finish + increment, increment):
        x_axis.append(start)
        test_size = 1 - (start) / 100
        evaluate = Eva.Evaluation(
            df_sliced, feature_vector, test_size, fold_quantity
        )
        classifier_max_ent, metrics_max_ent = evaluate.evaluate_MaxEnt()
        classifier_svm, metrics_svm = evaluate.evaluate_SVM()
        classifier_naive, metrics_naive = evaluate.evaluate_Naive_Bayes()

        maxEnt_accuracy_test.append(metrics_max_ent.get_accuracy_score())
        svm_accuracy_test.append(metrics_svm.get_accuracy_score())
        naive_accuracy_test.append(metrics_naive.get_accuracy_score())

        maxEnt_precision_test.append(metrics_max_ent.get_precision_score())
        svm_precision_test.append(metrics_svm.get_precision_score())
        naive_precision_test.append(metrics_naive.get_precision_score())

        maxEnt_recall_test.append(metrics_max_ent.get_recall_score())
        svm_recall_test.append(metrics_svm.get_recall_score())
        naive_recall_test.append(metrics_naive.get_recall_score())

    ##############ACCURACY########################

    Graphs.plot_line_graph("Accuracy over over train size", x_axis, {'naive': naive_accuracy_test,
                                                                     'maxEnt': maxEnt_accuracy_test,
                                                                     'svm': svm_accuracy_test
                                                                     }, "Train size (%)", "Accuracy")
    ##############################################

    ##############PRECISION#######################
    Graphs.plot_line_graph("Weighted avg. precision over train size", x_axis, {'naive': naive_precision_test,
                                                                               'maxEnt': maxEnt_precision_test,
                                                                               'svm': svm_precision_test
                                                                               }, "Train size (%)",
                           "W.avg. precision", )
    ##############RECALL#########################
    Graphs.plot_line_graph("Weighted avg. recall over train size", x_axis, {'naive': naive_recall_test,
                                                                            'maxEnt': maxEnt_recall_test,
                                                                            'svm': svm_recall_test
                                                                            }, "Train size (%)", "W.avg. recall", )


def testing_abs_size(dataFrame, start, increment, finish, feature_vector):
    fold_quantity = 10
    maxEnt_accuracy_test = []
    svm_accuracy_test = []
    naive_accuracy_test = []

    maxEnt_precision_test = []
    svm_precision_test = []
    naive_precision_test = []

    maxEnt_recall_test = []
    svm_recall_test = []
    naive_recall_test = []

    x_axis = []
    df_sliced = Utils.remove_concerns_under_quantity_threshold(dataFrame)
    for start in range(start, finish + increment, increment):
        df_sliced = Utils.remove_concerns_under_quantity_threshold(df_sliced, start)
        x_axis.append(start)
        evaluate = Eva.Evaluation(
            df_sliced, feature_vector, numberOfFiles=start, fold_quantity=fold_quantity
        )
        classifier_max_ent, metrics_max_ent = evaluate.evaluate_MaxEnt('custom')
        classifier_svm, metrics_svm = evaluate.evaluate_SVM('custom')
        classifier_naive, metrics_naive = evaluate.evaluate_Naive_Bayes('custom')

        maxEnt_accuracy_test.append(metrics_max_ent.get_accuracy_score())
        svm_accuracy_test.append(metrics_svm.get_accuracy_score())
        naive_accuracy_test.append(metrics_naive.get_accuracy_score())

        maxEnt_precision_test.append(metrics_max_ent.get_precision_score())
        svm_precision_test.append(metrics_svm.get_precision_score())
        naive_precision_test.append(metrics_naive.get_precision_score())

        maxEnt_recall_test.append(metrics_max_ent.get_recall_score())
        svm_recall_test.append(metrics_svm.get_recall_score())
        naive_recall_test.append(metrics_naive.get_recall_score())

    ##############ACCURACY########################

    Graphs.plot_line_graph("Accuracy over over train size", x_axis, {'naive': naive_accuracy_test,
                                                                     'maxEnt': maxEnt_accuracy_test,
                                                                     'svm': svm_accuracy_test
                                                                     }, "Train size (files)", "Accuracy")
    ##############################################

    ##############PRECISION#######################
    Graphs.plot_line_graph("Weighted avg. precision over train size", x_axis, {'naive': naive_precision_test,
                                                                               'maxEnt': maxEnt_precision_test,
                                                                               'svm': svm_precision_test
                                                                               }, "Train size (files)",
                           "W.avg. precision", )
    ##############RECALL#########################
    Graphs.plot_line_graph("Weighted avg. recall over train size", x_axis, {'naive': naive_recall_test,
                                                                            'maxEnt': maxEnt_recall_test,
                                                                            'svm': svm_recall_test
                                                                            }, "Train size (files)", "W.avg. recall", )


def testing_test_size(dataFrame, test_size_start, test_size_increment, test_size_stop, feature_vector, abs_size=False):
    if abs_size == False:
        testing_percentage(dataFrame, start=test_size_start, increment=test_size_increment, finish=test_size_stop,
                           feature_vector=feature_vector)
    else:
        testing_abs_size(dataFrame, start=test_size_start, increment=test_size_increment, finish=test_size_stop,
                         feature_vector=feature_vector)

