# Sample run

A real run of the skill, recorded while preparing the 1.0.0 release.

- **Host:** Claude Code, isolated mode, general-purpose subagents on Sonnet (no adapter installed).
- **Date:** 2026-10-26.
- **Scenario:** hypothetical. The team, app, and numbers are invented for the test.
- **Editing:** seat and Outsider texts are lightly edited for readability. Stances, confidence scores, labels, and the verdict are unchanged. Two seats (Skeptic, First-Principles) returned 5 points where the format asked for 3, and the Outsider ran past its 250-word cap. They are shown as returned. Release 1.0.0 tightened the format wording ("exactly 3") in response.

## Prompt

> /prism-council My recommendation is to rewrite our Android app in Flutter so we get iOS for free. Pressure-test that.

## BRIEF (written by the main agent, sent to the four insiders)

> Decision: should a 3-developer team rewrite their working native Android app (Kotlin, ~60k LOC, 4 years old) in Flutter so they can also ship iOS, or keep Android native and build a separate native iOS app (SwiftUI)? Options: (1) full Flutter rewrite of both platforms; (2) keep Android, build native iOS separately; (3) keep Android, build iOS in Flutter only (new code), revisit Android later. The agent's current opinion: option 1, because one codebase halves long-term maintenance. Facts: all three devs are strong in Kotlin, none has shipped Flutter or Swift. App is an order-tracking app with maps, background location, push notifications and offline sync. Business wants iOS live within 6 months; an investor demo is in 4 months. Android app has 200k MAU and a 4.6 rating; regressions there directly hit revenue. Stakes: missing the iOS deadline vs destabilizing the revenue-generating Android app.

## BARE QUESTION (sent to the Outsider)

> A small team has a successful Android app and must also launch on iPhone within 6 months, with a demo in 4 months. Should they (1) rewrite everything in one cross-platform framework, (2) keep Android and build a separate native iPhone app, or (3) keep Android and build only the iPhone app in the cross-platform framework?

## Relay (what the user sees)

## Council verdict (The Outsider)
Option 2, with a scoped first release (tracking and order status), plus one contractor or hire who has shipped iOS. Leave Android untouched. Revisit sharing code later, with measured evidence.
**First step:** Start Apple Developer enrollment and a TestFlight build with background location this week, and begin recruiting an iOS contractor at the same time.

**Seats**
| Seat | Stance | Confidence |
|---|---|---|
| Skeptic | modify: option 2, thin demo-first iOS build | 4 |
| First-Principles | modify: option 2, shared logic held in reserve | 4 |
| Expansionist | modify: option 3, with a shared Kotlin core | 4 |
| Executor | modify: option 3, after a 2-week spike | 4 |

**Agreement:** All four seats reject the full rewrite and keep the Android app untouched.
**Clash:** Native iOS (Skeptic, First-Principles) versus Flutter for iOS only (Expansionist, Executor).
**Blind spots:** "Dart in 2 weeks" and "Swift is easier" are unsupported guesses. Nobody asked whether the demo needs the real app, whether Apple review blocks background location, who fixes Android bugs meanwhile, or whether an iOS hire is possible.
**Strongest argument:** First-Principles. The goal is iOS without harming Android revenue, not one codebase.
**Mode:** isolated subagents

**Agent's note:** The council overturned the agent's original recommendation (option 1). No seat supported it.

## Full seat answers (anonymized label in brackets)

**The Skeptic [B]**
```
STANCE: modify (option 2, with native iOS scoped as a thin, demo-first build; reject option 1 outright)
CONFIDENCE: 4
POINTS:
- Option 1 rewrites a 60k LOC, 4-year-old app whose bugs are paid for in revenue, and the team has never shipped Flutter. Rewrites routinely take 2-3x the estimate, so the 6-month iOS date and the 4-month demo both slip. The Android rating (4.6) and the 200k MAU are put at risk, and nothing is gained for that risk.
- "One codebase halves maintenance" is the claim that costs more than stated. Background location, push, and offline sync are exactly where Flutter needs native platform channels on both OS. You end up maintaining Kotlin, Swift, and Dart, which is worse than two native apps.
- Option 3 has the same flaw in a smaller form. Three Kotlin devs would learn Flutter and Swift/iOS background-location rules at once, and then run a Flutter app next to a native one with no shared code.
- The Swift learning curve is smaller than Flutter's, because the devs already know Kotlin and Compose-style declarative UI. Cap the scope of the first iOS build: tracking and order status only, and skip secondary features until after the demo.
- Cut cost by sharing the backend contract and a spec, not code. Kotlin Multiplatform for the sync and domain layers is a possible later step, but only if measured.
MISSED BY OTHERS: iOS background location and push approval (App Store review, permission copy, battery behavior) are schedule risks that no framework removes. Start a TestFlight submission in the first month.
```

