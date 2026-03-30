# Microservices Architecture

- **API Gateway**: Routes client requests to the appropriate backend services and enforces authentication, rate limiting, and API versioning.
- **Auth Service**: Handles user login, session management, subscription access, and token validation.
- **Catalog Service**: Provides audiobook discovery, search, filtering, and metadata retrieval.
- **Playback Service**: Manages playback state, speed/pitch controls, bookmarks, and synchronization across devices.
- **Content Service**: Supports creator uploads, audio storage, metadata management, and publication workflows.
- **Accessibility Service**: Applies accessibility settings such as screen reader support, dyslexia-friendly text, and high-contrast mode.
- **User Profile Service**: Stores user preferences, offline download status, progress sync, and account settings.
- **Analytics Service**: Collects usage metrics, engagement data, and generates reports for creators and admins.
- **Notification Service**: Sends alerts, reminders, and system updates via email, push, or in-app notifications.
- **Data Stores**: Each service maintains its own storage, such as Auth Database, Catalog Database, Playback Database, Content Storage, Accessibility Config Store, User Data Store, Metrics Store, and Messaging Queue for asynchronous communication.
