# Automatic and Intelligent Engineering Design

This is a temporal home for the research "Automatic and Intelligent Engineering Design".

by Qingfeng Xia

2019

## 1. Introduction to Intelligent engineering design

The schematic of the current time-consuming and the proposed future intelligent engineering design can be found: <https://github.com/qingfengxia/CAE_pipeline>

To enable intelligent engineering design, I (Qingfeng Xia) have initiated several sub-projects on github since 2016.

##  2. Ccurrently active sub-projects

### 2.1 CAD: FreeCAD

ebook: *Module developer's Guide to FreeCAD* <https://github.com/qingfengxia/FreeCAD_Mod_Dev_Guide>

### 2.2 Geometry processing

During my employment in UKAEA, I design a "parallel preprocessor" to pre-process large assemblies (tens of thousands parts) to enable meshing and simulation.  It is designed to use both MPI and multi-threading parallelism;  this software will be open source very soon. Independently, I will dive into the research problem of geometry recognition using machine learning.

### 2.3 Parallel meshing

It is expected third-party meshing tools will be used, while "parallel pre-processor" will make a parallel meshing framework to accelerate meshing large assemblies (underway). [MOAB]() is a library to import mesh from various meshing tools and export meshing for different solvers.

### 2.4. Solver input: OpenFOAM

I developed a [CFD module (using OpenFOAM solver) for FreeCAD](https://github.com/qingfengxia/Cfd), to enable one-stop design and simulation, with the topology optimization capacity.  There is a independent module inside this CFD module, [*FoamCaseBuilder*](), aiming at simulation automation.

![OpenFOAM as a CFD solver in CfdWorkbench of FreeCAD](https://github.com/qingfengxia/qingfengxia.github.io/blob/master/images/FreeCAD_CFDworkbench_screenshot.png)
![OpenFOAM as a CFD solver in CfdWorkbench of FreeCAD](http://www.iesensor.com/blog/wp-content/uploads/2018/05/FreeCAD_CFD_module_openfoam_now_working_with_WSL.png)


C++ code is merged to Fem module <https://github.com/qingfengxia/FreeCAD.git>,  while python code is developed as an independent module: <https://github.com/qingfengxia/Cfd>

### 2.5 Multiphysics Solver: [FenicsSolver](https://github.com/qingfengxia/FenicsSolver)

   This is a multiphysics FEM solver based on Fenics.  Currently, I am working on coupling Fenics with OpenFOAM, etc.  See  my presentation on [OpenFOAM workshop 2018])https://www.iesensor.com/blog/2018/06/25/coupling-openfoam-with-fenics-for-multiphysis-simulation-openfoam-workshop-13-presentation/)

### 2.6 Solver coupling:

To coupling and coordinate different physical model solvers. 

### 2.7 Post processing

Currently, VTK and **Paraview** is sufficient is support the engineering design pipeline.

### 2.8 Report, optimization and machine learning

This work will start once the research in intelligent preprocessing reaches mature. 


### 2.9 other relevant 

CC-SA book: ["Design large scale science and engineering software"]()

`python-wrap`(https://github.com/qingfengxia/python-wrap): comparison of different approaches of write python interface for C++ code.


## 3. My other projects and research 

ResearchGate profile: <https://www.researchgate.net/profile/Qingfeng_Xia/>

My research projects

- Heat and mass transfer enhancement (by synthetic jet): PhD research
- Condition monitoring and tribology for Turbomachinery:  Post doctoral research
- sensor and measurement for extreme conditions: ongoing

Other links

- Personal website <http://www.iesensor.com>

+ Linkedin profile:   <http://uk.linkedin.com/pub/qingfeng-xia/28/67b/b6a>


## 4. Other open source projects

- clUtils v0.2			Basic Linear OpenCL C library (released by BSD licensed), used by clFoam;
  clFoam v0.1       	OpenCL solver for OpenFoam1.7,   6th OpenFoam workshop, 2011;
                             	<https://sourceforge.net/projects/opencl4openfoam>
- [Matlab flow visualization Toolbox v1.2](https://sourceforge.net/projects/flowviz/) for PLIF, PSP, BOS and TSCL 
      organization of my script used in PhD research
- [Arduino robot wheel car](https://github.com/qingfengxia/arduinorobotcar) 
- [PIV image processing using Python](https://github.com/qingfengxia/openpiv-python) contributed python3 wrapping