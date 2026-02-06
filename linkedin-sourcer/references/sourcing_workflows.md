# Sourcing Workflows

## Boolean Search String Patterns

Generate LinkedIn/X-Ray boolean search queries for finding candidates. Adapt these templates based on the role requirements.

### LinkedIn Search Bar

```
"software engineer" AND ("Python" OR "Go") AND "distributed systems" NOT "recruiter"
```

### Google X-Ray Search

```
site:linkedin.com/in/ "software engineer" "Python" "distributed systems" -intitle:"recruiter"
```

### Template Variables

| Variable | Example |
|----------|---------|
| {title} | "Senior Backend Engineer" |
| {must_have_skills} | "Python" AND "PostgreSQL" |
| {nice_to_have_skills} | "Kubernetes" OR "Docker" |
| {industry_keywords} | "fintech" OR "payments" |
| {exclude} | NOT "recruiter" NOT "talent" |
| {location} | "San Francisco" OR "Bay Area" |

### Compound Pattern

```
("{title_1}" OR "{title_2}") AND ({must_have_skills}) AND ({location}) {exclude}
```

## Candidate Scorecard Template

Use this template when evaluating a candidate against a role. Adjust criteria weights based on role priorities.

```
# Candidate Scorecard: {candidate_name}
## Role: {role_title}

### Fit Summary
Overall: {STRONG_FIT | GOOD_FIT | PARTIAL_FIT | WEAK_FIT}

### Criteria Evaluation

| Criteria | Weight | Rating (1-5) | Notes |
|----------|--------|--------------|-------|
| Relevant experience | {w}% | {n} | {notes} |
| Technical skills match | {w}% | {n} | {notes} |
| Industry experience | {w}% | {n} | {notes} |
| Seniority alignment | {w}% | {n} | {notes} |
| Education/credentials | {w}% | {n} | {notes} |
| Location/remote fit | {w}% | {n} | {notes} |

Weighted Score: {score}/5.0

### Strengths
- {strength_1}
- {strength_2}

### Concerns / Gaps
- {concern_1}
- {concern_2}

### Key Questions for Outreach
- {question_1}
- {question_2}
```

## Candidate Summary Template

Concise summary for quick review of a single candidate.

```
## {candidate_name} — {headline}
**Location:** {location}
**Current:** {current_role} at {current_company} ({duration})
**Prior:** {notable_prior_roles}
**Skills:** {relevant_skills}
**Education:** {degree}, {institution}
**Fit:** {STRONG | GOOD | PARTIAL | WEAK} — {one_line_rationale}
**Flags:** {red_flags_or_none}
```

## Candidate Comparison Table

Side-by-side comparison of multiple candidates against role criteria.

```
# Candidate Comparison: {role_title}

| Criteria | {candidate_1} | {candidate_2} | {candidate_3} |
|----------|---------------|---------------|---------------|
| Current role | ... | ... | ... |
| Years relevant exp | ... | ... | ... |
| Key skills match | ... | ... | ... |
| Industry fit | ... | ... | ... |
| Seniority level | ... | ... | ... |
| Location | ... | ... | ... |
| Overall fit | {rating}/5 | {rating}/5 | {rating}/5 |

**Recommendation:** {ranking_with_rationale}
```

## Evaluation Heuristics

When assessing candidate-role fit, consider:

- **Title progression**: Upward trajectory signals growth; lateral moves may indicate specialization
- **Tenure patterns**: Very short stints (<1yr) at multiple companies may signal risk; long tenures (5yr+) signal stability but verify adaptability
- **Company caliber**: Experience at well-known companies in the target domain is a positive signal but not a requirement
- **Skill recency**: Recent use of required skills matters more than historical experience
- **Scope indicators**: Look for mentions of team size, revenue impact, scale metrics in experience descriptions
- **Education relevance**: Degree matters more for early-career; experience dominates for senior roles
