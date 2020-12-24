def log_request(req: 'flask_request', res: str) -> None:
    """ """
    with open('walking.log','a') as log:
        print(req.form, req.remote_addr, req.user_agent, res, file=log, sep='|')
