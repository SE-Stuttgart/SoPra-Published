# https://github.com/gpocentek/python-gitlab
# pip install python-gitlab
import gitlab
import time


'''
set credentials
'''


sopraAdminUserName='sopra-ws1718' # sopra-ws1718
sopraAdminUserPassword=''
sopraAdminUserToken=''

sopraGitlabHostname='sopra.informatik.uni-stuttgart.de' # eg sopra.informatik.uni-stuttgart.de
sopraProjectTemplatePath='minderki/SoPra-Project-Template.git' # eg sopra-ws1718/SoPra-Project-Template.git
sopraGitlabProtocol='https://'

groupAmount=40

gl = gitlab.Gitlab(sopraGitlabProtocol + sopraGitlabHostname,sopraAdminUserToken, api_version=4)
gl.auth()

# measure time

startTime = time.time()



for x in range(1,groupAmount+1):
  project = gl.projects.create({'name':'SoPra Team ' + str(x),'path':'sopra-team-' + str(x), 'import_url': sopraGitlabProtocol + sopraAdminUserName + ':' + sopraAdminUserPassword + '@' + sopraGitlabHostname + '/' + sopraProjectTemplatePath})
  print 'Created Project for Team ' + str(x) + ':\n'
  print project
  print 'Elapsed time ' + str(time.time()-startTime)
