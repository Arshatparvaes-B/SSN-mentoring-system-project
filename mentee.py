class mentee:

    def __init__(self,fname=None,lname=None,BloodGroup=None,EmailId=None,
    MobileNumber=None,gender=None,nationality=None,religion=None,MotherTongue=None,
    ProgramName=None,ModeOfAdm=None,AdmissionCategory=None,AssociatedDepartment='Information Technology'):

        self._fname = fname
        self._lname = lname
        self._fullname = fname+" "+lname
        self._blood_group = BloodGroup
        self._EmailId = EmailId
        self._MobileNumber=MobileNumber
        self._gender=gender
        self._nationality = nationality 
        self._religion = religion 
        self._MotherTongue= MotherTongue
        self._ProgramName=ProgramName
        self._AssociatedDepartment = AssociatedDepartment
        self._ModeOFAdm = ModeOfAdm
        self._AdmissionCategory=AdmissionCategory
    
    
    



