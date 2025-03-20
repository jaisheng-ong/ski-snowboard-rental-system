class cCustomer:
    #Constructor
    def __init__(self, strFirstName, strLastName, strPhoneID , intRentalQuantitySkis, intRentalQuantitySnowboards, strRentalRateCategory, dtmRentalDate, intRentalDuration, strCouponCode) :
        
        self.strFirstName = strFirstName
        self.strLastName = strLastName
        self.strPhoneID = strPhoneID

        self.intRentalQuantitySkis = intRentalQuantitySkis
        self.intRentalQuantitySnowboards = intRentalQuantitySnowboards
        self.strRentalRateCategory = strRentalRateCategory
        self.intRentalDuration = intRentalDuration
        self.strCouponCode = strCouponCode
        self.dtmRentalDate = dtmRentalDate

    #------------------------
    #Getter/Setter First Name
    #------------------------
        
    @property
    def strFirstName(self):
        return self.__strFirstName


    @strFirstName.setter
    def strFirstName(self, strFirstName):
      
      if (str(strFirstName).isdecimal() == False):
          self.__strFirstName = strFirstName

      else:
          self.__strFirstName = ""
          raise Exception("First Name Is Required. The value of strFirstName was: {}".format(strFirstName))

    #-----------------------
    #Getter/Setter Last Name
    #-----------------------

    @property
    def strLastName(self):
        return self.__strLastName


    @strLastName.setter
    def strLastName(self, strLastName):
      
      if (str(strLastName).isdecimal() == False):
          self.__strLastName = strLastName

      else:
          self.__strLastName = ""
          raise Exception("Last Name Is Required. The value of strLastName was: {}".format(strLastName))

    #-------------------------------------
    #Getter/Setter ID Phone Number
    #-------------------------------------

    @property
    def strPhoneID(self):
        return self.__strPhoneID

    @strPhoneID.setter
    def strPhoneID(self, strPhoneID):
      if strPhoneID== "":

          self.__strPhoneID = ""
          raise Exception("ID Phone Number Must Exist. The value of strPhoneID was: {}".format(strPhoneID))

      else:
          self.__strPhoneID = strPhoneID


    #-------------------------
    #Getter/Setter Rental Product
    #-------------------------

    @property
    def strRentalProduct(self):
        return self.__strRentalProduct

    @strRentalProduct.setter
    def strRentalProduct(self, strRentalProduct):
       if (str(strRentalProduct).isdecimal() == False):

           self.__strRentalProduct = strRentalProduct
       else:

           self.__strRentalProduct = ""
           raise Exception("Rent Type Is Required. The value of strRentalProduct was: {}".format(strRentalProduct))

    #-------------------------------------
    #Getter/Setter Rental Product Quantity
    #-------------------------------------

    @property
    def intRentalProductQuantity(self):
        return self.__intRentalProductQuantity

    @intRentalProductQuantity.setter
    def intRentalProductQuantity(self, intRentalProductQuantity):
       if (type(intRentalProductQuantity) is int):

           self.__intRentalProductQuantity = intRentalProductQuantity

       else:

           self.__intRentalProductQuantity = 0
           raise Exception("Rental Number Must Be Numeric. The value of intRentalProductQuantity was: {}".format(intRentalProductQuantity))

    #-------------------------
    #Getter/Setter Rental Rate Category
    #-------------------------

    @property
    def strRentalRateCategory(self):
        return self.__strRentalRateCategory

    @strRentalRateCategory.setter
    def strRentalRateCategory(self, strRentalRateCategory):
       if (str(strRentalRateCategory).isdecimal() == False):

           self.__strRentalRateCategory = strRentalRateCategory

       else:
           self.__strRentalRateCategory = ""
           raise Exception("Rental Rate Category Is Required. The value of strRentalRateCategory was: {}".format(strRentalRateCategory))


    #--------------------------
    #Getter/Setter Date Rented
    #--------------------------

    @property
    def dtmDateRented(self):
        return self.__dtmDateRented


    @dtmDateRented.setter
    def dtmDateRented(self, dtmDateRented):
      
      if (str(dtmDateRented).isdecimal() == False):
          self.__dtmDateRented = dtmDateRented

      else:
          self.__dtmDateRented = ""
          raise Exception("Rent Date Is Required. The value of dtmDateRented was: {}".format(dtmDateRented))

    #---------------------------
    #Getter/Setter Date Expected
    #---------------------------

    @property
    def dtmDateExpected(self):
        return self.__dtmDateExpected


    @dtmDateExpected.setter
    def dtmDateExpected(self, dtmDateExpected):
      
      if (str(dtmDateExpected).isdecimal() == False):
          self.__dtmDateExpected = dtmDateExpected

      else:
          self.__dtmDateExpected = ""
          raise Exception("Date Expected Is Required. The value of dtmDateExpected was: {}".format(dtmDateExpected))

   

    #---------------------------
    #Getter/Setter Date Returned
    #---------------------------

    @property
    def dtmDateReturned(self):
        return self.__dtmDateReturned


    @dtmDateReturned.setter
    def dtmDateReturned(self, dtmDateReturned):
      
      if (str(dtmDateReturned).isdecimal() == False):
          self.__dtmDateReturned = dtmDateReturned

      else:
          self.__dtmDateReturned = ""
          raise Exception("Return Date Is Required. The value of dtmDateReturned was: {}".format(dtmDateReturned))

    #------------------------------------------------
    #Getter/Setter Rental Product Quantity Returned
    #------------------------------------------------

    @property
    def intRentalProductQuantityReturned(self):
        return self.__intRentalProductQuantityReturned

    @intRentalProductQuantityReturned.setter
    def intRentalProductQuantityReturned(self, intRentalProductQuantityReturned):
       if (type(intRentalProductQuantityReturned) is int):

           self.__intRentalProductQuantityReturned = intRentalProductQuantityReturned

       else:

           self.__intRentalProductQuantityReturned = 0
           raise Exception("Rental Product Quantity Returned Must Be Numeric. The value of intRentalProductQuantityReturned was: {}".format(intRentalProductQuantityReturned))


    # --------------------------------------------------------------------------------------------
    # Method Name:        See_Available_Skis
    # --------------------------------------------------------------------------------------------
    def See_Available_Skis(self, _intSkisInventory):

        if _intSkisInventory >= 1:

            print("Available Skis: ", _intSkisInventory)

        else:
            print("Skis Unavailable At This Time.")


    # --------------------------------------------------------------------------------------------
    # Method Name:        See_Available_Snowboards
    # --------------------------------------------------------------------------------------------
    def See_Available_Snowboards(self, _intSnowboardsInventory):

        if _intSnowboardsInventory >= 1:

            print("Available Snowboards: ", _intSnowboardsInventory)

        else:
            print("Snowboards Unavailable At This Time.")


     #----------------------------
     #    Expected Rental Length 
     #----------------------------

    def intExpectedRentalLength(self):
        
        from datetime import datetime


        date_time_obj = datetime.strptime(self.dtmDateRented, "%m/%d/%y")
        date_time_obj2 = datetime.strptime(self.dtmDateExpected, "%m/%d/%y")


        # difference between datetime in timedelta
        delta = date_time_obj2 - date_time_obj
        print(f'Difference is {delta.days} days')

