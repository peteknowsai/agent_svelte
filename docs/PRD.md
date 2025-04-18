# Product Requirements Document (PRD)

## 1. Project Overview
Build an OpenAI-powered agent backend (Python) with a SvelteKit frontend. The frontend is a simple text-only chat interface that communicates with the agent API.

## 2. Objectives
- Enable user to send/receive messages to the AI agent
- Clean, responsive chat UI in SvelteKit
- Plug-and-play UI components for rapid development
- Easily extensible for new features (e.g., file upload, attachments)
- Progressive streaming of agent responses

## 3. Functional Requirements
- Text input box with send button
- Scrollable message list with user/agent message bubbles
- Loading indicator while agent processes
- Real-time streaming of agent replies (progressive token rendering)
- Error handling / retry button

## 4. Non-Functional Requirements
- Fast initial load (<200 ms)
- Mobile-first responsive design
- Accessible (ARIA landmarks, labels)
- Dark/light mode support

## 5. UI Libraries & Component Research (SvelteKit)

### 5.1 Tailwind CSS + DaisyUI
- DaisyUI plugin for Tailwind offers a ready-made `.chat` component
- Highly customizable with Tailwind utility classes

### 5.2 Flowbite Svelte
- Svelte wrapper around Flowbite/Tailwind components
- Provides input, buttons, avatars, modals
- No built-in chat bubbles but easily assembled from list + avatar

### 5.3 Svelte Material UI (SMUI)
- Material Design components for Svelte
- Good form controls (text fields, buttons)
- Requires custom styling for chat bubbles

### 5.4 Headless UI + Shadcn Svelte
- Unstyled, accessible components (menus, dialogs)
- Build custom chat UI from primitives

### 5.5 Other Options
- `svelte-chat-ui` community package (bubbles & avatars)

## 6. Proposed Stack
- SvelteKit v1.x
- Vercel AI SDK v4.x (streaming chat support)
- Tailwind CSS v3.x + DaisyUI
- Optional Flowbite Svelte for shared components
- Svelte stores for message state
- Agent backend: `agents-python/` (OpenAI Agents SDK)
