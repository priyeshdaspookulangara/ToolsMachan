from .tasks import run_payroll_task

class PayrollEngine:
    def queue_payroll_run(self, payroll_run):
        """
        Queues a payroll run to be executed by a Celery worker.
        """
        run_payroll_task.delay(payroll_run.id)
