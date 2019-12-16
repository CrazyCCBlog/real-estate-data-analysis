import logging
import os
from apscheduler.schedulers.blocking import BlockingScheduler

logger = logging.getLogger('tasks')
FORMAT = '%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s'
logging.basicConfig(filename=os.getcwd() + '/log/tasks.log', filemode='a', format=FORMAT)
logger.setLevel(logging.INFO)


def run_task_scrapper(params):
    logger.info("Starting executing crawller with params: {}".format(params))

    cw = os.getcwd()
    path = '/imoveis_crawling'
    scrapper_path = cw + os.path.join(path)

    if scrapper_path:
        os.chdir(scrapper_path)
        command = 'scrapy crawl OLX  {}'.format(params)
        os.system(command)

    os.chdir(cw)
    logger.info("Job concluded!")


if __name__ == "__main__":
    logger.info("Starting program")

    scheduler = BlockingScheduler(timezone="UTC")

    scheduler.add_job(run_task_scrapper, 'cron', hour='17', minute='24',
                      args=["-a category=aluguel -a region=grande-goiania-e-anapolis -a state=go"])
    scheduler.add_job(run_task_scrapper, 'cron', hour='16', minute='24',
                      args=["-a category=venda -a region=grande-goiania-e-anapolis -a state=go"])

    try:
        logger.info("Starting jobs")
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        scheduler.remove_all_jobs()
        logger.info("All jobs have been removed")
