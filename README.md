# 지혜서원 (Static Export)

이 저장소는 **정적(Static) 웹사이트 내보내기(export)** 결과물입니다.  
서버(PHP/Node 등) 없이 **GitHub Pages**에서 바로 배포할 수 있습니다.

## 1) GitHub Pages 배포

1. 이 폴더를 그대로 GitHub 저장소에 업로드합니다.
2. GitHub → **Settings → Pages**
3. **Build and deployment**
   - Source: `Deploy from a branch`
   - Branch: `main` / Folder: `/ (root)`
4. 저장 후 Pages URL이 생성되면 접속해 확인합니다.

> 참고: 이 프로젝트에는 `_next/` 폴더가 포함되어 있어 **.nojekyll** 파일이 필요합니다(이미 포함됨).

## 2) admin 영역(주의)

`/admin` 및 `admin.html`은 **서버 인증이 없는 정적 페이지**입니다.  
이번 정리본에서는 '가벼운 억제용'으로 **브라우저 프롬프트(passphrase)**를 추가했습니다.

- 보안 수준: **실제 보안이 아님** (정적 호스팅 한계)
- 비밀번호 변경:
  - `ADMIN_PASSWORD` 문자열을 검색해 원하는 값으로 바꾸세요.

원칙적으로는:
- admin을 삭제하거나
- private 저장소로 분리하거나
- 별도 백오피스(서버/인증)로 이전하는 것을 권장합니다.

## 3) TXT 원고 파일 처리

- `site_public` 변형: `.txt` 원고 파일 포함
- `site_no_txt` 변형: `.txt` 원고 파일 제거 + `.gitignore`로 txt 제외

## 4) TXT → HTML 변환 스크립트

`tools/convert_txt_to_html.py` 를 제공합니다.

예:
```bash
python tools/convert_txt_to_html.py --root . --out same
```

## 5) SEO 기본 구성

- Open Graph 메타 태그(주요 루트 페이지)
- `sitemap.xml`, `robots.txt` 생성

추가로 더 강화하려면:
- 실제 배포 도메인/경로에 맞춘 canonical URL 설정
- 페이지별 고유 description 작성
- 검색 엔진 등록(GSC 등)
