#
# Copyright 2022 DMetaSoul
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

class Flow:
    @classmethod
    def _add_subargparser(cls, subparsers):
        command_parser = subparsers.add_parser('flow', help='metaspore flow management')
        command_parser.set_defaults(command_executor=cls._execute_flow)
        subcommand_parsers = command_parser.add_subparsers(dest='subcommand_name')
        up_parser = subcommand_parsers.add_parser('up', help='start metaspore flow')
        up_parser.set_defaults(subcommand_executor=cls._execute_flow_up)
        down_parser = subcommand_parsers.add_parser('down', help='stop metaspore flow')
        down_parser.set_defaults(subcommand_executor=cls._execute_flow_down)
        update_parser = subcommand_parsers.add_parser('update', help='update metaspore flow')
        update_parser.set_defaults(subcommand_executor=cls._execute_flow_update)
        status_parser = subcommand_parsers.add_parser('status', help='show metaspore flow status')
        status_parser.set_defaults(subcommand_executor=cls._execute_flow_status)

    @classmethod
    def _execute_flow(cls, args):
        print('no flow command specified')

    @classmethod
    def _execute_flow_up(cls, args):
        print('flow up ...')

    @classmethod
    def _execute_flow_down(cls, args):
        print('flow down ...')

    @classmethod
    def _execute_flow_update(cls, args):
        print('flow update ...')

    @classmethod
    def _execute_flow_status(cls, args):
        print('flow status ...')
