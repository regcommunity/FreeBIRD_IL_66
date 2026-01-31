# coding=UTF-8
# Copyright (c) 2025 Arfa Digital Consulting
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License 2.0
# which accompanies this distribution, and is available at
# https://www.eclipse.org/legal/epl-2.0/
#
# SPDX-License-Identifier: EPL-2.0
#
# Contributors:
#    Auto-generated from ECB logical transformation rules
#
"""
Auto-generated derivation for CRDT_FCLTY.DFLT_STTS_DRVD.

This file was generated from ECB sddlogicaltransformationrule data.
Manual edits may be overwritten when regenerating.
"""
  
from django.db import models
from pybirdai.annotations.decorators import lineage
from dateutil.relativedelta import relativedelta

class CRDT_FCLTY(models.Model):
    """Auto-generated derivation for DFLT_STTS_DRVD."""

    @property
    @lineage(dependencies={'CRDT_FCLTY_EIL.DFLT_STTS_DRVD', 'INSTRMNT_RL_IL.DFLT_STTS', 'PRTY_IL.DFLT_STTS'})
    def DFLT_STTS_DRVD(self):
        """
        Auto-generated from rule: DFLT_STTS_DRVD_TR
        Source: IL -> EIL
        
        Original algorithm:
        SET BIRD_CRDT_FCLTY_EIL.DFLT_STTS_DRVD = 
              CASE
                WHEN BIRD_INSTRMNT_RL_IL.DFLT_STTS IN (18, 19, 20)
                OR BIRD_PRTY_IL.DFLT_STTS IN (18, 19, 20)
                THEN 6
                ELSE 14
              END;
        """
        # Initialize fields from related tables
        prty_dflt_stts = self.thePRTY.DFLT_STTS if self.thePRTY else None
        instrmnt_rl_dflt_stts = self.theINSTRMNT_RL.DFLT_STTS if self.theINSTRMNT_RL else None
        if (instrmnt_rl_dflt_stts in (18, 19, 20) or prty_dflt_stts in (18, 19, 20)):
            return 6
        else:
            return 14

    class Meta:
        pass
