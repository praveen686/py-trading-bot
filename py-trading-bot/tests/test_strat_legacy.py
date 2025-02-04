#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 19:45:34 2022

@author: maxime
"""

from django.test import TestCase
from core import strat_legacy
import vectorbtpro as vbt

class TestStrat(TestCase):
    @classmethod
    def setUpClass(self):  
        super().setUpClass()
        self.period="2007_2022_08"
        self.symbol_index="CAC40"
        
    def test_strat_kama_stoch(self):
        self.ust=strat_legacy.StratKamaStoch(self.period, symbol_index=self.symbol_index)
        self.ust.run()
        
        pf=vbt.Portfolio.from_signals(self.ust.close, self.ust.entries,self.ust.exits,
                                      short_entries=self.ust.entries_short,
                                      short_exits  =self.ust.exits_short)  

        self.assertEqual(round(pf.get_total_return()[pf.wrapper.columns[0]],2),1.04)
        self.assertEqual(round(pf.get_total_return()[pf.wrapper.columns[1]],2),1.4)
        self.assertEqual(round(pf.get_total_return()[pf.wrapper.columns[2]],2),4.78)
        self.assertEqual(round(pf.get_total_return()[pf.wrapper.columns[6]],2),4.72)
     
    def test_strat_kama_stoch_super_bbands(self):   
        self.ust=strat_legacy.StratKamaStochSuperBbands(self.period, symbol_index=self.symbol_index)
        self.ust.run()
        
        pf=vbt.Portfolio.from_signals(self.ust.close, self.ust.entries,self.ust.exits,
                                      short_entries=self.ust.entries_short,
                                      short_exits  =self.ust.exits_short)              

        self.assertEqual(round(pf.get_total_return()[pf.wrapper.columns[0]],2),2.33)
        self.assertEqual(round(pf.get_total_return()[pf.wrapper.columns[1]],2),1.21)        
        self.assertEqual(round(pf.get_total_return()[pf.wrapper.columns[2]],2),7.64)  
        self.assertEqual(round(pf.get_total_return()[pf.wrapper.columns[6]],2),2.84)  

    def test_strat_kama_stoch_matrend_macdbb(self):   
        self.ust=strat_legacy.StratKamaStochMatrendMacdbb(self.period, symbol_index=self.symbol_index)
        self.ust.run()
        
        pf=vbt.Portfolio.from_signals(self.ust.close, self.ust.entries,self.ust.exits,
                                      short_entries=self.ust.entries_short,
                                      short_exits  =self.ust.exits_short)   
            
        self.assertEqual(round(pf.get_total_return()[pf.wrapper.columns[0]],2),1.39)
        self.assertEqual(round(pf.get_total_return()[pf.wrapper.columns[1]],2),0.5)        
        self.assertEqual(round(pf.get_total_return()[pf.wrapper.columns[2]],2),5.25)  
        self.assertEqual(round(pf.get_total_return()[pf.wrapper.columns[6]],2),3.61)  

    def test_strat_kama_stoch_super_macdbb(self):
        self.ust=strat_legacy.StratKamaStochSuperMacdbb(self.period, symbol_index=self.symbol_index)
        self.ust.run()
        
        pf=vbt.Portfolio.from_signals(self.ust.close, self.ust.entries,self.ust.exits,
                                      short_entries=self.ust.entries_short,
                                      short_exits  =self.ust.exits_short)               

        self.assertEqual(round(pf.get_total_return()[pf.wrapper.columns[0]],2),1.15)
        self.assertEqual(round(pf.get_total_return()[pf.wrapper.columns[1]],2),0.7)        
        self.assertEqual(round(pf.get_total_return()[pf.wrapper.columns[2]],2),4.2)  
        self.assertEqual(round(pf.get_total_return()[pf.wrapper.columns[6]],2),4.93)  

    def test_strat_kama_stoch_matrend_bbands_macro(self):
        self.ust=strat_legacy.StratKamaStochMatrendBbandsMacro(
            self.period, 
            symbol_index=self.symbol_index,
            dir_bull="long",
            dir_uncertain="long",
            dir_bear="both")
        self.ust.run()
        
        pf=vbt.Portfolio.from_signals(self.ust.close, self.ust.entries,self.ust.exits,
                                      short_entries=self.ust.entries_short,
                                      short_exits  =self.ust.exits_short)              

        self.assertEqual(round(pf.get_total_return()[pf.wrapper.columns[0]],2),0.92)
        self.assertEqual(round(pf.get_total_return()[pf.wrapper.columns[1]],2),1.47)        
        self.assertEqual(round(pf.get_total_return()[pf.wrapper.columns[2]],2),1.29)  
        self.assertEqual(round(pf.get_total_return()[pf.wrapper.columns[6]],2),1.76)  

        self.ust=strat_legacy.StratKamaStochMatrendBbandsMacro(
            self.period, 
            symbol_index=self.symbol_index,
            dir_bull="long",
            dir_uncertain="both",
            dir_bear="both")
        self.ust.run()
        
        pf=vbt.Portfolio.from_signals(self.ust.close, self.ust.entries,self.ust.exits,
                                      short_entries=self.ust.entries_short,
                                      short_exits  =self.ust.exits_short)   
        
        self.assertEqual(round(pf.get_total_return()[pf.wrapper.columns[0]],2),1.82)
        self.assertEqual(round(pf.get_total_return()[pf.wrapper.columns[1]],2),0.24)        
        self.assertEqual(round(pf.get_total_return()[pf.wrapper.columns[2]],2),1.86)  
        self.assertEqual(round(pf.get_total_return()[pf.wrapper.columns[6]],2),1.84) 

    def test_strat_kama_stoch_macro(self): 
        self.ust=strat_legacy.StratKamaStochMacro(
            self.period, 
            symbol_index=self.symbol_index,
            dir_bull="long",
            dir_uncertain="long",
            dir_bear="both")
        self.ust.run()
        
        pf=vbt.Portfolio.from_signals(self.ust.close, self.ust.entries,self.ust.exits,
                                      short_entries=self.ust.entries_short,
                                      short_exits  =self.ust.exits_short)   
    
        self.assertEqual(round(pf.get_total_return()[pf.wrapper.columns[0]],2),0.01)
        self.assertEqual(round(pf.get_total_return()[pf.wrapper.columns[1]],2),1.07)        
        self.assertEqual(round(pf.get_total_return()[pf.wrapper.columns[2]],2),1.2)  
        self.assertEqual(round(pf.get_total_return()[pf.wrapper.columns[6]],2),9.71)  
    
          

