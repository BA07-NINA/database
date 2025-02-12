# Book Bank

Link to our website: ""

PAM is a dashboard where you can have an overview over devices deployed in the field, with their associated audio files.

## Contributors

- Johanne Burns Bergan
- Sander Stenbakk Ekanger
- Jacob Gullesen Hagen
- Ingrid Helene Kvitnes
- Noah Lund Syrdal
- Siri Arnesen
- Marius Bølset Gisleberg


## Table of contents
- [PAM](#pam)
  - [Contributors](#contributors)
  - [Table of contents](#table-of-contents)
  - [Environment](#environment)
    - [Setting Up the Correct Versions](#setting-up-the-correct-versions)
    - [Start development](#start-development)
  - [Login system](#login-system)
  - [Dataset](#dataset)
  - [Technologies](#technologies)
    - [Frontend](#frontend)
    - [Backend](#backend)
    - [Database](#database)
  - [Features](#features)
  - [Tests](#tests)
  - [Responsiveness](#responsiveness)
  - [HTML Web Storage API](#html-web-storage-api)
    - [LocalStorage Implementation](#localstorage-implementation)
    - [SessionStorage Implementation](#sessionstorage-implementation)
  - [Version Control](#version-control)
  - [Web accessibility](#web-accessibility)
    - [Testing with Lighthouse](#testing-with-lighthouse)
  - [Sustainable web development](#sustainable-web-development)
    - [Supporting the UN’s Sustainable Development Goals (SDGs):](#supporting-the-uns-sustainable-development-goals-sdgs)
  - [Architecture](#architecture)

## Environment

The application is designed to work with Node.js version 22.7.0 and npm version 10.8.2. We can't guarantee that it will work properly with other versions of Node.js.

### Setting Up the Correct Versions

To ensure your environment matches the required versions, follow these steps:

1. **Set the Node.js version:**

```shell
nvm install 22.7.0
nvm use 22.7.0
```

2. **Update npm to the correct version**

```shell
npm install -g npm@10.8.2
```

### Start development

**Run frontend**
```shell
cd frontend
npm install
npm run dev
```


```
**Start backend**
```shell

```

## Login system



## Dataset



## Technologies

MÅ ENDRE HER

We selected technologies that enable us to build a responsive, efficient, and scalable web application. Our frontend stack allows for dynamic, interactive interfaces with strong type safety and consistent styling. The backend is designed for high performance and flexibility, with a GraphQL API to handle complex queries. The database provides reliable storage and fast access to large datasets. Together, these technologies create a cohesive and maintainable foundation for our application.

### Frontend
- **React**: A JavaScript library for building interactive, component-based user interfaces.
- **TypeScript**:  A superset of JavaScript that adds static typing for improved code quality and maintainability.
- **Vite**: A fast development tool that accelerates build times and hot module replacement.
- **Tailwind CSS**: A utility-first CSS framework for rapid and consistent styling.
- **Apollo Client**: A state management library that handles GraphQL queries and caching for smoother data fetching.
- **Prettier**: A code formatter that enforces consistent style, making the codebase easier to read and maintain.

### Backend
- **Node.js**: A JavaScript runtime that allows for building scalable server-side applications.
- **Apollo Server**: A GraphQL server library that provides a flexible and efficient API layer.
- **TypeScript**: Adds type safety to backend code, reducing errors and improving readability.
- **GraphQL**: A query language for APIs that enables efficient data fetching and flexible queries.
- **Prettier**: Ensures consistent code formatting across the backend codebase.

### Database
- **MongoDB**: A NoSQL database that stores data in flexible, JSON-like documents, allowing for efficient storage and quick retrieval of large datasets.

## Features

To meet the requirements of our application, we have implemented key features that make it easy to search for books. Users can search, filter, and sort books in ways that fit the dataset and purpose of the platform. We have taken inspiration from [Goodreads](https://www.goodreads.com/explore) to include useful functionalities for a book discovery site.

1. Book Search and Discovery
    - **Search by Title or Author**: Users can search for a specific book or author.
    - **Filters**: Users can filter search results by genre, rating, and publication year.
    - **Sort Options**: Users can sort books alphabetically by title and author name.

## Tests

We have made a separate document for tests. You can find it [here](../bookbank/frontend/TEST_README.md). 

## Responsiveness
Our application has been developed with responsiveness, allowing it to adapt effectively to a wide range of devices and screen sizes.

- **Dynamic Layout**: The design adjusts automatically to different screen dimensions and orientations, ensuring a smooth and user-friendly experience on both mobile and desktop devices.
- **Testing**: During development, the application was tested on a range of screen sizes, including larger mobile screens like the iPhone 14 Pro Max, to ensure compatibility and usability. However, due to time constraints, we were only able to test responsiveness on screens larger than 400 pixels in width.

While the application performs well on these devices, we recognize the need to refine and expand testing to include smaller screens in future iterations. This will ensure a fully inclusive experience for all users, regardless of their device size.


## HTML Web Storage API

The project utilizes the HTML Web Storage API for managing data persistence across user sessions. Specifically, it employs:

### LocalStorage Implementation
We have utilized localStorage to persist data on the client side, allowing it to remain available even after the browser is closed and reopened. While we acknowledge that localStorage is not the most secure method for handling sensitive data, it provides a practical approach for implementing user logic at this stage of development. Our focus has been on frontend functionality, logic, and features, making this a sufficient solution for our current needs. Below is a breakdown of how we use localStorage in the application:

**1. User Logic**: 
LocalStorage is used to store data tied to individual users. This includes information such as booklists and preferences, which are essential for creating a personalized experience. While this is not ideal for secure, large-scale applications, it demonstrates a functional approach to user logic in a frontend-focused project.

**2. Booklists**:
Each user's booklists are saved in localStorage, allowing them to access previously saved books every time they revisit the site. This feature is central to our application, enabling users to maintain their curated lists across sessions without needing a backend integration.

**3. Theme Preferences (Light/Dark Mode)**:
User-selected theme preferences are also stored in localStorage. If a user specifies a preference for light or dark mode, this choice is remembered across sessions. For first-time visitors or users who haven’t set a specific preference, the application defaults to the system's color scheme, ensuring a seamless and adaptive experience.


### SessionStorage Implementation
We have integrated sessionStorage to manage temporary data storage for user interactions within a single page session. This data is cleared when the page session ends, such as when the page is closed or reloaded. Below is a breakdown of how sessionStorage is used in the application:

**1. Search, Filtering, and Sorting**: sessionStorage is utilized to save the user's search input, selected filters, and sorting preferences in the filter menu and search functionalities. This ensures that even if the user reloads the page or navigates back after viewing a book card, their choices remain intact for the duration of the session. 

## Version Control

Our project uses Git for version control, hosted on GitHub: [https://git.ntnu.no/IT2810-H24/T15-Project-2](https://git.ntnu.no/IT2810-H24/T15-Project-2). We manage our codebase using:

**Branching Strategy**
Main branch: Contains the stable, production-ready code.

Other branches: Each new feature or fix is developed on a separate branch. This keeps the main branch clean and only includes clean code. Each branch is connected to an issue. Branches are integrated into main through pull requests (PRs) with code review from a minimum of one team member, ensuring quality and consistency across the codebase.

**Tracking**

Issue Creation: Each task or bug is documented in an issue. These are tagged for easy filtering (e.g., bug, frontend).

Commits: Each commit is linked to its corresponding task by including the issue number (e.g., #issue-number) and follows a clear [conventional commit message](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13) format for easy tracking of changes. A brief, descriptive summary of the changes is also provided to give a quick overview.

**Project Boards and Workflow**
To ensure an organized and efficient development process, we utilized project boards throughout the project. We structured our work into three sprints, one for each milestone assessment. For every sprint, we created a dedicated sprint board with columns for Backlog, To Do (max 5 tasks), In Progress (max 5 tasks), and Done. This visual approach helped us clearly see what needed to be done and track progress in real time. Limiting the number of tasks in the "To Do" and "In Progress" columns ensured a smooth workflow by preventing too many issues from being active simultaneously, allowing us to maintain focus and steady progress.

This workflow helps us maintain a clear and organized development process, ensuring high-quality code and efficient collaboration.

## Sustainable web development
In designing and implementing our application, we have prioritized sustainable web development practices to minimize the environmental impact of our solution while maximizing its utility. Below are the measures we have taken to align with responsible development principles and the [UN's Sustainable Development Goals](https://fn.no/om-fn/fns-baerekraftsmaal) (SDGs):

**1. Energy Efficiency with Light and Dark Modes:**
We have implemented both light and dark modes with a curated color palette, ensuring a consistent and user-friendly experience. Dark mode contributes to energy savings by reducing the power consumption of devices. This not only enhances usability but also reflects our commitment to creating environmentally conscious solutions.

**2. Reducing Data Usage:**

-   Debounced Search: To prevent unnecessary server calls, we utilize a debounce function for search inputs, reducing the number of queries sent to the backend.
-   Caching: API calls for fetching and filtering books are cached, minimizing redundant requests, so users don’t have to reload everything when navigating back to a page or when using the filter menu.
-   Pagination: We limit the number of API calls by using pagination on the "Find Books" page, fetching data in manageable chunks rather than retrieving all records at once.
- Efficient Database Usage: We have prioritized minimizing unnecessary calls to the database by only fetching the data required for each specific page and implementing caching wherever possible. This approach reduces server load and improves performance. However, when a user submits a review, we make a direct call to the database to ensure it is immediately updated with accurate information. We believe maintaining up-to-date data is crucial for providing a reliable and consistent user experience, and this trade-off aligns with our goal of delivering high-quality functionality.

**3. Simple and Focused Design:**
We have kept the website simple and avoided unnecessary features to reduce complexity and improve performance. For example:

-   We decided not to use videos, as they consume a lot of energy. Instead, we use images, which are more relevant to our app and essential for user experience.

### Supporting the UN’s Sustainable Development Goals (SDGs):

**SDG 12: Responsible Consumption and Production:**
Through our focus on efficient resource usage, minimal data consumption, and a balance between utility and impact, we contribute to responsible consumption and production practices.

[Source for the UN's SDGs](https://fn.no/om-fn/fns-baerekraftsmaal)

## Architecture
The project is structured to maintain a clear separation of concerns and to ensure scalability and maintainability. Here is an overview of the **key** directories and files:

**Backend**
- `src/`: Contains the main source code for the backend.
    - `graphql/`: Handles GraphQL logic.
    - `server.ts`: Entry point for the backend server, setting up middleware and starting the application.
    - `types.ts`: TypeScript type definitions used in the backend.



**Frontend**
- `src/`: Contains the main source code for the frontend.
    - `api/`: Manages API calls, such as GraphQL queries.
    - `components/`: Houses reusable React components, each in its own directory.
        - `ui/`: Includes user interface components.
            - `addPopup/`: Shows options for adding books in lists. 
            - `navbar/`: The navigation bar component.
            - `bookCard/`: Displays book details in a card format.
            - `filterMenu/`: Allows filtering of book results.
            - `reviewForm/`: A form for users to write reviews.
            - `bookStatus/`: Displays the reading status of a book.
            - `placeholderCard/`: Renders placeholder when empty lists on your profile.
        - `auth/`: Handles authentication-related components (privateRoute)
        - `context/`: Handles user logic for users that have not logged in.
        - `graphql/`: Stores GraphQL operations.
        - `hooks/`: Contains custom React hooks.
            - `useSearchStorage.ts`: Manages persistent search state.
            - `useDebounceSearch.ts`: Implements a debounce function for search.
            - `useDarkMode.ts`: Toggles dark mode.
            - `themeContext.tsx`: Context provider for managing the app theme.
            - `useClickOutside.ts`: Making it possible to click outside of pop ups.
        - `pages/`: Contains the main page components for routing.
            - `searchPage.tsx`: Displays all books.
            - `bookDetailPage.tsx`: Shows detailed book information.
            - `profilePage.tsx`: Displays user profile details.
            - `loginPage.tsx`: Handles user login.
            - `homePage.tsx`: The homepage of the application.
    - `app.css`: Contains our color paletts
- `index.html`: The entry HTML file for the frontend.

This structure ensures the project is organized, with each component and asset easy to locate and manage. It supports maintainability, scalability, and a streamlined development process.