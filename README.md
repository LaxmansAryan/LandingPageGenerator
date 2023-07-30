# Landing Page Generator using OpenAI API

## Screenshots
Main Page: 
<img width="960" alt="1" src="https://user-images.githubusercontent.com/102072945/235968023-3e053692-cb8f-48dc-b3a8-54b3524cf9cb.PNG">

Result Page:
<img width="960" alt="2" src="https://user-images.githubusercontent.com/102072945/235968098-970a2dad-200b-422f-9bba-8f17858a077e.PNG">

Some Template Examples:
<img width="960" alt="3" src="https://user-images.githubusercontent.com/102072945/235968352-fdef3d17-e768-42cf-aced-75d313589ce0.PNG">

<img width="960" alt="4" src="https://user-images.githubusercontent.com/102072945/235968373-438ca33b-e9a9-4579-b4f4-42f5f3e83b5c.PNG">

<img width="960" alt="5" src="https://user-images.githubusercontent.com/102072945/235968412-d498fa87-1c4e-4c5c-8b4c-543cd121a38c.PNG">

<img width="960" alt="6" src="https://user-images.githubusercontent.com/102072945/235968446-2b6c8872-b0e2-4dee-9243-7cc88272a994.PNG">

<img width="960" alt="7" src="https://user-images.githubusercontent.com/102072945/235968466-eeb36236-3ff9-4184-93c4-d6a1c0f600e3.PNG">

## Description
The Landing Page Generator is a Django web application that allows users to easily create custom landing pages for their businesses. By simply inputting the name and details of their business, the project leverages the power of the OpenAI API and pre-stored templates to generate a visually appealing landing page. Users can then download the HTML file of the generated landing page, making it quick and convenient to kickstart their online presence.

## Installation
To set up the Landing Page Generator, follow these steps:

- Clone the repository to your local machine using the following command:
git clone https://github.com/your-username/landing-page-generator.git
- Navigate to the project directory:
cd landing-page-generator
- Create a virtual environment (optional, but recommended):
python -m venv env
source env/bin/activate   # For Windows: env\Scripts\activate
- Install the required dependencies:
pip install -r requirements.txt
- Set up the OpenAI API credentials by creating a .env file in the project root and adding your API key:
OPENAI_API_KEY=your_openai_api_key
- Run the Django development server:
python manage.py runserver

- Access the website at http://localhost:8000 in your web browser.

## Usage
- On the landing page, the user needs to provide the name and details of their business in the input form.

- After submitting the form, the Landing Page Generator will process the data using the OpenAI API and generate a preview of the landing page based on the selected template.

- The user can choose from different templates available, each with a unique design and layout.

- Upon satisfaction with the generated preview, the user can click the "Download" button to obtain the HTML file of the landing page.

- The downloaded HTML file can be easily hosted on any web server, allowing the user to launch their landing page with minimal effort.

## Contributing
Contributions to the Landing Page Generator are welcome and encouraged! If you find any issues or want to enhance the project, please follow the guidelines outlined in CONTRIBUTING.md.

## Credits
The Landing Page Generator project was inspired by the creativity and simplicity of OpenAI's API. We would like to extend our gratitude to the developers and contributors of Django, OpenAI, and other open-source libraries that made this project possible.

## Contact
If you have any questions, suggestions, or feedback, feel free to reach out to us at sawantaryan16@gmail.com or through our social media channels.