# ----------------------------------------------------------------------------------
# Function Name:       Display_Total_For_Day
# Function Purpose:    Display Accumulated Totals for the Day
# ----------------------------------------------------------------------------------

def Display_Total_For_Day(intDayTotalSkis, intDayTotalSnowboards, dblDayRevenue):

    print("")
    
    print("Total of Skis Rented for Day:  ", "${:,.2f}".format(intDayTotalSkis))
    print("Total of Snowboards Rented for Day: ", "${:,.2f}".format(intDayTotalSnowboards))
    print("Daily Revenue Collected for Day: ", "${:,.2f}".format(dblDayRevenue))



import math
from datetime import datetime, timedelta

# -----------------------------------------------------------------
# Class Name:        Shops
# -----------------------------------------------------------------

class cShop:

   #Class Attributes
    _intSkisInventory = int(0)
    _intSnowboardsInventory = int(0)

    dblRentalCost = float(0)
    dblCouponDiscount = float(0)
    dblFamilyDiscount = float(0)
    dblRentalTotal = float(0)
    intDailySkis = int(0)
    intDailySnowboards = int(0)
    dblDailyRevenue = float(0)

 #######NOTE###########
 #### dtmDateRented, dtmDateExpected, dtmDateReturned, intRentalProductQuantityReturned NOT IN CUSTOMER CLASS THOUGHT THEY WENT HERE (CAN CHANGE IF NEEDED)
 #### CUSTOMER VARIABLE intRentalProductQuantity CHANGED TO 2 VARAIBLES intRentalQuantitySkis and intRentalQuantitySnowboards (can sell both at once apparently!, think I changed all current methods to reflect)


    #Initialization Method (Constructor)
    def __init__(self, _dblSkisHourlyRate, _dblSkisDailyRate, _dblSkisWeeklyRate, _dblSnowboardsHourlyRate, _dblSnowboardsDailyRate,  _dblSnowboardsWeeklyRate, _intInitialSkisInventory, _intInitialSnowboardsInventory ):

        #Instance Variables
        self._dblSkisHourlyRate = _dblSkisHourlyRate
        self._dblSkisDailyRate = _dblSkisDailyRate
        self._dblSkisWeeklyRate = _dblSkisWeeklyRate
        self._dblSnowboardsHourlyRate = _dblSnowboardsHourlyRate
        self._dblSnowboardsDailyRate = _dblSnowboardsDailyRate
        self._dblSnowboardsWeeklyRate = _dblSnowboardsWeeklyRate
        self._intInitialSkisInventory = _intInitialSkisInventory
        self._intInitialSnowboardsInventory = _intInitialSnowboardsInventory


    #-----------------------------------
    # Getter/Setter SkisHourlyRate
    #-----------------------------------

    @property
    def _dblSkisHourlyRate(self):
        return self.__dblSkisHourlyRate

    @_dblSkisHourlyRate.setter
    def _dblSkisHourlyRate(self, _dblSkisHourlyRate):
       if (type(_dblSkisHourlyRate) is float):

           self.__dblSkisHourlyRate = _dblSkisHourlyRate

       else:
           self.__dblSkisHourlyRate = 0
           raise Exception("Hourly Rate of Skis Must Be Numeric. The value of _dblSkisHourlyRate was: {}".format(_dblSkisHourlyRate))


    #-----------------------------------
    # Getter/Setter SnowboardsHourlyRate
    #-----------------------------------

    @property
    def _dblSnowboardsHourlyRate(self):
        return self.__dblSnowboardsHourlyRate

    @_dblSnowboardsHourlyRate.setter
    def _dblSnowboardsHourlyRate(self, _dblSnowboardsHourlyRate):
       if (type(_dblSnowboardsHourlyRate) is float):

           self.__dblSnowboardsHourlyRate = _dblSnowboardsHourlyRate

       else:
           self.__dblSnowboardsHourlyRate = 0
           raise Exception("Hourly Rate of Snowboards Must Be Numeric. The value of dblSnowboardsHourlyRate was: {}".format(_dblSnowboardsHourlyRate))
   
       
    #---------------------------------
    #Getter/Setter SkisDailyRate
    #---------------------------------

    @property
    def _dblSkisDailyRate(self):
        return self.__dblSkisDailyRate


    @_dblSkisDailyRate.setter
    def _dblSkisDailyRate(self, _dblSkisDailyRate):
       if (type(_dblSkisDailyRate) is float):
           self.__dblSkisDailyRate = _dblSkisDailyRate

       else:
           self.__dblSkisDailyRate = 0
           raise Exception("Daily Rate of Skis Must Be Numeric. The value of dblSkisDailyRate was: {}".format(_dblSkisDailyRate))


    #---------------------------------
    #Getter/Setter SnowboardsDailyRate
    #---------------------------------

    @property
    def _dblSnowboardsDailyRate(self):
        return self.__dblSnowboardsDailyRate


    @_dblSnowboardsDailyRate.setter
    def _dblSnowboardsDailyRate(self, _dblSnowboardsDailyRate):
       if (type(_dblSnowboardsDailyRate) is float):
           self.__dblSnowboardsDailyRate = _dblSnowboardsDailyRate

       else:
           self.__dblSnowboardsDailyRate = 0
           raise Exception("Daily Rate of Snowboards Must Be Numeric. The value of dblSnowboardsDailyRate was: {}".format(_dblSnowboardsDailyRate))

    #----------------------------------
    #Getter/Setter Skis WeeklyRate
    #----------------------------------

    @property
    def _dblSkisWeeklyRate(self):
        return self.__dblSkisWeeklyRate

    @_dblSkisWeeklyRate.setter
    def _dblSkisWeeklyRate(self, _dblSkisWeeklyRate):
       if (type(_dblSkisWeeklyRate) is float):
           self.__dblSkisWeeklyRate = _dblSkisWeeklyRate

       else:
           self.__dblSkisWeeklyRate = 0
           raise Exception("Weekly Rate of Skis Must Be Numeric. The value of dblSkisWeeklyRate was: {}".format(_dblSkisWeeklyRate))

    #----------------------------------
    #Getter/Setter Snowboards WeeklyRate
    #----------------------------------

    @property
    def _dblSnowboardsWeeklyRate(self):
        return self.__dblSnowboardsWeeklyRate

    @_dblSnowboardsWeeklyRate.setter
    def _dblSnowboardsWeeklyRate(self, _dblSnowboardsWeeklyRate):
       if (type(_dblSnowboardsWeeklyRate) is float):
           self.__dblSnowboardsWeeklyRate = _dblSnowboardsWeeklyRate

       else:
           self.__dblSnowboardsWeeklyRate = 0
           raise Exception("Weekly Rate of Snowboards Must Be Numeric. The value of dblSnowboardsWeeklyRate were: {}".format(_dblSnowboardsWeeklyRate))


    #----------------------------------
    #Getter/Setter InitialSkisInventory
    #----------------------------------

    @property
    def _intInitialSkisInventory(self):
        return self.__intInitialSkisInventory

    @_intInitialSkisInventory.setter
    def _intInitialSkisInventory(self, _intInitialSkisInventory):
       if (type(_intInitialSkisInventory) is int):
           self.__intInitialSkisInventory = _intInitialSkisInventory

       else:
           self.__intInitialSkisInventory = 0
           raise Exception("Initial Inventory of Skis Must Be Numeric. The value of intInitialSkisInventory were: {}".format(_intInitialSkisInventory))

    #-----------------------------------------
    #Getter/Setter InitialSnowboardsInventory
    #----------------------------------------

    @property
    def _intInitialSnowboardsInventory(self):
        return self.__intInitialSnowboardsInventory

    @_intInitialSnowboardsInventory.setter
    def _intInitialSnowboardsInventory(self, _intInitialSnowboardsInventory):
       if (type(_intInitialSnowboardsInventory) is int):
           self.__intInitialSnowboardsInventory = _intInitialSnowboardsInventory

       else:
           self.__intInitialSnowboardsInventory = 0
           raise Exception("Initial Inventory of Snowboard Must Be Numeric. The value of intInitialSnowboardsInventory were: {}".format(_intInitialSnowboardsInventory))

    #-------------------------
    #Getter/Setter Coupon Code
    #-------------------------

    @property
    def _strCouponCode(self):
        return self.__strCouponCode


    @_strCouponCode.setter
    def _strCouponCode(self, _strCouponCode):
      
      if (str(_strCouponCode).isdecimal() == False):
          self.__strCouponCode = _strCouponCode

      else:
          self.__strCouponCode = ""

    # --------------------------------------------------------------------------------------------
    # Method Name:        Establish_Skis_Inventory
    # --------------------------------------------------------------------------------------------


    def Establish_Skis_Inventory(self):
        
        cShop._intSkisInventory += self._intInitialSkisInventory


    # --------------------------------------------------------------------------------------------
    # Method Name:        Establish_Snowboards_Inventory
    # --------------------------------------------------------------------------------------------

    def Establish_Snowboards_Inventory(self):

        cShop._intSnowboardsInventory += self._intInitialSnowboardsInventory


    # --------------------------------------------------------------------------------------------
    # Method Name:        Display_Skis_Inventory
    # --------------------------------------------------------------------------------------------

    def Display_Skis_Inventory(self):

        if cShop._intSkisInventory >= 1:

            print("Available Skis: ", cShop._intSkisInventory)

        else:

            print("Skis Unavailable In Inventory.")


    # --------------------------------------------------------------------------------------------
    # Method Name:        Display_Snowboards_Inventory
    # --------------------------------------------------------------------------------------------

    def Display_Snowboards_Inventory(self):

        if cShop._intSnowboardsInventory >= 1:

            print("Available Snowboards: ", cShop._intSnowboardsInventory)

        else:
            print("Snowboards Unavailable In Inventory.")


    # --------------------------------------------------------------------------------------------
    # Method Name:        Update_Inventory_Rented_Skis
    # --------------------------------------------------------------------------------------------

    def  Update_Inventory_Rented_Skis(intRentalQuantitySkis):

        cShop._intSkisInventory -= int(intRentalQuantitySkis)

        return cShop._intSkisInventory

    # --------------------------------------------------------------------------------------------
    # Method Name:        Update_Inventory_Rented_Snowboards
    # --------------------------------------------------------------------------------------------

    def  Update_Inventory_Rented_Snowboards(intRentalQuantitySnowboards):

        cShop._intSnowboardsInventory -= intRentalQuantitySnowboards

        return cShop._intSnowboardsInventory
    # --------------------------------------------------------------------------------------------
    # Method Name:        Update_Inventory_Return_Skis
    # --------------------------------------------------------------------------------------------

    def  Update_Inventory_Return_Skis(self, intRentalProductQuantityReturned):
        
        cShop._intSkisInventory += intRentalProductQuantityReturned

        return cShop._intSkisInventory


    # --------------------------------------------------------------------------------------------
    # Method Name:        Update_Inventory_Return_Snowboards
    # --------------------------------------------------------------------------------------------

    def  Update_Inventory_Return_Snowboards(self, intRentalProductQuantityReturned):
        
        cShop._intSnowboardsInventory += intRentalProductQuantityReturned

        return cShop._intSnowboardsInventory


    
    # --------------------------------------------------------------------------------------------
    # Method Name:        Date_And_Time_Rented
    # --------------------------------------------------------------------------------------------
    def Date_rented(dtmDateRented):

        dtmDateRented = datetime.now() #Y/M/D 15:00:00

        return dtmDateRented


    # --------------------------------------------------------------------------------------------
    # Method Name:        Date_And_Time_Expected_Return
    # --------------------------------------------------------------------------------------------
    def Date_rented(dtmDateExpected):

        dtmDateExpected = datetime.now() #Y/M/D 15:00:00

        return dtmDateExpected


    # --------------------------------------------------------------------------------------------
    # Method Name:        Date_And_Time_Returned
    # --------------------------------------------------------------------------------------------
    def Date_rented(dtmDateReturned):

        dtmDateReturned = datetime.now() #Y/M/D 15:00:00

        return dtmDateReturned

    # --------------------------------------------------------------------------------------------
    # Method Name:        Calculate_Skis_Hourly_Rental_Cost
    # --------------------------------------------------------------------------------------------
    def Calculate_Skis_Hourly_Rental_Cost (self, _dblSkisHourlyRate, _dblSkisDailyRate, _dblSkisWeeklyRate, intRentalDuration , intRentalQuantitySkis):            
        dblHourlyRentalCost = float(0)
        dblDailyRentalCost = float(0)
        dblWeeklyRentalCost = float(0)
        dblRentalDuration = float(0)
        rateslist = []
        
        dblHourlyRentalCost += _dblSkisHourlyRate * intRentalDuration * int(intRentalQuantitySkis)
        dblWeeklyRentalCost += _dblSkisWeeklyRate * math.ceil(intRentalDuration / 168) * int(intRentalQuantitySkis)
        dblDailyRentalCost += _dblSkisDailyRate * int(intRentalQuantitySkis)

        rateslist.insert(0,dblHourlyRentalCost)
        rateslist.insert(1,dblDailyRentalCost)
        rateslist.insert(2,dblWeeklyRentalCost)
        rateslist.sort() 

        cShop.dblRentalCost += rateslist[0]

        return cShop.dblRentalCost
    # --------------------------------------------------------------------------------------------
    # Method Name:        Calculate_Snowboards_Hourly_Rental_Cost
    # --------------------------------------------------------------------------------------------
    def Calculate_Snowboards_Hourly_Rental_Cost (self, _dblSnowboardsHourlyRate, _dblSnowboardsDailyRate, _dblSnowboardsWeeklyRate, intRentalDuration , intRentalQuantitySnowboards):
       
        dblHourlyRentalCost = float(0)
        dblDailyRentalCost = float(0)
        dblWeeklyRentalCost = float(0)
        rateslist = []

        dblHourlyRentalCost += _dblSnowboardsHourlyRate * intRentalDuration * intRentalQuantitySnowboards
        dblWeeklyRentalCost += _dblSnowboardsWeeklyRate * math.ceil(intRentalDuration / 168) * intRentalQuantitySnowboards
        dblDailyRentalCost += _dblSnowboardsDailyRate * intRentalQuantitySnowboards

        rateslist.insert(0,dblHourlyRentalCost)
        rateslist.insert(1,dblDailyRentalCost)
        rateslist.insert(2,dblWeeklyRentalCost)
        rateslist.sort() #this orders the array values from lowest to highest

        cShop.dblRentalCost += rateslist[0]

        return cShop.dblRentalCost

    # --------------------------------------------------------------------------------------------
    # Method Name:        Calculate_Skis_Daily_Rental_Cost
    # --------------------------------------------------------------------------------------------
    def Calculate_Skis_Daily_Rental_Cost (self, _dblSkisDailyRate, _dblSkisWeeklyRate, intRentalDuration, intRentalQuantitySkis):
        dblDailyRentalCost = float(0)
        dblWeeklyRentalCost = float(0)
        rateslist = []

        dblDailyRentalCost += _dblSkisDailyRate * intRentalDuration * int(intRentalQuantitySkis)
        dblWeeklyRentalCost += _dblSkisWeeklyRate * math.ceil(intRentalDuration / 7) * int(intRentalQuantitySkis)

        rateslist.insert(0,dblDailyRentalCost)
        rateslist.insert(1,dblWeeklyRentalCost)
        rateslist.sort() #this orders the array values from lowest to highest

        cShop.dblRentalCost += rateslist[0]

        return cShop.dblRentalCost
    # --------------------------------------------------------------------------------------------
    # Method Name:        Calculate_Snowboards_Daily_Rental_Cost
    # --------------------------------------------------------------------------------------------
    def Calculate_Snowboards_Daily_Rental_Cost (self, _dblSnowboardsDailyRate, _dblSnowBoardsWeeklyRate, intRentalDuration, intRentalQuantitySnowboards):
        dblDailyRentalCost = float(0)
        dblWeeklyRentalCost = float(0)
        rateslist = []
       
        dblDailyRentalCost += _dblSnowboardsDailyRate * intRentalDuration * intRentalQuantitySnowboards
        dblWeeklyRentalCost += _dblSnowBoardsWeeklyRate * math.ceil(intRentalDuration / 7) * intRentalQuantitySnowboards

        rateslist.insert(0,dblDailyRentalCost)
        rateslist.insert(1,dblWeeklyRentalCost)
        rateslist.sort() #this orders the array values from lowest to highest

        cShop.dblRentalCost += rateslist[0]
        
        return cShop.dblRentalCost
        
    # --------------------------------------------------------------------------------------------
    # Method Name:        Calculate_Skis_Weekly_Rental_Cost
    # --------------------------------------------------------------------------------------------
    def Calculate_Skis_Weekly_Rental_Cost (self, _dblSkisWeeklyRate, intRentalDuration, intRentalQuantitySkis):

        cShop.dblRentalCost += _dblSkisWeeklyRate * intRentalDuration * int(intRentalQuantitySkis)

        return cShop.dblRentalCost

    # --------------------------------------------------------------------------------------------
    # Method Name:        Calculate_Snowboards_Weekly_Rental_Cost
    # --------------------------------------------------------------------------------------------
    def Calculate_Snowboards_Weekly_Rental_Cost (self, _dblSnowboardsWeeklyRate, intRentalDuration, intRentalQuantitySnowboards):

        cShop.dblRentalCost += _dblSnowboardsWeeklyRate * intRentalDuration * intRentalQuantitySnowboards

        return cShop.dblRentalCost
    # --------------------------------------------------------------------------------------------
    # Method Name:        Calculate_Coupon_Discount
    # --------------------------------------------------------------------------------------------

    def Calculate_Coupon_Discount(self, strCouponCode):
       
        if strCouponCode.endswith('BBP'):

            cShop.dblCouponDiscount = cShop.dblRentalCost * .1

        else:

            cShop.dblCouponDiscount = 0

        return cShop.dblCouponDiscount

    # --------------------------------------------------------------------------------------------
    # Method Name:        Calculate_Family_Discount
    # --------------------------------------------------------------------------------------------

    def Calculate_Family_Discount(self, intRentalQuantitySkis, intRentalQuantitySnowboards):
       
        intQuantity = int(0)
        intcustomersubdis = int(0)
        intCustomerDis = int(0)
        if (int(intRentalQuantitySkis) + int(intRentalQuantitySnowboards)) > 2 and (int(intRentalQuantitySkis) + int(intRentalQuantitySnowboards)) < 6:
           
            cShop.dblFamilyDiscount = cShop.dblRentalCost * .25

        elif int(intRentalQuantitySkis) + int(intRentalQuantitySnowboards) >= 6:

           cShop.dblFamilyDiscount = intCustomerDis * .25 * cShop.dblRentalCost/(int(intRentalQuantitySkis) + int(intRentalQuantitySnowboards))
           dblAvgCost = cShop.dblRentalCost/(int(intRentalQuantitySkis) + int(intRentalQuantitySnowboards))
           cShop.dblFamilyDiscount = (dblAvgCost * 5) * .25

        else:

            cShop.dblFamilyDiscount = 0

        return cShop.dblFamilyDiscount
   
    #-------------------------------------------------------------------------------------------
    # Method Name:        Calculate_Rental_Total
    # --------------------------------------------------------------------------------------------
        
    def Calculate_Rental_Total(self):

        cShop.dblRentalTotal = cShop.dblRentalCost - cShop.dblFamilyDiscount - cShop.dblCouponDiscount 

        return cShop.dblRentalTotal

    # --------------------------------------------------------------------------------------------
    # Method Name:        Display_Bill
    # --------------------------------------------------------------------------------------------
    
    def Display_Bill(self):

        print("RentalCost:\t", "${:,.2f}".format(cShop.dblRentalCost) )
        print("Discounts:\t", "${:,.2f}".format((cShop.dblCouponDiscount + cShop.dblFamilyDiscount)))
        print("Rental Total:\t", "${:,.2f}".format(cShop.dblRentalTotal))

