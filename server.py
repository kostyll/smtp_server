# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from secure_smtpd import (
        SMTPServer,
        FakeCredentialValidator,
    )

import argparse

class AuthSMTPServer(SMTPServer):

    def process_message(self, peer, mailfrom, rcpttos, message_data):
        print message_data


class ConfiguredServer(object):

    def __init__(self,port):
        self.server=AuthSMTPServer(
                    ('0.0.0.0', port),
                    None,
                    require_authentication=True,
                    ssl=False,
                    credential_validator=FakeCredentialValidator(),
                    maximum_execution_time=1.0
                )


def start_server(port):
    server = ConfiguredServer(port)
    server.server.run()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '-p',
            action='store',
            dest='port',
            type=int,
            help='port to bind lo bcoe:foobar@localhost'
        )
    args = parser.parse_args()
    if args.port is None:
        parser.print_help()
        return
    start_server(args.port)

if __name__ == "__main__":
    main()


