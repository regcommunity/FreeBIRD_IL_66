# Copyright (c) 2025 Contributors to the Eclipse Foundation
#
# See the NOTICE file(s) distributed with this work for additional
# information regarding copyright owners.
#
# This program and the accompanying materials are made available under the
# terms of the Eclipse Public License 2.0 which is available at
# https://www.eclipse.org/legal/epl-2.0
#
# SPDX-License-Identifier: EPL-2.0
"""
FINREP framework report cell definitions.

Auto-generated file containing cell classes for FINREP regulatory templates.
"""
from pybirdai.models.bird_data_model import *
from pybirdai.process_steps.pybird.orchestration import Orchestration
from pybirdai.annotations.decorators import lineage

# Import FINREP logic from templates
from pybirdai.process_steps.filter_code.templates.FINREP.joins.F_04_01_REF_FINREP_3_0_logic import *
from pybirdai.process_steps.filter_code.templates.FINREP.joins.F_05_01_REF_FINREP_3_0_logic import *

class Cell_F_04_01_REF_FINREP_3_0_67315_REF:
	F_04_01_REF_FINREP_3_0_Equity_instruments_security_Table = None
	F_04_01_REF_FINREP_3_0_Equity_instruments_instrument_Table = None
	F_04_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Equity_instruments_security.CRRYNG_AMNT", "Equity_instruments_instrument.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_04_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Equity_instruments_security.ACCNTNG_CLSSFCTN", "Equity_instruments_instrument.ACCNTNG_CLSSFCTN", "Equity_instruments_security.HLD_SL_INDCTR", "Equity_instruments_instrument.HLD_SL_INDCTR", "Equity_instruments_security.SBJCT_IMPRMNT_INDCTR", "Equity_instruments_instrument.SBJCT_IMPRMNT_INDCTR", "Equity_instruments_security.INSTTTNL_SCTR", "Equity_instruments_instrument.INSTTTNL_SCTR", "Equity_instruments_security.PRTY_RL_TYP", "Equity_instruments_instrument.PRTY_RL_TYP", "Equity_instruments_security.INSTRMNT_TYP_PRDCT", "Equity_instruments_instrument.INSTRMNT_TYP_PRDCT", "Equity_instruments_security.NGTBL_SCRTY_INDCTR", "Equity_instruments_instrument.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_04_01_REF_FINREP_3_0_Equity_instruments_security_Table
		if self.F_04_01_REF_FINREP_3_0_Equity_instruments_security_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Equity_instruments_security_Table.Equity_instruments_securitys
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['8'],
					item.INSTRMNT_TYP_PRDCT() in ['', '2'],
					item.NGTBL_SCRTY_INDCTR() in ['2', '1'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Equity_instruments_instrument_Table
		if self.F_04_01_REF_FINREP_3_0_Equity_instruments_instrument_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Equity_instruments_instrument_Table.Equity_instruments_instruments
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['8'],
					item.INSTRMNT_TYP_PRDCT() in ['', '2'],
					item.NGTBL_SCRTY_INDCTR() in ['2', '1'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_04_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_04_01_REF_FINREP_3_0_11112_REF:
	F_04_01_REF_FINREP_3_0_Equity_instruments_security_Table = None
	F_04_01_REF_FINREP_3_0_Equity_instruments_instrument_Table = None
	F_04_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Equity_instruments_security.CRRYNG_AMNT", "Equity_instruments_instrument.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_04_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Equity_instruments_security.ACCNTNG_CLSSFCTN", "Equity_instruments_instrument.ACCNTNG_CLSSFCTN", "Equity_instruments_security.HLD_SL_INDCTR", "Equity_instruments_instrument.HLD_SL_INDCTR", "Equity_instruments_security.SBJCT_IMPRMNT_INDCTR", "Equity_instruments_instrument.SBJCT_IMPRMNT_INDCTR", "Equity_instruments_security.INSTTTNL_SCTR", "Equity_instruments_instrument.INSTTTNL_SCTR", "Equity_instruments_security.PRTY_RL_TYP", "Equity_instruments_instrument.PRTY_RL_TYP", "Equity_instruments_security.INSTRMNT_TYP_PRDCT", "Equity_instruments_instrument.INSTRMNT_TYP_PRDCT", "Equity_instruments_security.NGTBL_SCRTY_INDCTR", "Equity_instruments_instrument.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_04_01_REF_FINREP_3_0_Equity_instruments_security_Table
		if self.F_04_01_REF_FINREP_3_0_Equity_instruments_security_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Equity_instruments_security_Table.Equity_instruments_securitys
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11', '', 'S121'],
					item.PRTY_RL_TYP() in ['8'],
					item.INSTRMNT_TYP_PRDCT() in ['', '2'],
					item.NGTBL_SCRTY_INDCTR() in ['2', '1'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Equity_instruments_instrument_Table
		if self.F_04_01_REF_FINREP_3_0_Equity_instruments_instrument_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Equity_instruments_instrument_Table.Equity_instruments_instruments
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11', '', 'S121'],
					item.PRTY_RL_TYP() in ['8'],
					item.INSTRMNT_TYP_PRDCT() in ['', '2'],
					item.NGTBL_SCRTY_INDCTR() in ['2', '1'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_04_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_04_01_REF_FINREP_3_0_11114_REF:
	F_04_01_REF_FINREP_3_0_Other_loans_Table = None
	F_04_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_04_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_04_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_04_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_04_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_04_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_04_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_04_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_04_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Debt_securities.SBJCT_IMPRMNT_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Credit_card_debt.INSTRMNT_TYP_PRDCT", "Trade_receivables.INSTRMNT_TYP_PRDCT", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT", "Finance_leases.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT", "Debt_securities.INSTRMNT_TYP_PRDCT", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_04_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_04_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_04_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_04_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_04_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_04_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_04_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_04_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_04_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_04_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_04_01_REF_FINREP_3_0_11089_REF:
	F_04_01_REF_FINREP_3_0s = []
	@lineage(dependencies={})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_04_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={})
	def calc_referenced_items(self):
		# ERROR: No TYP_INSTRMNT found for this combination
		pass

	def init(self):
		Orchestration().init(self)
		self.F_04_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_04_01_REF_FINREP_3_0_11106_REF:
	F_04_01_REF_FINREP_3_0s = []
	@lineage(dependencies={})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_04_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={})
	def calc_referenced_items(self):
		# ERROR: No TYP_INSTRMNT found for this combination
		pass

	def init(self):
		Orchestration().init(self)
		self.F_04_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_04_01_REF_FINREP_3_0_11082_REF:
	F_04_01_REF_FINREP_3_0_Other_loans_Table = None
	F_04_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_04_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_04_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_04_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_04_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_04_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_04_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_04_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_04_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Debt_securities.SBJCT_IMPRMNT_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Credit_card_debt.INSTRMNT_TYP_PRDCT", "Trade_receivables.INSTRMNT_TYP_PRDCT", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT", "Finance_leases.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT", "Debt_securities.INSTRMNT_TYP_PRDCT", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_04_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_04_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_04_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_04_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_04_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_04_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_04_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_04_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_04_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_04_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_04_01_REF_FINREP_3_0_11090_REF:
	F_04_01_REF_FINREP_3_0_Equity_instruments_security_Table = None
	F_04_01_REF_FINREP_3_0_Equity_instruments_instrument_Table = None
	F_04_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Equity_instruments_security.CRRYNG_AMNT", "Equity_instruments_instrument.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_04_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Equity_instruments_security.ACCNTNG_CLSSFCTN", "Equity_instruments_instrument.ACCNTNG_CLSSFCTN", "Equity_instruments_security.HLD_SL_INDCTR", "Equity_instruments_instrument.HLD_SL_INDCTR", "Equity_instruments_security.SBJCT_IMPRMNT_INDCTR", "Equity_instruments_instrument.SBJCT_IMPRMNT_INDCTR", "Equity_instruments_security.INSTTTNL_SCTR", "Equity_instruments_instrument.INSTTTNL_SCTR", "Equity_instruments_security.PRTY_RL_TYP", "Equity_instruments_instrument.PRTY_RL_TYP", "Equity_instruments_security.INSTRMNT_TYP_PRDCT", "Equity_instruments_instrument.INSTRMNT_TYP_PRDCT", "Equity_instruments_security.NGTBL_SCRTY_INDCTR", "Equity_instruments_instrument.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_04_01_REF_FINREP_3_0_Equity_instruments_security_Table
		if self.F_04_01_REF_FINREP_3_0_Equity_instruments_security_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Equity_instruments_security_Table.Equity_instruments_securitys
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['8'],
					item.INSTRMNT_TYP_PRDCT() in ['', '2'],
					item.NGTBL_SCRTY_INDCTR() in ['2', '1'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Equity_instruments_instrument_Table
		if self.F_04_01_REF_FINREP_3_0_Equity_instruments_instrument_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Equity_instruments_instrument_Table.Equity_instruments_instruments
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['8'],
					item.INSTRMNT_TYP_PRDCT() in ['', '2'],
					item.NGTBL_SCRTY_INDCTR() in ['2', '1'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_04_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_04_01_REF_FINREP_3_0_11084_REF:
	F_04_01_REF_FINREP_3_0_Equity_instruments_security_Table = None
	F_04_01_REF_FINREP_3_0_Equity_instruments_instrument_Table = None
	F_04_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Equity_instruments_security.CRRYNG_AMNT", "Equity_instruments_instrument.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_04_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Equity_instruments_security.ACCNTNG_CLSSFCTN", "Equity_instruments_instrument.ACCNTNG_CLSSFCTN", "Equity_instruments_security.HLD_SL_INDCTR", "Equity_instruments_instrument.HLD_SL_INDCTR", "Equity_instruments_security.SBJCT_IMPRMNT_INDCTR", "Equity_instruments_instrument.SBJCT_IMPRMNT_INDCTR", "Equity_instruments_security.MLTLTRL_DVLPMNT_BNK_INDCTR", "Equity_instruments_instrument.MLTLTRL_DVLPMNT_BNK_INDCTR", "Equity_instruments_security.PRTY_RL_TYP", "Equity_instruments_instrument.PRTY_RL_TYP", "Equity_instruments_security.INSTRMNT_TYP_PRDCT", "Equity_instruments_instrument.INSTRMNT_TYP_PRDCT", "Equity_instruments_security.NGTBL_SCRTY_INDCTR", "Equity_instruments_instrument.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_04_01_REF_FINREP_3_0_Equity_instruments_security_Table
		if self.F_04_01_REF_FINREP_3_0_Equity_instruments_security_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Equity_instruments_security_Table.Equity_instruments_securitys
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['8'],
					item.INSTRMNT_TYP_PRDCT() in ['', '2'],
					item.NGTBL_SCRTY_INDCTR() in ['2', '1'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Equity_instruments_instrument_Table
		if self.F_04_01_REF_FINREP_3_0_Equity_instruments_instrument_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Equity_instruments_instrument_Table.Equity_instruments_instruments
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['8'],
					item.INSTRMNT_TYP_PRDCT() in ['', '2'],
					item.NGTBL_SCRTY_INDCTR() in ['2', '1'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_04_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_04_01_REF_FINREP_3_0_11091_REF:
	F_04_01_REF_FINREP_3_0_Other_loans_Table = None
	F_04_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_04_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_04_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_04_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_04_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_04_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_04_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_04_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_04_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Debt_securities.SBJCT_IMPRMNT_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Credit_card_debt.INSTRMNT_TYP_PRDCT", "Trade_receivables.INSTRMNT_TYP_PRDCT", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT", "Finance_leases.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT", "Debt_securities.INSTRMNT_TYP_PRDCT", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_04_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_04_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_04_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_04_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_04_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_04_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_04_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_04_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_04_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_04_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_04_01_REF_FINREP_3_0_67314_REF:
	F_04_01_REF_FINREP_3_0s = []
	@lineage(dependencies={})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_04_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={})
	def calc_referenced_items(self):
		# ERROR: No TYP_INSTRMNT found for this combination
		pass

	def init(self):
		Orchestration().init(self)
		self.F_04_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_04_01_REF_FINREP_3_0_11083_REF:
	F_04_01_REF_FINREP_3_0s = []
	@lineage(dependencies={})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_04_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={})
	def calc_referenced_items(self):
		# ERROR: No TYP_INSTRMNT found for this combination
		pass

	def init(self):
		Orchestration().init(self)
		self.F_04_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_04_01_REF_FINREP_3_0_11088_REF:
	F_04_01_REF_FINREP_3_0_Other_loans_Table = None
	F_04_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_04_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_04_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_04_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_04_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_04_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_04_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_04_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_04_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Debt_securities.SBJCT_IMPRMNT_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Credit_card_debt.INSTRMNT_TYP_PRDCT", "Trade_receivables.INSTRMNT_TYP_PRDCT", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT", "Finance_leases.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT", "Debt_securities.INSTRMNT_TYP_PRDCT", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_04_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_04_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_04_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_04_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_04_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_04_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_04_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_04_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_04_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_04_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_04_01_REF_FINREP_3_0_11087_REF:
	F_04_01_REF_FINREP_3_0_Other_loans_Table = None
	F_04_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_04_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_04_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_04_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_04_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_04_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_04_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_04_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_04_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Debt_securities.SBJCT_IMPRMNT_INDCTR", "Other_loans.MLTLTRL_DVLPMNT_BNK_INDCTR", "Credit_card_debt.MLTLTRL_DVLPMNT_BNK_INDCTR", "Trade_receivables.MLTLTRL_DVLPMNT_BNK_INDCTR", "Advances_that_are_not_loans.MLTLTRL_DVLPMNT_BNK_INDCTR", "Finance_leases.MLTLTRL_DVLPMNT_BNK_INDCTR", "On_demand_and_short_notice.MLTLTRL_DVLPMNT_BNK_INDCTR", "Reverse_repurchase_agreements.MLTLTRL_DVLPMNT_BNK_INDCTR", "Debt_securities.MLTLTRL_DVLPMNT_BNK_INDCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Credit_card_debt.INSTRMNT_TYP_PRDCT", "Trade_receivables.INSTRMNT_TYP_PRDCT", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT", "Finance_leases.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT", "Debt_securities.INSTRMNT_TYP_PRDCT", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_04_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_04_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_04_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_04_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_04_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_04_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_04_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_04_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_04_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_04_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_04_01_REF_FINREP_3_0_11108_REF:
	F_04_01_REF_FINREP_3_0_Derivatives_ETC_Table = None
	F_04_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Derivatives_ETC.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_04_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Derivatives_ETC.ACCNTNG_CLSSFCTN", "Derivatives_ETC.HLD_SL_INDCTR", "Derivatives_ETC.SBJCT_IMPRMNT_INDCTR", "Derivatives_ETC.INSTTTNL_SCTR", "Derivatives_ETC.PRTY_RL_TYP", "Derivatives_ETC.INSTRMNT_TYP_PRDCT"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_04_01_REF_FINREP_3_0_Derivatives_ETC_Table
		if self.F_04_01_REF_FINREP_3_0_Derivatives_ETC_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Derivatives_ETC_Table.Derivatives_ETCs
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['20', '14'],
					item.INSTRMNT_TYP_PRDCT() in ['9', '10', '380', '8', '6', '7', '5'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_04_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_04_01_REF_FINREP_3_0_11110_REF:
	F_04_01_REF_FINREP_3_0s = []
	@lineage(dependencies={})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_04_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={})
	def calc_referenced_items(self):
		# ERROR: No TYP_INSTRMNT found for this combination
		pass

	def init(self):
		Orchestration().init(self)
		self.F_04_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_04_01_REF_FINREP_3_0_11081_REF:
	F_04_01_REF_FINREP_3_0s = []
	@lineage(dependencies={})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_04_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={})
	def calc_referenced_items(self):
		# ERROR: No TYP_INSTRMNT found for this combination
		pass

	def init(self):
		Orchestration().init(self)
		self.F_04_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_04_01_REF_FINREP_3_0_11086_REF:
	F_04_01_REF_FINREP_3_0s = []
	@lineage(dependencies={})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_04_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={})
	def calc_referenced_items(self):
		# ERROR: No TYP_INSTRMNT found for this combination
		pass

	def init(self):
		Orchestration().init(self)
		self.F_04_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_04_01_REF_FINREP_3_0_11085_REF:
	F_04_01_REF_FINREP_3_0_Other_loans_Table = None
	F_04_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_04_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_04_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_04_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_04_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_04_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_04_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_04_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_04_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Debt_securities.SBJCT_IMPRMNT_INDCTR", "Other_loans.MLTLTRL_DVLPMNT_BNK_INDCTR", "Credit_card_debt.MLTLTRL_DVLPMNT_BNK_INDCTR", "Trade_receivables.MLTLTRL_DVLPMNT_BNK_INDCTR", "Advances_that_are_not_loans.MLTLTRL_DVLPMNT_BNK_INDCTR", "Finance_leases.MLTLTRL_DVLPMNT_BNK_INDCTR", "On_demand_and_short_notice.MLTLTRL_DVLPMNT_BNK_INDCTR", "Reverse_repurchase_agreements.MLTLTRL_DVLPMNT_BNK_INDCTR", "Debt_securities.MLTLTRL_DVLPMNT_BNK_INDCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Credit_card_debt.INSTRMNT_TYP_PRDCT", "Trade_receivables.INSTRMNT_TYP_PRDCT", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT", "Finance_leases.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT", "Debt_securities.INSTRMNT_TYP_PRDCT", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_04_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_04_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_04_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_04_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_04_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_04_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_04_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_04_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_04_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_04_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_04_01_REF_FINREP_3_0_67316_REF:
	F_04_01_REF_FINREP_3_0_Other_loans_Table = None
	F_04_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_04_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_04_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_04_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_04_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_04_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_04_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_04_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_04_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Debt_securities.SBJCT_IMPRMNT_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Credit_card_debt.INSTRMNT_TYP_PRDCT", "Trade_receivables.INSTRMNT_TYP_PRDCT", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT", "Finance_leases.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT", "Debt_securities.INSTRMNT_TYP_PRDCT", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_04_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_04_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_04_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_04_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_04_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_04_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_04_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_04_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)
		# Process F_04_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_04_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_04_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.ACCNTNG_CLSSFCTN() in ['2'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_04_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_04_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None


class Cell_F_05_01_REF_FINREP_3_0_408956_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.GRSS_CRRYNG_AMNT", "Credit_card_debt.GRSS_CRRYNG_AMNT", "Trade_receivables.GRSS_CRRYNG_AMNT", "Advances_that_are_not_loans.GRSS_CRRYNG_AMNT", "Finance_leases.GRSS_CRRYNG_AMNT", "On_demand_and_short_notice.GRSS_CRRYNG_AMNT", "Reverse_repurchase_agreements.GRSS_CRRYNG_AMNT", "Debt_securities.GRSS_CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.GRSS_CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS", "Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Debt_securities.SBJCT_IMPRMNT_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Credit_card_debt.INSTRMNT_TYP_PRDCT", "Trade_receivables.INSTRMNT_TYP_PRDCT", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT", "Finance_leases.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT", "Debt_securities.INSTRMNT_TYP_PRDCT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152439_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS", "Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Debt_securities.SBJCT_IMPRMNT_INDCTR", "Other_loans.MLTLTRL_DVLPMNT_BNK_INDCTR", "Credit_card_debt.MLTLTRL_DVLPMNT_BNK_INDCTR", "Trade_receivables.MLTLTRL_DVLPMNT_BNK_INDCTR", "Advances_that_are_not_loans.MLTLTRL_DVLPMNT_BNK_INDCTR", "Finance_leases.MLTLTRL_DVLPMNT_BNK_INDCTR", "On_demand_and_short_notice.MLTLTRL_DVLPMNT_BNK_INDCTR", "Reverse_repurchase_agreements.MLTLTRL_DVLPMNT_BNK_INDCTR", "Debt_securities.MLTLTRL_DVLPMNT_BNK_INDCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Credit_card_debt.INSTRMNT_TYP_PRDCT", "Trade_receivables.INSTRMNT_TYP_PRDCT", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT", "Finance_leases.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT", "Debt_securities.INSTRMNT_TYP_PRDCT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152430_REF:
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Advances_that_are_not_loans.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Advances_that_are_not_loans.PRPS", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.MLTLTRL_DVLPMNT_BNK_INDCTR", "Advances_that_are_not_loans.PRTY_RL_TYP", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['130', '140'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152591_REF:
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Trade_receivables.GRSS_CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.GRSS_CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Trade_receivables.PRPS", "Trade_receivables.ACCNTNG_CLSSFCTN", "Trade_receivables.HLD_SL_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.INSTTTNL_SCTR", "Trade_receivables.PRTY_RL_TYP", "Trade_receivables.MN_DBTR_INDCTR", "Trade_receivables.INSTRMNT_TYP_PRDCT"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['1023', '1020'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_408950_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS", "Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Debt_securities.SBJCT_IMPRMNT_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Credit_card_debt.INSTRMNT_TYP_PRDCT", "Trade_receivables.INSTRMNT_TYP_PRDCT", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT", "Finance_leases.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT", "Debt_securities.INSTRMNT_TYP_PRDCT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152464_REF:
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"On_demand_and_short_notice.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"On_demand_and_short_notice.PRPS", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.HLD_SL_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "On_demand_and_short_notice.PRTY_RL_TYP", "On_demand_and_short_notice.MN_DBTR_INDCTR", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.RPYMNT_RGHTS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['511', '1201', '1202', '522'],
					item.RPYMNT_RGHTS() in ['1'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152443_REF:
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Finance_leases.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Finance_leases.PRPS", "Finance_leases.ACCNTNG_CLSSFCTN", "Finance_leases.HLD_SL_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "Finance_leases.PRTY_RL_TYP", "Finance_leases.MN_DBTR_INDCTR", "Finance_leases.INSTTTNL_SCTR", "Finance_leases.INSTRMNT_TYP_PRDCT"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152453_REF:
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Advances_that_are_not_loans.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Advances_that_are_not_loans.PRPS", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Advances_that_are_not_loans.PRTY_RL_TYP", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['130', '140'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_408952_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS", "Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Debt_securities.SBJCT_IMPRMNT_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Credit_card_debt.INSTRMNT_TYP_PRDCT", "Trade_receivables.INSTRMNT_TYP_PRDCT", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT", "Finance_leases.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT", "Debt_securities.INSTRMNT_TYP_PRDCT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152418_REF:
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Reverse_repurchase_agreements.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Reverse_repurchase_agreements.PRPS", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['1003'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152426_REF:
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Trade_receivables.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Trade_receivables.PRPS", "Trade_receivables.ACCNTNG_CLSSFCTN", "Trade_receivables.HLD_SL_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.MLTLTRL_DVLPMNT_BNK_INDCTR", "Trade_receivables.PRTY_RL_TYP", "Trade_receivables.MN_DBTR_INDCTR", "Trade_receivables.INSTRMNT_TYP_PRDCT"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['1023', '1020'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152429_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS", "Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Debt_securities.SBJCT_IMPRMNT_INDCTR", "Other_loans.MLTLTRL_DVLPMNT_BNK_INDCTR", "Credit_card_debt.MLTLTRL_DVLPMNT_BNK_INDCTR", "Trade_receivables.MLTLTRL_DVLPMNT_BNK_INDCTR", "Advances_that_are_not_loans.MLTLTRL_DVLPMNT_BNK_INDCTR", "Finance_leases.MLTLTRL_DVLPMNT_BNK_INDCTR", "On_demand_and_short_notice.MLTLTRL_DVLPMNT_BNK_INDCTR", "Reverse_repurchase_agreements.MLTLTRL_DVLPMNT_BNK_INDCTR", "Debt_securities.MLTLTRL_DVLPMNT_BNK_INDCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Credit_card_debt.INSTRMNT_TYP_PRDCT", "Trade_receivables.INSTRMNT_TYP_PRDCT", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT", "Finance_leases.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT", "Debt_securities.INSTRMNT_TYP_PRDCT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_408955_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.GRSS_CRRYNG_AMNT", "Credit_card_debt.GRSS_CRRYNG_AMNT", "Trade_receivables.GRSS_CRRYNG_AMNT", "Advances_that_are_not_loans.GRSS_CRRYNG_AMNT", "Finance_leases.GRSS_CRRYNG_AMNT", "On_demand_and_short_notice.GRSS_CRRYNG_AMNT", "Reverse_repurchase_agreements.GRSS_CRRYNG_AMNT", "Debt_securities.GRSS_CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.GRSS_CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS", "Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Debt_securities.SBJCT_IMPRMNT_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Credit_card_debt.INSTRMNT_TYP_PRDCT", "Trade_receivables.INSTRMNT_TYP_PRDCT", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT", "Finance_leases.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT", "Debt_securities.INSTRMNT_TYP_PRDCT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152440_REF:
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Advances_that_are_not_loans.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Advances_that_are_not_loans.PRPS", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.PRTY_RL_TYP", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['130', '140'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152590_REF:
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Reverse_repurchase_agreements.GRSS_CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.GRSS_CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Reverse_repurchase_agreements.PRPS", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['1003'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_408946_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS", "Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Debt_securities.SBJCT_IMPRMNT_INDCTR", "Other_loans.MLTLTRL_DVLPMNT_BNK_INDCTR", "Credit_card_debt.MLTLTRL_DVLPMNT_BNK_INDCTR", "Trade_receivables.MLTLTRL_DVLPMNT_BNK_INDCTR", "Advances_that_are_not_loans.MLTLTRL_DVLPMNT_BNK_INDCTR", "Finance_leases.MLTLTRL_DVLPMNT_BNK_INDCTR", "On_demand_and_short_notice.MLTLTRL_DVLPMNT_BNK_INDCTR", "Reverse_repurchase_agreements.MLTLTRL_DVLPMNT_BNK_INDCTR", "Debt_securities.MLTLTRL_DVLPMNT_BNK_INDCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Credit_card_debt.INSTRMNT_TYP_PRDCT", "Trade_receivables.INSTRMNT_TYP_PRDCT", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT", "Finance_leases.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT", "Debt_securities.INSTRMNT_TYP_PRDCT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152445_REF:
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Reverse_repurchase_agreements.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Reverse_repurchase_agreements.PRPS", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['1003'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_408951_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS", "Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Debt_securities.SBJCT_IMPRMNT_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Credit_card_debt.INSTRMNT_TYP_PRDCT", "Trade_receivables.INSTRMNT_TYP_PRDCT", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT", "Finance_leases.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT", "Debt_securities.INSTRMNT_TYP_PRDCT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152463_REF:
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Advances_that_are_not_loans.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Advances_that_are_not_loans.PRPS", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Advances_that_are_not_loans.PRTY_RL_TYP", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['130', '140'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152452_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS", "Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Debt_securities.SBJCT_IMPRMNT_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Credit_card_debt.INSTRMNT_TYP_PRDCT", "Trade_receivables.INSTRMNT_TYP_PRDCT", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT", "Finance_leases.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT", "Debt_securities.INSTRMNT_TYP_PRDCT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152424_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Non_Negotiable_bonds.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.PRPS", "Non_Negotiable_bonds.PRPS", "Other_loans.ACCNTNG_CLSSFCTN", "Non_Negotiable_bonds.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Non_Negotiable_bonds.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Non_Negotiable_bonds.SBJCT_IMPRMNT_INDCTR", "Other_loans.MLTLTRL_DVLPMNT_BNK_INDCTR", "Non_Negotiable_bonds.MLTLTRL_DVLPMNT_BNK_INDCTR", "Other_loans.PRTY_RL_TYP", "Non_Negotiable_bonds.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Non_Negotiable_bonds.MN_DBTR_INDCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Non_Negotiable_bonds.INSTRMNT_TYP_PRDCT", "Other_loans.RPYMNT_RGHTS", "Non_Negotiable_bonds.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Non_Negotiable_bonds.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['1022'],
					item.RPYMNT_RGHTS() in ['2'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table
		if self.F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table.Non_Negotiable_bondss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['1022'],
					item.RPYMNT_RGHTS() in ['2'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152600_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.GRSS_CRRYNG_AMNT", "Credit_card_debt.GRSS_CRRYNG_AMNT", "Trade_receivables.GRSS_CRRYNG_AMNT", "Advances_that_are_not_loans.GRSS_CRRYNG_AMNT", "Finance_leases.GRSS_CRRYNG_AMNT", "On_demand_and_short_notice.GRSS_CRRYNG_AMNT", "Reverse_repurchase_agreements.GRSS_CRRYNG_AMNT", "Debt_securities.GRSS_CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.GRSS_CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS", "Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Debt_securities.SBJCT_IMPRMNT_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Credit_card_debt.INSTRMNT_TYP_PRDCT", "Trade_receivables.INSTRMNT_TYP_PRDCT", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT", "Finance_leases.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT", "Debt_securities.INSTRMNT_TYP_PRDCT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['1'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['1'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['1'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['1'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['1'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['1'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['1'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['1'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152420_REF:
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Advances_that_are_not_loans.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Advances_that_are_not_loans.PRPS", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.MLTLTRL_DVLPMNT_BNK_INDCTR", "Advances_that_are_not_loans.PRTY_RL_TYP", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['130', '140'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_408947_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS", "Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Debt_securities.SBJCT_IMPRMNT_INDCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Credit_card_debt.INSTRMNT_TYP_PRDCT", "Trade_receivables.INSTRMNT_TYP_PRDCT", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT", "Finance_leases.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT", "Debt_securities.INSTRMNT_TYP_PRDCT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152423_REF:
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Finance_leases.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Finance_leases.PRPS", "Finance_leases.ACCNTNG_CLSSFCTN", "Finance_leases.HLD_SL_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "Finance_leases.MLTLTRL_DVLPMNT_BNK_INDCTR", "Finance_leases.PRTY_RL_TYP", "Finance_leases.MN_DBTR_INDCTR", "Finance_leases.INSTRMNT_TYP_PRDCT"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_408949_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS", "Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Debt_securities.SBJCT_IMPRMNT_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Credit_card_debt.INSTRMNT_TYP_PRDCT", "Trade_receivables.INSTRMNT_TYP_PRDCT", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT", "Finance_leases.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT", "Debt_securities.INSTRMNT_TYP_PRDCT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152465_REF:
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Credit_card_debt.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Credit_card_debt.PRPS", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Credit_card_debt.HLD_SL_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.INSTTTNL_SCTR", "Credit_card_debt.PRTY_RL_TYP", "Credit_card_debt.MN_DBTR_INDCTR", "Credit_card_debt.INSTRMNT_TYP_PRDCT"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['51'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152417_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Non_Negotiable_bonds.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.PRPS", "Non_Negotiable_bonds.PRPS", "Other_loans.ACCNTNG_CLSSFCTN", "Non_Negotiable_bonds.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Non_Negotiable_bonds.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Non_Negotiable_bonds.SBJCT_IMPRMNT_INDCTR", "Other_loans.INSTTTNL_SCTR", "Non_Negotiable_bonds.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Non_Negotiable_bonds.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Non_Negotiable_bonds.MN_DBTR_INDCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Non_Negotiable_bonds.INSTRMNT_TYP_PRDCT", "Other_loans.RPYMNT_RGHTS", "Non_Negotiable_bonds.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Non_Negotiable_bonds.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['1022'],
					item.RPYMNT_RGHTS() in ['2'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table
		if self.F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table.Non_Negotiable_bondss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['1022'],
					item.RPYMNT_RGHTS() in ['2'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152457_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Non_Negotiable_bonds.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.PRPS", "Non_Negotiable_bonds.PRPS", "Other_loans.ACCNTNG_CLSSFCTN", "Non_Negotiable_bonds.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Non_Negotiable_bonds.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Non_Negotiable_bonds.SBJCT_IMPRMNT_INDCTR", "Other_loans.INSTTTNL_SCTR", "Non_Negotiable_bonds.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Non_Negotiable_bonds.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Non_Negotiable_bonds.MN_DBTR_INDCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Non_Negotiable_bonds.INSTRMNT_TYP_PRDCT", "Other_loans.RPYMNT_RGHTS", "Non_Negotiable_bonds.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Non_Negotiable_bonds.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['1022'],
					item.RPYMNT_RGHTS() in ['2'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table
		if self.F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table.Non_Negotiable_bondss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['1022'],
					item.RPYMNT_RGHTS() in ['2'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152454_REF:
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"On_demand_and_short_notice.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"On_demand_and_short_notice.PRPS", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.HLD_SL_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "On_demand_and_short_notice.PRTY_RL_TYP", "On_demand_and_short_notice.MN_DBTR_INDCTR", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.RPYMNT_RGHTS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['511', '1201', '1202', '522'],
					item.RPYMNT_RGHTS() in ['1'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152416_REF:
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Finance_leases.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Finance_leases.PRPS", "Finance_leases.ACCNTNG_CLSSFCTN", "Finance_leases.HLD_SL_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "Finance_leases.INSTTTNL_SCTR", "Finance_leases.PRTY_RL_TYP", "Finance_leases.MN_DBTR_INDCTR", "Finance_leases.INSTRMNT_TYP_PRDCT"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_408948_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS", "Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Debt_securities.SBJCT_IMPRMNT_INDCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Credit_card_debt.INSTRMNT_TYP_PRDCT", "Trade_receivables.INSTRMNT_TYP_PRDCT", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT", "Finance_leases.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT", "Debt_securities.INSTRMNT_TYP_PRDCT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152598_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.GRSS_CRRYNG_AMNT", "Credit_card_debt.GRSS_CRRYNG_AMNT", "Trade_receivables.GRSS_CRRYNG_AMNT", "Advances_that_are_not_loans.GRSS_CRRYNG_AMNT", "Finance_leases.GRSS_CRRYNG_AMNT", "On_demand_and_short_notice.GRSS_CRRYNG_AMNT", "Reverse_repurchase_agreements.GRSS_CRRYNG_AMNT", "Debt_securities.GRSS_CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.GRSS_CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS", "Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Debt_securities.SBJCT_IMPRMNT_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Credit_card_debt.INSTRMNT_TYP_PRDCT", "Trade_receivables.INSTRMNT_TYP_PRDCT", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT", "Finance_leases.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT", "Debt_securities.INSTRMNT_TYP_PRDCT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152446_REF:
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Trade_receivables.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Trade_receivables.PRPS", "Trade_receivables.ACCNTNG_CLSSFCTN", "Trade_receivables.HLD_SL_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.PRTY_RL_TYP", "Trade_receivables.MN_DBTR_INDCTR", "Trade_receivables.INSTTTNL_SCTR", "Trade_receivables.INSTRMNT_TYP_PRDCT"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['1023', '1020'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152456_REF:
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Finance_leases.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Finance_leases.PRPS", "Finance_leases.ACCNTNG_CLSSFCTN", "Finance_leases.HLD_SL_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "Finance_leases.INSTTTNL_SCTR", "Finance_leases.PRTY_RL_TYP", "Finance_leases.MN_DBTR_INDCTR", "Finance_leases.INSTRMNT_TYP_PRDCT"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152588_REF:
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Finance_leases.GRSS_CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.GRSS_CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Finance_leases.PRPS", "Finance_leases.ACCNTNG_CLSSFCTN", "Finance_leases.HLD_SL_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "Finance_leases.INSTTTNL_SCTR", "Finance_leases.PRTY_RL_TYP", "Finance_leases.MN_DBTR_INDCTR", "Finance_leases.INSTRMNT_TYP_PRDCT"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152455_REF:
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Credit_card_debt.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Credit_card_debt.PRPS", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Credit_card_debt.HLD_SL_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.INSTTTNL_SCTR", "Credit_card_debt.PRTY_RL_TYP", "Credit_card_debt.MN_DBTR_INDCTR", "Credit_card_debt.INSTRMNT_TYP_PRDCT"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['51'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_408942_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS", "Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Debt_securities.SBJCT_IMPRMNT_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Credit_card_debt.INSTRMNT_TYP_PRDCT", "Trade_receivables.INSTRMNT_TYP_PRDCT", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT", "Finance_leases.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT", "Debt_securities.INSTRMNT_TYP_PRDCT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152441_REF:
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"On_demand_and_short_notice.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"On_demand_and_short_notice.PRPS", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.HLD_SL_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.PRTY_RL_TYP", "On_demand_and_short_notice.MN_DBTR_INDCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.RPYMNT_RGHTS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['511', '1201', '1202', '522'],
					item.RPYMNT_RGHTS() in ['1'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152449_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS", "Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Debt_securities.SBJCT_IMPRMNT_INDCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Credit_card_debt.INSTRMNT_TYP_PRDCT", "Trade_receivables.INSTRMNT_TYP_PRDCT", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT", "Finance_leases.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT", "Debt_securities.INSTRMNT_TYP_PRDCT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152466_REF:
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Finance_leases.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Finance_leases.PRPS", "Finance_leases.ACCNTNG_CLSSFCTN", "Finance_leases.HLD_SL_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "Finance_leases.INSTTTNL_SCTR", "Finance_leases.PRTY_RL_TYP", "Finance_leases.MN_DBTR_INDCTR", "Finance_leases.INSTRMNT_TYP_PRDCT"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_408945_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS", "Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Debt_securities.SBJCT_IMPRMNT_INDCTR", "Other_loans.MLTLTRL_DVLPMNT_BNK_INDCTR", "Credit_card_debt.MLTLTRL_DVLPMNT_BNK_INDCTR", "Trade_receivables.MLTLTRL_DVLPMNT_BNK_INDCTR", "Advances_that_are_not_loans.MLTLTRL_DVLPMNT_BNK_INDCTR", "Finance_leases.MLTLTRL_DVLPMNT_BNK_INDCTR", "On_demand_and_short_notice.MLTLTRL_DVLPMNT_BNK_INDCTR", "Reverse_repurchase_agreements.MLTLTRL_DVLPMNT_BNK_INDCTR", "Debt_securities.MLTLTRL_DVLPMNT_BNK_INDCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Credit_card_debt.INSTRMNT_TYP_PRDCT", "Trade_receivables.INSTRMNT_TYP_PRDCT", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT", "Finance_leases.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT", "Debt_securities.INSTRMNT_TYP_PRDCT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152589_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.GRSS_CRRYNG_AMNT", "Non_Negotiable_bonds.GRSS_CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.GRSS_CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.PRPS", "Non_Negotiable_bonds.PRPS", "Other_loans.ACCNTNG_CLSSFCTN", "Non_Negotiable_bonds.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Non_Negotiable_bonds.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Non_Negotiable_bonds.SBJCT_IMPRMNT_INDCTR", "Other_loans.INSTTTNL_SCTR", "Non_Negotiable_bonds.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Non_Negotiable_bonds.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Non_Negotiable_bonds.MN_DBTR_INDCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Non_Negotiable_bonds.INSTRMNT_TYP_PRDCT", "Other_loans.RPYMNT_RGHTS", "Non_Negotiable_bonds.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Non_Negotiable_bonds.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['1022'],
					item.RPYMNT_RGHTS() in ['2'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table
		if self.F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table.Non_Negotiable_bondss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['1022'],
					item.RPYMNT_RGHTS() in ['2'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152434_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Non_Negotiable_bonds.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.PRPS", "Non_Negotiable_bonds.PRPS", "Other_loans.ACCNTNG_CLSSFCTN", "Non_Negotiable_bonds.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Non_Negotiable_bonds.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Non_Negotiable_bonds.SBJCT_IMPRMNT_INDCTR", "Other_loans.MLTLTRL_DVLPMNT_BNK_INDCTR", "Non_Negotiable_bonds.MLTLTRL_DVLPMNT_BNK_INDCTR", "Other_loans.PRTY_RL_TYP", "Non_Negotiable_bonds.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Non_Negotiable_bonds.MN_DBTR_INDCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Non_Negotiable_bonds.INSTRMNT_TYP_PRDCT", "Other_loans.RPYMNT_RGHTS", "Non_Negotiable_bonds.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Non_Negotiable_bonds.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['1022'],
					item.RPYMNT_RGHTS() in ['2'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table
		if self.F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table.Non_Negotiable_bondss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['1022'],
					item.RPYMNT_RGHTS() in ['2'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152432_REF:
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Credit_card_debt.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Credit_card_debt.PRPS", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Credit_card_debt.HLD_SL_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.MLTLTRL_DVLPMNT_BNK_INDCTR", "Credit_card_debt.PRTY_RL_TYP", "Credit_card_debt.MN_DBTR_INDCTR", "Credit_card_debt.INSTRMNT_TYP_PRDCT"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['51'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152415_REF:
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Credit_card_debt.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Credit_card_debt.PRPS", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Credit_card_debt.HLD_SL_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.INSTTTNL_SCTR", "Credit_card_debt.PRTY_RL_TYP", "Credit_card_debt.MN_DBTR_INDCTR", "Credit_card_debt.INSTRMNT_TYP_PRDCT"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['51'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152585_REF:
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Advances_that_are_not_loans.GRSS_CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.GRSS_CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Advances_that_are_not_loans.PRPS", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Advances_that_are_not_loans.PRTY_RL_TYP", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['130', '140'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152444_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Non_Negotiable_bonds.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.PRPS", "Non_Negotiable_bonds.PRPS", "Other_loans.ACCNTNG_CLSSFCTN", "Non_Negotiable_bonds.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Non_Negotiable_bonds.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Non_Negotiable_bonds.SBJCT_IMPRMNT_INDCTR", "Other_loans.PRTY_RL_TYP", "Non_Negotiable_bonds.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Non_Negotiable_bonds.MN_DBTR_INDCTR", "Other_loans.INSTTTNL_SCTR", "Non_Negotiable_bonds.INSTTTNL_SCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Non_Negotiable_bonds.INSTRMNT_TYP_PRDCT", "Other_loans.RPYMNT_RGHTS", "Non_Negotiable_bonds.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Non_Negotiable_bonds.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['1022'],
					item.RPYMNT_RGHTS() in ['2'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table
		if self.F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table.Non_Negotiable_bondss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['1022'],
					item.RPYMNT_RGHTS() in ['2'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152601_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.GRSS_CRRYNG_AMNT", "Credit_card_debt.GRSS_CRRYNG_AMNT", "Trade_receivables.GRSS_CRRYNG_AMNT", "Advances_that_are_not_loans.GRSS_CRRYNG_AMNT", "Finance_leases.GRSS_CRRYNG_AMNT", "On_demand_and_short_notice.GRSS_CRRYNG_AMNT", "Reverse_repurchase_agreements.GRSS_CRRYNG_AMNT", "Debt_securities.GRSS_CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.GRSS_CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS", "Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Debt_securities.SBJCT_IMPRMNT_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Credit_card_debt.INSTRMNT_TYP_PRDCT", "Trade_receivables.INSTRMNT_TYP_PRDCT", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT", "Finance_leases.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT", "Debt_securities.INSTRMNT_TYP_PRDCT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['12'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['12'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['12'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['12'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['12'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['12'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['12'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['12'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152414_REF:
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"On_demand_and_short_notice.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"On_demand_and_short_notice.PRPS", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.HLD_SL_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "On_demand_and_short_notice.PRTY_RL_TYP", "On_demand_and_short_notice.MN_DBTR_INDCTR", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.RPYMNT_RGHTS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['511', '1201', '1202', '522'],
					item.RPYMNT_RGHTS() in ['1'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152421_REF:
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"On_demand_and_short_notice.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"On_demand_and_short_notice.PRPS", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.HLD_SL_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.MLTLTRL_DVLPMNT_BNK_INDCTR", "On_demand_and_short_notice.PRTY_RL_TYP", "On_demand_and_short_notice.MN_DBTR_INDCTR", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.RPYMNT_RGHTS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['511', '1201', '1202', '522'],
					item.RPYMNT_RGHTS() in ['1'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_441809_REF:
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Trade_receivables.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Trade_receivables.PRPS", "Trade_receivables.ACCNTNG_CLSSFCTN", "Trade_receivables.HLD_SL_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.INSTTTNL_SCTR", "Trade_receivables.PRTY_RL_TYP", "Trade_receivables.MN_DBTR_INDCTR", "Trade_receivables.INSTRMNT_TYP_PRDCT"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['1023', '1020'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152472_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS", "Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Debt_securities.SBJCT_IMPRMNT_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Credit_card_debt.INSTRMNT_TYP_PRDCT", "Trade_receivables.INSTRMNT_TYP_PRDCT", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT", "Finance_leases.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT", "Debt_securities.INSTRMNT_TYP_PRDCT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152458_REF:
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Reverse_repurchase_agreements.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Reverse_repurchase_agreements.PRPS", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['1003'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152431_REF:
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"On_demand_and_short_notice.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"On_demand_and_short_notice.PRPS", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.HLD_SL_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.MLTLTRL_DVLPMNT_BNK_INDCTR", "On_demand_and_short_notice.PRTY_RL_TYP", "On_demand_and_short_notice.MN_DBTR_INDCTR", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.RPYMNT_RGHTS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['511', '1201', '1202', '522'],
					item.RPYMNT_RGHTS() in ['1'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152435_REF:
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Reverse_repurchase_agreements.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Reverse_repurchase_agreements.PRPS", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.MLTLTRL_DVLPMNT_BNK_INDCTR", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['1003'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152442_REF:
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Credit_card_debt.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Credit_card_debt.PRPS", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Credit_card_debt.HLD_SL_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.PRTY_RL_TYP", "Credit_card_debt.MN_DBTR_INDCTR", "Credit_card_debt.INSTTTNL_SCTR", "Credit_card_debt.INSTRMNT_TYP_PRDCT"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['51'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152469_REF:
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Trade_receivables.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Trade_receivables.PRPS", "Trade_receivables.ACCNTNG_CLSSFCTN", "Trade_receivables.HLD_SL_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.INSTTTNL_SCTR", "Trade_receivables.PRTY_RL_TYP", "Trade_receivables.MN_DBTR_INDCTR", "Trade_receivables.INSTRMNT_TYP_PRDCT"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['1023', '1020'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152451_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS", "Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Debt_securities.SBJCT_IMPRMNT_INDCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Credit_card_debt.INSTRMNT_TYP_PRDCT", "Trade_receivables.INSTRMNT_TYP_PRDCT", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT", "Finance_leases.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT", "Debt_securities.INSTRMNT_TYP_PRDCT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['12'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['12'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['12'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['12'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['12'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['12'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['12'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['12'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152468_REF:
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Reverse_repurchase_agreements.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Reverse_repurchase_agreements.PRPS", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['1003'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152419_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS", "Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Debt_securities.SBJCT_IMPRMNT_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Credit_card_debt.INSTRMNT_TYP_PRDCT", "Trade_receivables.INSTRMNT_TYP_PRDCT", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT", "Finance_leases.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT", "Debt_securities.INSTRMNT_TYP_PRDCT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152413_REF:
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Advances_that_are_not_loans.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Advances_that_are_not_loans.PRPS", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Advances_that_are_not_loans.PRTY_RL_TYP", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['130', '140'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152459_REF:
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Trade_receivables.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Trade_receivables.PRPS", "Trade_receivables.ACCNTNG_CLSSFCTN", "Trade_receivables.HLD_SL_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.INSTTTNL_SCTR", "Trade_receivables.PRTY_RL_TYP", "Trade_receivables.MN_DBTR_INDCTR", "Trade_receivables.INSTRMNT_TYP_PRDCT"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['1023', '1020'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152425_REF:
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Reverse_repurchase_agreements.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Reverse_repurchase_agreements.PRPS", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.MLTLTRL_DVLPMNT_BNK_INDCTR", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['1003'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152586_REF:
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"On_demand_and_short_notice.GRSS_CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.GRSS_CRRYNG_AMNT()
		return total
	@lineage(dependencies={"On_demand_and_short_notice.PRPS", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.HLD_SL_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "On_demand_and_short_notice.PRTY_RL_TYP", "On_demand_and_short_notice.MN_DBTR_INDCTR", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.RPYMNT_RGHTS"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['511', '1201', '1202', '522'],
					item.RPYMNT_RGHTS() in ['1'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152584_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.GRSS_CRRYNG_AMNT", "Credit_card_debt.GRSS_CRRYNG_AMNT", "Trade_receivables.GRSS_CRRYNG_AMNT", "Advances_that_are_not_loans.GRSS_CRRYNG_AMNT", "Finance_leases.GRSS_CRRYNG_AMNT", "On_demand_and_short_notice.GRSS_CRRYNG_AMNT", "Reverse_repurchase_agreements.GRSS_CRRYNG_AMNT", "Debt_securities.GRSS_CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.GRSS_CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS", "Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Debt_securities.SBJCT_IMPRMNT_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Credit_card_debt.INSTRMNT_TYP_PRDCT", "Trade_receivables.INSTRMNT_TYP_PRDCT", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT", "Finance_leases.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT", "Debt_securities.INSTRMNT_TYP_PRDCT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152587_REF:
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Credit_card_debt.GRSS_CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.GRSS_CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Credit_card_debt.PRPS", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Credit_card_debt.HLD_SL_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.INSTTTNL_SCTR", "Credit_card_debt.PRTY_RL_TYP", "Credit_card_debt.MN_DBTR_INDCTR", "Credit_card_debt.INSTRMNT_TYP_PRDCT"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S123', 'S122_B2', 'S122_B1', 'S122_A_1', 'S122_A_2', 'S128', 'S129', 'S124', 'S126', 'S125_I', 'S125_C', 'S125_B', 'S125_D', 'S125_E', 'S125_A', 'S127', 'S1312', 'S1313', 'S1311', 'S1314', 'S11', 'S14_B', 'S14_A', 'S15', ''],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['51'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152422_REF:
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Credit_card_debt.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Credit_card_debt.PRPS", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Credit_card_debt.HLD_SL_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.MLTLTRL_DVLPMNT_BNK_INDCTR", "Credit_card_debt.PRTY_RL_TYP", "Credit_card_debt.MN_DBTR_INDCTR", "Credit_card_debt.INSTRMNT_TYP_PRDCT"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['51'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152436_REF:
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Trade_receivables.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Trade_receivables.PRPS", "Trade_receivables.ACCNTNG_CLSSFCTN", "Trade_receivables.HLD_SL_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.MLTLTRL_DVLPMNT_BNK_INDCTR", "Trade_receivables.PRTY_RL_TYP", "Trade_receivables.MN_DBTR_INDCTR", "Trade_receivables.INSTRMNT_TYP_PRDCT"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['1023', '1020'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152462_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS", "Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Debt_securities.SBJCT_IMPRMNT_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Credit_card_debt.INSTRMNT_TYP_PRDCT", "Trade_receivables.INSTRMNT_TYP_PRDCT", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT", "Finance_leases.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT", "Debt_securities.INSTRMNT_TYP_PRDCT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S11'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152450_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS", "Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Debt_securities.SBJCT_IMPRMNT_INDCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.INSTTTNL_SCTR", "Credit_card_debt.INSTTTNL_SCTR", "Trade_receivables.INSTTTNL_SCTR", "Advances_that_are_not_loans.INSTTTNL_SCTR", "Finance_leases.INSTTTNL_SCTR", "On_demand_and_short_notice.INSTTTNL_SCTR", "Reverse_repurchase_agreements.INSTTTNL_SCTR", "Debt_securities.INSTTTNL_SCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Credit_card_debt.INSTRMNT_TYP_PRDCT", "Trade_receivables.INSTRMNT_TYP_PRDCT", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT", "Finance_leases.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT", "Debt_securities.INSTRMNT_TYP_PRDCT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['1'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['1'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['1'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['1'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['1'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['1'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['1'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['1'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTTTNL_SCTR() in ['S14_B', 'S14_A', 'S15'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152467_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Non_Negotiable_bonds.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.PRPS", "Non_Negotiable_bonds.PRPS", "Other_loans.ACCNTNG_CLSSFCTN", "Non_Negotiable_bonds.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Non_Negotiable_bonds.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Non_Negotiable_bonds.SBJCT_IMPRMNT_INDCTR", "Other_loans.INSTTTNL_SCTR", "Non_Negotiable_bonds.INSTTTNL_SCTR", "Other_loans.PRTY_RL_TYP", "Non_Negotiable_bonds.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Non_Negotiable_bonds.MN_DBTR_INDCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Non_Negotiable_bonds.INSTRMNT_TYP_PRDCT", "Other_loans.RPYMNT_RGHTS", "Non_Negotiable_bonds.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Non_Negotiable_bonds.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['1022'],
					item.RPYMNT_RGHTS() in ['2'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table
		if self.F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Non_Negotiable_bonds_Table.Non_Negotiable_bondss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.INSTTTNL_SCTR() in ['S121', 'S126', 'S124', 'S123', 'S127', 'S129', 'S128'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['1022'],
					item.RPYMNT_RGHTS() in ['2'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_408943_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS", "Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Debt_securities.SBJCT_IMPRMNT_INDCTR", "Other_loans.MLTLTRL_DVLPMNT_BNK_INDCTR", "Credit_card_debt.MLTLTRL_DVLPMNT_BNK_INDCTR", "Trade_receivables.MLTLTRL_DVLPMNT_BNK_INDCTR", "Advances_that_are_not_loans.MLTLTRL_DVLPMNT_BNK_INDCTR", "Finance_leases.MLTLTRL_DVLPMNT_BNK_INDCTR", "On_demand_and_short_notice.MLTLTRL_DVLPMNT_BNK_INDCTR", "Reverse_repurchase_agreements.MLTLTRL_DVLPMNT_BNK_INDCTR", "Debt_securities.MLTLTRL_DVLPMNT_BNK_INDCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Credit_card_debt.INSTRMNT_TYP_PRDCT", "Trade_receivables.INSTRMNT_TYP_PRDCT", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT", "Finance_leases.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT", "Debt_securities.INSTRMNT_TYP_PRDCT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_408944_REF:
	F_05_01_REF_FINREP_3_0_Other_loans_Table = None
	F_05_01_REF_FINREP_3_0_Credit_card_debt_Table = None
	F_05_01_REF_FINREP_3_0_Trade_receivables_Table = None
	F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table = None
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table = None
	F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table = None
	F_05_01_REF_FINREP_3_0_Debt_securities_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Other_loans.CRRYNG_AMNT", "Credit_card_debt.CRRYNG_AMNT", "Trade_receivables.CRRYNG_AMNT", "Advances_that_are_not_loans.CRRYNG_AMNT", "Finance_leases.CRRYNG_AMNT", "On_demand_and_short_notice.CRRYNG_AMNT", "Reverse_repurchase_agreements.CRRYNG_AMNT", "Debt_securities.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Other_loans.PRPS", "Credit_card_debt.PRPS", "Trade_receivables.PRPS", "Advances_that_are_not_loans.PRPS", "Finance_leases.PRPS", "On_demand_and_short_notice.PRPS", "Reverse_repurchase_agreements.PRPS", "Debt_securities.PRPS", "Other_loans.ACCNTNG_CLSSFCTN", "Credit_card_debt.ACCNTNG_CLSSFCTN", "Trade_receivables.ACCNTNG_CLSSFCTN", "Advances_that_are_not_loans.ACCNTNG_CLSSFCTN", "Finance_leases.ACCNTNG_CLSSFCTN", "On_demand_and_short_notice.ACCNTNG_CLSSFCTN", "Reverse_repurchase_agreements.ACCNTNG_CLSSFCTN", "Debt_securities.ACCNTNG_CLSSFCTN", "Other_loans.HLD_SL_INDCTR", "Credit_card_debt.HLD_SL_INDCTR", "Trade_receivables.HLD_SL_INDCTR", "Advances_that_are_not_loans.HLD_SL_INDCTR", "Finance_leases.HLD_SL_INDCTR", "On_demand_and_short_notice.HLD_SL_INDCTR", "Reverse_repurchase_agreements.HLD_SL_INDCTR", "Debt_securities.HLD_SL_INDCTR", "Other_loans.SBJCT_IMPRMNT_INDCTR", "Credit_card_debt.SBJCT_IMPRMNT_INDCTR", "Trade_receivables.SBJCT_IMPRMNT_INDCTR", "Advances_that_are_not_loans.SBJCT_IMPRMNT_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "On_demand_and_short_notice.SBJCT_IMPRMNT_INDCTR", "Reverse_repurchase_agreements.SBJCT_IMPRMNT_INDCTR", "Debt_securities.SBJCT_IMPRMNT_INDCTR", "Other_loans.MLTLTRL_DVLPMNT_BNK_INDCTR", "Credit_card_debt.MLTLTRL_DVLPMNT_BNK_INDCTR", "Trade_receivables.MLTLTRL_DVLPMNT_BNK_INDCTR", "Advances_that_are_not_loans.MLTLTRL_DVLPMNT_BNK_INDCTR", "Finance_leases.MLTLTRL_DVLPMNT_BNK_INDCTR", "On_demand_and_short_notice.MLTLTRL_DVLPMNT_BNK_INDCTR", "Reverse_repurchase_agreements.MLTLTRL_DVLPMNT_BNK_INDCTR", "Debt_securities.MLTLTRL_DVLPMNT_BNK_INDCTR", "Other_loans.PRTY_RL_TYP", "Credit_card_debt.PRTY_RL_TYP", "Trade_receivables.PRTY_RL_TYP", "Advances_that_are_not_loans.PRTY_RL_TYP", "Finance_leases.PRTY_RL_TYP", "On_demand_and_short_notice.PRTY_RL_TYP", "Reverse_repurchase_agreements.PRTY_RL_TYP", "Debt_securities.PRTY_RL_TYP", "Other_loans.MN_DBTR_INDCTR", "Credit_card_debt.MN_DBTR_INDCTR", "Trade_receivables.MN_DBTR_INDCTR", "Advances_that_are_not_loans.MN_DBTR_INDCTR", "Finance_leases.MN_DBTR_INDCTR", "On_demand_and_short_notice.MN_DBTR_INDCTR", "Reverse_repurchase_agreements.MN_DBTR_INDCTR", "Debt_securities.MN_DBTR_INDCTR", "Other_loans.INSTRMNT_TYP_PRDCT", "Credit_card_debt.INSTRMNT_TYP_PRDCT", "Trade_receivables.INSTRMNT_TYP_PRDCT", "Advances_that_are_not_loans.INSTRMNT_TYP_PRDCT", "Finance_leases.INSTRMNT_TYP_PRDCT", "On_demand_and_short_notice.INSTRMNT_TYP_PRDCT", "Reverse_repurchase_agreements.INSTRMNT_TYP_PRDCT", "Debt_securities.INSTRMNT_TYP_PRDCT", "Other_loans.RPYMNT_RGHTS", "Credit_card_debt.RPYMNT_RGHTS", "Trade_receivables.RPYMNT_RGHTS", "Advances_that_are_not_loans.RPYMNT_RGHTS", "Finance_leases.RPYMNT_RGHTS", "On_demand_and_short_notice.RPYMNT_RGHTS", "Reverse_repurchase_agreements.RPYMNT_RGHTS", "Debt_securities.RPYMNT_RGHTS", "Other_loans.NGTBL_SCRTY_INDCTR", "Credit_card_debt.NGTBL_SCRTY_INDCTR", "Trade_receivables.NGTBL_SCRTY_INDCTR", "Advances_that_are_not_loans.NGTBL_SCRTY_INDCTR", "Finance_leases.NGTBL_SCRTY_INDCTR", "On_demand_and_short_notice.NGTBL_SCRTY_INDCTR", "Reverse_repurchase_agreements.NGTBL_SCRTY_INDCTR", "Debt_securities.NGTBL_SCRTY_INDCTR"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Other_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Other_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Other_loans_Table.Other_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Credit_card_debt_Table
		if self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Credit_card_debt_Table.Credit_card_debts
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Trade_receivables_Table
		if self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Trade_receivables_Table.Trade_receivabless
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table
		if self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Advances_that_are_not_loans_Table.Advances_that_are_not_loanss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table
		if self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_On_demand_and_short_notice_Table.On_demand_and_short_notices
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table
		if self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Reverse_repurchase_agreements_Table.Reverse_repurchase_agreementss
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)
		# Process F_05_01_REF_FINREP_3_0_Debt_securities_Table
		if self.F_05_01_REF_FINREP_3_0_Debt_securities_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Debt_securities_Table.Debt_securitiess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['1'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80', '51', '1022', '1003'],
					item.RPYMNT_RGHTS() in ['2', '1'],
					item.NGTBL_SCRTY_INDCTR() in ['2'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None

class Cell_F_05_01_REF_FINREP_3_0_152433_REF:
	F_05_01_REF_FINREP_3_0_Finance_leases_Table = None
	F_05_01_REF_FINREP_3_0s = []
	@lineage(dependencies={"Finance_leases.CRRYNG_AMNT"})
	def metric_value(self):
		total = 0
		# Sum from filtered items collected in calc_referenced_items
		for item in self.F_05_01_REF_FINREP_3_0s:
			total += item.CRRYNG_AMNT()
		return total
	@lineage(dependencies={"Finance_leases.PRPS", "Finance_leases.ACCNTNG_CLSSFCTN", "Finance_leases.HLD_SL_INDCTR", "Finance_leases.SBJCT_IMPRMNT_INDCTR", "Finance_leases.MLTLTRL_DVLPMNT_BNK_INDCTR", "Finance_leases.PRTY_RL_TYP", "Finance_leases.MN_DBTR_INDCTR", "Finance_leases.INSTRMNT_TYP_PRDCT"})
	def calc_referenced_items(self):
		# Filter directly on product-specific classes
		# Process F_05_01_REF_FINREP_3_0_Finance_leases_Table
		if self.F_05_01_REF_FINREP_3_0_Finance_leases_Table is not None:
			items = self.F_05_01_REF_FINREP_3_0_Finance_leases_Table.Finance_leasess
			for item in items:
				filter_passed = True
				filter_passed = all([
					item.PRPS() in ['7', '9', '6', '8', '4', '5', '12', '13', '1', '19'],
					item.ACCNTNG_CLSSFCTN() in ['6', '14', '45', '9', '7', '8', '41', '4', '47', '77', '76', '74', '73'],
					item.HLD_SL_INDCTR() in ['2'],
					item.SBJCT_IMPRMNT_INDCTR() in ['1', '2'],
					item.MLTLTRL_DVLPMNT_BNK_INDCTR() in ['2'],
					item.PRTY_RL_TYP() in ['18', '4', '19', '28', '8'],
					item.MN_DBTR_INDCTR() in ['1'],
					item.INSTRMNT_TYP_PRDCT() in ['80'],
				])
				if filter_passed:
					self.F_05_01_REF_FINREP_3_0s.append(item)

	def init(self):
		Orchestration().init(self)
		self.F_05_01_REF_FINREP_3_0s = []
		self.calc_referenced_items()
		return None