from typing import final
from datetime import datetime, timedelta
import math
############################################################################
# Project Name:  Ski & Snowboard Rental System
############################################################################

#########NOTE#########
####CHANGES TO CUSTOMER CLASS VARIABLES B/C CAN RENT SKIS AND SNOWBOARDS IN SAME TRANSACTION
#### CURRENTLY DOESNT CAPTURE DATES (can adjust if needed)

#FUNCTIONS (VALIDATION) 

# ----------------------------------------------------------------------------------
# Function Name:       Display_Total_For_Day
# Function Purpose:    Display Accumulated Totals for the Day
# ----------------------------------------------------------------------------------

def Display_Total_For_Day(intDayTotalSkis, intDayTotalSnowboards, dblDayRevenue):

    print("")
    
    print("Total of Skis Rented for Day:  ", "${:,.2f}".format(intDayTotalSkis))
    print("Total of Snowboards Rented for Day: ", "${:,.2f}".format(intDayTotalSnowboards))
    print("Daily Revenue Collected for Day: ", "${:,.2f}".format(dblDayRevenue))

# ----------------------------------------------------------------------------------
# Function Name:       Format_Rental_Rate
# Function Purpose:    Format Rental Rate for Customer Input Question
# ----------------------------------------------------------------------------------

def Format_Rental_Rate(strRentalRateCategory):

    if strRentalRateCategory == 'hourly':
        strHoursDaysWeeks = 'Hour(s)'

    elif strRentalRateCategory == 'daily':
        strHoursDaysWeeks = 'Day(s)'

    else:
        strHoursDaysWeeks = 'Week(s)'

    return strHoursDaysWeeks


