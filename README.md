# Invoice Generator

This is a small application to generate invoices. I used this project to learn the basics of flask and database migrations. The design is based on the colors from Material. It will give the option to generate all invoices into a pdf file; or as a single pdf per invoice.
In another project I also import data from excel directly, but the effort for a quick manual input seemed lower than to explain to me the values in excel that had to be checked again anyway when creating the invoices.

https://github.com/JazzCore/python-pdfkit/wiki/Installing-wkhtmltopdf pdf printer used that has to be installed locally on the system.

## Interface for adding new entries and editing existing ones:

![](https://i.imgur.com/u2DhrGZ.png)

## Resulting Invoice.

![](https://i.imgur.com/8hAdk2q.png)

## Notes / Possible Improvements.

While this project has a procfile and a heroku bug specific fix for database connections it is not deployed to heroku yet but only run locally. Some input helper functions might not be in the optimal position for the data serialization, but I only realised this afterwards after learning more about how Django would make the connection between input and data models.
