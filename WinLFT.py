import sys
from java.net import URI
from java.io import File
print(sys.path)
sys.path.append("C:\Program Files (x86)\HPE\Unified Functional Testing\SDK\Java\com.hp.lft.sdk-standalone.jar")
sys.path.append("C:\Program Files (x86)\HPE\Unified Functional Testing\SDK\Java\com.hp.lft.common.jar")
sys.path.append("C:\Program Files (x86)\HPE\Unified Functional Testing\SDK\Java\com.hp.lft.report.jar")
sys.path.append("C:\Program Files (x86)\HPE\Unified Functional Testing\SDK\Java\com.hp.lft.unittesting.jar")
from com.hp.lft import sdk as LFT
from com.hp.lft.sdk import Keyboard
#from com.hp.lft.sdk import Mouse as MouseButton
from com.hp.lft.sdk import Mouse
import java.awt.Point as Point
import java.awt.Desktop as Desktop
import com.company.ApplicationModel
print(dir(LFT))


class WinLFT:

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    """ Library for Interacting with Web Applications using LeanFT (UFT14+) as  Driver. The User is Expected to have the LeanFT Application Model Project handy. """

    def __init__(self):

        # self.LaunchApplication("C:\\Program Files (x86)\\HPE\\Unified Functional Testing\\bin\\LFTRuntime.exe")
        newConfig = LFT.ModifiableSDKConfiguration()
        address=URI("ws://localhost:5095")
        print("I am here")
        newConfig.setServerAddress(address)
        print("I am there")
        LFT.SDK.init(newConfig)
        print("I am Done")
        self.appModel=com.company.ApplicationModel()
        print(dir(self.appModel))
        
    def Launch_Application(self,path):

        Desktop.getDesktop().open(File(path))    

    def ActivateNode(self,element,index):

        """Method for activating node in the tree by index"""

        target=self._scrambler(self.appModel,element)
        target.activateNode(int(index))

    def SelectNode(self,element,index):

        """Method for selecting node in the tree by index"""

        target=self._scrambler(self.appModel,element)
        target.select(int(index))

    def Click(self,element):

        """Method for Clicking any clickable  element ex:  a button, hyper link etc.

         Format: Click  <Identifier>

         The <Identifier> field needs to be a fully classified LEanFT object as identified within the Application Model

         ex: Click     googlePage.googleSearchButton // where the identifier is as generated by LEanFT"""

        target= self._scrambler(self.appModel,element)
        target.click()

    def _scrambler(self,object,x):

        param= (x.split('.'))
        print("Scrambler got "+ str(param))
        for i in param:
            if i=='appModel':
                continue
            print ("This is namespace for "+i)
            print(dir(object))
            method_to_call=getattr(object,i[0:-2])
            object= method_to_call()
        return object

    def killLFT(self):
        LFT.SDK.cleanup()


    def EnterText(self,element,text):

        """Method for entering text into  any editable web element ex:  text box, edit  etc.

         Format: Enter Text  <Identifier>

         The <Identifier> field needs to be a fully classified LEanFT object as identified within the Application Model

         ex: Click     googlePage.searchEditField    // where the identifier is as generated by LEanFT"""

        target= self._scrambler(self.appModel,element)
        try:
            target.setText(text)
        except:
            try:
                target.setValue(text)
            except:
                target.sendKeys(text)

    def Enter(self):


        key=LFT.Keyboard.Keys
        LFT.Keyboard.pressKey(key.ENTER)

    def Tab(self):


        key=LFT.Keyboard.Keys
        LFT.Keyboard.pressKey(key.TAB)

    def Down(self):


        key=LFT.Keyboard.Keys
        LFT.Keyboard.pressKey(key.DOWN)


    def CloseWindow(self, window):

        """ Closes the specified Window passed as parameter"""

        # self.app.Close()
        # self.app=None
        target= self._scrambler(self.appModel,window)
        target.close()

    def MinimizeWindow(self, window):

        """ Minimizes the specified Window passed as parameter"""

        target= self._scrambler(self.appModel,window)
        target.minimize()

    def MaximizeWindow(self, window):

        """ Minimizes the specified Window passed as parameter"""

        target= self._scrambler(self.appModel,window)
        target.maximize()

    def SelectValueFromDropDown(self,element,option):

        """Method for selecting value from dropdown

         Format: Select Value From Dropdown  <element>   <option>
         The option could be a numieric representing the count of the option in the droplist or
          a  value matching exactly the text of the dropdown"""


        numFlag=False
        for i in option:
            print("I got "+i)
            if i in '1234567890':
                numFlag=True
            else:
                numFlag=False

        if(numFlag):
            target= self._scrambler(self.appModel,element)
            target.select((int(option))-1)

        else:

            target= self._scrambler(self.appModel,element)
            target.select(option)

    def GetVisibleText(self, window):

        """Returns all the visible text as a string. Accepts No Parameters. It reads from the current  window """
        target= self._scrambler(self.appModel,window)
        return target.getVisibleText()

    def DoubleClick(self,element):

        """ Method for Double Clicking on an element"""

        object=self.appModel
        target= self._scrambler(self.appModel,element)
        target.doubleClick()


    def GetLocation(self,element):

        """ Method for Double Clicking on an element"""

        object=self.appModel
        target= self._scrambler(self.appModel,element)
        return target.location


    def FocusWindow(self,element):

        """Method for Focusing any window when multiple windows are present on the desktop

         Format: Focus Window     <Identifier>

         The <Identifier> field needs to be a fully classified LEanFT object as identified within the Application Model


        """

        target= self._scrambler(self.appModel,element)
        target.activate()


    def MenuSelect(self, windowobject, menuname, item):

        targetWindow= self._scrambler(self.appModel,windowobject)
        # print(dir(SDK.StdWin.MenuType.Menu))
        # print(dir(targetWindow))
        menuType= LFT.SDK.StdWin.MenuType.Menu
        menuDescription= LFT.SDK.StdWin.MenuDescription(menuType)
        menu=targetWindow.Describe[LFT.SDK.StdWin.IMenu](menuDescription)
        path=menu.BuildMenuPath(menuname,int(item))
        menuItem= menu.getItem(path)
        print(dir(menu))
        menu.select(menuItem)

    def SendKeys(self,element,keys):

        """Method for entering text into  any editable web element ex:  text box, edit  etc.

         Format: Send Keys  <element>   <keys>

         The <element> field needs to be a fully classified LEanFT object as identified within the Application Model

         ex: Send Keys     googlePage.searchEditField   \n     // where the identifier is as generated by LEanFT"""

        target= self._scrambler(self.appModel,element)
        target.sendKeys(keys)

    def ClickAtLocation(self,x, y):

        #m=MouseButton()
        point= Point(int(x),int(y))
        Mouse.click(point)