# -----------------------------------------------------------------
# Function Name:        Validate_Navigation_Selection
# Function Purpose:     Validate Navigation Selection Number
# -----------------------------------------------------------------

def Validate_Navigation_Selection( intSelection ):
   try:
        intSelection = int(intSelection)
        if(intSelection > 0 and intSelection < 5):
            blnValidation = True
        else:
            blnValidation = False
            print("Navigation Selection Number Must Be 1 Through 4")
   except ValueError:
        blnValidation = False
        print("Nagivation Selection Number Is Required and Must Be Numeric")

   return blnValidation

# -----------------------------------------------------------------
# Function Name:        Validate_First_Name
# Function Purpose:     Validate First Name
# -----------------------------------------------------------------

def Validate_First_Name( strFirstName ):
    
   if strFirstName != "":

      blnValidation = True

   else:
      blnValidation = False

      print("Must Enter a First Name")
   
   return blnValidation 

# -----------------------------------------------------------------
# Function Name:        Validate_Last_Name
# Function Purpose:     Validate Last Name
# -----------------------------------------------------------------

def Validate_Last_Name( strLastName ):
    
   if strLastName != "":

      blnValidation = True

   else:
      blnValidation = False

      print("Must Enter a Last Name")
   
   return blnValidation 


# -----------------------------------------------------------------
# Function Name:        Validate_Phone_ID
# Function Purpose:     Validate Phone ID
# -----------------------------------------------------------------

