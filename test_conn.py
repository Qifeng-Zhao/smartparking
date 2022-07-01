import pymysql
import traceback

if __name__ == '__main__':
    try:
        # 导入pymysql模块
        # 连接database
        conn = pymysql.connect(host="127.0.0.1", user ="root", password ="Jingdongyun", database ="smartparking", charset ="utf8")
        # 得到一个可以执行SQL语句的光标对象
        cursor = conn.cursor()
        # 定义要执行的SQL语句
        sql = """
         UPDATE id SET gloable_id =778 where local_id =1 ;
        """
        # 执行SQL语句
        cursor.execute(sql)
        conn.commit()
        # 关闭光标对象
        # cursor.close()
        # 关闭数据库连接
    except:
        # 输出异常信息
        traceback.print_exc()
        # 如果发生异常，则回滚
        conn.rollback()
    finally:
        # 最终关闭数据库连接
        conn.close()
