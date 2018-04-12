# Copyright 2018 <PUT YOUR NAME/COMPANY HERE>
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

"""add_backup_field

Revision ID: 35ef45873963
Revises: 844352f9fe6f
Create Date: 2018-04-12 17:20:57.349215

"""

# revision identifiers, used by Alembic.
revision = '35ef45873963'
down_revision = '844352f9fe6f'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('lbaas_members', sa.Column(
        u'backup', sa.Boolean(), default=False, nullable=False))
