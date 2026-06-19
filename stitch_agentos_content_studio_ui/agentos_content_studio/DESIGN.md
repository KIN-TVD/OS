---
name: AgentOS Content Studio
colors:
  surface: '#faf9ff'
  surface-dim: '#d8d9e3'
  surface-bright: '#faf9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f3fd'
  surface-container: '#ecedf7'
  surface-container-high: '#e7e7f1'
  surface-container-highest: '#e1e2ec'
  on-surface: '#191b22'
  on-surface-variant: '#424753'
  inverse-surface: '#2e3038'
  inverse-on-surface: '#eff0fa'
  outline: '#727785'
  outline-variant: '#c2c6d6'
  surface-tint: '#0059c6'
  primary: '#0057c2'
  on-primary: '#ffffff'
  primary-container: '#2c70e2'
  on-primary-container: '#fefcff'
  inverse-primary: '#afc6ff'
  secondary: '#505f76'
  on-secondary: '#ffffff'
  secondary-container: '#d0e1fb'
  on-secondary-container: '#54647a'
  tertiary: '#8c4b00'
  on-tertiary: '#ffffff'
  tertiary-container: '#b06000'
  on-tertiary-container: '#fffbff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d9e2ff'
  primary-fixed-dim: '#afc6ff'
  on-primary-fixed: '#001a43'
  on-primary-fixed-variant: '#004398'
  secondary-fixed: '#d3e4fe'
  secondary-fixed-dim: '#b7c8e1'
  on-secondary-fixed: '#0b1c30'
  on-secondary-fixed-variant: '#38485d'
  tertiary-fixed: '#ffdcc2'
  tertiary-fixed-dim: '#ffb77b'
  on-tertiary-fixed: '#2e1500'
  on-tertiary-fixed-variant: '#6d3a00'
  background: '#faf9ff'
  on-background: '#191b22'
  surface-variant: '#e1e2ec'
typography:
  h1:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.02em
  h2:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  h3:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
    letterSpacing: -0.01em
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 22px
  body-sm:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 20px
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
  caption:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.01em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  container-max: 1280px
  sidebar-width: 260px
  topbar-height: 64px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 32px
---

## Brand & Style
The design system is engineered for high-velocity productivity and clarity, drawing inspiration from the "developer-centric" minimalism of modern SaaS leaders. The aesthetic is professional, functional, and unobtrusive, ensuring that user content remains the focal point.

The style is characterized by a "Soft-Modern" approach: a refinement of corporate minimalism that utilizes generous whitespace, subtle depth through layering, and a restrained color palette. It avoids unnecessary decoration in favor of precise alignment and rhythmic spacing, evoking a sense of reliability and technical sophistication.

## Colors
The color palette is anchored in a neutral slate scale to maintain a calm, focused environment. 

- **Primary Blue:** Reserved for primary actions and active states, providing a clear focal point without overwhelming the interface.
- **Surface & Background:** A subtle distinction between the background (`#F8FAFC`) and card surfaces (`#FFFFFF`) creates natural containment for content blocks.
- **Semantic Colors:** Success, Warning, and Danger colors are used sparingly for feedback loops and status indicators, ensuring high glanceability.
- **Typography Tones:** Primary text uses a deep slate for maximum legibility, while secondary text is softened to create a clear hierarchy.

## Typography
This design system utilizes **Inter** exclusively to ensure a systematic, utilitarian feel. The type scale is optimized for information density, favoring smaller body sizes (14px) common in professional dashboard environments.

- **Headlines:** Use a semi-bold weight (600) with slight negative letter-spacing to feel tight and modern.
- **Body Text:** Standardized at 14px for general content to maximize data visibility without sacrificing readability.
- **Labels:** Use a medium weight (500) to distinguish interactive elements and form titles from static body text.
- **Mobile Scaling:** On devices below 768px, H1 should scale down to 24px (H2 equivalent) to prevent excessive line wrapping.

## Layout & Spacing
The layout follows a structured, fixed-sidebar model characteristic of modern SaaS tools.

- **Sidebar:** A fixed 260px left-hand navigation allows for consistent access to global tools. It uses a slightly darker tint or a subtle border separation from the main stage.
- **Main Stage:** A centered content area with a max-width of 1280px to maintain line-length readability.
- **Grid:** A 12-column fluid grid is used within the main stage for dashboard widgets and content blocks.
- **Rhythm:** Spacing follows a 4px baseline. Use 16px (4 units) for internal card padding and 24px (6 units) for gaps between major layout sections.

## Elevation & Depth
Depth is conveyed through "Tonal Layering" and "Ambient Shadows" rather than heavy gradients.

- **Level 0 (Background):** The base canvas (`#F8FAFC`).
- **Level 1 (Cards/Surfaces):** Raised surfaces (`#FFFFFF`) featuring a 1px solid border (`#E5E7EB`).
- **Level 2 (Dropdowns/Modals):** Elements that sit above the UI use a soft, multi-layered shadow: `0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)`.
- **Active States:** Subtle inner shadows or a 2px primary border indicate focus and selection.

## Shapes
The design system employs a "Rounded-2xl" philosophy for major components to soften the technical nature of the UI.

- **Standard Radius:** 8px (0.5rem) for small components like buttons, inputs, and chips.
- **Container Radius:** 16px (1rem) for cards, modals, and main content wrappers.
- **Inner-Outer Alignment:** When nesting elements (e.g., a button inside a card), ensure the inner radius is smaller than the outer radius to maintain geometric harmony.

## Components
Components are designed with a "Refined Utility" approach, similar to the Shadcn/UI aesthetic.

- **Buttons:** Primary buttons use a solid `#4F8CFF` background with white text. Ghost and Outline variants use the slate scale for secondary actions. All buttons have a height of 36px (sm) or 40px (md).
- **Inputs:** Fields use a 1px border (`#E5E7EB`) that transitions to a 2px primary blue ring on focus. Background remains white.
- **Cards:** White surfaces with a 16px corner radius and a subtle 1px border. Avoid heavy shadows unless the card is draggable.
- **Data Tables:** Row-based with 1px bottom borders. Header cells use the `caption` type style with uppercase treatment and increased tracking for a professional look.
- **Status Chips:** Small, low-saturation backgrounds with high-saturation text (e.g., Success chip: Light green background with dark green text) for quick status identification.