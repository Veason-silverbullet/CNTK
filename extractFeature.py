import os
import sys

if __name__ == '__main__':
    assert len(sys.argv) == 4, '3 args are needed'
    card_num = int(sys.argv[1])
    mapping_file_path = sys.argv[2]
    model_path = sys.argv[3]
    path_dict = dict()
    index = 0
    with open(os.path.join(mapping_file_path, 'test.index.tsv'), 'r') as f:
        while True:
            line = f.readline()
            if line is None or len(line) <= 1:
                break
            s = line.strip('\n').split('\t')
            path_dict[s[0]] = index
            index += 1

    result = []
    with open(os.path.join(model_path, 'result.txt'), 'w') as result_file:
        for i in range(card_num):
            with open(os.path.join(model_path, 'feature_' + str(i) + '_' + str(card_num) + '.txt'), 'r') as feature_file, open(os.path.join(model_path, 'path_' + str(i) + '_' + str(card_num) + '.txt'), 'r') as path_file:
                feature_lines = feature_file.readlines()
                path_lines = path_file.readlines()
                print('%d of %d' % (i, card_num))
                assert len(feature_lines) == len(path_lines), '%d vs %d' % (len(feature_lines), len(path_lines))
                num = len(feature_lines)
                for j in range(num):
                    s = path_lines[j][22:-1]
                    result.append((path_dict[s], feature_lines[j].strip('\n').strip(' ')))
        result.sort(key=lambda x: x[0])
        for r in result:
            result_file.write(str(r[0]) + '\t' + r[1] + '\n')
