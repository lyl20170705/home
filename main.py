import os
import sys
import INIT


def git_log(repo_path, log_path, dictionary, dict_key, br, file_type):
    os.chdir(log_path)
    fo = open('log_'+dict_key+'.txt','a')
    if br == '':
        for i in range(len(dictionary[dict_key][2])):
            os.chdir(repo_path)  #
            os.system('git checkout ' + dictionary[dict_key][2][i])
            log = os.popen('git log --pretty="%an %h %ad %s" ' + file_type).read()
            os.chdir(log_path)
            fo.write('log of ' + dictionary[dict_key][2][i] + ':' + '\n')
            fo.write(log + '\n')
    else:
        os.chdir(repo_path)  #
        os.system('git checkout ' + br)
        log = os.popen('git log --pretty="%an %h %ad %s" ' + file_type).read()
        os.chdir(log_path)
        fo.write('log of ' + br + ':' + '\n')
        fo.write(log + '\n')
    fo.close()


def analyse_instruction(repo, br, dictionary):
    dict_key_tmp = ''
    for dict_key in dictionary:
        if dict_key == repo:
            dict_key_tmp = dict_key
            break
    if (dict_key_tmp == repo) & (br != ''):
        br_tmp = ''
        for i in range(len(dictionary[dict_key_tmp][2])):
            if br == dictionary[dict_key_tmp][2][i]:
                br_tmp = br
                break
        return br_tmp == br
    elif (dict_key_tmp == repo) & (br == ''):
        return True
    else:
        return False


if __name__ == '__main__':

    if sys.argv[1] == '--log':
        if len(sys.argv) == 2: # main.py --log
            for key in INIT.ID:
                git_log(INIT.ID[key][1]+key, INIT.ID[key][1], INIT.ID, key, '', '')
        elif len(sys.argv) == 3:   # main.py --log repo
            if analyse_instruction(sys.argv[2], '', INIT.ID):
                git_log(INIT.ID[sys.argv[2]][1] + sys.argv[2], INIT.ID[sys.argv[2]][1], INIT.ID, sys.argv[2], '', '')
            else:
                print "ERROR1:The instruction you input is unexpected. The repository name is wrong."
        elif len(sys.argv) == 4: # main.py --log repo br
            if analyse_instruction(sys.argv[2], sys.argv[3], INIT.ID):
                git_log(INIT.ID[sys.argv[2]][1] + sys.argv[2], INIT.ID[sys.argv[2]][1], INIT.ID, sys.argv[2], sys.argv[3], '')
            else :
                print "ERROR2:The instruction you input is unexpected. The repository or branch name is wrong."
        elif len(sys.argv) == 5: # main.py --log repo br *.mak
            if analyse_instruction(sys.argv[2], sys.argv[3], INIT.ID):
                git_log(INIT.ID[sys.argv[2]][1] + sys.argv[2], INIT.ID[sys.argv[2]][1], INIT.ID, sys.argv[2], sys.argv[3], sys.argv[4])
            else :
                print "ERROR3:The instruction you input is unexpected. The repository or branch name is wrong."
        else:
            print "ERROR4:The instruction you input is unexpected. Please refer to the --help"
    elif sys.argv[1] == '--merge':
        if len(sys.argv) == 5:
            if analyse_instruction(sys.argv[2], sys.argv[3], INIT.ID):
                print ''