def Validate_Phone_ID( intPhoneID ):

    if intPhoneID != "":
        if len(intPhoneID) == 10:
            blnValidation = True
        else:
            blnValidation = False
            print("Phone Number Must Be 10 Digits and Contain No Dashes, Spaces, Or Parentheses")
    else: 
        blnValidation = False
        print("Phone Number Is Required")

    return blnValidation

# -----------------------------------------------------------------
# Function Name:        Validate_Rental_Quantity_Skis
# Function Purpose:     Validate Rental Quantity Skis
# -----------------------------------------------------------------
def Validate_Rental_Quantity_Skis( intRentalQuantitySkis ):
   try:
        intRentalQuantitySkis = int(intRentalQuantitySkis)
        if intRentalQuantitySkis >= 0 and intRentalQuantitySkis <= BobsShop._intSkisInventory:
            blnValidation = True
        else:
            blnValidation = False
            print("Quantity of Skis Must Be Less Than or Equal To " + str(BobsShop._intSkisInventory) + " (Number Currently in Inventory)")
   except ValueError:
        blnValidation = False
        print("Quantity of Skis Is Required and Must Be Numeric (Enter 0 for None)")

   return blnValidation

# -----------------------------------------------------------------
# Function Name:        Validate_Rental_Quantity_Snowboards
# Function Purpose:     Validate Rental Quantity Snowboards
# -----------------------------------------------------------------
def Validate_Rental_Quantity_Snowboards( intRentalQuantitySnowboards ):
   try:
        intRentalQuantitySnowboards = int(intRentalQuantitySnowboards)
        if intRentalQuantitySnowboards >= 0 and intRentalQuantitySnowboards <= BobsShop._intSnowboardsInventory: 
            blnValidation = True
        else:
            blnValidation = False
            print("Quantity of Snowboards Must Be Less Than of Equal To " + str(BobsShop._intSnowboardsInventory) + " (Number Currently in Inventory)")
   except ValueError:
        blnValidation = False
        print("Quantity of Snowboards Is Required and Must Be Numeric (Enter 0 for None)")

   return blnValidation


