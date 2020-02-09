class Cgi(object):

    def debugPage():
        import cgitb; cgitb.enable()
        cgi.test()