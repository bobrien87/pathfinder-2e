---
type: creature
group: ["Kami", "Spirit"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Sakugami"
level: "15"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Kami"
trait_02: "Spirit"
trait_03: "Wood"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+30; [[Darkvision]]"
languages: "Common, Empyrean (Speak with plants, Telepathy 150 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +30, Diplomacy +31, Medicine +28, Nature +30, Stealth +28, Survival +30"
abilityMods: ["+5", "+7", "+6", "+2", "+7", "+8"]
abilities_top:
  - name: "Telepathy 150 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Ward"
    desc: "Every kami is bound to a ward: a specific animal, plant, object, or location. A kami can merge with or emerge from their ward as a single action, which has the concentrate trait. While merged, the kami can observe their surroundings with their usual senses as well as the senses of their ward, but can't move, communicate with, or control their ward. Additionally, a kami merged with their ward recovers Hit Points each minute as if they spent an entire day resting. <br>  <br> A sakugami's ward is typically a specific deciduous tree with seasonal blossoms, such as a chery, plum, or wisteria."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Fleeting Blossoms"
    desc: "A sakugami's staff Strikes stir up fleeting blossoms that bloom, wilt, and decay all in the space of an instant. On a hit, they deal an additional 1d6 mental damage, as well as an additional 1d6 void damage to living creatures and an additional 1d6 vitality damage to undead."
  - name: "Touch of Ages"
    desc: "A sakugami's attacks bestow a curse that alters the very flow of time in those they attack. When a sakugami hits a creature with a melee Strike, the creature must attempt a DC 36 [[Fortitude]] save as its perspective shifts rapidly between that of advanced age and an infantile state. Regardless of the outcome, the creature is temporarily immune for 1 minute. <br> - **Critical Success** The creature is unaffected. <br> - **Success** The creature becomes [[Clumsy]] 1, [[Enfeebled]] 1, and [[Stupefied 1]] for 1 round. <br> - **Failure** The creature becomes [[Clumsy]] 2, [[Enfeebled]] 2, and [[Stupefied 2]] for 1 minute. <br> - **Critical Failure** As failure, but the conditions are permanent."
armorclass:
  - name: AC
    desc: "35; **Fort** +25, **Ref** +28, **Will** +30"
health:
  - name: HP
    desc: "350; **Weaknesses** cold iron 15"
abilities_mid:
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Sakugami's Foresight"
    desc: "`pf2:r` **Trigger** The sakugami is subject to a hostile action or needs to roll to defend itself <br>  <br> **Effect** The sakugami rolls twice and uses the higher result for its saving throw or other defense (a fortune effect) or forces the hostile creature or danger to roll twice and use the lower result for its attack roll or similar roll (a misfortune effect)."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Staff +30 (`pf2:1`) (magical, two hand d8), **Damage** 2d4+13 bludgeoning plus [[Fleeting Blossoms]] plus [[Touch Of Ages]]"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 36, attack +28<br>**7th** [[Execute]], [[Regenerate]]<br>**5th** [[Nature's Pathway (At Will) (Flowering Only)]]<br>**3rd** [[Haste]], [[Slow]]<br>**2nd** [[Cleanse Affliction]], [[One with Plants (Flowering Trees Only)]], [[Peaceful Rest]], [[Status]]<br>**1st** [[Heal]]"
abilities_bot:
  - name: "Swift Staff Strike"
    desc: "`pf2:2` In a rapid series of movements, the sakugami unleashes a deadly assault. The sakugami makes three staff Strikes. The sakugami's multiple attack penalty doesn't increase until after they've made all three Strikes."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Sakugami are especially powerful kami who protect seasonally blossoming trees, particularly ones in places where the primeval powers of nature remain strong. The cycle of a barren tree bursting into a riot of flowers once a year, before those blossoms inevitably fade with the turning of the seasons, provides a striking visual metaphor for sakugami, whose association with this annual cycle of growth and decay grants them powers over time as well as nature. Also known as blossom kami, sakugami have a particular fascination with mortals. Many folk legends tell of sakugami who bestow their blessing upon worthy individuals who fight for just causes. In truth, while blossom kami are mesmerized by such mortals—seeing the essence of a flower in a short life devoted to bringing beauty and comfort to its surroundings—they're so rare and enigmatically aloof that few ever encounter them. Decades, even centuries, might pass before a humble village realizes that a sakugami has been watching over it.

The stories persist, however, as they have for ages, leading to a widespread appreciation for blossoming trees. The site of a new village might be chosen due to its proximity to an ancient wisteria, or a temple might be carefully constructed around a single young plum. As sakugami are most commonly associated with cherry trees, many larger population centers in Minkai will plant and carefully tend small groves of cherries, both for their beauty and out of respect for the blossom kami.

Kami are divine nature spirits from the lands of Tian Xia, far to the east of the Inner Sea region. They serve as guardians of natural objects and places they protect—their wards—and are ancient enemies of oni (Pathfinder Monster Core 252–255). Kami can merge with their wards, allowing them to surreptitiously watch anyone who treads upon their sacred grounds. Kami leave those who they deem harmless alone, but fight vigilantly to scare away anyone perceived as a threat.

```statblock
creature: "Sakugami"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
