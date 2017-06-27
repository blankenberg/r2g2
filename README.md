# R2-G2 Automatically Generates Galaxy tools on a per-function basis from any R Library


```
$ ./scripts/r2g2_on_package.py --help
usage: r2g2_on_package.py [-h] --name NAME [--package_name PACKAGE_NAME]
                          [--package_version PACKAGE_VERSION] [--out OUT]
                          [--create_load_matrix_tool]
                          [--galaxy_tool_version GALAXY_TOOL_VERSION]

optional arguments:
  -h, --help            show this help message and exit
  --name NAME           Package Name
  --package_name PACKAGE_NAME
                        [Conda] Package Name
  --package_version PACKAGE_VERSION
                        [Conda] Package Version
  --out OUT             Output directory
  --create_load_matrix_tool
                        Output a tool that will create an RDS from a tabular
                        matrix
  --galaxy_tool_version GALAXY_TOOL_VERSION
                        Additional Galaxy Tool Version
```