**The First-Principles Thinker [D]**
```
STANCE: modify (option 2, with a thin shared-logic option held in reserve)
CONFIDENCE: 4
POINTS:
- The real problem is "get iOS live in 6 months without hurting Android revenue". It is not "one codebase". Option 1 treats a code-sharing goal as the objective and puts the 200k-MAU asset at risk to reach it.
- A 60k-LOC rewrite by three developers who have never shipped Flutter is also a learning curve, and Flutter still needs native bridges for background location and push, which are the hard parts of this app. "Halves maintenance" is only a projection. The cost of the rewrite is certain, and it comes during the 4-month demo window.
- Option 3 gives you two stacks plus a new unfamiliar one, so you pay for both.
- Option 2 touches no Android code. The unknown becomes one language (Swift), and the iOS app can be built from the existing API contracts and Android behaviour as a spec. If sharing matters later, Kotlin Multiplatform can share sync and domain logic without rewriting the UI.
- Add a contractor or one iOS hire. That is cheaper than three devs losing a year.
MISSED BY OTHERS: Nobody has tested the assumption that maintenance is the dominant cost. For an app with a 4.6 rating, the dominant risk is regression, and a rewrite maximises it.
```

**The Expansionist [A]**
```
STANCE: modify (option 3, with a shared-core upside)
CONFIDENCE: 4
POINTS:
- Option 3 is a cheap experiment that can grow into option 1 later. iOS is greenfield, so Flutter's cross-platform value applies there with zero regression risk. If it works, you have a proven Flutter codebase and can migrate Android screen by screen, or embed Flutter modules in the Android app via add-to-app. The 200k MAU revenue app never has to take a big-bang rewrite.
- A 4-month investor demo is a stronger asset than a 6-month parity deadline. A fast Flutter iOS prototype with maps, tracking and push shows momentum, and the same team can then show a roadmap with one codebase going forward.
- Consider Kotlin Multiplatform for the order, sync and networking core. It reuses the team's Kotlin skills and is shared by Android now and iOS later. That lets option 3 grow into a shared-logic architecture instead of a second full app.
MISSED BY OTHERS: Option 3 is also the cheapest way to learn whether Flutter is worth betting the whole company on. Run the iOS build as a 6-week spike with a go/no-go gate, and you get real data on background location and offline sync before the Android decision, instead of guessing.
```

**The Executor [C]**
```
STANCE: modify (option 3, with a 2-week spike first and an Android freeze rule)
CONFIDENCE: 4
POINTS:
- Option 1 fails on Monday morning. Three Kotlin devs would spend about 4 months rewriting a 60k LOC revenue app in a framework none has shipped. Background location, push and offline sync are exactly where Flutter plugins bite. The investor demo and the iOS date would both slip, and 200k MAU would be at regression risk.
- Option 3 ships. The Android code is not touched and stays green. Dart is learnable by Kotlin devs in about 2 weeks. A thin iOS slice (login, order list, tracking map, push) is demoable in 4 months. Month 1 is a spike on background location and push on a real iPhone. If the spike fails, fall back to option 2 with a month lost.
- Option 2 means learning Swift, SwiftUI and iOS background rules from zero. It is the same ramp-up as Flutter but with no shared code later. Consider KMP for the sync and domain layer only if the spike fails.
MISSED BY OTHERS: Apple Developer enrollment, App Review (background location justification) and TestFlight setup take weeks. Start them Monday, because they are on the critical path regardless of framework.
```

**The Outsider**
```
GUT TAKE: Don't rewrite a working, revenue-earning app under a deadline, and don't make a small team learn two new stacks at once. Pick the path with the fewest unknowns that still produces a demo in 4 months.
STRONGEST: D, because it names the real objective (iOS live without harming Android revenue), points out that a rewrite's cost is certain while its benefit is only projected, and proposes adding capacity (contractor or iOS hire) instead of stretching the team.
WEAKEST: A, because its main argument is that option 3 is a cheap experiment that can grow into a full migration. But it adds a third stack (Dart) to a team that has shipped none, and it counts "grow into option 1 later" as a benefit even though that is the rewrite risk the others reject. Its own "6-week spike" admits the unknown.
INSIDER ASSUMPTIONS: C: "Dart is learnable in about 2 weeks" and "fall back with a month lost" are unsupported. B and D: "Swift is easier than Flutter" and "Flutter needs native bridges for background location and push" are asserted without evidence. Everyone treats the facts (3 Kotlin devs, 60k LOC, 200k MAU, background location) as settled.
ALL MISSED: Whether the investor demo needs the real app or only a convincing slice. Whether Apple's review rules for background location are a blocker. Who owns Android bug fixes while the team builds iOS. Whether hiring someone with iOS experience is possible.
VERDICT: Option 2, with a scoped first release (tracking and order status), plus one contractor or hire who has shipped iOS. Leave Android untouched. Revisit sharing code later, with measured evidence.
FIRST STEP: Start Apple Developer enrollment and a TestFlight build with background location this week, and begin recruiting an iOS contractor at the same time.
```

## What this run shows, and what it does not

- The Outsider picked a seat it judged strongest and named claims that were only asserted. A single pass would probably not have done that.
- The council overturned the agent's starting opinion. That is the intended behavior when the evidence points the other way. It does not prove the verdict is correct.
- All seats ran on the same model family. They disagreed on the option, but they share that model's training biases.
