---
type: creature
group: ["Kami", "Spirit"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Kodama"
level: "5"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Kami"
trait_02: "Spirit"
trait_03: "Wood"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+15; [[Darkvision]]"
languages: "Common, Empyrean (Speak with plants, Telepathy 50 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +11, Athletics +11, Nature +13, Stealth +13, Survival +13"
abilityMods: ["+2", "+4", "+5", "+0", "+4", "+4"]
abilities_top:
  - name: "Telepathy 50 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
  - name: "Ward"
    desc: "Every kami is bound to a ward: a specific animal, plant, object, or location. A kami can merge with or emerge from their ward as a single action, which has the concentrate trait. While merged, the kami can observe their surroundings with their usual senses as well as the senses of their ward, but can't move, communicate with, or control their ward. Additionally, a kami merged with their ward recovers Hit Points each minute as if they spent an entire day resting. <br>  <br> A kodama's ward is a specific tree."
  - name: "Constant Spells"
    desc: "A constant spell affects the monster without the monster needing to cast it, and its duration is unlimited. If a constant spell gets counteracted, the monster can reactivate it by spending the normal spellcasting actions the spell requires."
  - name: "Spiritual Rope"
    desc: "The kodama spends 1 minute to fashion an enchanted straw rope out of nearby materials. The rope can be wrapped around other kami creatures to protect them from fell forces. A kami who wears a spiritual rope gains resistance 5 to damage from unholy creatures and effects and a +1 status bonus to AC and saving throws against unholy effects and attacks and effects from unholy creatures. <br>  <br> A kodama always wears a spiritual rope, and they can have one other spiritual rope in existence at a time. Creating a new rope beyond these two releases the magic of one of the other two ropes of the kodama's choosing. A spiritual rope around a creature other than a kodama loses its magic after 24 hours or if it's taken outside the kodama's forest."
armorclass:
  - name: AC
    desc: "21 +1 status vs. unholy creatures; **Fort** +12, **Ref** +11, **Will** +13"
health:
  - name: HP
    desc: "95; **Weaknesses** cold iron 5; **Resistances** unholy 5"
abilities_mid:
  - name: "Distracting Gaze"
    desc: "30 feet. When a creature ends its turn in the aura, it must attempt a DC 21 [[Will]] save. The kodama can activate or deactivate this aura by using a single action, which has the concentrate trait. <br> - **Success** The creature is unaffected. <br> - **Failure** The creature is [[Fascinated]] with the kodama. This condition ends if the creature ends its turn outside the aura. <br> - **Critical Failure** As failure, plus the creature is [[Slowed]] 1 as long as it remains fascinated."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +13 (`pf2:1`) (agile, finesse), **Damage** 2d6+4 bludgeoning"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 23, attack +15<br>**5th** [[Nature's Pathway]]<br>**3rd** [[Speak with Plants]] (Constant)<br>**2nd** [[One with Plants]]<br>**1st** [[Figment]]"
abilities_bot: []
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

A kodama is a type of kami who inhabits a tree. Kodama commonly appear in old Tian forests, especially old-growth forests far removed from civilization. In the Forest of Spirits in Minkai, for example, so many trees are possessed by kodama that a traveler might pass by hundreds, if not thousands, of these beings while journeying through a single acre of woodland.

Kodama try their utmost to protect their sacred trees, but a single kodama is a minor obstacle to most oni or others who have no qualms about desecrating forests or harvesting them for natural resources. Like trees in a forest, kodama are most powerful in great numbers and among other kami, whom they can bolster with their magical straw ropes while distracting strong enemies with their mesmerizing presence. On the other hand, kodama bear no ill will toward those who respect their wards, even allowing druids and other deferential creatures to dwell within their bounds. They might even subtly guide lost travelers out of the forest or back to safety.

Kami are divine nature spirits from the lands of Tian Xia, far to the east of the Inner Sea region. They serve as guardians of natural objects and places they protect—their wards—and are ancient enemies of oni (Pathfinder Monster Core 252–255). Kami can merge with their wards, allowing them to surreptitiously watch anyone who treads upon their sacred grounds. Kami leave those who they deem harmless alone, but fight vigilantly to scare away anyone perceived as a threat.

```statblock
creature: "Kodama"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