# -----------------------------------------------------------------
# Function Name:        Validate_Rental_Rate_Category
# Function Purpose:     Validate Input for Hourly, Daily, or Weekly
# -----------------------------------------------------------------
def Validate_Rental_Rate_Category(strRentalRateCategory):
    
   if(strRentalRateCategory == 'hourly') or (strRentalRateCategory == 'daily') or (strRentalRateCategory == 'weekly'):
      blnValidation = True
   else:
      print("Rental Rate Category Must Be 'Hourly', 'Daily', or 'Weekly'")
      blnValidation = False

   return blnValidation


# -----------------------------------------------------------------
# Function Name:        Validate_Rental_Duration
# Function Purpose:     Validate Rental Duration
# -----------------------------------------------------------------

def Validate_Rental_Duration( intRentalDuration ):
    try:
        intRentalDuration = int(intRentalDuration)
        if(intRentalDuration > 0):
            blnValidation = True
        else:
            blnValidation = False
            print("Rental Duration Must Be Greater Than 0")
    except ValueError:
        blnValidation = False
        print("Rental Duration Must be Numeric")

    return blnValidation

# -----------------------------------------------------------------
# Function Name:        Validate_Coupon_Code
# Function Purpose:     Validate Coupon Code 
# -----------------------------------------------------------------
def Validate_Coupon_Code(strCouponCode):

    if len(strCouponCode) == 6 and strCouponCode.endswith('BBP'):
        blnValidation = True
        print("Valid Coupon Code")
    
    elif strCouponCode == "":   
        blnValidation = True

    else:
        blnValidation = False
        print("Invaild Coupon Code Entered")

    return blnValidation

# -----------------------------------------------------------------
# Function Name:        Validate_Yes_No
# Function Purpose:     Validate Yes No 
# -----------------------------------------------------------------

def Validate_Yes_No(strYesNo):

    if strYesNo == 'y' or strYesNo == 'n':
        global blnValidation
        blnValidation = True
    else:
        print("Please Enter 'Y' or 'N'")

    return strYesNo
# -----------------------------------------------------------------
# Project 2: Main Processing Area   
# -----------------------------------------------------------------

strFirstName = str("")
strLastName = str("")
strPhoneID = str("")

#strRentalProduct = str("")
intRentalQuantitySkis = int(0)
intRentalQuantitySnowboards = int(0)
strRentalRateCategory = str("")
intRentalDuration = int(0)
strCouponCode = str("")

intSelection = int(0)
blnProgramLoop = bool(True)
blnValidation = bool(False)

#-------------------------------
intRentSkisAmount = int(0)
intRentSnowboardsAmount = int(0)

intInventoryAvailable = int(0)

strTotalTimeRent = str("")
dblSubtotal = float(0)
dblDiscount = float(0)
dblFinalTotal = float(0)

intDisplaySkis = int(0)
intDisplaySnowboards = int(0)

intDayTotalSkis = int(0)
intDayTotalSnowboards = int(0)
dblDayRevenue = float(0)

#ESTABLISH SHOP WITH INITIAL RATES AND INVENTORY

