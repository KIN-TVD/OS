# Frontend Sprint F5 Report (Run Pipeline)

## Objective
Xây dựng trang `/run` với form đầy đủ: Input Content, Platform, Profile, Dataset và nút Generate.

## Files Created
- `frontend/src/app/run/page.tsx`
- `frontend/src/components/layout/Sidebar.tsx` [MODIFIED]

## API Used
- `POST /api/drafts/rerun` — Kích hoạt pipeline với topic

## UI Implemented
- Textarea lớn để nhập chủ đề/nội dung gốc
- Platform toggle: Instagram / Threads
- Profile radio group: Content Creator / Brand Marketing / Personal Blog / E-commerce
- Dataset radio group: General Knowledge / AI & Technology / Business / Lifestyle
- Nút Generate to với icon auto_awesome, loading spinner
- Success card: hiển thị Draft ID + links đến /review và /missions
- Error card

## Testing
- Trang render đầy đủ với tất cả options, nút Generate disabled khi không có input

## Result
PASS
