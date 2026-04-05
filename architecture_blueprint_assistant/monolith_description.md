# Monolithic Architecture

- **Frontend App**: Mobile/web interface for listeners, creators, and admins.
- **Backend Monolith**: Single application that hosts all server-side components.
- **Authentication Module**: Manages login, sessions, subscription access, and user roles.
- **Catalog/Search Module**: Handles audiobook discovery, search queries, filters, and metadata lookup.
- **Playback Module**: Controls audiobook playback, speed/pitch settings, bookmarks, and quick summaries.
- **Content Management Module**: Enables creators to upload audio, manage metadata, and publish titles.
- **Accessibility Module**: Provides screen reader support, dyslexia-friendly text, high contrast, and audio cues.
- **User Profile & Sync Module**: Stores profile settings, offline downloads, and syncs progress across devices.
- **Analytics & Reporting Module**: Tracks engagement, usage metrics, and creator/admin reports.
- **Database**: Central storage for users, audiobooks, bookmarks, downloads, and analytics.
- **Notification Service**: Sends alerts for downloads, updates, moderation status, and account actions.