BobsShop = cShop( 15.00, 50.00, 200.00, 10.00, 40.00, 160.00, 60, 60)
BobsShop.Establish_Skis_Inventory()
BobsShop.Establish_Snowboards_Inventory()

#CREATE CUSTOMER LIST

lCustomers = []

while blnProgramLoop is True:

    print("")
    print ("Navigational Selection.")
    print("")
    print("(1) New Customer Rental")
    print("(2) Rental Return")
    print("(3) Show Inventory")
    print("(4) End of Day")

    #GET VALIDATE NAVIGATION SELECTION
    while blnValidation is False:
        intSelection = input("Please Enter Number between Number 1 to 4: ")
        blnValidation = True #Validate_Navigation_Selection(intSelection) 

    intSelection = int(intSelection)
    blnValidation = bool(False)

    # Determine Selection

    if intSelection == 1:

        #GET VALIDATE FIRST NAME
        while blnValidation is False:
            strFirstName = input("Enter First Name: ")
            blnValidation = Validate_First_Name (strFirstName) 

        strFirstName = str(strFirstName.strip())
        blnValidation = bool(False)

        #GET VALIDATE LAST NAME
        while blnValidation is False:
            strLastName = input("Enter Last Name: ")
            blnValidation = Validate_Last_Name (strLastName) 

        strLastName = str(strLastName.strip())
        blnValidation = bool(False)

        #GET VALIDATE PHONE ID
        while blnValidation is False:
            strPhoneID = input("Please Enter 10 Digit Phone Number (No Space, Dashes, or Parentheses): ")
            blnValidation = Validate_Phone_ID (strPhoneID) 
       
        #strPhoneID = str(intPhoneID)
        blnValidation = bool(False)

        #GET VALIDATE RENTAL QUANTITY SKIS
        while blnValidation is False:
            intRentalQuantitySkis = int(input("Enter Number of Skis to Rent (Enter 0 if None): "))
            blnValidation = Validate_Rental_Quantity_Skis(intRentalQuantitySkis) 
       
        intRentalQuantitySkis = int(intRentalQuantitySkis)
        blnValidation = bool(False)

        #GET VALIDATE RENTAL QUANTITY SNOWBOARDS
        while blnValidation is False:
            intRentalQuantitySnowboards = int(input("Enter Number of Snowboards to Rent (Enter 0 if None): "))
            blnValidation = Validate_Rental_Quantity_Snowboards(intRentalQuantitySnowboards) 
       
        intRentalQuantitySnowboards = int(intRentalQuantitySnowboards)
        blnValidation = bool(False)

        #GET VALIDATE RENTAL RATE CATEGORY
        while blnValidation is False:
            strRentalRateCategory = input("Enter Rental Category (Hourly, Daily, or Weekly): ")
            strRentalRateCategory = strRentalRateCategory.lower()
            blnValidation = Validate_Rental_Rate_Category(strRentalRateCategory.strip()) 
       
        strRentalRateCategory = str(strRentalRateCategory)
        blnValidation = bool(False)
        
        #CALL FORMAT RENTAL RATE FUNCTION FOR NEXT GET VALIDATE
            
        strHoursDaysWeeks = Format_Rental_Rate(strRentalRateCategory)

        #GET RENTAL DURATION
        while blnValidation is False:
            intRentalDuration = input("Enter the Number of " + strHoursDaysWeeks + " to Rent: ")
            blnValidation = Validate_Rental_Duration(intRentalDuration) 
       
        intRentalDuration = int(intRentalDuration)
        blnValidation = bool(False)

        #GET COUPON CODE
        while blnValidation is False:
            strCouponCode = input("Enter Coupon Code or Press Enter: ")
            blnValidation = Validate_Coupon_Code(strCouponCode) 
       
        strCouponCode = str(strCouponCode)
        blnValidation = bool(False)

        ##CALCULATE AND DISPLAY ESTIMATE
        if strRentalRateCategory == "weekly":

            BobsShop.Calculate_Skis_Weekly_Rental_Cost(BobsShop._dblSkisWeeklyRate, intRentalDuration, intRentalQuantitySkis)
            BobsShop.Calculate_Snowboards_Weekly_Rental_Cost(BobsShop._dblSnowboardsWeeklyRate, intRentalDuration, intRentalQuantitySnowboards)

        elif strRentalRateCategory == "daily":

            BobsShop.Calculate_Skis_Daily_Rental_Cost(BobsShop._dblSkisDailyRate, BobsShop._dblSkisWeeklyRate, intRentalDuration, intRentalQuantitySkis)
            BobsShop.Calculate_Snowboards_Daily_Rental_Cost(BobsShop._dblSnowboardsDailyRate, BobsShop._dblSnowboardsWeeklyRate, intRentalDuration, intRentalQuantitySnowboards)

        else:
                                                                 
            BobsShop.Calculate_Skis_Hourly_Rental_Cost(BobsShop._dblSkisHourlyRate, BobsShop._dblSkisDailyRate, BobsShop._dblSkisWeeklyRate, intRentalDuration, intRentalQuantitySkis)
            BobsShop.Calculate_Snowboards_Hourly_Rental_Cost(BobsShop._dblSnowboardsHourlyRate, BobsShop._dblSnowboardsDailyRate, BobsShop._dblSnowboardsWeeklyRate, intRentalDuration, intRentalQuantitySnowboards)

        BobsShop.Calculate_Family_Discount(intRentalQuantitySkis, intRentalQuantitySnowboards)
        BobsShop.Calculate_Coupon_Discount(strCouponCode)
        BobsShop.Calculate_Rental_Total()
        BobsShop.Display_Bill()

        ##COMPLETE RENTAL - SAVE CUSTOMER TO LIST 
        strYesNo = input("Would Like to Rent at This Time? (Y or N) ")
        strYesNo = strYesNo.lower()
        strYesNo = Validate_Yes_No(strYesNo)

        blnValidation = bool(False)
        
        if strYesNo == 'y':
            lCustomers.append(cCustomer(strFirstName, strLastName, strPhoneID , intRentalQuantitySkis, intRentalQuantitySnowboards, strRentalRateCategory, datetime.today(), intRentalDuration, strCouponCode))
            cShop.intDailySkis += int(intRentalQuantitySkis)
            cShop.intDailySnowboards += intRentalQuantitySnowboards
            cShop.Update_Inventory_Rented_Skis(intRentalQuantitySkis)
            cShop.Update_Inventory_Rented_Snowboards(intRentalQuantitySnowboards)
            
            cShop.dblRentalCost = 0
            cShop.dblCouponDiscount = 0
            cShop.dblFamilyDiscount = 0
            cShop.dblRentalTotal = 0
        else:
            print("Thank you for visiting Bob's Skis and Snowboards!")
            cShop.dblRentalCost = 0
            cShop.dblCouponDiscount = 0
            cShop.dblFamilyDiscount = 0
            cShop.dblRentalTotal = 0

    if intSelection == 2:
        #Request customer identification (Phone Number)
         strPhoneID = input("Please Enter 10 Digit Phone Number (No Space, Dashes, or Parentheses): ")

         for customer in lCustomers:
             if strPhoneID == customer.strPhoneID:
                 strFName = customer.strFirstName
                 strLName = customer.strLastName

                 if customer.strRentalRateCategory == 'hourly':
                    #########################################
                    #FOR DEMONSTRATION ONLY.  Forcing Days to 1
                    intRentalTotTime = abs((datetime.today() - customer.dtmRentalDate)).seconds
                    if intRentalTotTime < 3600:
                    #intRentalTotTime = (intRentalTotTime/60)/60
                        intRentalTotTime = 1
                    #########################################

                    BobsShop.Calculate_Skis_Hourly_Rental_Cost(BobsShop._dblSkisHourlyRate, BobsShop._dblSkisDailyRate, BobsShop._dblSkisWeeklyRate, intRentalTotTime, customer.intRentalQuantitySkis)
                    BobsShop.Calculate_Snowboards_Hourly_Rental_Cost(BobsShop._dblSnowboardsHourlyRate, BobsShop._dblSnowboardsDailyRate, BobsShop._dblSnowboardsWeeklyRate, intRentalTotTime, customer.intRentalQuantitySnowboards)
                    BobsShop.Calculate_Family_Discount(customer.intRentalQuantitySkis, customer.intRentalQuantitySnowboards)
                    BobsShop.Calculate_Coupon_Discount(customer.strCouponCode)
                    BobsShop.Calculate_Rental_Total()

                 if customer.strRentalRateCategory == 'daily':
                    intRentalTotTime = abs((datetime.today() - customer.dtmRentalDate)).days

                    #########################################
                    #FOR DEMONSTRATION ONLY.  Forcing Days to 1
                    if intRentalTotTime < 1:
                        intRentalTotTime = 1
                    #########################################

                    BobsShop.Calculate_Skis_Daily_Rental_Cost(BobsShop._dblSkisDailyRate, BobsShop._dblSkisWeeklyRate, intRentalTotTime, customer.intRentalQuantitySkis)
                    BobsShop.Calculate_Snowboards_Daily_Rental_Cost(BobsShop._dblSnowboardsDailyRate, BobsShop._dblSnowboardsWeeklyRate, intRentalTotTime, customer.intRentalQuantitySnowboards)
                    BobsShop.Calculate_Family_Discount(customer.intRentalQuantitySkis, customer.intRentalQuantitySnowboards)
                    BobsShop.Calculate_Coupon_Discount(customer.strCouponCode)
                    BobsShop.Calculate_Rental_Total()

                 if customer.strRentalRateCategory == 'weekly':
                    #########################################
                    #FOR DEMONSTRATION ONLY.  Forcing weeks to 1
                    intRentalTotTime = abs((datetime.today() - customer.dtmRentalDate)).days
                    if intRentalTotTime < 7:
                        intRentalTotTime = 1
                    #########################################
                    #intRentalTotTime = intRentalTotTime/7

                    BobsShop.Calculate_Skis_Weekly_Rental_Cost(BobsShop._dblSkisWeeklyRate, intRentalTotTime, customer.intRentalQuantitySkis)
                    BobsShop.Calculate_Snowboards_Weekly_Rental_Cost(BobsShop._dblSnowboardsWeeklyRate, intRentalTotTime, customer.intRentalQuantitySnowboards)
                    BobsShop.Calculate_Family_Discount(customer.intRentalQuantitySkis, customer.intRentalQuantitySnowboards)
                    BobsShop.Calculate_Coupon_Discount(customer.strCouponCode)
                    BobsShop.Calculate_Rental_Total()
                    
                 intSBRented = customer.intRentalQuantitySnowboards
                 intSkisRented = customer.intRentalQuantitySkis

                 print("Customer Name: " + strFName + ' ' + strLName)
                 print("Skis Rented: " + str(intSkisRented))
                 print("Snowboards Rented: " + str(intSBRented))

                 BobsShop.Display_Bill()

                 BobsShop.Update_Inventory_Return_Skis(int(intSBRented))
                 BobsShop.Update_Inventory_Return_Snowboards(int(intSkisRented))

                 print(str(intSkisRented) + " skis returned.")
                 print(str(intSBRented) + " snowboards returned.")
                 lCustomers.remove(customer)
                 cShop.dblDailyRevenue += cShop.dblRentalTotal
                 cShop.dblRentalCost = 0
                 cShop.dblCouponDiscount = 0
                 cShop.dblFamilyDiscount = 0
                 cShop.dblRentalTotal = 0
    
    if intSelection == 3:
        BobsShop.Display_Skis_Inventory()
        BobsShop.Display_Snowboards_Inventory()

    if intSelection == 4:
        print("Total skis rented today:\t", cShop.intDailySkis )
        print("Total snowboards rented today:\t", cShop.intDailySnowboards)
        print("Total Sales:\t", "${:,.2f}".format(cShop.dblDailyRevenue))

        blnProgramLoop = bool(False)
