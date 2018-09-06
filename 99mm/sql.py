#_*_ coding:utf-8 _*_

from MySQL import MySQL
from config import host,user,password,database



class mysql(MySQL):

    def __init__(self,host=host,user=user,password=password,db=''):
        super(mysql,self).__init__(host=host,user=user,password=password,db=db)

    def create_database(self,):

        query='create database if not exists %s'%database
        self.execute(query=query)


    def create_table_item(self,):

        query='''create table if not exists %s.item(
                id int primary key auto_increment,
                num int not null,
                total int not null,
                host varchar(50) not null,
                keyword varchar(20) not null,
                page int not null,
                status int not null default '0',
                create_time timestamp default current_timestamp
                )default charset utf8'''%(database)

        self.execute(query=query)


    def check_table_item(self,):

        query='select host,keyword,num,page from item where status=0'

        return self.execute(query=query)



    def insert_table_item(self,num,total,host,keyword,page):

        query='insert ignore into item (num,total,host,keyword,page) values("%s","%s","%s","%s","%s")'%(num,total,host,keyword,page)
        self.execute(query=query)


    def update_table_item_status(self,keyword,page,status=1):

        query='update item set status="%s" where keyword="%s" and page="%s"'%(status,keyword,page)
        self.execute(query=query)




    def create_table_html(self,):

        query='''create table if not exists %s.html(
                host varchar(50) not null,
                path varchar(50)not null  primary key,
                status int not null default '0',
                create_time timestamp default current_timestamp
                )default charset utf8'''%(database)

        self.execute(query=query)


    def check_table_html(self,):

        query='select host,path from html where status=0'

        return self.execute(query=query)



    def insert_table_html(self,host,path):

        query='insert ignore into html (host,path) values("%s","%s")'%(host,path)

        self.execute(query=query)


    def update_table_html_status(self,path,status=1):

        query='update html set status="%s" where path="%s"'%(status,path)
        self.execute(query=query)



    def create_table_img(self,):

        query='''create table if not exists %s.img(
                title varchar(50)not null, 
                refer varchar(100)not null primary key,
                path varchar(50) not null ,
                host varchar(50) not null,
                iaStr varchar(500)not null,
                total int not null,
                status int not null default '0',
                create_time timestamp default current_timestamp
                )default charset utf8'''%(database)

        self.execute(query=query)




    def check_table_img(self,):

        query='select title,host,iaStr,path,refer from img where status=0 '

        return self.execute(query=query)


    def insert_table_img(self,title,path,host,iaStr,total,refer):

        query='insert ignore into img (title,path,host,iaStr,total,refer) values("%s","%s","%s","%s","%s","%s")'%(title,path,host,iaStr,total,refer)

        self.execute(query=query)

    def update_table_img_status(self,refer,status=1):

        query='update img set status="%s" where refer="%s"'%(status,refer)
        self.execute(query=query)


    def truncate_table(self,tb):

        query='truncate table %s'%(tb)
        self.execute(query=query)

    def drop_table(self,tb):

        query='drop table %s'%(tb)
        self.execute(query=query)





def test():

    sql=mysql(db=database)

    # sql.create_database()
    # sql.create_table_item()
    # sql.create_table_html()
    # sql.create_table_img()
    print sql.check_table_html()


if __name__=='__main__':

    test()

    pass




